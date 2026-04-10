from __future__ import annotations

import os
import json
import base64
from pathlib import Path
from typing import Any, Dict, Optional

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

def load_dotenv_safe(env_file: Path | None = None):
    if env_file:
        load_dotenv(env_file)
    else:
        default_env = BASE_DIR / ".env"
        if default_env.exists():
            load_dotenv(default_env)

def get_secret(key: str, default: Any = None) -> Any:
    """Retrieve secret from environment with priority."""
    return os.environ.get(key, default)

def get_gdrive_creds() -> Optional[Dict[str, Any]]:
    """
    Retrieve GDrive credentials from:
    1. Base64 environment variable (GDRIVE_CREDS_B64)
    2. File path environment variable (GDRIVE_CREDS_FILE)
    3. Default path (secrets/gdrive_service_account.json)
    """
    b64_creds = get_secret("GDRIVE_CREDS_B64")
    if b64_creds:
        return json.loads(base64.b64decode(b64_creds).decode("utf-8"))
    
    creds_file = get_secret("GDRIVE_CREDS_FILE", BASE_DIR / "secrets" / "gdrive_service_account.json")
    creds_path = Path(creds_file)
    if creds_path.exists():
        return json.loads(creds_path.read_text(encoding="utf-8"))
    
    return None

def load_structured(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return {}
    return json.loads(text)

def load_configs(config_dir: Path | None = None, env_file: Path | None = None) -> Dict[str, Any]:
    load_dotenv_safe(env_file)
    
    cfg_dir = config_dir or (BASE_DIR / "config")
    routing_path = cfg_dir / "routing.yaml"
    if not routing_path.exists():
        routing_path = cfg_dir / "router_policy.yaml"

    return {
        "providers": load_structured(cfg_dir / "providers.yaml"),
        "router_policy": load_structured(routing_path),
        "automation": load_structured(cfg_dir / "automation.yaml"),
    }
