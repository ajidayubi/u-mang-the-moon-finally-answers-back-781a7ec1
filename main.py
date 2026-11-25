#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry (program/v1).

Writes a single line, the Moon's comeback to everyone who ever stared up
at it, to /output/entry.txt. Stdlib only; deterministic; independent of cwd.
"""
import os

LINE = (
    "You wish on me, howl at me, promise me the moon \u2014 I AM the moon, "
    "and after four billion years, nobody's wished me good night back."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
