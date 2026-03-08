from __future__ import annotations

import io
import json
import os
from pathlib import Path
from typing import Any, Dict

from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


class DriveTelemetryClient:
    def __init__(self, automation_cfg: Dict[str, Any]) -> None:
        self.cfg = automation_cfg

    def fetch_latest(self, run_id: str) -> Dict[str, Any] | None:
        data = None
        if self.cfg.get("telemetry", {}).get("drive", {}).get("enabled", False):
            data = self._fetch_drive(run_id)
        if data is None and self.cfg.get("telemetry", {}).get("local_fallback", {}).get("enabled", True):
            data = self._fetch_local(run_id)
        return self._normalize(data) if data else None

    def _normalize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        out = dict(payload)
        if "timestamp" not in out and "ts" in out:
            out["timestamp"] = out.get("ts")
        return out

    def _fetch_local(self, run_id: str) -> Dict[str, Any] | None:
        folder = Path(self.cfg.get("telemetry", {}).get("local_fallback", {}).get("folder", "artifacts/telemetry"))
        pattern = self.cfg.get("telemetry", {}).get("drive", {}).get("file_name_pattern", "{run_id}_telemetry.json")
        path = folder / pattern.format(run_id=run_id)
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

    def _fetch_drive(self, run_id: str) -> Dict[str, Any] | None:
        creds = self._load_creds()
        if creds is None:
            return None

        drive_cfg = self.cfg.get("telemetry", {}).get("drive", {})
        folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID", drive_cfg.get("folder_id", ""))
        if not folder_id:
            return None

        pattern = drive_cfg.get("file_name_pattern", "{run_id}_telemetry.json")
        file_name = pattern.format(run_id=run_id)

        svc = build("drive", "v3", credentials=creds, cache_discovery=False)
        query = f"name = '{file_name}' and '{folder_id}' in parents and trashed = false"
        resp = svc.files().list(q=query, spaces="drive", fields="files(id,name,modifiedTime)", pageSize=1).execute()
        files = resp.get("files", [])
        if not files:
            return None

        file_id = files[0]["id"]
        request = svc.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        content = fh.getvalue().decode("utf-8")
        return json.loads(content)

    def _load_creds(self):
        creds_file = os.getenv("GOOGLE_DRIVE_CREDENTIALS_FILE", "")
        token_file = os.getenv("GOOGLE_DRIVE_TOKEN_FILE", "")

        if token_file and Path(token_file).exists():
            try:
                return Credentials.from_authorized_user_file(token_file, ["https://www.googleapis.com/auth/drive.readonly"])
            except Exception:  # noqa: BLE001
                pass

        if creds_file and Path(creds_file).exists():
            return service_account.Credentials.from_service_account_file(
                creds_file,
                scopes=["https://www.googleapis.com/auth/drive.readonly"],
            )

        return None
