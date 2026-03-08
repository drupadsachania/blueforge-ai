from __future__ import annotations

import json
import uuid
from typing import Any, Dict

from agentic_soc_factory.automation.common import now_iso
from agentic_soc_factory.db import DB


class EventStore:
    def __init__(self, db: DB) -> None:
        self.db = db

    def record_event(
        self,
        event_type: str,
        payload: Dict[str, Any],
        run_id: str | None = None,
        dedupe_key: str | None = None,
        source: str = "internal",
    ) -> Dict[str, Any]:
        dkey = dedupe_key or f"{run_id or 'global'}:{event_type}:{json.dumps(payload, sort_keys=True)}"
        existing = self.db.fetch_one("SELECT * FROM events WHERE dedupe_key=?", (dkey,))
        if existing:
            return {"created": False, "event": existing}

        event_id = f"evt_{uuid.uuid4().hex[:16]}"
        row = {
            "event_id": event_id,
            "run_id": run_id,
            "event_type": event_type,
            "payload_json": json.dumps(payload),
            "dedupe_key": dkey,
            "source": source,
            "created_at": now_iso(),
        }
        self.db.insert(
            "INSERT INTO events(event_id,run_id,event_type,payload_json,dedupe_key,source,created_at,delivered_at) VALUES(?,?,?,?,?,?,?,?)",
            (
                row["event_id"],
                row["run_id"],
                row["event_type"],
                row["payload_json"],
                row["dedupe_key"],
                row["source"],
                row["created_at"],
                None,
            ),
        )
        return {"created": True, "event": row}

    def list_events(self, run_id: str | None = None, limit: int = 200) -> list[Dict[str, Any]]:
        if run_id:
            return self.db.fetch_all(
                "SELECT * FROM events WHERE run_id=? ORDER BY created_at DESC LIMIT ?",
                (run_id, limit),
            )
        return self.db.fetch_all("SELECT * FROM events ORDER BY created_at DESC LIMIT ?", (limit,))
