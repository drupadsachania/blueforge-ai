from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


def write_run_summary(run_root: Path, summary: Dict) -> Path:
    run_root.mkdir(parents=True, exist_ok=True)
    out = run_root / "summary.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return out
