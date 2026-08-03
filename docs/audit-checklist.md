# Reproducibility & Provenance Audit Checklist

Use this checklist while auditing the training repository. For each
item, mark ✅ (verified clean) or ❌ (defect found), and note the
file/line where you found it.

## The Four Questions

For every result the pipeline produces, can you answer:

- [ ] **Which code?** Is there a tagged release or committed version, not just "whatever's on disk"?
- [ ] **Which container?** Is it pinned to an exact, immutable version, not a rolling tag like `latest`?
- [ ] **Which input?** Is there a hash or fixed reference to the exact input file used?
- [ ] **Which version?** Is the rule/logic version emitted by the code itself, not typed in by a person?

## Six Things to Check

| # | Check | Where to look | Found? |
|---|-------|----------------|--------|
| 1 | Does every shell script actually parse? Run `bash -n <script>.sh` | Root-level `.sh` files | ☐ |
| 2 | Is any package installed at runtime instead of baked into the container? | `script:` blocks in `.nf` files | ☐ |
| 3 | Does any container use a rolling tag (`latest`, no version) instead of a pinned digest? | `container` line in each `.nf` process | ☐ |
| 4 | Does the output include a timestamp that would differ between two otherwise-identical runs? | Output records in `bin/*.py` | ☐ |
| 5 | Is any provenance field (version, commit, etc.) typed in by hand rather than captured automatically? | `input:` blocks and script calls in `.nf` files | ☐ |
| 6 | Is there a tagged release and automated CI check for this repo? | Repo's release page and Actions tab | ☐ |

## For Each Defect You Find, Answer:

1. **What could go wrong** if this defect stayed in a real, published pipeline?
2. **How would you fix it?** (one sentence is enough)

## Remember

> Declaring provenance is not the same as capturing it.

A value a human typed can be wrong, outdated, or copy-pasted incorrectly.
A value the system captures automatically cannot.