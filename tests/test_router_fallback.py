from dataclasses import dataclass

from agentic_soc_factory.models import ModelResponse, Task
from agentic_soc_factory.providers.base import ProviderClient
from agentic_soc_factory.routing.router import Router


class FailingProvider(ProviderClient):
    provider_name = "fail"

    def generate(self, prompt, model, context):
        raise RuntimeError("boom")


@dataclass
class OkProvider(ProviderClient):
    provider_name: str = "ok"

    def generate(self, prompt, model, context):
        return ModelResponse(provider=self.provider_name, model=model, text='{"ok":true}', raw={}, latency_ms=1)


def test_router_fallback_on_failure():
    policy = {
        "retries": 0,
        "fallback_order": ["openai", "anthropic", "gemini"],
        "circuit_breaker": {"failure_threshold": 1, "cooldown_seconds": 1},
        "workload_routing": {
            "cheap_extraction": {"provider": "openai", "model": "m1"},
        },
    }
    router = Router(policy, {"openai": FailingProvider(), "anthropic": OkProvider("anthropic")})
    _, resp = router.dispatch(Task(id="1", text="x", workload="cheap_extraction"))
    assert resp.provider == "anthropic"
