from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Task:
    id: str
    text: str
    workload: str = "cheap_extraction"
    context: Dict[str, Any] = field(default_factory=dict)
    token_estimate: int = 0
    reasoning_hops: int = 1
    creative: bool = False


@dataclass
class ModelResponse:
    provider: str
    model: str
    text: str
    raw: Dict[str, Any]
    latency_ms: int
    input_tokens: int = 0
    output_tokens: int = 0


@dataclass
class PhaseResult:
    step_name: str
    status: str
    details: Dict[str, Any]
