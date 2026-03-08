import json
from pathlib import Path

from agentic_soc_factory.agents import FactorySupervisorAgent
from agentic_soc_factory.db import DB
from agentic_soc_factory.models import Task
from agentic_soc_factory.providers.anthropic_adapter import AnthropicClient
from agentic_soc_factory.providers.gemini_adapter import GeminiClient
from agentic_soc_factory.providers.openai_adapter import OpenAIClient
from agentic_soc_factory.routing.router import Router


def test_factory_supervisor_run(tmp_path: Path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "d.md").write_text("yara rule and soar playbook", encoding="utf-8")

    db = DB(tmp_path / "factory.db")
    db.initialize()

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
        {
            "openai": OpenAIClient(api_key=""),
            "anthropic": AnthropicClient(api_key=""),
            "gemini": GeminiClient(api_key=""),
        },
    )

    supervisor = FactorySupervisorAgent(db=db, router=router)
    out = supervisor.run(
        corpus_root=corpus,
        artifacts_root=tmp_path / "artifacts",
        tasks=[Task(id="x", text="extract patterns", workload="cheap_extraction")],
    )

    assert out["run_id"].startswith("run_")
    assert "cost" in out
    assert "ops" in out
    assert (tmp_path / "artifacts" / out["run_id"] / "summary.json").exists()

    rows = db.fetch_all("SELECT summary_json FROM runs WHERE run_id=?", (out["run_id"],))
    assert json.loads(rows[0]["summary_json"])["run_id"] == out["run_id"]
