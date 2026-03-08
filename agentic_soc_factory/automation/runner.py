from __future__ import annotations

import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from agentic_soc_factory.automation.common import now_iso
from agentic_soc_factory.automation.drive_telemetry import DriveTelemetryClient
from agentic_soc_factory.automation.events import EventStore
from agentic_soc_factory.automation.notifications import NotificationDispatcher
from agentic_soc_factory.db import DB
from agentic_soc_factory.evaluation.runner import run_evaluations
from agentic_soc_factory.models import Task
from agentic_soc_factory.orchestration.execute_stub import execute_stub
from agentic_soc_factory.orchestration.validate import validate_outputs
from agentic_soc_factory.pipeline.dataset import compile_and_write_dataset
from agentic_soc_factory.pipeline.ingest import load_docs
from agentic_soc_factory.pipeline.quality import deduplicate, leakage_overlap, validate_against_schema
from agentic_soc_factory.pipeline.reason import distill_docs_to_reasoning_units
from agentic_soc_factory.routing.router import Router


ACTIVE_STATES = {"queued", "running", "waiting_colab", "training", "export", "eval"}


class AutomatedRunExecutor:
    def __init__(
        self,
        db: DB,
        router: Router,
        automation_cfg: Dict[str, Any],
        event_store: EventStore,
        notifier: NotificationDispatcher,
        telemetry_client: DriveTelemetryClient,
        tasks: List[Task],
        corpus_root: Path,
        artifacts_root: Path,
        policy_profile: str = "default",
    ) -> None:
        self.db = db
        self.router = router
        self.automation_cfg = automation_cfg
        self.event_store = event_store
        self.notifier = notifier
        self.telemetry_client = telemetry_client
        self.tasks = tasks
        self.corpus_root = corpus_root
        self.artifacts_root = artifacts_root
        self.policy_profile = policy_profile

    def has_active_run(self) -> bool:
        row = self.db.fetch_one(
            "SELECT run_id FROM runs WHERE status IN ('queued','running','waiting_colab','training','export','eval') ORDER BY created_at DESC LIMIT 1"
        )
        return row is not None

    def run_once(self, trigger: str = "scheduled") -> Dict[str, Any]:
        run_id = f"run_{uuid.uuid4().hex[:12]}"
        run_root = self.artifacts_root / run_id
        dataset_dir = run_root / "dataset"
        run_root.mkdir(parents=True, exist_ok=True)

        self.db.insert(
            "INSERT INTO runs(run_id,created_at,status,policy_profile,summary_json) VALUES(?,?,?,?,?)",
            (run_id, now_iso(), "queued", self.policy_profile, "{}"),
        )
        self._emit(run_id, "run_started", {"trigger": trigger, "state": "queued"})

        try:
            self._set_state(run_id, "running")

            docs = list(load_docs(self.corpus_root))
            self._log_step(run_id, "ingest", "completed", {"docs_count": len(docs)})

            units = deduplicate(distill_docs_to_reasoning_units(docs))
            self._log_step(run_id, "reason", "completed", {"reasoning_units": len(units)})

            split_paths = compile_and_write_dataset(units, dataset_dir)
            self._log_step(run_id, "dataset_compile", "completed", split_paths)

            self.db.insert(
                "INSERT INTO artifacts(run_id,kind,path,metadata_json,created_at) VALUES(?,?,?,?,?)",
                (run_id, "dataset", str(dataset_dir), json.dumps(split_paths), now_iso()),
            )

            train_rows = [json.loads(x) for x in Path(split_paths["train"]).read_text(encoding="utf-8").splitlines() if x.strip()]
            schema_errors = validate_against_schema(train_rows[:500], Path("schemas/dataset_record.schema.json"))
            self._log_step(run_id, "quality", "completed" if not schema_errors else "warning", {"schema_errors": len(schema_errors)})

            self._emit(run_id, "dataset_ready", {"dataset_paths": split_paths, "schema_errors": len(schema_errors)})

            model_call_results = []
            for t in self.tasks:
                decision, response = self.router.dispatch(t)
                model_call_results.append({"task": t.id, "route": decision.provider, "response": response.text, "fallback_used": decision.fallback_used})
                self.db.insert(
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
                        json.dumps({"text": response.text, "raw": response.raw}),
                        now_iso(),
                    ),
                )
                self.db.insert(
                    "INSERT INTO cost_tokens(run_id,provider,model,input_tokens,output_tokens,created_at) VALUES(?,?,?,?,?,?)",
                    (run_id, response.provider, response.model, response.input_tokens, response.output_tokens, now_iso()),
                )

            self._log_step(run_id, "route", "completed", {"calls": len(model_call_results)})
            executed = execute_stub(model_call_results)
            validated = validate_outputs(executed)
            self._log_step(run_id, "execute_stub", "completed", {"executed": len(executed)})
            self._log_step(run_id, "validate", "completed", validated)

            self._set_state(run_id, "waiting_colab")
            self._emit(run_id, "waiting_colab", {"message": "Awaiting Colab training telemetry", "run_id": run_id})

            telemetry = self._monitor_training(run_id)

            if telemetry is None:
                self._set_state(run_id, "failed")
                self._emit(run_id, "run_failed", {"reason": "colab_timeout_or_stale", "run_id": run_id})
                return self._finalize_summary(run_id, docs, units, split_paths, validated, telemetry, failed=True)

            self._set_state(run_id, "eval")
            eval_summary = run_evaluations(self.db, run_id, split_paths)
            self._emit(run_id, "eval_gate", {"passed": eval_summary.get("gate", {}).get("passed", False)})

            test_rows = [json.loads(x) for x in Path(split_paths["test"]).read_text(encoding="utf-8").splitlines() if x.strip()]
            leakage = leakage_overlap(train_rows, test_rows)

            final = self._finalize_summary(
                run_id,
                docs,
                units,
                split_paths,
                validated,
                telemetry,
                eval_summary,
                leakage,
                failed=False,
            )

            self._set_state(run_id, "completed")
            self._emit(run_id, "run_completed", {"run_id": run_id, "gpu_minutes": telemetry.get("gpu_minutes", 0.0)})
            return final

        except Exception as exc:  # noqa: BLE001
            self._set_state(run_id, "failed")
            self._emit(run_id, "run_failed", {"error": str(exc)})
            raise

    def _monitor_training(self, run_id: str) -> Dict[str, Any] | None:
        mon_cfg = self.automation_cfg.get("automation", {}).get("monitor", {})
        poll_seconds = int(mon_cfg.get("poll_interval_seconds", 60))
        stale_seconds = int(mon_cfg.get("stale_heartbeat_seconds", 900))
        max_wait_minutes = int(mon_cfg.get("max_wait_minutes", 360))

        start = time.time()
        max_wait_seconds = max_wait_minutes * 60
        training_started = False
        last_heartbeat_ts: datetime | None = None
        last_payload: Dict[str, Any] | None = None

        while time.time() - start <= max_wait_seconds:
            payload = self.telemetry_client.fetch_latest(run_id)
            if payload:
                last_payload = payload
                hb = self._parse_ts(payload.get("timestamp") or payload.get("ts")) or datetime.now(timezone.utc)
                last_heartbeat_ts = hb
                self.db.insert(
                    "INSERT INTO training_telemetry(run_id,phase,step,loss,gpu_minutes,status,heartbeat_at,raw_json,source) VALUES(?,?,?,?,?,?,?,?,?)",
                    (
                        run_id,
                        str(payload.get("phase", "")),
                        int(payload.get("step", 0) or 0),
                        float(payload.get("loss", 0.0) or 0.0),
                        float(payload.get("gpu_minutes", 0.0) or 0.0),
                        str(payload.get("status", "")),
                        hb.isoformat(),
                        json.dumps(payload),
                        "drive_poll",
                    ),
                )

                status = str(payload.get("status", "")).lower()
                if not training_started and status in {"training", "started", "running"}:
                    training_started = True
                    self._set_state(run_id, "training")
                    self._emit(run_id, "training_started", {"step": payload.get("step", 0), "gpu_minutes": payload.get("gpu_minutes", 0.0)})

                if training_started and status in {"training", "running"}:
                    self._emit(run_id, "training_heartbeat", {"step": payload.get("step", 0), "gpu_minutes": payload.get("gpu_minutes", 0.0), "loss": payload.get("loss")}, dedupe_suffix=str(payload.get("step", 0)))

                if status in {"training_complete", "completed", "export_done", "ready_for_eval"}:
                    self._set_state(run_id, "export")
                    self._emit(run_id, "training_completed", {"gpu_minutes": payload.get("gpu_minutes", 0.0)})
                    self._emit(run_id, "export_done", {"artifact_hint": payload.get("artifact", ""), "gpu_minutes": payload.get("gpu_minutes", 0.0)})
                    return payload

                if status in {"failed", "error", "aborted"}:
                    return None

            if training_started and last_heartbeat_ts is not None:
                age = (datetime.now(timezone.utc) - last_heartbeat_ts).total_seconds()
                if age > stale_seconds:
                    self._emit(run_id, "run_stalled", {"heartbeat_age_seconds": age})
                    return None

            time.sleep(poll_seconds)

        return last_payload

    def _finalize_summary(
        self,
        run_id: str,
        docs: List[Dict[str, Any]],
        units: List[Dict[str, Any]],
        split_paths: Dict[str, str],
        validated: Dict[str, Any],
        telemetry: Dict[str, Any] | None,
        eval_summary: Dict[str, Any] | None = None,
        leakage: float = 0.0,
        failed: bool = False,
    ) -> Dict[str, Any]:
        summary = {
            "run_id": run_id,
            "docs_count": len(docs),
            "reasoning_units": len(units),
            "dataset_paths": split_paths,
            "execute_stub": validated,
            "eval": eval_summary or {},
            "leakage_overlap": leakage,
            "gpu_minutes": float((telemetry or {}).get("gpu_minutes", 0.0) or 0.0),
            "status": "failed" if failed else "completed",
            "artifacts_root": str(self.artifacts_root / run_id),
        }
        summary_path = self.artifacts_root / run_id / "summary.json"
        summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

        self.db.insert(
            "INSERT INTO artifacts(run_id,kind,path,metadata_json,created_at) VALUES(?,?,?,?,?)",
            (run_id, "summary", str(summary_path), json.dumps({}), now_iso()),
        )
        self.db.insert("UPDATE runs SET summary_json=? WHERE run_id=?", (json.dumps(summary), run_id))
        self._log_step(run_id, "report", "completed", {"summary_path": str(summary_path)})
        return summary

    def _set_state(self, run_id: str, state: str) -> None:
        self.db.insert("UPDATE runs SET status=? WHERE run_id=?", (state, run_id))

    def _log_step(self, run_id: str, step_name: str, status: str, details: Dict[str, Any]) -> None:
        self.db.insert(
            "INSERT INTO steps(run_id,step_name,status,started_at,ended_at,details_json) VALUES(?,?,?,?,?,?)",
            (run_id, step_name, status, now_iso(), now_iso(), json.dumps(details)),
        )

    def _emit(self, run_id: str, event_type: str, payload: Dict[str, Any], dedupe_suffix: str = "") -> None:
        dedupe_key = f"{run_id}:{event_type}:{dedupe_suffix or payload.get('state','')}"
        result = self.event_store.record_event(
            run_id=run_id,
            event_type=event_type,
            payload=payload,
            dedupe_key=dedupe_key,
            source="automation_daemon",
        )
        if result.get("created"):
            event = result["event"]
            event_payload = {
                "event_id": event["event_id"],
                "run_id": run_id,
                "event_type": event_type,
                "payload": payload,
                "created_at": event["created_at"],
            }
            try:
                self.notifier.dispatch(event_payload, milestone_only=True)
            except Exception as exc:  # noqa: BLE001
                self.db.insert(
                    "INSERT INTO notifications(run_id,event_id,channel,target,status,attempts,error_message,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)",
                    (run_id, event["event_id"], "dispatcher", "internal", "failed", 1, str(exc), now_iso(), now_iso()),
                )
            finally:
                self.db.insert("UPDATE events SET delivered_at=? WHERE event_id=?", (now_iso(), event["event_id"]))

    def _parse_ts(self, value: Any) -> datetime | None:
        if not value:
            return None
        if isinstance(value, (int, float)):
            return datetime.fromtimestamp(float(value), tz=timezone.utc)
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                return None
        return None



