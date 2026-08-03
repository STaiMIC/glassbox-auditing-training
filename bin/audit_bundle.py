#!/usr/bin/env python3
"""
audit_bundle.py
~~~~~~~~~~~~~~~
Creates one audit "receipt" record per run, capturing everything needed to trace back exactly what produced a given triage result: input hash,
rule version, workflow provenance, and validation outcome counts.

All provenance fields are either calculated from a committed artefact (the input file hash) or read from Nextflow's own runtime (commit,
revision, release version) — none are supplied as a typed argument that a person could enter incorrectly.
"""
import sys
import json
import hashlib
from datetime import datetime, timezone


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def count_lines(path):
    with open(path) as f:
        return sum(1 for _ in f)


def main(input_vcf, valid_jsonl, quarantine_jsonl, rule_version,
         workflow_commit, workflow_revision, release_version, out_path):
    timestamp = datetime.now(timezone.utc).isoformat()

    n_valid = count_lines(valid_jsonl)
    n_quarantined = count_lines(quarantine_jsonl)

    if n_valid == 0:
        validation_status = "FAIL"
    elif n_quarantined == 0:
        validation_status = "PASS"
    else:
        validation_status = "PARTIAL_QUARANTINE"

    bundle = {
        "run_timestamp": timestamp,
        "input_vcf": input_vcf,
        "input_vcf_sha256": sha256_of_file(input_vcf),
        "rule_version": rule_version,
        "workflow_commit": workflow_commit,
        "workflow_revision": workflow_revision,
        "release_version": release_version,
        "n_valid": n_valid,
        "n_quarantined": n_quarantined,
        "validation_status": validation_status,
    }

    with open(out_path, "w") as out:
        out.write(json.dumps(bundle, indent=2))

    print(f"Audit bundle written to {out_path}")
    print(json.dumps(bundle, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 9:
        sys.exit(
            "Usage: audit_bundle.py <input.vcf> <valid.jsonl> <quarantine.jsonl> "
            "<rule_version> <workflow_commit> <workflow_revision> "
            "<release_version> <out.json>"
        )
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4],
         sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])