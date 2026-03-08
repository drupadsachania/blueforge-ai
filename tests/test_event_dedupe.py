from pathlib import Path

from agentic_soc_factory.automation.events import EventStore
from agentic_soc_factory.db import DB


def test_event_dedupe(tmp_path: Path):
    db = DB(tmp_path / "db.sqlite")
    db.initialize()
    store = EventStore(db)

    a = store.record_event(run_id="r1", event_type="dataset_ready", payload={"x": 1}, dedupe_key="k1")
    b = store.record_event(run_id="r1", event_type="dataset_ready", payload={"x": 1}, dedupe_key="k1")

    assert a["created"] is True
    assert b["created"] is False
    rows = db.fetch_all("SELECT * FROM events")
    assert len(rows) == 1
