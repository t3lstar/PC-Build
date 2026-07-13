#!/usr/bin/env python3
"""Validate digital twin JSON data against JSON Schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "data" / "schemas" / "digital-twin.schema.json"
DATA_FILES = [ROOT / "data" / "digital-twin" / "build.json"]


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    errors: list[str] = []
    for data_file in DATA_FILES:
        instance = load_json(data_file)
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
            path = "/".join(str(part) for part in error.path) or "<root>"
            rel_file = data_file.relative_to(ROOT)
            errors.append(f"{rel_file}:{path}: {error.message}")

    if errors:
        print("Digital twin data validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Digital twin data validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
