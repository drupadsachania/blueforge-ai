import pytest
from pathlib import Path
import json
import shutil
import os
from agentic_soc_factory.telemetry.health import PipelineHealthCheck, SignalDriftDetector

@pytest.fixture
def local_tmp_dir():
    path = Path("tests/tmp_telemetry")
    path.mkdir(parents=True, exist_ok=True)
    yield path
    if path.exists():
        shutil.rmtree(path)

def test_signal_drift_detector_identifies_divergence(local_tmp_dir):
    # RED: This should fail as SignalDriftDetector is not implemented.
    
    # Baseline: mostly login/auth logs
    baseline_records = [
        {"messages": [{"role": "user", "content": "login auth signal"}]} for _ in range(20)
    ]
    
    # New data: mostly cloud/api logs (significant drift)
    new_records = [
        {"messages": [{"role": "user", "content": "cloud aws api signal"}]} for _ in range(20)
    ]
    
    detector = SignalDriftDetector(threshold=0.5)
    detector.fit(baseline_records)
    
    drift_report = detector.check_drift(new_records)
    
    assert drift_report["drift_detected"] == True
    assert drift_report["drift_score"] > 0.5

def test_health_check_identifies_small_dataset(local_tmp_dir):
    # Create a dummy dataset with only 2 records (minimum threshold will be 5)
    dataset_path = local_tmp_dir / "train.jsonl"
    records = [
        {"id": "1", "messages": []},
        {"id": "2", "messages": []}
    ]
    with open(dataset_path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
            
    checker = PipelineHealthCheck(min_records=5)
    health_report = checker.check_dataset(dataset_path)
    
    assert health_report["status"] == "unhealthy"
    assert any("Dataset too small" in issue for issue in health_report["issues"])

def test_health_check_identifies_schema_mismatch(local_tmp_dir):
    # Create a dataset with missing required fields
    dataset_path = local_tmp_dir / "train.jsonl"
    records = [
        {"wrong_field": "data"} for _ in range(10)
    ]
    with open(dataset_path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
            
    checker = PipelineHealthCheck()
    health_report = checker.check_dataset(dataset_path)
    
    assert health_report["status"] == "unhealthy"
    assert any("Schema mismatch" in issue for issue in health_report["issues"])
