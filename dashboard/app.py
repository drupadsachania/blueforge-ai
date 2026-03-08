from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List

import streamlit as st

DB_PATH = Path("artifacts/factory.db")

st.set_page_config(page_title="Agentic SOC LLM Factory", layout="wide")
st.title("Agentic SOC LLM Factory Dashboard")

if not DB_PATH.exists():
    st.warning("No database found yet. Run orchestrator/daemon first.")
    st.stop()

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row


def q(sql: str, params: tuple[Any, ...] = ()) -> List[dict[str, Any]]:
    try:
        cur = conn.execute(sql, params)
        return [dict(r) for r in cur.fetchall()]
    except Exception:  # noqa: BLE001
        return []


runs = q("SELECT run_id, created_at, status, policy_profile FROM runs ORDER BY created_at DESC")
model_calls = q("SELECT run_id, provider, model, workload, latency_ms, input_tokens, output_tokens, status FROM model_calls")
evals = q("SELECT run_id, suite_name, test_name, passed, score, created_at FROM eval_results")
artifacts = q("SELECT run_id, kind, path, created_at FROM artifacts")
costs = q("SELECT run_id, provider, model, input_tokens, output_tokens FROM cost_tokens")
jobs = q("SELECT job_name, timezone, next_run, last_run, status, updated_at FROM jobs ORDER BY updated_at DESC")
events = q("SELECT event_id, run_id, event_type, source, created_at, delivered_at FROM events ORDER BY created_at DESC")
notifs = q("SELECT run_id, event_id, channel, target, status, attempts, error_message, updated_at FROM notifications ORDER BY updated_at DESC")
telemetry = q("SELECT run_id, phase, step, loss, gpu_minutes, status, heartbeat_at FROM training_telemetry ORDER BY heartbeat_at DESC")

left, mid, right, far = st.columns(4)
left.metric("Runs", len(runs))
mid.metric("Model Calls", len(model_calls))
right.metric("Events", len(events))
far.metric("Notifications", len(notifs))

active_state = "idle"
for run in runs:
    if run["status"] in {"queued", "running", "waiting_colab", "training", "export", "eval"}:
        active_state = str(run["status"])
        break

last_heartbeat_age = "n/a"
if telemetry:
    hb = str(telemetry[0].get("heartbeat_at", ""))
    try:
        hb_dt = datetime.fromisoformat(hb.replace("Z", "+00:00"))
        age = int((datetime.now(timezone.utc) - hb_dt).total_seconds())
        last_heartbeat_age = f"{age}s"
    except ValueError:
        pass

gpu_minutes = max(float(t.get("gpu_minutes") or 0.0) for t in telemetry) if telemetry else 0.0
notif_failures = sum(1 for n in notifs if n.get("status") == "failed")
next_run = jobs[0].get("next_run", "n/a") if jobs else "n/a"

st.subheader("Automation Status")
a, b, c, d = st.columns(4)
a.metric("Active Run State", active_state)
b.metric("Last Heartbeat Age", last_heartbeat_age)
c.metric("GPU Minutes (latest)", f"{gpu_minutes:.2f}")
d.metric("Notification Failures", notif_failures)
st.caption(f"Next Scheduled Run: {next_run}")

st.subheader("Scheduler Jobs")
st.dataframe(jobs, use_container_width=True)

st.subheader("Phase and Stage Progress")
st.dataframe(runs, use_container_width=True)

st.subheader("Routing and Token Metrics")
if model_calls:
    agg: dict[tuple[str, str], dict[str, Any]] = {}
    for row in model_calls:
        k = (str(row["provider"]), str(row["workload"]))
        if k not in agg:
            agg[k] = {
                "provider": k[0],
                "workload": k[1],
                "calls": 0,
                "total_latency_ms": 0.0,
                "input_tokens": 0,
                "output_tokens": 0,
            }
        agg[k]["calls"] += 1
        agg[k]["total_latency_ms"] += float(row.get("latency_ms") or 0)
        agg[k]["input_tokens"] += int(row.get("input_tokens") or 0)
        agg[k]["output_tokens"] += int(row.get("output_tokens") or 0)

    rows = []
    for item in agg.values():
        calls = item["calls"] or 1
        rows.append(
            {
                "provider": item["provider"],
                "workload": item["workload"],
                "calls": item["calls"],
                "avg_latency_ms": round(item["total_latency_ms"] / calls, 2),
                "input_tokens": item["input_tokens"],
                "output_tokens": item["output_tokens"],
            }
        )
    st.dataframe(rows, use_container_width=True)
else:
    st.info("No model call records yet.")

st.subheader("Cost Governor View")
if costs:
    cagg: dict[tuple[str, str], dict[str, Any]] = {}
    for row in costs:
        k = (str(row["provider"]), str(row["model"]))
        if k not in cagg:
            cagg[k] = {"provider": k[0], "model": k[1], "calls": 0, "input_tokens": 0, "output_tokens": 0}
        cagg[k]["calls"] += 1
        cagg[k]["input_tokens"] += int(row.get("input_tokens") or 0)
        cagg[k]["output_tokens"] += int(row.get("output_tokens") or 0)
    rows = []
    for item in cagg.values():
        item["total_tokens"] = item["input_tokens"] + item["output_tokens"]
        rows.append(item)
    rows.sort(key=lambda x: x["total_tokens"], reverse=True)
    st.dataframe(rows, use_container_width=True)
else:
    st.info("No token records yet.")

st.subheader("Training Telemetry")
st.dataframe(telemetry, use_container_width=True)

st.subheader("Event Timeline")
st.dataframe(events, use_container_width=True)

st.subheader("Notification Delivery")
st.dataframe(notifs, use_container_width=True)

st.subheader("Failure Diagnostics")
fail_events = [e for e in events if e.get("event_type") in {"run_failed", "run_stalled"}]
if fail_events:
    st.dataframe(fail_events, use_container_width=True)
else:
    st.info("No failure events recorded.")

st.subheader("Eval and Gate Status")
st.dataframe(evals, use_container_width=True)

st.subheader("Artifacts and Deployment")
st.dataframe(artifacts, use_container_width=True)

if runs:
    options = [str(r["run_id"]) for r in runs]
    chosen = st.selectbox("Run Drill-down", options)
    st.markdown("### Raw Responses")
    details = q(
        "SELECT task_id, provider, model, workload, response_json FROM model_calls WHERE run_id = ?",
        (chosen,),
    )
    for row in details:
        with st.expander(f"Task {row['task_id']} - {row['provider']} / {row['model']}"):
            payload = json.loads(row["response_json"])
            st.code(json.dumps(payload, indent=2), language="json")

conn.close()
