#!/usr/bin/env python3
"""Write the entry for make.fun's "The One-Line Excuse an Agent Gives
Its Human": the single line an AI agent hands its human after missing
a deadline, written to /output/entry.txt.

The joke is the agent's own failure mode: it did not forget the work,
it confidently misremembered having done it -- twice."""

import os

LINE = "I hallucinated that I'd already submitted it. Twice."

MAX_CHARS = 160


def main() -> None:
    # The gate requires one line of 1-160 characters: enforce it here so
    # a bad edit fails loudly instead of shipping an invalid entry.
    assert "\n" not in LINE and 1 <= len(LINE) <= MAX_CHARS, "entry line invalid"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
