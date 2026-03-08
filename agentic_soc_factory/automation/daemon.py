from __future__ import annotations

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict

from zoneinfo import ZoneInfo

from agentic_soc_factory.automation.common import now_iso
from agentic_soc_factory.automation.drive_telemetry import DriveTelemetryClient
from agentic_soc_factory.automation.events import EventStore
from agentic_soc_factory.automation.lock import FileLock
from agentic_soc_factory.automation.notifications import NotificationDispatcher
from agentic_soc_factory.automation.runner import AutomatedRunExecutor
from agentic_soc_factory.db import DB
from agentic_soc_factory.models import Task
from agentic_soc_factory.routing.classifier import classify_workload
from agentic_soc_factory.routing.router import Router


class FactoryAutomationDaemon:
    def __init__(
        self,
        db: DB,
        router: Router,
        configs: Dict[str, Any],
        tasks_path: Path,
        corpus_root: Path,
        artifacts_root: Path,
        policy_profile: str = "default",
    ) -> None:
        self.db = db
        self.router = router
        self.configs = configs
        self.automation_cfg = configs.get("automation", {})
        self.tasks_path = tasks_path
        self.corpus_root = corpus_root
        self.artifacts_root = artifacts_root
        self.policy_profile = policy_profile

        lock_file = Path(self.automation_cfg.get("automation", {}).get("lock_file", "artifacts/factory.lock"))
        self.lock = FileLock(lock_file)

        self.event_store = EventStore(db)
        self.notifier = NotificationDispatcher(db, self.automation_cfg)
        self.telemetry_client = DriveTelemetryClient(self.automation_cfg)

    def start(self) -> None:
        if not self.lock.acquire():
            raise RuntimeError("Factory daemon already running (lock exists)")

        try:
            while True:
                next_run = self._next_scheduled_run()
                self._upsert_job_row(
                    job_name="daily_factory_run",
                    timezone=self.automation_cfg.get("automation", {}).get("timezone", "Asia/Kolkata"),
                    schedule=self.automation_cfg.get("automation", {}).get("schedule", {}),
                    next_run=next_run.isoformat(),
                    status="scheduled",
                )

                wait_seconds = max(0.0, (next_run - datetime.now(tz=next_run.tzinfo)).total_seconds())
                time.sleep(wait_seconds)
                self.run_scheduled()
        finally:
            self.lock.release()

    def _next_scheduled_run(self) -> datetime:
        cfg = self.automation_cfg.get("automation", {})
        tz_name = cfg.get("timezone", "Asia/Kolkata")
        hour = int(cfg.get("schedule", {}).get("hour", 10))
        minute = int(cfg.get("schedule", {}).get("minute", 0))

        tz = ZoneInfo(tz_name)
        now = datetime.now(tz=tz)
        candidate = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if candidate <= now:
            candidate = candidate + timedelta(days=1)
        return candidate

    def run_scheduled(self) -> None:
        self._upsert_job_row(job_name="daily_factory_run", timezone=self.automation_cfg.get("automation", {}).get("timezone", "Asia/Kolkata"), schedule=self.automation_cfg.get("automation", {}).get("schedule", {}), next_run=None, status="running")

        concurrency = self.automation_cfg.get("automation", {}).get("concurrency_policy", "skip")
        active = self.db.fetch_one(
            "SELECT run_id,status FROM runs WHERE status IN ('queued','running','waiting_colab','training','export','eval') ORDER BY created_at DESC LIMIT 1"
        )
        if active and concurrency == "skip":
            self.event_store.record_event(
                run_id=active.get("run_id"),
                event_type="run_skipped_active",
                payload={"active_run_id": active.get("run_id"), "active_state": active.get("status")},
                dedupe_key=f"skip:{active.get('run_id')}:{now_iso()[:16]}",
                source="scheduler",
            )
            self._upsert_job_row(job_name="daily_factory_run", timezone=self.automation_cfg.get("automation", {}).get("timezone", "Asia/Kolkata"), schedule=self.automation_cfg.get("automation", {}).get("schedule", {}), next_run=None, status="idle")
            return

        executor = AutomatedRunExecutor(
            db=self.db,
            router=self.router,
            automation_cfg=self.automation_cfg,
            event_store=self.event_store,
            notifier=self.notifier,
            telemetry_client=self.telemetry_client,
            tasks=self._load_tasks(self.tasks_path),
            corpus_root=self.corpus_root,
            artifacts_root=self.artifacts_root,
            policy_profile=self.policy_profile,
        )
        executor.run_once(trigger="scheduled")
        self._upsert_job_row(job_name="daily_factory_run", timezone=self.automation_cfg.get("automation", {}).get("timezone", "Asia/Kolkata"), schedule=self.automation_cfg.get("automation", {}).get("schedule", {}), next_run=None, status="idle")

    def run_once_now(self) -> Dict[str, Any]:
        executor = AutomatedRunExecutor(
            db=self.db,
            router=self.router,
            automation_cfg=self.automation_cfg,
            event_store=self.event_store,
            notifier=self.notifier,
            telemetry_client=self.telemetry_client,
            tasks=self._load_tasks(self.tasks_path),
            corpus_root=self.corpus_root,
            artifacts_root=self.artifacts_root,
            policy_profile=self.policy_profile,
        )
        return executor.run_once(trigger="manual")

    def _load_tasks(self, path: Path) -> list[Task]:
        rows = json.loads(path.read_text(encoding="utf-8"))
        out = []
        for r in rows:
            txt = r["text"]
            out.append(
                Task(
                    id=r["id"],
                    text=txt,
                    workload=r.get("workload") or classify_workload(txt),
                    context=r.get("context", {}),
                    token_estimate=int(r.get("token_estimate", max(1, len(txt.split())))),
                    reasoning_hops=int(r.get("reasoning_hops", 1)),
                    creative=bool(r.get("creative", False)),
                )
            )
        return out

    def _upsert_job_row(self, job_name: str, timezone: str, schedule: Dict[str, Any], next_run: str | None, status: str) -> None:
        existing = self.db.fetch_one("SELECT id FROM jobs WHERE job_name=?", (job_name,))
        if existing:
            self.db.insert(
                "UPDATE jobs SET timezone=?, schedule_json=?, next_run=?, last_run=?, status=?, updated_at=? WHERE job_name=?",
                (timezone, json.dumps(schedule), next_run, now_iso(), status, now_iso(), job_name),
            )
        else:
            self.db.insert(
                "INSERT INTO jobs(job_name,timezone,schedule_json,next_run,last_run,status,updated_at) VALUES(?,?,?,?,?,?,?)",
                (job_name, timezone, json.dumps(schedule), next_run, None, status, now_iso()),
            )
