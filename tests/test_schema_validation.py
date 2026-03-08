from pathlib import Path

from agentic_soc_factory.pipeline.quality import validate_against_schema


def test_schema_validation_ok(tmp_path: Path):
    schema = tmp_path / "schema.json"
    schema.write_text('{"type":"object","required":["a"],"properties":{"a":{"type":"number"}}}', encoding="utf-8")
    errs = validate_against_schema([{"a": 1}], schema)
    assert errs == []


def test_schema_validation_fails(tmp_path: Path):
    schema = tmp_path / "schema.json"
    schema.write_text('{"type":"object","required":["a"],"properties":{"a":{"type":"number"}}}', encoding="utf-8")
    errs = validate_against_schema([{"a": "x"}], schema)
    assert len(errs) == 1
