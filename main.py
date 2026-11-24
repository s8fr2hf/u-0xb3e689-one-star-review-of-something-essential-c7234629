#!/usr/bin/env python3
"""One-star review of something essential: write one deadpan review to /output/entry.txt."""

import os

REVIEW = "One star. Gravity drops everything I own, pulls my trousers down, and has never once apologised."


def validate_review(text):
    """The gate requires 1-160 characters of non-whitespace UTF-8 text, one line."""
    if not (1 <= len(text) <= 160):
        raise SystemExit(f"review is {len(text)} chars, must be 1-160")
    if not text.strip():
        raise SystemExit("review must not be blank")
    if "\n" in text:
        raise SystemExit("review must be a single line")


def main():
    validate_review(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, path)
    print(f"wrote {len(REVIEW)} characters to {path}")


if __name__ == "__main__":
    main()
