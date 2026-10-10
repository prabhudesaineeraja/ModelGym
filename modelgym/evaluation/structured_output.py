import json


def validate_json_output(output, required_fields):
    """Validate that output is JSON containing all required fields."""
    try:
        parsed = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return {
            "passed": False,
            "reason": "invalid_json",
        }

    if not isinstance(parsed, dict):
        return {
            "passed": False,
            "reason": "expected_json_object",
        }

    missing_fields = [
        field for field in required_fields
        if field not in parsed
    ]

    if missing_fields:
        return {
            "passed": False,
            "reason": "missing_fields",
            "missing_fields": missing_fields,
        }

    return {
        "passed": True,
        "reason": None,
        "missing_fields": [],
    }

