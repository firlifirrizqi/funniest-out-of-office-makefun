"""Funniest Out-of-Office entry for Make.fun.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Standard library only; nothing to install.
"""

import os

ENTRY = (
    "Out of office. I've set this auto-reply to auto-reply to itself, "
    "so by Monday we'll have had a very productive meeting without you."
)

OUTPUT_PATH = "/output/entry.txt"


def verify() -> None:
    """Re-read the output and assert it is byte-identical to ENTRY."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output differs from ENTRY"
    assert content == content.encode("utf-8").decode("utf-8")
    assert 1 <= len(content) <= 140, f"length {len(content)} out of range"
    assert content.strip(), "entry is only whitespace"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
