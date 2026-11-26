#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry.

Writes one funny line pitching the worst pizza topping imaginable
to /output/entry.txt. Pure standard library.
"""

import os

LINE = (
    "Anchovy-flavoured gummy bears, melted on at 450 degrees, "
    "so every slice tastes like a beach at low tide."
)


def main():
    line = LINE.strip()
    assert line, "entry line must not be blank"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) < 200, "entry must be 1-199 characters"
    assert line.isascii(), "entry must be plain ASCII"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
