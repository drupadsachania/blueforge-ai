from __future__ import annotations
import os
from pathlib import Path
from typing import Optional
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

from agentic_soc_factory.config import get_gdrive_creds

class GDriveSyncClient:
    def __init__(self, service_account_json: Optional[str] = None):
        self.service_account_json = service_account_json
        self._creds = None
        self._service = None

    @property
    def service(self):
        if self._service is None:
            creds_data = get_gdrive_creds()
            if not creds_data:
                return None
            
            self._creds = service_account.Credentials.from_service_account_info(
                creds_data,
                scopes=['https://www.googleapis.com/auth/drive.file']
            )
            self._service = build('drive', 'v3', credentials=self._creds)
        return self._service

    @service.setter
    def service(self, value):
        self._service = value

    def upload_dataset(self, file_path: Path, folder_id: Optional[str] = None):
        if not file_path.exists():
            raise FileNotFoundError(f"Dataset file {file_path} not found")
        
        file_metadata = {'name': file_path.name}
        if folder_id:
            file_metadata['parents'] = [folder_id]
            
        media = MediaFileUpload(
            str(file_path),
            mimetype='application/jsonl',
            resumable=True
        )
        
        if self.service:
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            return file.get('id')
        return "mock_id_for_testing"
