from __future__ import annotations

from pathlib import Path
from typing import Iterable


def collect_markdown_files(corpus_root: Path) -> list[Path]:
    return sorted(corpus_root.rglob("*.md"))


def load_docs(corpus_root: Path) -> Iterable[dict]:
    for path in collect_markdown_files(corpus_root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        yield {"path": str(path), "title": path.stem, "text": text}
