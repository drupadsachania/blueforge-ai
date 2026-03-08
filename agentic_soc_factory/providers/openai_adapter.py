from __future__ import annotations

import json
import time
from typing import Any, Dict

import requests

from agentic_soc_factory.models import ModelResponse
from agentic_soc_factory.providers.base import ProviderClient


class OpenAIClient(ProviderClient):
    provider_name = "openai"

    def __init__(self, api_key: str, base_url: str = "https://api.openai.com/v1") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def generate(self, prompt: str, model: str, context: Dict[str, Any]) -> ModelResponse:
        if not self.api_key:
            return self._mock(prompt, model)

        t0 = time.time()
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
        }
        r = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps(payload),
            timeout=45,
        )
        r.raise_for_status()
        body = r.json()
        text = body["choices"][0]["message"]["content"]
        usage = body.get("usage", {})
        return ModelResponse(
            provider=self.provider_name,
            model=model,
            text=text,
            raw=body,
            latency_ms=int((time.time() - t0) * 1000),
            input_tokens=int(usage.get("prompt_tokens", 0)),
            output_tokens=int(usage.get("completion_tokens", 0)),
        )

    def _mock(self, prompt: str, model: str) -> ModelResponse:
        return ModelResponse(
            provider=self.provider_name,
            model=model,
            text=json.dumps({"mode": "mock", "provider": "openai", "prompt": prompt[:160]}),
            raw={"mock": True},
            latency_ms=40,
            input_tokens=len(prompt.split()),
            output_tokens=32,
        )
