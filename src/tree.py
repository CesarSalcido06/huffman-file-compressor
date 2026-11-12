"""Stage 2 and 3: sort characters by frequency and build the Huffman tree."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    char: str | None
    freq: int
    left: "Node | None" = None
    right: "Node | None" = None


def build_tree(freq_table: dict[str, int]) -> Node:
    """Build and return the root Node of the Huffman tree for freq_table."""
    raise NotImplementedError
