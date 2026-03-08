import json
from pathlib import Path

from agentic_soc_factory.automation.daemon import FactoryAutomationDaemon
from agentic_soc_factory.db import DB
from agentic_soc_factory.providers.anthropic_adapter import AnthropicClient
from agentic_soc_factory.providers.gemini_adapter import GeminiClient
from agentic_soc_factory.providers.openai_adapter import OpenAIClient
from agentic_soc_factory.routing.router import Router


def test_daemon_skip_when_active(tmp_path: Path):
    db = DB(tmp_path / "db.sqlite")
    db.initialize()
    db.insert(
        "INSERT INTO runs(run_id,created_at,status,policy_profile,summary_json) VALUES(?,?,?,?,?)",
        ("run_active", "2026-01-01T00:00:00+00:00", "training", "default", "{}"),
    )

    tasks_path = tmp_path / "tasks.json"
    tasks_path.write_text(json.dumps([{"id": "t1", "text": "x"}]), encoding="utf-8")
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "a.md").write_text("ingest logs", encoding="utf-8")

    router = Router(
        {
            "retries": 0,
            "fallback_order": ["openai", "anthropic", "gemini"],
            "circuit_breaker": {"failure_threshold": 3, "cooldown_seconds": 1},
            "workload_routing": {
                "cheap_extraction": {"provider": "gemini", "model": "m"},
                "deep_reasoning/planning": {"provider": "openai", "model": "m"},
                "format_repair/guardrails": {"provider": "anthropic", "model": "m"},
            },
        },
        {"openai": OpenAIClient(api_key=""), "anthropic": AnthropicClient(api_key=""), "gemini": GeminiClient(api_key="")},
    )

    cfg = {
        "automation": {
            "automation": {
                "timezone": "Asia/Kolkata",
                "schedule": {"hour": 10, "minute": 0},
                "concurrency_policy": "skip",
                "lock_file": str(tmp_path / "lock"),
            },
            "notifier": {"webhook": {"enabled": False}, "email": {"enabled": False}},
            "telemetry": {"drive": {"enabled": False}, "local_fallback": {"enabled": False}},
        }
    }

    daemon = FactoryAutomationDaemon(
        db=db,
        router=router,
        configs=cfg,
        tasks_path=tasks_path,
        corpus_root=corpus,
        artifacts_root=tmp_path / "artifacts",
    )

    daemon.run_scheduled()

    ev = db.fetch_all("SELECT * FROM events WHERE event_type='run_skipped_active'")
    assert len(ev) == 1
