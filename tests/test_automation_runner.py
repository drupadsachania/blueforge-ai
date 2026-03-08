from datetime import datetime, timezone
from pathlib import Path

from agentic_soc_factory.automation.events import EventStore
from agentic_soc_factory.automation.notifications import NotificationDispatcher
from agentic_soc_factory.automation.runner import AutomatedRunExecutor
from agentic_soc_factory.db import DB
from agentic_soc_factory.models import Task
from agentic_soc_factory.providers.anthropic_adapter import AnthropicClient
from agentic_soc_factory.providers.gemini_adapter import GeminiClient
from agentic_soc_factory.providers.openai_adapter import OpenAIClient
from agentic_soc_factory.routing.router import Router


class FakeTelemetry:
    def __init__(self):
        self.calls = 0

    def fetch_latest(self, run_id):
        self.calls += 1
        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        if self.calls == 1:
            return {"run_id": run_id, "status": "training", "phase": "training", "step": 10, "loss": 1.2, "gpu_minutes": 3.0, "ts": now}
        return {"run_id": run_id, "status": "training_complete", "phase": "export", "step": 20, "loss": 0.9, "gpu_minutes": 8.5, "artifact": "m.gguf", "ts": now}


def test_automation_runner_cycle(tmp_path: Path):
    db = DB(tmp_path / "db.sqlite")
    db.initialize()

    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "d.md").write_text("ingest logs and detection rule", encoding="utf-8")

    router = Router(
        {
            "retries": 0,
            "fallback_order": ["openai", "anthropic", "gemini"],
            "circuit_breaker": {"failure_threshold": 3, "cooldown_seconds": 10},
            "workload_routing": {
                "cheap_extraction": {"provider": "gemini", "model": "gemini-2.0-flash"},
                "deep_reasoning/planning": {"provider": "openai", "model": "o3-mini"},
                "format_repair/guardrails": {"provider": "anthropic", "model": "claude-3-5-haiku-latest"},
            },
        },
        {"openai": OpenAIClient(api_key=""), "anthropic": AnthropicClient(api_key=""), "gemini": GeminiClient(api_key="")},
    )

    cfg = {
        "automation": {"monitor": {"poll_interval_seconds": 0, "stale_heartbeat_seconds": 99999999, "max_wait_minutes": 1}},
        "notifier": {"webhook": {"enabled": False}, "email": {"enabled": False}},
        "telemetry": {"drive": {"enabled": False}, "local_fallback": {"enabled": False}},
    }

    runner = AutomatedRunExecutor(
        db=db,
        router=router,
        automation_cfg=cfg,
        event_store=EventStore(db),
        notifier=NotificationDispatcher(db, cfg),
        telemetry_client=FakeTelemetry(),
        tasks=[Task(id="t1", text="test", workload="cheap_extraction")],
        corpus_root=corpus,
        artifacts_root=tmp_path / "artifacts",
    )

    out = runner.run_once(trigger="test")
    assert out["status"] == "completed"
    assert out["gpu_minutes"] == 8.5

    run = db.fetch_one("SELECT status FROM runs WHERE run_id=?", (out["run_id"],))
    assert run and run["status"] == "completed"
    ev = db.fetch_all("SELECT event_type FROM events WHERE run_id=?", (out["run_id"],))
    names = {e["event_type"] for e in ev}
    assert "dataset_ready" in names
    assert "training_started" in names
    assert "run_completed" in names
