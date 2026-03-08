from __future__ import annotations

import json
import time
from typing import Any, Dict

import requests

from agentic_soc_factory.models import ModelResponse
from agentic_soc_factory.providers.base import ProviderClient


class AnthropicClient(ProviderClient):
    provider_name = "anthropic"

    def __init__(self, api_key: str, base_url: str = "https://api.anthropic.com") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def generate(self, prompt: str, model: str, context: Dict[str, Any]) -> ModelResponse:
        if not self.api_key:
            return self._mock(prompt, model)

        t0 = time.time()
        payload = {
            "model": model,
            "max_tokens": 512,
            "messages": [{"role": "user", "content": prompt}],
        }
        r = requests.post(
            f"{self.base_url}/v1/messages",
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            data=json.dumps(payload),
            timeout=45,
        )
        r.raise_for_status()
        body = r.json()
        text = body.get("content", [{}])[0].get("text", "")
        usage = body.get("usage", {})
        return ModelResponse(
            provider=self.provider_name,
            model=model,
            text=text,
            raw=body,
            latency_ms=int((time.time() - t0) * 1000),
            input_tokens=int(usage.get("input_tokens", 0)),
            output_tokens=int(usage.get("output_tokens", 0)),
        )

    def _mock(self, prompt: str, model: str) -> ModelResponse:
        return ModelResponse(
            provider=self.provider_name,
            model=model,
            text=json.dumps({"mode": "mock", "provider": "anthropic", "prompt": prompt[:160]}),
            raw={"mock": True},
            latency_ms=50,
            input_tokens=len(prompt.split()),
            output_tokens=28,
        )
