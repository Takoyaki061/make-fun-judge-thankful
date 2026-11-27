#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
outside the grader). Standard library only, no network.
"""

import os

TEXT = (
    "Your coffee went cold while you read this. Two rings on the page, "
    "the second smaller than the first, and you drank it anyway. You "
    "never once looked at the cup."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
