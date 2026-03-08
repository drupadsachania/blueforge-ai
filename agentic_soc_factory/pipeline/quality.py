from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Set


TYPE_MAP = {
    "object": dict,
    "array": list,
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "null": type(None),
}


def _sig(record: Dict) -> str:
    payload_obj = record.get("messages", record)
    payload = json.dumps(payload_obj, sort_keys=True)
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()


def deduplicate(records: List[Dict]) -> List[Dict]:
    seen: Set[str] = set()
    out = []
    for r in records:
        s = _sig(r)
        if s in seen:
            continue
        seen.add(s)
        out.append(r)
    return out


def _validate_type(path: str, value: Any, expected: str, errors: List[str]) -> bool:
    py_type = TYPE_MAP.get(expected)
    if py_type is None:
        return True
    if expected == "number":
        ok = isinstance(value, py_type) and not isinstance(value, bool)
    else:
        ok = isinstance(value, py_type)
    if not ok:
        errors.append(f"{path} expected type '{expected}'")
    return ok


def _validate_record(value: Any, schema: Dict[str, Any], path: str, errors: List[str]) -> None:
    expected_type = schema.get("type")
    if expected_type and not _validate_type(path, value, expected_type, errors):
        return

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path} value not in enum")

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path} missing required key '{key}'")

        props = schema.get("properties", {})
        for key, prop_schema in props.items():
            if key in value:
                _validate_record(value[key], prop_schema, f"{path}.{key}", errors)

    if isinstance(value, list):
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(value) < min_items:
            errors.append(f"{path} requires at least {min_items} items")

        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for idx, item in enumerate(value):
                _validate_record(item, item_schema, f"{path}[{idx}]", errors)


def validate_against_schema(records: List[Dict], schema_path: Path) -> List[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors: List[str] = []
    for i, record in enumerate(records):
        _validate_record(record, schema, f"record[{i}]", errors)
    return errors


def leakage_overlap(train: List[Dict], test: List[Dict]) -> float:
    a = {_sig(r) for r in train}
    b = {_sig(r) for r in test}
    if not b:
        return 0.0
    return len(a & b) / len(b)
