from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent


def load_structured(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return {}
    # Config files are stored as JSON-compatible YAML for zero extra parser deps.
    return json.loads(text)


def load_configs(config_dir: Path | None = None, env_file: Path | None = None) -> Dict[str, Any]:
    if env_file:
        load_dotenv(env_file)
    else:
        default_env = BASE_DIR / ".env"
        if default_env.exists():
            load_dotenv(default_env)

    cfg_dir = config_dir or (BASE_DIR / "config")
    routing_path = cfg_dir / "routing.yaml"
    if not routing_path.exists():
        # Backward compatibility for older repository snapshots.
        routing_path = cfg_dir / "router_policy.yaml"

    return {
        "providers": load_structured(cfg_dir / "providers.yaml"),
        "router_policy": load_structured(routing_path),
        "automation": load_structured(cfg_dir / "automation.yaml"),
    }
