import json
from pathlib import Path

from agentic_soc_factory.db import DB
from agentic_soc_factory.models import Task
from agentic_soc_factory.orchestration.orchestrator import run_pipeline
from agentic_soc_factory.providers.anthropic_adapter import AnthropicClient
from agentic_soc_factory.providers.gemini_adapter import GeminiClient
from agentic_soc_factory.providers.openai_adapter import OpenAIClient
from agentic_soc_factory.routing.router import Router


def test_end_to_end_dry_run(tmp_path: Path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "doc1.md").write_text("Ingest logs and build yara rules for detection", encoding="utf-8")

    db = DB(tmp_path / "factory.db")
    db.initialize()

    providers = {
        "openai": OpenAIClient(api_key=""),
        "anthropic": AnthropicClient(api_key=""),
        "gemini": GeminiClient(api_key=""),
    }
    policy = {
        "retries": 0,
        "fallback_order": ["openai", "anthropic", "gemini"],
        "circuit_breaker": {"failure_threshold": 3, "cooldown_seconds": 60},
        "workload_routing": {
            "cheap_extraction": {"provider": "gemini", "model": "gemini-2.0-flash"},
            "deep_reasoning/planning": {"provider": "openai", "model": "o3-mini"},
            "format_repair/guardrails": {"provider": "anthropic", "model": "claude-3-5-haiku-latest"},
        },
    }

    router = Router(policy, providers)
    tasks = [Task(id="x", text="test", workload="cheap_extraction")]

    summary = run_pipeline(
        db=db,
        router=router,
        corpus_root=corpus,
        artifacts_root=tmp_path / "artifacts",
        tasks=tasks,
    )

    assert summary["docs_count"] == 1
    assert (tmp_path / "artifacts" / summary["run_id"] / "dataset" / "train.jsonl").exists()
    assert "gate" in summary["eval"]

    runs = db.fetch_all("SELECT * FROM runs")
    assert len(runs) == 1
    assert json.loads(runs[0]["summary_json"])["run_id"] == summary["run_id"]
