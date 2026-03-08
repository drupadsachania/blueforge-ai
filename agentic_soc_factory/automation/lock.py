from __future__ import annotations

import os
from pathlib import Path


class FileLock:
    def __init__(self, lock_path: Path) -> None:
        self.lock_path = lock_path
        self.fd: int | None = None

    def acquire(self) -> bool:
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            self.fd = os.open(self.lock_path, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            os.write(self.fd, str(os.getpid()).encode("utf-8"))
            return True
        except FileExistsError:
            return False

    def release(self) -> None:
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
        if self.lock_path.exists():
            self.lock_path.unlink(missing_ok=True)
