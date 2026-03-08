from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterator


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS runs (
    run_id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL,
    status TEXT NOT NULL,
    policy_profile TEXT NOT NULL,
    summary_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS steps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    step_name TEXT NOT NULL,
    status TEXT NOT NULL,
    started_at TEXT NOT NULL,
    ended_at TEXT,
    details_json TEXT NOT NULL,
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS model_calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    provider TEXT NOT NULL,
    model TEXT NOT NULL,
    workload TEXT NOT NULL,
    latency_ms INTEGER NOT NULL,
    input_tokens INTEGER NOT NULL,
    output_tokens INTEGER NOT NULL,
    status TEXT NOT NULL,
    response_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS cost_tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    provider TEXT NOT NULL,
    model TEXT NOT NULL,
    input_tokens INTEGER NOT NULL,
    output_tokens INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS artifacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    kind TEXT NOT NULL,
    path TEXT NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS eval_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    suite_name TEXT NOT NULL,
    test_name TEXT NOT NULL,
    passed INTEGER NOT NULL,
    score REAL NOT NULL,
    details_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_name TEXT NOT NULL UNIQUE,
    timezone TEXT NOT NULL,
    schedule_json TEXT NOT NULL,
    next_run TEXT,
    last_run TEXT,
    status TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL UNIQUE,
    run_id TEXT,
    event_type TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    dedupe_key TEXT NOT NULL,
    source TEXT NOT NULL,
    created_at TEXT NOT NULL,
    delivered_at TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_events_dedupe ON events(dedupe_key);

CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT,
    event_id TEXT,
    channel TEXT NOT NULL,
    target TEXT NOT NULL,
    status TEXT NOT NULL,
    attempts INTEGER NOT NULL,
    error_message TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS training_telemetry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    phase TEXT,
    step INTEGER,
    loss REAL,
    gpu_minutes REAL,
    status TEXT,
    heartbeat_at TEXT NOT NULL,
    raw_json TEXT NOT NULL,
    source TEXT NOT NULL
);
"""


class DB:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def conn(self) -> Iterator[sqlite3.Connection]:
        c = sqlite3.connect(self.db_path)
        try:
            c.row_factory = sqlite3.Row
            yield c
            c.commit()
        finally:
            c.close()

    def initialize(self) -> None:
        with self.conn() as c:
            c.executescript(SCHEMA_SQL)

    def execute(self, query: str, params: tuple[Any, ...] = ()) -> None:
        with self.conn() as c:
            c.execute(query, params)

    def insert(self, query: str, params: tuple[Any, ...]) -> None:
        self.execute(query, params)

    def fetch_all(self, query: str, params: tuple[Any, ...] = ()) -> list[Dict[str, Any]]:
        with self.conn() as c:
            rows = c.execute(query, params).fetchall()
            return [dict(r) for r in rows]

    def fetch_one(self, query: str, params: tuple[Any, ...] = ()) -> Dict[str, Any] | None:
        rows = self.fetch_all(query, params)
        return rows[0] if rows else None
