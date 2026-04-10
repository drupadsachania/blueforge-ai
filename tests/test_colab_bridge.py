import pytest
from unittest.mock import MagicMock
from pathlib import Path
import shutil
from agentic_soc_factory.training.colab_mcp_client import GDriveSyncClient

@pytest.fixture
def local_tmp_dir():
    path = Path("tests/tmp_colab")
    path.mkdir(parents=True, exist_ok=True)
    yield path
    if path.exists():
        try:
            shutil.rmtree(path)
        except:
            pass

def test_gdrive_sync_client_upload_checks_existence(local_tmp_dir):
    client = GDriveSyncClient(service_account_json="fake.json")
    
    # Mocking GDrive API response
    mock_drive = MagicMock()
    client.service = mock_drive
    
    test_file = local_tmp_dir / "test_dataset.jsonl"
    test_file.touch()
    
    client.upload_dataset(test_file, folder_id="root")
    assert mock_drive.files().create.called
