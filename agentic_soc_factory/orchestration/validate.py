from __future__ import annotations

from typing import Dict, List


def validate_outputs(executed: List[Dict]) -> Dict:
    total = len(executed)
    success = sum(1 for e in executed if e.get("status") == "simulated")
    return {
        "total": total,
        "success": success,
        "success_rate": (success / total) if total else 0.0,
        "failed": total - success,
    }
