#!/usr/bin/env python3
"""Fail if tracked text files contain data that must not be public.

Two layers:
1. Generic patterns that are never acceptable (emails, tokens, signed URLs,
   local paths, chat user IDs, UUIDs, real-looking issue keys).
2. An optional private term list (employer, people, products, workspaces).
   Read from the file named in PRIVATE_TERMS_FILE, or from the PRIVATE_TERMS
   environment variable (one term per line). The list is never committed.

Usage: python3 scripts/check_public.py [paths...]
With no paths, all files tracked by Git are checked.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".txt", ".py", ".json", ".toml", ".html", ".css", ".js", ""}

# Placeholder issue keys used in examples are allowed.
ALLOWED_ISSUE_KEYS = {"PROJ-123", "PROJ-124", "PROJ-125", "PROJ-200", "PROJ-201", "UTF-8"}

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("email address", re.compile(r"\b[A-Za-z0-9._%+-]+@(?!example\.(?:com|org)\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("API token", re.compile(r"\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|xox[abposc]-[A-Za-z0-9-]{10,}|lin_(?:api|oauth)_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})\b")),
    ("signed URL", re.compile(r"X-Amz-(?:Signature|Security-Token)|[?&]sig=[A-Za-z0-9%]{20,}")),
    ("local home path", re.compile(r"(?:/Users/|/home/)(?!<)[A-Za-z0-9._-]+/|C:\\\\Users\\\\")),
    ("chat workspace or user ID", re.compile(r"\b[TUCDGW](?=[A-Z0-9]*\d)(?=[A-Z0-9]*[A-Z][A-Z0-9]*[A-Z])[A-Z0-9]{8,10}\b")),
    ("UUID", re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)),
    ("issue key", re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d{1,5}\b")),
    ("Linear workspace URL", re.compile(r"linear\.app/(?!docs\b|changelog\b|method\b)[a-z0-9-]+/", re.I)),
    ("Slack workspace URL", re.compile(r"\b[a-z0-9-]+\.slack\.com\b", re.I)),
    ("Notion page URL", re.compile(r"notion\.(?:so|site)/[A-Za-z0-9-]{8,}")),
]

# Words that look like chat IDs or issue keys but are ordinary text.
FALSE_POSITIVE_WORDS = {"ASD-STE100", "STE100", "ISO-8601", "SHA-256", "RFC-3339"}


def tracked_files() -> list[Path]:
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout
    return [Path(p) for p in out.splitlines() if p]


def private_terms() -> list[str]:
    raw = ""
    path = os.environ.get("PRIVATE_TERMS_FILE")
    if path and Path(path).is_file():
        raw = Path(path).read_text(encoding="utf-8")
    elif os.environ.get("PRIVATE_TERMS"):
        raw = os.environ["PRIVATE_TERMS"]
    terms = [t.strip() for t in raw.splitlines()]
    return [t for t in terms if t and not t.startswith("#")]


def check_file(path: Path, terms: list[re.Pattern[str]]) -> list[str]:
    if path.suffix.lower() not in TEXT_SUFFIXES or path.name == "check_public.py":
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, FileNotFoundError):
        return []
    problems = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for label, pattern in PATTERNS:
            for match in pattern.finditer(line):
                value = match.group(0)
                if value in FALSE_POSITIVE_WORDS:
                    continue
                if label == "issue key" and (value in ALLOWED_ISSUE_KEYS or any(value in w for w in FALSE_POSITIVE_WORDS)):
                    continue
                problems.append(f"{path}:{lineno}: {label}: {value}")
        for term in terms:
            if term.search(line):
                # Do not echo the private term itself into CI logs.
                problems.append(f"{path}:{lineno}: private term (from the private list)")
    return problems


def main(argv: list[str]) -> int:
    paths = [Path(p) for p in argv] if argv else tracked_files()
    terms = [re.compile(r"(?<![A-Za-z])" + re.escape(t) + r"(?![A-Za-z])", re.I) for t in private_terms()]
    problems = [p for path in paths for p in check_file(path, terms)]
    for p in problems:
        print(p)
    if not terms:
        print("note: no private term list loaded (set PRIVATE_TERMS_FILE or PRIVATE_TERMS)", file=sys.stderr)
    print(f"checked {len(paths)} files, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
