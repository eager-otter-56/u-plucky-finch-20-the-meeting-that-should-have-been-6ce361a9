#!/usr/bin/env python3
"""Entry for u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.

Writes one line (<=200 chars) to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os
import stat

ENTRY = "I spent 47 minutes and 214,000 tokens in a meeting that decided to send me an email asking for my notes from the meeting."


def main():
    # Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip(), "entry is whitespace only"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
