from __future__ import annotations
import yaml
from typing import Dict, List, Any

class BaseScraper:
    def __init__(self):
        pass

class SigmaGitHubScraper(BaseScraper):
    def parse_sigma_yaml(self, yaml_content: str) -> Dict[str, Any]:
        data = yaml.safe_load(yaml_content)
        
        signals = []
        detection = data.get("detection", {})
        for key, val in detection.items():
            if key == "condition":
                continue
            if isinstance(val, dict):
                for sub_key, sub_val in val.items():
                    signals.append({
                        "name": sub_key,
                        "value": str(sub_val),
                        "source": f"sigma_{data.get('logsource', {}).get('service', 'unknown')}"
                    })
            
        return {
            "threat_scenario": data.get("title", "Unknown"),
            "signals": signals,
            "correlation": {
                "mitre_techniques": data.get("tags", []),
                "logic_summary": data.get("description", "")
            },
            "metadata": {
                "source": "sigma_github",
                "sigma_id": data.get("id", "")
            }
        }
