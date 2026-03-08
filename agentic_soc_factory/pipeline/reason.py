from __future__ import annotations

import re
from typing import Any, Dict, List

DOMAIN_HINTS = {
    "D1": ["ingest", "parser", "udm", "forwarder", "log"],
    "D2": ["yara", "rule", "query", "detect"],
    "D3": ["api", "sdk", "integration", "endpoint"],
    "D4": ["threat intel", "ioc", "misp", "virustotal"],
    "D5": ["mitre", "attack", "tactic", "technique"],
    "D6": ["soar", "playbook", "automation", "response"],
    "D7": ["asset", "discovery", "inventory", "surface"],
    "D8": ["vulnerability", "cve", "patch"],
    "D9": ["gap", "risk", "assessment", "score"],
}


def infer_domain(text: str) -> str:
    low = text.lower()
    best = "D9"
    best_score = 0
    for domain, hints in DOMAIN_HINTS.items():
        score = sum(1 for h in hints if h in low)
        if score > best_score:
            best_score = score
            best = domain
    return best


def extract_required_params(text: str) -> List[str]:
    fields = set()
    for m in re.findall(r"([a-zA-Z_]+\.[a-zA-Z0-9_\.]+)", text):
        fields.add(m)
    return sorted(fields)[:20]


def build_reasoning_unit(doc: Dict[str, Any]) -> Dict[str, Any]:
    text = doc["text"]
    domain = infer_domain(text)
    return {
        "source_path": doc["path"],
        "title": doc["title"],
        "domain": domain,
        "callable_action": "analyze_and_generate_tool_call",
        "required_params": extract_required_params(text),
        "refusal_boundaries": [
            "undocumented_udm_field",
            "undocumented_api_endpoint",
            "undocumented_function",
        ],
        "gap_questions": [
            "Which data source and log type are in scope?",
            "What threshold/time window should detection use?",
            "Should execution require manual approval?",
        ],
    }


def distill_docs_to_reasoning_units(docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [build_reasoning_unit(d) for d in docs]
