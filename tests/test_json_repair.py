from agentic_soc_factory.reporting.json_repair import parse_or_repair_json


def test_parse_or_repair_json():
    assert parse_or_repair_json('{"a":1}')['a'] == 1
    assert parse_or_repair_json('"a":1')['a'] == 1
