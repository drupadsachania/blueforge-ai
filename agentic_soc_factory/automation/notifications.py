from __future__ import annotations

import json
import os
import smtplib
import ssl
import time
from email.mime.text import MIMEText
from typing import Any, Dict

import requests

from agentic_soc_factory.automation.common import now_iso
from agentic_soc_factory.db import DB


class NotificationDispatcher:
    def __init__(self, db: DB, automation_cfg: Dict[str, Any]) -> None:
        self.db = db
        self.cfg = automation_cfg
        self.retry_attempts = int(automation_cfg.get("automation", {}).get("retry", {}).get("attempts", 3))
        self.backoff_seconds = int(automation_cfg.get("automation", {}).get("retry", {}).get("backoff_seconds", 20))

    def dispatch(self, event: Dict[str, Any], milestone_only: bool = True) -> None:
        event_type = event.get("event_type", "")
        if milestone_only and not self._is_milestone(event_type):
            return

        webhook_cfg = self.cfg.get("notifier", {}).get("webhook", {})
        if webhook_cfg.get("enabled", False):
            self._send_with_retry(
                channel="webhook",
                target=webhook_cfg.get("url", ""),
                fn=lambda: self._post_webhook(event, webhook_cfg),
                run_id=event.get("run_id"),
                event_id=event.get("event_id"),
            )

        email_cfg = self.cfg.get("notifier", {}).get("email", {})
        if email_cfg.get("enabled", False):
            self._send_with_retry(
                channel="email",
                target=os.getenv("SMTP_TO", ""),
                fn=lambda: self._send_email(event),
                run_id=event.get("run_id"),
                event_id=event.get("event_id"),
            )

    def _is_milestone(self, event_type: str) -> bool:
        milestones = {
            "run_started",
            "dataset_ready",
            "waiting_colab",
            "training_started",
            "training_heartbeat",
            "training_completed",
            "export_done",
            "eval_gate",
            "run_failed",
            "run_completed",
            "run_stalled",
        }
        return event_type in milestones

    def _post_webhook(self, event: Dict[str, Any], webhook_cfg: Dict[str, Any]) -> None:
        url = webhook_cfg.get("url", "")
        if not url:
            raise RuntimeError("webhook URL is empty")

        headers = {"Content-Type": "application/json"}
        secret = os.getenv("WEBHOOK_SIGNING_SECRET", "")
        if secret:
            headers["X-Factory-Signature"] = secret

        timeout = int(webhook_cfg.get("timeout_seconds", 10))
        resp = requests.post(url, data=json.dumps(event), headers=headers, timeout=timeout)
        resp.raise_for_status()

    def _send_email(self, event: Dict[str, Any]) -> None:
        host = os.getenv("SMTP_HOST", "")
        port = int(os.getenv("SMTP_PORT", "587"))
        user = os.getenv("SMTP_USER", "")
        password = os.getenv("SMTP_PASSWORD", "")
        mail_from = os.getenv("SMTP_FROM", "")
        mail_to = os.getenv("SMTP_TO", "")
        use_tls = os.getenv("SMTP_USE_TLS", "true").lower() == "true"

        if not host or not mail_from or not mail_to:
            raise RuntimeError("SMTP env vars are incomplete")

        subject = f"[SOC Factory] {event.get('event_type')} ({event.get('run_id')})"
        body = json.dumps(event, indent=2)
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = mail_from
        msg["To"] = mail_to

        context = ssl.create_default_context()
        with smtplib.SMTP(host, port, timeout=20) as server:
            if use_tls:
                server.starttls(context=context)
            if user:
                server.login(user, password)
            server.sendmail(mail_from, [mail_to], msg.as_string())

    def _send_with_retry(self, channel: str, target: str, fn, run_id: str | None, event_id: str | None) -> None:
        last_error = None
        for attempt in range(1, self.retry_attempts + 1):
            try:
                fn()
                self.db.insert(
                    "INSERT INTO notifications(run_id,event_id,channel,target,status,attempts,error_message,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)",
                    (run_id, event_id, channel, target, "sent", attempt, None, now_iso(), now_iso()),
                )
                return
            except Exception as exc:  # noqa: BLE001
                last_error = str(exc)
                self.db.insert(
                    "INSERT INTO notifications(run_id,event_id,channel,target,status,attempts,error_message,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)",
                    (run_id, event_id, channel, target, "failed", attempt, last_error, now_iso(), now_iso()),
                )
                if attempt < self.retry_attempts:
                    time.sleep(self.backoff_seconds)

        if last_error:
            raise RuntimeError(f"{channel} notification failed: {last_error}")
