from __future__ import annotations

import json
import time
from typing import Any, Dict

import requests

from agentic_soc_factory.models import ModelResponse
from agentic_soc_factory.providers.base import ProviderClient


class OllamaClient(ProviderClient):
    provider_name = "ollama"

    def __init__(self, base_url: str = "http://localhost:11434/api/generate") -> None:
        self.base_url = base_url

    def generate(self, prompt: str, model: str, context: Dict[str, Any]) -> ModelResponse:
        t0 = time.time()
        payload = {"model": model, "prompt": prompt, "stream": False}
        r = requests.post(self.base_url, data=json.dumps(payload), headers={"content-type": "application/json"}, timeout=60)
        r.raise_for_status()
        body = r.json()
        return ModelResponse(
            provider=self.provider_name,
            model=model,
            text=body.get("response", ""),
            raw=body,
            latency_ms=int((time.time() - t0) * 1000),
            input_tokens=int(body.get("prompt_eval_count", 0)),
            output_tokens=int(body.get("eval_count", 0)),
        )
