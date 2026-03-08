from __future__ import annotations


def classify_workload(text: str) -> str:
    low = text.lower()
    if any(k in low for k in ["plan", "architecture", "chain", "reason"]):
        return "deep_reasoning/planning"
    if any(k in low for k in ["repair", "schema", "json", "guardrail", "fix"]):
        return "format_repair/guardrails"
    return "cheap_extraction"
