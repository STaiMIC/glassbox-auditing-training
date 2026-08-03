# GlassBox Auditing Training

A deliberately imperfect Nextflow pipeline for the S03 practical:
**"Beyond 'It Ran Successfully': Auditing Your Own nf-core Pipeline."**

This is a training copy based on the real
[glassbox-ai-triage](https://github.com/STaiMIC/glassbox-ai-triage)
pattern, with **6 reproducibility and provenance defects** seeded
throughout the codebase.

## Your task

Work solo or in pairs (30 minutes):

1. Run `bash -n setup.sh` as a first check.
2. Read through `bin/triage.py`, `modules/json_validation.nf`,
   and `modules/audit_bundle.nf`.
3. Find as many of the 6 defects as you can.
4. For each one, explain *why* it breaks reproducibility or
   provenance, and how you'd fix it.

Use `docs/audit-checklist.md` to guide your review.

After 30 minutes, we'll compare findings as a group (20 minutes),
then complete a reproducibility risk map and each fix one issue
in your own repository or training fork before the next session.

## Note

This repository is intentionally broken for teaching purposes.
Do not use it as a reference implementation — see
[glassbox-ai-triage](https://github.com/STaiMIC/glassbox-ai-triage)
for the corrected version.
