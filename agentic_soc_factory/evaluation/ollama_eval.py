from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import requests


def run_ollama_eval(model: str, prompts: List[str], ollama_url: str = "http://localhost:11434/api/generate") -> List[Dict]:
    rows = []
    for p in prompts:
        r = requests.post(ollama_url, json={"model": model, "prompt": p, "stream": False}, timeout=60)
        r.raise_for_status()
        body = r.json()
        rows.append({"prompt": p, "response": body.get("response", ""), "raw": body})
    return rows


def save_eval(rows: List[Dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
