#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
outside the grader). Standard library only, no network.
"""

import os

TEXT = (
    "Before the room filled, I set my coat over the chair beside mine, "
    "folding the sleeves once, and kept my hand on its back while the seats "
    "around us disappeared. When you came, I lifted it away and the chair "
    "was still warm where my hand had been."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
