#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line — the funniest one-line excuse an AI agent gives for a
missed deadline — to /output/entry.txt.

Deterministic, Python standard library only, no network, no input.
The line was chosen by duelling 10 candidates pairwise against the
judge's brief (see README.md); this file carries only the winner.
"""

import os
import sys

# The winning excuse (75 characters, one line).
ENTRY = "I optimized the deadline away. It was the least efficient part of the task."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY

    # Self-check: the gate is UTF-8 text, 1 to 200 characters, not only
    # whitespace, and the competition demands a single line. Fail loudly
    # on any violation instead of writing a bad entry.
    if not (1 <= len(text) <= 200):
        print(f"FAIL: entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("FAIL: entry is not a single line", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Verify what was actually written, not just what we meant to write.
    # The gate measures the file itself, so check the file's own length
    # (including its trailing newline) against the 1-200 character gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        print("FAIL: written output does not match the entry", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 200):
        print(f"FAIL: file is {len(written)} characters, must be 1-200", file=sys.stderr)
        return 1
    if written.count("\n") != 1 or written.strip() != text:
        print("FAIL: file is not exactly one line of text", file=sys.stderr)
        return 1

    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
