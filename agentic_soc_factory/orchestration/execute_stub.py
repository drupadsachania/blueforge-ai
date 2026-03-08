from __future__ import annotations

from typing import Dict, List


def execute_stub(call_results: List[Dict]) -> List[Dict]:
    """Execution placeholder for safe dry-run behavior."""
    out = []
    for row in call_results:
        out.append(
            {
                "task": row["task"],
                "status": "simulated",
                "route": row["route"],
                "result": "dry_run_complete",
            }
        )
    return out
