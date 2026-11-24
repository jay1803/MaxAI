#!/usr/bin/env python3
"""Fail when a nested list item is indented by fewer than four spaces.

The site's Markdown parser nests a list only when its items are indented by
a multiple of four spaces. With two or three spaces, a sub-list renders as
extra items of the parent list (for example as numbered steps 2, 3, 4).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BAD = re.compile(r"^(?: {4})* {1,3}(?:[-*+]|\d+\.)\s")


def main() -> int:
    problems = []
    for path in sorted((ROOT / "docs").rglob("*.md")):
        in_fence = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
                continue
            if not in_fence and BAD.match(line):
                problems.append(f"{path.relative_to(ROOT)}:{number}: indent nested list items by 4 spaces")
    for problem in problems:
        print(problem)
    if problems:
        return 1
    print("check_lists: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
