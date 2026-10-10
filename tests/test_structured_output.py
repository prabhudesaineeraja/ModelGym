
from modelgym.evaluation.structured_output import validate_json_output


def test_valid_json_with_required_fields():
    result = validate_json_output(
        '{"name": "Maya", "age": 25}',
        ["name", "age"],
    )
    assert result["passed"] is True


def test_invalid_json():
    result = validate_json_output(
        '{"name": "Maya"',
        ["name"],
    )
    assert result["passed"] is False
    assert result["reason"] == "invalid_json"


def test_missing_required_field():
    result = validate_json_output(
        '{"name": "Maya"}',
        ["name", "age"],
    )
    assert result["passed"] is False
    assert result["reason"] == "missing_fields"
    assert result["missing_fields"] == ["age"]


def test_json_array_is_not_an_object():
    result = validate_json_output(
        '["Maya", 25]',
        ["name"],
    )
    assert result["passed"] is False
    assert result["reason"] == "expected_json_object"

