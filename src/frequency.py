"""Stage 1: read a text file and build a character frequency table."""

from __future__ import annotations

from pathlib import Path


def count_frequencies(path: Path) -> dict[str, int]:
    """Return a mapping of character to occurrence count for the file at path."""
    raise NotImplementedError
