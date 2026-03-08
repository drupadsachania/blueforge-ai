import json
from pathlib import Path

from agentic_soc_factory.automation.drive_telemetry import DriveTelemetryClient


def test_local_telemetry_read(tmp_path: Path):
    telemetry_dir = tmp_path / "telemetry"
    telemetry_dir.mkdir()
    file_path = telemetry_dir / "run_abc_telemetry.json"
    file_path.write_text(json.dumps({"run_id": "run_abc", "status": "training", "gpu_minutes": 7.5}), encoding="utf-8")

    cfg = {
        "telemetry": {
            "drive": {"enabled": False, "file_name_pattern": "{run_id}_telemetry.json"},
            "local_fallback": {"enabled": True, "folder": str(telemetry_dir)},
        }
    }

    client = DriveTelemetryClient(cfg)
    out = client.fetch_latest("run_abc")
    assert out is not None
    assert out["gpu_minutes"] == 7.5
