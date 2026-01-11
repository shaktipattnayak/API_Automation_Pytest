from pathlib import Path
import json
from jsonschema import validate

def validate_schema(instance, schema_name: str):
    schema_path = (
        Path(__file__)
        .parent.parent        # project root
        / "schemas"
        / schema_name
    )

    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    validate(instance=instance, schema=schema)
