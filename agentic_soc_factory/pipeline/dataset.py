from __future__ import annotations

import json
import random
import warnings
from pathlib import Path
from typing import Dict, List

EXAMPLE_TYPES = {
    "positive": "Well-formed detection workflow recommendation",
    "negative": "Flawed reasoning with gaps model must learn to avoid",
    "boundary": "Edge case requiring specific decision criteria",
}


def workflow_unit_to_chatml(unit: Dict, example_type: str = "positive") -> Dict:
    threat_scenario = unit.get("threat_scenario", "Unknown threat")

    user_prompt = f"""Threat Scenario: {threat_scenario}

You are a detection engineering expert. Analyze this threat and provide:
1. Relevant signals and telemetry to correlate
2. MITRE ATT&CK mapping and threat behavior
3. UDM/detection schema fields needed
4. Coverage gaps in current detections
5. Detection rule logic and implementation
6. Validation constraints and false positive mitigation

Reason through each step, considering signal dependencies, latencies, and coverage gaps."""

    assistant_response = format_workflow_reasoning_response(unit, example_type)

    return {
        "id": unit.get("metadata", {}).get("source_corpus", "unknown").replace("/", "_"),
        "tag": _classify_tag(unit),
        "example_type": example_type,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert detection engineer reasoning through security detection workflows. "
                    "Provide structured analysis covering signals, telemetry, rules, gaps, and validation. "
                    "Output valid JSON for tooling integration."
                ),
            },
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": assistant_response},
        ],
        "metadata": {
            "source_path": unit.get("source_corpus", ""),
            "threat_category": unit.get("threat_scenario", ""),
            "domain": unit.get("metadata", {}).get("domain", "D9"),
            "secondary_domains": unit.get("metadata", {}).get("secondary_domains", []),
            "example_type": example_type,
            "signal_count": len(unit.get("signals", [])),
            "gap_count": len(unit.get("gap_analysis", {}).get("missing_gaps", [])),
        },
    }


def format_workflow_reasoning_response(unit: Dict, example_type: str) -> str:
    response_obj = {
        "signals": unit.get("signals", []),
        "correlation": unit.get("correlation", {}),
        "udm_mapping": unit.get("udm_mapping", {}),
        "gap_analysis": unit.get("gap_analysis", {}),
        "rule_logic": unit.get("rule_logic", {}),
        "implementation_code": unit.get("implementation_code", {}),
        "validation": unit.get("validation", {}),
        "metadata": {
            **unit.get("metadata", {}),
            "example_type": "boundary_case" if example_type == "boundary" else example_type,
        },
        # Optional backward-compatible field for downstream tool execution flows.
        "tool_call": {
            "recommended_next_action": _recommend_tool_call(unit),
            "domains": [unit.get("metadata", {}).get("domain", "D9")]
            + unit.get("metadata", {}).get("secondary_domains", []),
            "requires_approval": example_type == "negative",
        },
    }

    if example_type == "negative":
        response_obj["correction"] = {
            "issue": "This detection logic has gaps; here is the fix",
            "problem_analysis": "Missing correlation window and false positive mitigation",
            "corrected_approach": "See gap_analysis.recommendations",
        }

    return json.dumps(response_obj, indent=2, ensure_ascii=True)


def _classify_tag(unit: Dict) -> str:
    domains = [unit.get("metadata", {}).get("domain", "D9")]
    domains.extend(unit.get("metadata", {}).get("secondary_domains", []))

    gap_count = len(unit.get("gap_analysis", {}).get("missing_gaps", []))
    if gap_count > 2:
        return "gap_analysis"
    if len(domains) > 1:
        return "multi_domain_chain"
    return "single_domain"


def _recommend_tool_call(unit: Dict) -> Dict:
    primary = unit.get("metadata", {}).get("domain", "D9")
    secondary = unit.get("metadata", {}).get("secondary_domains", [])
    domains = [primary] + secondary

    if "D2" in domains:
        return {
            "domain": "D2",
            "function": "generate_detection_rule",
            "parameters": {
                "threat": unit.get("threat_scenario", ""),
                "rule_format": unit.get("implementation_code", {}).get("rule_format", "udm_query"),
            },
        }
    if "D9" in domains:
        return {
            "domain": "D9",
            "function": "analyze_coverage_gaps",
            "parameters": {
                "threat_category": unit.get("threat_scenario", ""),
                "current_signals": [s.get("name", "") for s in unit.get("signals", [])],
            },
        }
    if "D5" in domains:
        return {
            "domain": "D5",
            "function": "map_threat_to_attack_surface",
            "parameters": {
                "threat": unit.get("threat_scenario", ""),
                "techniques": unit.get("correlation", {}).get("mitre_techniques", []),
            },
        }
    return {
        "domain": primary,
        "function": "analyze_threat_workflow",
        "parameters": {"threat": unit.get("threat_scenario", "")},
    }


def workflow_units_to_chatml_examples(
    units: List[Dict], example_distribution: Dict[str, float] | None = None
) -> List[Dict]:
    if example_distribution is None:
        example_distribution = {"positive": 0.60, "negative": 0.25, "boundary": 0.15}

    examples = []
    shuffled = units[:]
    random.shuffle(shuffled)

    n_positive = int(len(shuffled) * example_distribution["positive"])
    n_negative = int(len(shuffled) * example_distribution["negative"])

    for idx, unit in enumerate(shuffled):
        if idx < n_positive:
            example_type = "positive"
        elif idx < n_positive + n_negative:
            example_type = "negative"
        else:
            example_type = "boundary"
        examples.append(workflow_unit_to_chatml(unit, example_type))

    return examples


def split_dataset(examples: List[Dict], seed: int = 42) -> Dict[str, List[Dict]]:
    rng = random.Random(seed)
    by_tag: Dict[str, List[Dict]] = {}

    for ex in examples:
        tag = ex.get("tag", "single_domain")
        by_tag.setdefault(tag, []).append(ex)

    train: List[Dict] = []
    val: List[Dict] = []
    test: List[Dict] = []

    for _, exs in by_tag.items():
        rng.shuffle(exs)
        n = len(exs)
        n_train = int(n * 0.8)
        n_val = int(n * 0.1)
        train.extend(exs[:n_train])
        val.extend(exs[n_train : n_train + n_val])
        test.extend(exs[n_train + n_val :])

    rng.shuffle(train)
    rng.shuffle(val)
    rng.shuffle(test)
    return {"train": train, "val": val, "test": test}


def write_jsonl(records: List[Dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=True) + "\n")


def compile_and_write_dataset(
    workflow_units: List[Dict],
    out_dir: Path,
    example_distribution: Dict[str, float] | None = None,
) -> Dict[str, str]:
    examples = workflow_units_to_chatml_examples(workflow_units, example_distribution)
    splits = split_dataset(examples)
    out: Dict[str, str] = {}
    for split_name, rows in splits.items():
        p = out_dir / f"{split_name}.jsonl"
        write_jsonl(rows, p)
        out[split_name] = str(p)
    return out


# Backward-compatible wrapper (deprecated)
def units_to_examples(units: List[Dict]) -> List[Dict]:
    warnings.warn(
        "units_to_examples() is deprecated; use workflow_units_to_chatml_examples()",
        DeprecationWarning,
        stacklevel=2,
    )
    return workflow_units_to_chatml_examples(units)
