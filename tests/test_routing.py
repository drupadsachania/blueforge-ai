from agentic_soc_factory.models import Task
from agentic_soc_factory.routing.policy import select_route_for_task


def test_policy_route_selection():
    policy = {
        "retries": 1,
        "token_policy": {
            "local_max": 3000,
            "multi_hop_min": 2,
            "local_rule": {"provider": "ollama", "model": "qwen3.5:4b"},
            "multi_hop_rule": {"provider": "openai", "model": "o3-mini"},
        },
        "workload_routing": {
            "cheap_extraction": {"provider": "gemini", "model": "gemini-2.0-flash"},
            "deep_reasoning/planning": {"provider": "openai", "model": "o3-mini"},
            "format_repair/guardrails": {"provider": "anthropic", "model": "claude-3-5-haiku-latest"},
        },
    }
    d = select_route_for_task(Task(id="1", text="x", workload="deep_reasoning/planning", reasoning_hops=3), policy)
    assert d.provider == "openai"
    assert d.model == "o3-mini"
    assert d.retries == 1


def test_token_override_prefers_local():
    policy = {
        "retries": 1,
        "token_policy": {
            "local_max": 3000,
            "multi_hop_min": 2,
            "local_rule": {"provider": "ollama", "model": "qwen3.5:4b"},
        },
        "workload_routing": {
            "cheap_extraction": {"provider": "gemini", "model": "gemini-2.0-flash"},
            "deep_reasoning/planning": {"provider": "openai", "model": "o3-mini"},
            "format_repair/guardrails": {"provider": "anthropic", "model": "claude-3-5-haiku-latest"},
        },
    }
    d = select_route_for_task(Task(id="1", text="x", token_estimate=1200), policy)
    assert d.provider == "ollama"
