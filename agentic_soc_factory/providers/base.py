from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict

from agentic_soc_factory.models import ModelResponse


class ProviderClient(ABC):
    provider_name: str

    @abstractmethod
    def generate(self, prompt: str, model: str, context: Dict[str, Any]) -> ModelResponse:
        raise NotImplementedError
