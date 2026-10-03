"""Entry point for the Paper to Playground generator."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_FIELDS = ("source_url", "focus", "audience")


def load_case(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8") as stream:
        case = json.load(stream)
    if not isinstance(case, dict):
        raise ValueError("Input must be a JSON object")
    for field in REQUIRED_FIELDS:
        if not isinstance(case.get(field), str) or not case[field].strip():
            raise ValueError(f"Input field {field!r} must be a nonempty string")
    return case


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an interactive paper explanation")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()

    try:
        load_case(args.input)
        raise NotImplementedError("Generator is not implemented yet")
    except (OSError, json.JSONDecodeError, ValueError, NotImplementedError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
