"""Derive a binary code for each character by walking the Huffman tree."""

from __future__ import annotations

from src.tree import Node


def build_code_table(root: Node) -> dict[str, str]:
    """Return a mapping of character to its binary string code."""
    raise NotImplementedError
