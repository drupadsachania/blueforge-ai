from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from agentic_soc_factory.evaluation.ollama_eval import run_ollama_eval


def _load_cases(path: Path) -> List[Dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def compare_contains(response: str, expected_contains: List[str]) -> float:
    if not expected_contains:
        return 1.0
    hit = sum(1 for token in expected_contains if token.lower() in response.lower())
    return hit / len(expected_contains)


def run_fixed_suite(model: str, suite_path: Path, output_path: Path) -> Dict:
    cases = _load_cases(suite_path)
    prompts = [c["prompt"] for c in cases]
    rows = run_ollama_eval(model=model, prompts=prompts)

    scored = []
    for case, row in zip(cases, rows, strict=True):
        score = compare_contains(row["response"], case.get("expected_contains", []))
        scored.append({"name": case["name"], "score": score, "response": row["response"]})

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(scored, indent=2), encoding="utf-8")
    avg = sum(x["score"] for x in scored) / len(scored) if scored else 0.0
    return {"avg_score": avg, "count": len(scored), "output": str(output_path)}
