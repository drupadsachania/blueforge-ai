from agentic_soc_factory.agents import ModelRouterAgent
from agentic_soc_factory.models import Task


def test_model_router_agent_local_policy():
    policy = {
        "retries": 1,
        "token_policy": {
            "local_max": 3000,
            "local_rule": {"provider": "ollama", "model": "qwen3.5:4b"},
            "multi_hop_min": 2,
            "multi_hop_rule": {"provider": "openai", "model": "o3-mini"},
        },
        "workload_routing": {
            "cheap_extraction": {"provider": "gemini", "model": "gemini-2.0-flash"},
            "deep_reasoning/planning": {"provider": "openai", "model": "o3-mini"},
            "format_repair/guardrails": {"provider": "anthropic", "model": "claude-3-5-haiku-latest"},
        },
    }
    agent = ModelRouterAgent(policy)
    decision = agent.choose(Task(id="1", text="short", token_estimate=500, reasoning_hops=1))
    assert decision["provider"] == "ollama"
