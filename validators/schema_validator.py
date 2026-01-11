# import json
# from jsonschema import validate

# def validate_schema(instance: dict, schema_path: str):
#     """
#     Generic JSON schema validator
#     """
#     with open(schema_path) as schema_file:
#         schema = json.load(schema_file)

#     validate(instance=instance, schema=schema)


import json
from pathlib import Path
from jsonschema import validate

def validate_schema(instance: dict, schema_name: str):
    """
    Generic JSON schema validator (OS-independent)
    """
    schema_path = (
        Path(__file__).resolve()
        .parents[1]          # project root
        / "schemas"
        / schema_name
    )

    if not schema_path.exists():
        raise FileNotFoundError(
            f"Schema file not found.\nExpected path: {schema_path}"
        )

    with schema_path.open(encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    validate(instance=instance, schema=schema)
