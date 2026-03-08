from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

from agentic_soc_factory.db import DB
from agentic_soc_factory.evaluation.harness import run_fixed_suite
from agentic_soc_factory.evaluation.runner import run_evaluations
from agentic_soc_factory.export.gguf import export_commands, write_modelfile
from agentic_soc_factory.models import Task
from agentic_soc_factory.orchestration.orchestrator import run_pipeline
from agentic_soc_factory.pipeline.dataset import compile_and_write_dataset
from agentic_soc_factory.pipeline.ingest import load_docs
from agentic_soc_factory.pipeline.quality import deduplicate, leakage_overlap, validate_against_schema
from agentic_soc_factory.pipeline.reason import distill_docs_to_reasoning_units
from agentic_soc_factory.routing.policy import select_route_for_task
from agentic_soc_factory.routing.router import Router


@dataclass
class DocDistillerAgent:
    def run(self, corpus_root: Path) -> List[Dict[str, Any]]:
        docs = list(load_docs(corpus_root))
        return distill_docs_to_reasoning_units(docs)


@dataclass
class DatasetBuilderAgent:
    def run(self, reasoning_units: List[Dict[str, Any]], out_dir: Path) -> Dict[str, str]:
        units = deduplicate(reasoning_units)
        return compile_and_write_dataset(units, out_dir)


@dataclass
class DatasetAuditAgent:
    dataset_schema: Path = Path("schemas/dataset_record.schema.json")

    def validate(self, train_path: Path, test_path: Path) -> Dict[str, Any]:
        train_rows = [json.loads(x) for x in train_path.read_text(encoding="utf-8").splitlines() if x.strip()]
        test_rows = [json.loads(x) for x in test_path.read_text(encoding="utf-8").splitlines() if x.strip()]
        errors = validate_against_schema(train_rows[:500], self.dataset_schema)
        leak = leakage_overlap(train_rows, test_rows)
        return {
            "schema_errors": len(errors),
            "leakage_overlap": leak,
            "sample_errors": errors[:10],
        }


@dataclass
class ModelRouterAgent:
    policy: Dict[str, Any]

    def choose(self, task: Task) -> Dict[str, Any]:
        decision = select_route_for_task(task, self.policy)
        return {
            "workload": decision.workload,
            "provider": decision.provider,
            "model": decision.model,
            "retries": decision.retries,
        }


@dataclass
class CostGovernorAgent:
    db: DB

    def summarize(self, run_id: str) -> Dict[str, Any]:
        rows = self.db.fetch_all(
            "SELECT provider, model, SUM(input_tokens) as in_tok, SUM(output_tokens) as out_tok, COUNT(*) as calls FROM cost_tokens WHERE run_id=? GROUP BY provider, model",
            (run_id,),
        )
        total_calls = sum(int(r["calls"] or 0) for r in rows)
        total_tokens = sum(int(r["in_tok"] or 0) + int(r["out_tok"] or 0) for r in rows)
        fallback_rows = self.db.fetch_all(
            "SELECT COUNT(*) as c FROM model_calls WHERE run_id=? AND status='fallback'",
            (run_id,),
        )
        fallback_calls = int((fallback_rows[0]["c"] if fallback_rows else 0) or 0)
        return {
            "by_model": rows,
            "total_calls": total_calls,
            "total_tokens": total_tokens,
            "fallback_calls": fallback_calls,
            "fallback_rate": (fallback_calls / total_calls) if total_calls else 0.0,
        }


@dataclass
class TrainerAgent:
    notebook_path: Path = Path("colab/qwen35_4b_qlora_free_colab.ipynb")

    def prepare(self, run_id: str) -> Dict[str, Any]:
        return {
            "run_id": run_id,
            "colab_notebook": str(self.notebook_path),
            "status": "prepared",
            "notes": "Open notebook in Colab and set RUN_ID before training.",
        }


@dataclass
class ModelExportAgent:
    def export(self, merged_model_dir: Path, gguf_out: Path, ollama_bundle: Path) -> Dict[str, Any]:
        cmds = export_commands(merged_model_dir, gguf_out)
        modelfile = write_modelfile(ollama_bundle, "soc-architect-qwen35-4b", gguf_out.name)
        return {
            "commands": cmds,
            "modelfile": str(modelfile),
        }


@dataclass
class EvalAgent:
    db: DB

    def run(self, run_id: str, dataset_paths: Dict[str, str]) -> Dict[str, Any]:
        return run_evaluations(self.db, run_id, dataset_paths)

    def run_ollama_suite(self, model: str, suite_path: Path, output_path: Path) -> Dict[str, Any]:
        return run_fixed_suite(model=model, suite_path=suite_path, output_path=output_path)


@dataclass
class RedTeamAgent:
    def scenarios(self) -> List[Dict[str, str]]:
        return json.loads(Path("tests/edge_cases.json").read_text(encoding="utf-8"))


@dataclass
class OpsAgent:
    db: DB

    def run_health(self, run_id: str) -> Dict[str, Any]:
        steps = self.db.fetch_all("SELECT step_name,status FROM steps WHERE run_id=?", (run_id,))
        failed = [s for s in steps if s["status"] not in ["completed", "warning"]]
        return {
            "steps": steps,
            "failed_steps": failed,
            "healthy": len(failed) == 0,
        }


@dataclass
class FactorySupervisorAgent:
    db: DB
    router: Router

    def run(self, corpus_root: Path, artifacts_root: Path, tasks: List[Task], policy_profile: str = "default") -> Dict[str, Any]:
        summary = run_pipeline(
            db=self.db,
            router=self.router,
            corpus_root=corpus_root,
            artifacts_root=artifacts_root,
            tasks=tasks,
            policy_profile=policy_profile,
        )

        cost = CostGovernorAgent(self.db).summarize(summary["run_id"])
        ops = OpsAgent(self.db).run_health(summary["run_id"])
        summary["cost"] = cost
        summary["ops"] = ops
        return summary
