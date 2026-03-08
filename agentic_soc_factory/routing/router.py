from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Dict

from agentic_soc_factory.models import ModelResponse, Task
from agentic_soc_factory.providers.base import ProviderClient
from agentic_soc_factory.routing.policy import RouteDecision, select_route_for_task


@dataclass
class ProviderState:
    failures: int = 0
    open_until: float = 0.0


class Router:
    def __init__(self, policy: Dict, providers: Dict[str, ProviderClient]) -> None:
        self.policy = policy
        self.providers = providers
        self.states: Dict[str, ProviderState] = {
            name: ProviderState() for name in providers.keys()
        }
        self.failure_threshold = int(policy.get("circuit_breaker", {}).get("failure_threshold", 3))
        self.cooldown_seconds = int(policy.get("circuit_breaker", {}).get("cooldown_seconds", 60))

    def _is_open(self, provider_name: str) -> bool:
        state = self.states[provider_name]
        return state.open_until > time.time()

    def _mark_failure(self, provider_name: str) -> None:
        state = self.states[provider_name]
        state.failures += 1
        if state.failures >= self.failure_threshold:
            state.open_until = time.time() + self.cooldown_seconds

    def _mark_success(self, provider_name: str) -> None:
        state = self.states[provider_name]
        state.failures = 0
        state.open_until = 0

    def dispatch(self, task: Task) -> tuple[RouteDecision, ModelResponse]:
        decision = select_route_for_task(task, self.policy)
        fallback = self.policy.get("fallback_order", [])
        candidates = [decision.provider] + [p for p in fallback if p != decision.provider]
        last_error = None

        for provider_name in candidates:
            if provider_name not in self.providers:
                continue
            if self._is_open(provider_name):
                continue

            client = self.providers[provider_name]
            for _ in range(decision.retries + 1):
                try:
                    response = client.generate(task.text, decision.model, task.context)
                    self._mark_success(provider_name)
                    decision.fallback_used = provider_name != decision.requested_provider
                    decision.provider = provider_name
                    return decision, response
                except Exception as exc:  # noqa: BLE001
                    last_error = exc
                    self._mark_failure(provider_name)

        raise RuntimeError(f"All providers failed: {last_error}")
