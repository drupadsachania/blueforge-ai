from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from agentic_soc_factory.models import Task


@dataclass
class RouteDecision:
    workload: str
    provider: str
    model: str
    retries: int
    requested_provider: str = ""
    fallback_used: bool = False


def _infer_workload(task: Task) -> str:
    if task.workload and task.workload != "auto":
        return task.workload

    if task.reasoning_hops >= 2:
        return "deep_reasoning/planning"
    if task.creative:
        return "cheap_extraction"
    if task.token_estimate >= 3000:
        return "cheap_extraction"
    return "format_repair/guardrails"


def _build_decision(workload: str, provider: str, model: str, retries: int) -> RouteDecision:
    return RouteDecision(
        workload=workload,
        provider=provider,
        model=model,
        retries=retries,
        requested_provider=provider,
        fallback_used=False,
    )


def select_route_for_task(task: Task, policy: Dict) -> RouteDecision:
    routing = policy.get("workload_routing", {})
    workload = _infer_workload(task)
    if workload not in routing:
        workload = "cheap_extraction"
    rule = routing[workload]
    retries = int(policy.get("retries", 2))

    if task.token_estimate and task.token_estimate < int(policy.get("token_policy", {}).get("local_max", 3000)):
        local_rule = policy.get("token_policy", {}).get("local_rule", {})
        if local_rule:
            return _build_decision(
                workload="cheap_extraction",
                provider=local_rule.get("provider", rule["provider"]),
                model=local_rule.get("model", rule["model"]),
                retries=retries,
            )

    if task.reasoning_hops >= int(policy.get("token_policy", {}).get("multi_hop_min", 2)):
        deep_rule = policy.get("token_policy", {}).get("multi_hop_rule", {})
        if deep_rule:
            return _build_decision(
                workload="deep_reasoning/planning",
                provider=deep_rule.get("provider", rule["provider"]),
                model=deep_rule.get("model", rule["model"]),
                retries=retries,
            )

    return _build_decision(
        workload=workload,
        provider=rule["provider"],
        model=rule["model"],
        retries=retries,
    )
