from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import uvicorn

from agentic_soc_factory.agents import FactorySupervisorAgent
from agentic_soc_factory.automation.daemon import FactoryAutomationDaemon
from agentic_soc_factory.automation.event_api import create_event_app
from agentic_soc_factory.config import load_configs
from agentic_soc_factory.db import DB
from agentic_soc_factory.export.gguf import export_commands, write_modelfile
from agentic_soc_factory.models import Task
from agentic_soc_factory.providers.anthropic_adapter import AnthropicClient
from agentic_soc_factory.providers.gemini_adapter import GeminiClient
from agentic_soc_factory.providers.ollama_adapter import OllamaClient
from agentic_soc_factory.providers.openai_adapter import OpenAIClient
from agentic_soc_factory.routing.classifier import classify_workload
from agentic_soc_factory.routing.router import Router


def parse_tasks(tasks_path: Path) -> list[Task]:
    rows = json.loads(tasks_path.read_text(encoding="utf-8"))
    return [
        Task(
            id=r["id"],
            text=r["text"],
            workload=r.get("workload") or classify_workload(r["text"]),
            context=r.get("context", {}),
            token_estimate=int(r.get("token_estimate", max(1, len(r["text"].split())))),
            reasoning_hops=int(r.get("reasoning_hops", 1)),
            creative=bool(r.get("creative", False)),
        )
        for r in rows
    ]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Agentic SOC LLM Factory")
    sub = p.add_subparsers(dest="cmd", required=True)

    supervisor_cmd = sub.add_parser("supervisor", help="Run FactorySupervisorAgent")
    supervisor_cmd.add_argument("--tasks", required=True)
    supervisor_cmd.add_argument("--corpus-root", default=os.getenv("FACTORY_CORPUS_ROOT", "secops_rag"))
    supervisor_cmd.add_argument("--db", default=os.getenv("FACTORY_DB_PATH", "artifacts/factory.db"))
    supervisor_cmd.add_argument("--artifacts-root", default=os.getenv("FACTORY_ARTIFACTS_ROOT", "artifacts"))
    supervisor_cmd.add_argument("--profile", default="default")

    daemon_cmd = sub.add_parser("daemon", help="Start scheduled automation daemon")
    daemon_cmd.add_argument("--tasks", default=os.getenv("FACTORY_TASKS_FILE", "tasks.sample.json"))
    daemon_cmd.add_argument("--corpus-root", default=os.getenv("FACTORY_CORPUS_ROOT", "secops_rag"))
    daemon_cmd.add_argument("--db", default=os.getenv("FACTORY_DB_PATH", "artifacts/factory.db"))
    daemon_cmd.add_argument("--artifacts-root", default=os.getenv("FACTORY_ARTIFACTS_ROOT", "artifacts"))
    daemon_cmd.add_argument("--profile", default="default")

    daemon_once_cmd = sub.add_parser("daemon-once", help="Run one automation cycle immediately")
    daemon_once_cmd.add_argument("--tasks", default=os.getenv("FACTORY_TASKS_FILE", "tasks.sample.json"))
    daemon_once_cmd.add_argument("--corpus-root", default=os.getenv("FACTORY_CORPUS_ROOT", "secops_rag"))
    daemon_once_cmd.add_argument("--db", default=os.getenv("FACTORY_DB_PATH", "artifacts/factory.db"))
    daemon_once_cmd.add_argument("--artifacts-root", default=os.getenv("FACTORY_ARTIFACTS_ROOT", "artifacts"))
    daemon_once_cmd.add_argument("--profile", default="default")

    event_api_cmd = sub.add_parser("event-api", help="Run local event ingestion API")
    event_api_cmd.add_argument("--db", default=os.getenv("FACTORY_DB_PATH", "artifacts/factory.db"))
    event_api_cmd.add_argument("--host", default="0.0.0.0")
    event_api_cmd.add_argument("--port", type=int, default=8787)

    export_cmd = sub.add_parser("export", help="Print GGUF export commands + write Modelfile")
    export_cmd.add_argument("--merged-model-dir", required=True)
    export_cmd.add_argument("--gguf-out", required=True)
    export_cmd.add_argument("--ollama-bundle", default="artifacts/ollama_bundle")

    return p


def _build_runtime(args) -> tuple[DB, Router, dict]:
    configs = load_configs()
    providers_cfg = configs["providers"]
    providers = {
        "openai": OpenAIClient(
            api_key=providers_cfg.get("openai", {}).get("api_key", ""),
            base_url=providers_cfg.get("openai", {}).get("base_url", "https://api.openai.com/v1"),
        ),
        "anthropic": AnthropicClient(
            api_key=providers_cfg.get("anthropic", {}).get("api_key", ""),
            base_url=providers_cfg.get("anthropic", {}).get("base_url", "https://api.anthropic.com"),
        ),
        "gemini": GeminiClient(
            api_key=providers_cfg.get("gemini", {}).get("api_key", ""),
            base_url=providers_cfg.get("gemini", {}).get("base_url", "https://generativelanguage.googleapis.com/v1beta/models"),
        ),
        "ollama": OllamaClient(
            base_url=providers_cfg.get("ollama", {}).get("base_url", "http://localhost:11434/api/generate")
        ),
    }
    db = DB(Path(args.db))
    db.initialize()
    router = Router(configs["router_policy"], providers)
    return db, router, configs


def main() -> None:
    args = build_parser().parse_args()

    if args.cmd == "supervisor":
        db, router, _ = _build_runtime(args)
        supervisor = FactorySupervisorAgent(db=db, router=router)
        summary = supervisor.run(
            corpus_root=Path(args.corpus_root),
            artifacts_root=Path(args.artifacts_root),
            tasks=parse_tasks(Path(args.tasks)),
            policy_profile=args.profile,
        )
        print(json.dumps(summary, indent=2))
        return

    if args.cmd == "daemon":
        db, router, configs = _build_runtime(args)
        daemon = FactoryAutomationDaemon(
            db=db,
            router=router,
            configs=configs,
            tasks_path=Path(args.tasks),
            corpus_root=Path(args.corpus_root),
            artifacts_root=Path(args.artifacts_root),
            policy_profile=args.profile,
        )
        daemon.start()
        return

    if args.cmd == "daemon-once":
        db, router, configs = _build_runtime(args)
        daemon = FactoryAutomationDaemon(
            db=db,
            router=router,
            configs=configs,
            tasks_path=Path(args.tasks),
            corpus_root=Path(args.corpus_root),
            artifacts_root=Path(args.artifacts_root),
            policy_profile=args.profile,
        )
        summary = daemon.run_once_now()
        print(json.dumps(summary, indent=2))
        return

    if args.cmd == "event-api":
        app = create_event_app(Path(args.db))
        uvicorn.run(app, host=args.host, port=args.port, log_level="info")
        return

    if args.cmd == "export":
        merged = Path(args.merged_model_dir)
        gguf = Path(args.gguf_out)
        cmds = export_commands(merged, gguf)
        modelfile = write_modelfile(Path(args.ollama_bundle), "soc-architect-qwen35-4b", gguf.name)
        print(cmds)
        print(f"\nWrote Ollama Modelfile: {modelfile}")


if __name__ == "__main__":
    main()
