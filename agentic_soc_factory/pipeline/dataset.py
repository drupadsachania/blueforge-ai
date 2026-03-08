from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Dict, List

TAGS = [
    "single_domain",
    "multi_domain_chain",
    "gap_analysis",
    "refusal",
    "edge_case",
]


def _sample_tag(domain: str) -> str:
    if domain in {"D1", "D2", "D4", "D6"}:
        return random.choice(TAGS[:3])
    return random.choice(TAGS)


def units_to_examples(units: List[Dict]) -> List[Dict]:
    examples = []
    for idx, u in enumerate(units, start=1):
        tag = _sample_tag(u["domain"])
        examples.append(
            {
                "id": f"ex_{idx:06d}",
                "tag": tag,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an Agentic SOC Architect. Output only valid JSON.",
                    },
                    {
                        "role": "user",
                        "content": f"Using context from {u['title']}, generate a safe action plan.",
                    },
                    {
                        "role": "assistant",
                        "content": json.dumps(
                            {
                                "tool_call": {
                                    "domain": u["domain"],
                                    "function": u["callable_action"],
                                    "parameters": {"required_params": u["required_params"][:6]},
                                    "dry_run": True,
                                    "requires_approval": u["domain"] in ["D6", "D7"],
                                }
                            }
                        ),
                    },
                ],
                "metadata": {
                    "source_path": u["source_path"],
                    "refusal_boundaries": u["refusal_boundaries"],
                    "gap_questions": u["gap_questions"],
                },
            }
        )
    return examples


def split_dataset(examples: List[Dict], seed: int = 42) -> Dict[str, List[Dict]]:
    rng = random.Random(seed)
    shuffled = examples[:]
    rng.shuffle(shuffled)
    n = len(shuffled)
    n_train = int(n * 0.8)
    n_val = int(n * 0.1)
    return {
        "train": shuffled[:n_train],
        "val": shuffled[n_train : n_train + n_val],
        "test": shuffled[n_train + n_val :],
    }


def write_jsonl(records: List[Dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=True) + "\n")


def compile_and_write_dataset(units: List[Dict], out_dir: Path) -> Dict[str, str]:
    examples = units_to_examples(units)
    splits = split_dataset(examples)
    out = {}
    for split_name, rows in splits.items():
        p = out_dir / f"{split_name}.jsonl"
        write_jsonl(rows, p)
        out[split_name] = str(p)
    return out
