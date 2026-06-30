#!/usr/bin/env python3
"""Validate all Deskription definition YAML files against the JSON schemas.

Usage: python3 scripts/validate.py
Exits non-zero if any document fails validation.
"""

import json
import pathlib
import sys

import jsonschema
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
DEFINITIONS_DIR = ROOT / "definitions"

SCHEMAS = {
    "Resource": "resource.schema.json",
    "ResourceTable": "resourcetable.schema.json",
    "ResourceDetails": "resourcedetails.schema.json",
}


def main() -> int:
    validators = {
        kind: jsonschema.Draft7Validator(json.loads((SCHEMA_DIR / name).read_text()))
        for kind, name in SCHEMAS.items()
    }

    errors = 0
    documents = 0
    for path in sorted(DEFINITIONS_DIR.rglob("*.yaml")):
        rel = path.relative_to(ROOT)
        for index, doc in enumerate(yaml.safe_load_all(path.read_text())):
            if doc is None:
                continue
            documents += 1
            kind = doc.get("kind") if isinstance(doc, dict) else None
            validator = validators.get(kind)
            if validator is None:
                print(f"{rel} (doc {index}): unknown kind {kind!r}")
                errors += 1
                continue
            for error in validator.iter_errors(doc):
                location = "/".join(str(p) for p in error.absolute_path) or "<root>"
                print(f"{rel} (doc {index}, {kind}): {location}: {error.message}")
                errors += 1

    print(f"{documents} documents checked, {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
