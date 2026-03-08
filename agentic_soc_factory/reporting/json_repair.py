from __future__ import annotations

import json
from typing import Any, Dict


def parse_or_repair_json(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        cleaned = text.strip()
        if not cleaned.startswith("{"):
            cleaned = "{" + cleaned
        if not cleaned.endswith("}"):
            cleaned = cleaned + "}"
        return json.loads(cleaned)
