import json
from jsonschema import validate

def validate_schema(instance: dict, schema_path: str):
    """
    Generic JSON schema validator
    """
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)

    validate(instance=instance, schema=schema)
