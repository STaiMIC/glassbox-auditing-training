#!/usr/bin/env python3
"""
json_validation.py
~~~~~~~~~~~~~~~~~~~
Validates each AI_TRIAGE JSON record against docs/schema.json.
Valid records pass through; invalid ones are quarantined with the specific reason they failed.
"""
import sys
import json
from jsonschema import validate, ValidationError


def load_schema(schema_path):
    with open(schema_path) as f:
        return json.load(f)


def main(jsonl_path, schema_path, valid_out, quarantine_out):
    schema = load_schema(schema_path)

    n_valid = 0
    n_quarantined = 0

    with open(jsonl_path) as infile, \
         open(valid_out, "w") as valid_f, \
         open(quarantine_out, "w") as quarantine_f:

        for line in infile:
            line = line.strip()
            if not line:
                continue

            record = json.loads(line)

            try:
                validate(instance=record, schema=schema)
                valid_f.write(json.dumps(record) + "\n")
                n_valid += 1
            except ValidationError as e:
                quarantine_record = {
                    "original_record": record,
                    "validation_error": str(e.message),
                    "failed_field": list(e.path) if e.path else None,
                }
                quarantine_f.write(json.dumps(quarantine_record) + "\n")
                n_quarantined += 1

    print(f"Validation complete: {n_valid} valid, {n_quarantined} quarantined")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage: json_validation.py <input.jsonl> <schema.json> <valid_out.jsonl> <quarantine_out.jsonl>")
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])