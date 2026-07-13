#!/usr/bin/env python3
"""Validate repository documentation structure and local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
NAV_MD_RE = re.compile(r":\s*([A-Za-z0-9_./-]+\.md)\s*$")

REQUIRED_FILES = [
    "AGENTS.md",
    "MILESTONES.md",
    "README.md",
    "CONTRIBUTING.md",
    "mkdocs.yml",
    "requirements.txt",
    "scripts/build.sh",
    "docs/index.md",
    "docs/project/verification-register.md",
    "docs/project/milestone-05-06-validation-report.md",
]

IGNORED_SCHEMES = {"http", "https", "mailto", "tel"}


def strip_code_fences(markdown: str) -> str:
    return re.sub(r"```.*?```", "", markdown, flags=re.DOTALL)


def clean_target(raw_target: str) -> str:
    target = raw_target.strip()
    if " " in target and not target.startswith("<"):
        target = target.split()[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target


def is_external(target: str) -> bool:
    parsed = urlsplit(target)
    return parsed.scheme in IGNORED_SCHEMES or target.startswith("#")


def target_path(source: Path, target: str) -> Path | None:
    target = clean_target(target)
    if is_external(target):
        return None

    parsed = urlsplit(target)
    if parsed.scheme:
        return None

    path_part = unquote(parsed.path)
    if not path_part:
        return None

    if path_part.startswith("/"):
        candidate = DOCS / path_part.lstrip("/")
    else:
        candidate = source.parent / path_part

    return candidate.resolve()


def validate_required_files(errors: list[str]) -> None:
    for file_name in REQUIRED_FILES:
        path = ROOT / file_name
        if not path.exists():
            errors.append(f"Missing required file: {file_name}")


def validate_mkdocs_nav(errors: list[str]) -> None:
    if not MKDOCS.exists():
        return

    for line_no, line in enumerate(MKDOCS.read_text(encoding="utf-8").splitlines(), 1):
        match = NAV_MD_RE.search(line)
        if not match:
            continue
        nav_target = DOCS / match.group(1)
        if not nav_target.exists():
            errors.append(f"mkdocs.yml:{line_no}: nav target does not exist: {match.group(1)}")


def validate_links(errors: list[str]) -> None:
    for markdown_file in sorted(DOCS.rglob("*.md")):
        text = strip_code_fences(markdown_file.read_text(encoding="utf-8"))
        for regex in (LINK_RE, IMAGE_RE):
            for match in regex.finditer(text):
                raw_target = match.group(1)
                path = target_path(markdown_file, raw_target)
                if path is None:
                    continue
                if not path.exists():
                    rel_source = markdown_file.relative_to(ROOT)
                    errors.append(f"{rel_source}: missing local target: {raw_target}")


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    validate_mkdocs_nav(errors)
    validate_links(errors)

    if errors:
        print("Documentation validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
