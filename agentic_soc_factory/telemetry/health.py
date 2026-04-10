from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Any, Set

class PipelineHealthCheck:
    def __init__(self, min_records: int = 5):
        self.min_records = min_records

    def check_dataset(self, dataset_path: Path) -> Dict[str, Any]:
        issues = []
        records = []
        
        try:
            with open(dataset_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        records.append(json.loads(line))
        except Exception as e:
            return {"status": "unhealthy", "issues": [f"Failed to read dataset: {str(e)}"]}

        # Check size
        if len(records) < self.min_records:
            issues.append(f"Dataset too small: found {len(records)}, need {self.min_records}")

        # Check schema (simple check for TDD pass)
        for i, record in enumerate(records):
            if "messages" not in record or not isinstance(record["messages"], list):
                issues.append(f"Schema mismatch: missing or invalid 'messages' in record {i}")
                break

        status = "unhealthy" if issues else "healthy"
        return {
            "status": status,
            "issues": issues,
            "metrics": {
                "record_count": len(records)
            }
        }

class SignalDriftDetector:
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold
        self.baseline_vocabulary: Set[str] = set()

    def _get_tokens(self, records: List[Dict]) -> Set[str]:
        tokens = set()
        for record in records:
            for msg in record.get("messages", []):
                content = msg.get("content", "").lower()
                # Simple whitespace tokenization for baseline
                tokens.update(content.split())
        return tokens

    def fit(self, baseline_records: List[Dict]):
        self.baseline_vocabulary = self._get_tokens(baseline_records)

    def check_drift(self, new_records: List[Dict]) -> Dict[str, Any]:
        new_vocabulary = self._get_tokens(new_records)
        
        if not self.baseline_vocabulary:
            return {"drift_detected": False, "drift_score": 0.0, "reason": "No baseline fitted"}

        # Calculate overlap (Jaccard-like distance)
        intersection = self.baseline_vocabulary.intersection(new_vocabulary)
        union = self.baseline_vocabulary.union(new_vocabulary)
        
        if not union:
            return {"drift_detected": False, "drift_score": 0.0}

        overlap_score = len(intersection) / len(union)
        drift_score = 1.0 - overlap_score
        
        return {
            "drift_detected": drift_score > self.threshold,
            "drift_score": drift_score,
            "baseline_vocab_size": len(self.baseline_vocabulary),
            "new_vocab_size": len(new_vocabulary)
        }
