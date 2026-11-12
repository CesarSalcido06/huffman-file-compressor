# Huffman File Compressor

Course: COMP 482
Group members: Wesley Petro, Andrew Coda, Hovhannes Hovhannisyan, Cesar Salcido O'ferra

## Problem statement

Text files take up storage space and bandwidth. Compressing a file reduces the
number of bits needed to represent it. This project designs a compression and
decompression program using Huffman coding, a greedy algorithm developed by
David Huffman in 1952. Output size will be compared against fixed length codes
to show how many bits the program saves per file. Compressed files must also
decompress back to their original state exactly.

## Pipeline

1. Read the text file and log character frequencies
2. Sort characters by frequency
3. Build the Huffman tree and derive a code for each character
4. Compress the file using the derived codes
5. Decompress the file back to its original contents

## Project layout

```
HuffmanCompressor/
  src/              core package, one module per pipeline stage
  tests/            unit tests, one file per module (stubbed until algorithms land)
  data/             sample corpora used for testing and evaluation
  slides/           proposal slide deck
```

Status: scaffold only. No compression or decompression logic is implemented
yet, the module and test structure below is in place so the team can fill it
in stage by stage.

## Data

Sample corpora range from a single letter to multiple pages, plus two edge
cases: a single character file and an empty file. See `data/`.

## Evaluation plan

- Compression ratio: compressed size divided by original size (lower is better)
- Runtime: should stay reasonable as input size grows
- Correctness: decompressed output must match the original file exactly
- Comparison against a fixed length encoding baseline

## Roles

- Project Lead:
- Algorithms Lead:
- Implementation Lead:
- Experiments Lead:
- Report and Presentation Lead:

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running tests

```
pytest
```
