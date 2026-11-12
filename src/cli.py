"""Command line entry point: compress or decompress a file."""

import argparse
from pathlib import Path

from src.compressor import compress
from src.decompressor import decompress


def main() -> None:
    parser = argparse.ArgumentParser(description="Huffman file compressor")
    subparsers = parser.add_subparsers(dest="command", required=True)

    compress_parser = subparsers.add_parser("compress")
    compress_parser.add_argument("input", type=Path)
    compress_parser.add_argument("output", type=Path)

    decompress_parser = subparsers.add_parser("decompress")
    decompress_parser.add_argument("input", type=Path)
    decompress_parser.add_argument("output", type=Path)

    args = parser.parse_args()

    if args.command == "compress":
        compress(args.input, args.output)
    elif args.command == "decompress":
        decompress(args.input, args.output)


if __name__ == "__main__":
    main()
