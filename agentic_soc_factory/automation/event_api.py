from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agentic_soc_factory.automation.events import EventStore
from agentic_soc_factory.db import DB


class EventIn(BaseModel):
    run_id: str | None = None
    event_type: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    dedupe_key: str | None = None
    source: str = "webhook"


class EventOut(BaseModel):
    created: bool
    event: Dict[str, Any]


def create_event_app(db_path: Path) -> FastAPI:
    db = DB(db_path)
    db.initialize()
    store = EventStore(db)

    app = FastAPI(title="SOC Factory Event API", version="1.0.0")

    @app.get("/health")
    def health() -> Dict[str, str]:
        return {"status": "ok"}

    @app.post("/events", response_model=EventOut)
    def post_event(evt: EventIn) -> Dict[str, Any]:
        try:
            return store.record_event(
                run_id=evt.run_id,
                event_type=evt.event_type,
                payload=evt.payload,
                dedupe_key=evt.dedupe_key,
                source=evt.source,
            )
        except Exception as exc:  # noqa: BLE001
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @app.get("/events")
    def list_events(run_id: str | None = None, limit: int = 200) -> Dict[str, Any]:
        return {"items": store.list_events(run_id=run_id, limit=limit)}

    @app.get("/jobs")
    def list_jobs() -> Dict[str, Any]:
        rows = db.fetch_all("SELECT * FROM jobs ORDER BY updated_at DESC")
        return {"items": rows}

    return app
