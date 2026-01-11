# import json
# from jsonschema import validate

# def validate_schema(instance: dict, schema_path: str):
#     """
#     Generic JSON schema validator
#     """
#     with open(schema_path) as schema_file:
#         schema = json.load(schema_file)

#     validate(instance=instance, schema=schema)


from pathlib import Path
import json
from jsonschema import validate

def validate_schema(instance: dict, schema_path: str):
    """
    Auto-corrects Windows paths for Linux (last resort)
    """
    try:
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)

    except FileNotFoundError:
        corrected_path = Path(schema_path.replace("\\", "/"))

        if not corrected_path.exists():
            raise FileNotFoundError(
                f"Schema not found.\nTried paths:\n"
                f"- {schema_path}\n"
                f"- {corrected_path}"
            )

        with corrected_path.open(encoding="utf-8") as f:
            schema = json.load(f)

    validate(instance=instance, schema=schema)
