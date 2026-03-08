from pathlib import Path

import requests

from agentic_soc_factory.automation.notifications import NotificationDispatcher
from agentic_soc_factory.db import DB


class _Resp:
    def __init__(self, status_code: int):
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError("boom")


def test_webhook_retry(monkeypatch, tmp_path: Path):
    db = DB(tmp_path / "db.sqlite")
    db.initialize()
    cfg = {
        "automation": {"retry": {"attempts": 2, "backoff_seconds": 0}},
        "notifier": {"webhook": {"enabled": True, "url": "http://localhost/events", "timeout_seconds": 1}, "email": {"enabled": False}},
    }

    calls = {"n": 0}

    def _post(*args, **kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            return _Resp(500)
        return _Resp(200)

    monkeypatch.setattr(requests, "post", _post)

    d = NotificationDispatcher(db, cfg)
    d.dispatch({"event_id": "e1", "run_id": "r1", "event_type": "run_started", "payload": {}}, milestone_only=True)

    rows = db.fetch_all("SELECT * FROM notifications ORDER BY id")
    assert len(rows) == 2
    assert rows[0]["status"] == "failed"
    assert rows[1]["status"] == "sent"
