from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from agentic_soc_factory.db import DB
from agentic_soc_factory.evaluation.runner import run_evaluations
from agentic_soc_factory.models import Task
from agentic_soc_factory.orchestration.execute_stub import execute_stub
from agentic_soc_factory.orchestration.validate import validate_outputs
from agentic_soc_factory.pipeline.dataset import compile_and_write_dataset
from agentic_soc_factory.pipeline.ingest import load_docs
from agentic_soc_factory.pipeline.quality import (
    deduplicate,
    leakage_overlap,
    validate_against_schema,
)
from agentic_soc_factory.pipeline.reason import distill_docs_to_reasoning_units
from agentic_soc_factory.reporting.report import write_run_summary
from agentic_soc_factory.routing.router import Router


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _log_step(db: DB, run_id: str, step_name: str, status: str, details: Dict[str, Any]) -> None:
    db.insert(
        "INSERT INTO steps(run_id,step_name,status,started_at,ended_at,details_json) VALUES(?,?,?,?,?,?)",
        (run_id, step_name, status, now_iso(), now_iso(), json.dumps(details)),
    )


def run_pipeline(
    db: DB,
    router: Router,
    corpus_root: Path,
    artifacts_root: Path,
    tasks: List[Task],
    policy_profile: str = "default",
) -> Dict[str, Any]:
    run_id = f"run_{uuid.uuid4().hex[:12]}"
    run_root = artifacts_root / run_id
    dataset_dir = run_root / "dataset"
    run_root.mkdir(parents=True, exist_ok=True)

    db.insert(
        "INSERT INTO runs(run_id,created_at,status,policy_profile,summary_json) VALUES(?,?,?,?,?)",
        (run_id, now_iso(), "running", policy_profile, "{}"),
    )

    docs = list(load_docs(corpus_root))
    _log_step(db, run_id, "ingest", "completed", {"docs_count": len(docs)})

    units = distill_docs_to_reasoning_units(docs)
    units = deduplicate(units)
    _log_step(db, run_id, "reason", "completed", {"reasoning_units": len(units)})

    split_paths = compile_and_write_dataset(units, dataset_dir)
    _log_step(db, run_id, "dataset_compile", "completed", split_paths)

    # Data quality: schema validation on generated examples
    schema_path = Path("schemas/dataset_record.schema.json")
    train_lines = (Path(split_paths["train"]).read_text(encoding="utf-8").strip().splitlines())
    train_rows = [json.loads(x) for x in train_lines if x.strip()]
    schema_errors = validate_against_schema(train_rows[:500], schema_path)
    _log_step(
        db,
        run_id,
        "quality",
        "completed" if not schema_errors else "warning",
        {"schema_errors": len(schema_errors), "sample_errors": schema_errors[:10]},
    )

    db.insert(
        "INSERT INTO artifacts(run_id,kind,path,metadata_json,created_at) VALUES(?,?,?,?,?)",
        (run_id, "dataset", str(dataset_dir), json.dumps(split_paths), now_iso()),
    )

    model_call_results = []
    for t in tasks:
        decision, response = router.dispatch(t)
        model_call_results.append({"task": t.id, "route": decision.provider, "response": response.text, "fallback_used": decision.fallback_used})
        db.insert(
            "INSERT INTO model_calls(run_id,task_id,provider,model,workload,latency_ms,input_tokens,output_tokens,status,response_json,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (
                run_id,
                t.id,
                response.provider,
                response.model,
                decision.workload,
                response.latency_ms,
                response.input_tokens,
                response.output_tokens,
                "fallback" if decision.fallback_used else "ok",
                json.dumps({"text": response.text, "raw": response.raw, "route": {"requested_provider": decision.requested_provider, "final_provider": decision.provider, "fallback_used": decision.fallback_used}}),
                now_iso(),
            ),
        )
        db.insert(
            "INSERT INTO cost_tokens(run_id,provider,model,input_tokens,output_tokens,created_at) VALUES(?,?,?,?,?,?)",
            (
                run_id,
                response.provider,
                response.model,
                response.input_tokens,
                response.output_tokens,
                now_iso(),
            ),
        )

    _log_step(db, run_id, "route", "completed", {"calls": len(model_call_results)})

    executed = execute_stub(model_call_results)
    _log_step(db, run_id, "execute_stub", "completed", {"executed": len(executed)})

    validated = validate_outputs(executed)
    _log_step(db, run_id, "validate", "completed", validated)

    eval_summary = run_evaluations(db=db, run_id=run_id, dataset_paths=split_paths)

    test_lines = (Path(split_paths["test"]).read_text(encoding="utf-8").strip().splitlines())
    test_rows = [json.loads(x) for x in test_lines if x.strip()]
    leakage = leakage_overlap(train_rows, test_rows)

    summary = {
        "run_id": run_id,
        "docs_count": len(docs),
        "reasoning_units": len(units),
        "dataset_paths": split_paths,
        "quality": {"schema_errors": len(schema_errors)},
        "model_calls": len(model_call_results),
        "execute_stub": validated,
        "eval": eval_summary,
        "leakage_overlap": leakage,
        "artifacts_root": str(run_root),
    }

    summary_path = write_run_summary(run_root, summary)
    _log_step(db, run_id, "report", "completed", {"summary_path": str(summary_path)})

    db.insert(
        "INSERT INTO artifacts(run_id,kind,path,metadata_json,created_at) VALUES(?,?,?,?,?)",
        (run_id, "summary", str(summary_path), json.dumps({}), now_iso()),
    )

    db.insert(
        "INSERT INTO artifacts(run_id,kind,path,metadata_json,created_at) VALUES(?,?,?,?,?)",
        (
            run_id,
            "registry_layout",
            str(run_root),
            json.dumps(
                {
                    "dataset": str(run_root / "dataset"),
                    "checkpoints": str(run_root / "checkpoints"),
                    "merged": str(run_root / "merged"),
                    "gguf": str(run_root / "gguf"),
                    "ollama_bundle": str(run_root / "ollama_bundle"),
                }
            ),
            now_iso(),
        ),
    )

    db.insert(
        "UPDATE runs SET status=?, summary_json=? WHERE run_id=?",
        ("completed", json.dumps(summary), run_id),
    )
    return summary

