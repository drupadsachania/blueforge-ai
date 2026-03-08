from pathlib import Path

from fastapi.testclient import TestClient

from agentic_soc_factory.automation.event_api import create_event_app


def test_event_api_post_and_get(tmp_path: Path):
    app = create_event_app(tmp_path / "db.sqlite")
    client = TestClient(app)

    resp = client.post(
        "/events",
        json={"run_id": "r1", "event_type": "run_started", "payload": {"x": 1}, "dedupe_key": "k1", "source": "test"},
    )
    assert resp.status_code == 200
    assert resp.json()["created"] is True

    resp2 = client.get("/events", params={"run_id": "r1"})
    assert resp2.status_code == 200
    assert len(resp2.json()["items"]) == 1
