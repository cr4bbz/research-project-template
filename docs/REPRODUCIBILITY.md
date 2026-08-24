# Reproducibility record

## Evidence pipeline

```text
sources and assumptions → formal definitions / data → Lean or analysis check → claim ledger → paper
```

Each arrow must be inspectable in the repository. The paper may interpret a result, but
it must not claim more than the recorded evidence supports.

## Required clean-checkout commands

```text
python scripts/check.py
python scripts/check.py --paper
```

Record any project-specific prerequisites, platform limits, random seeds, dataset
versions, and expected output hashes here. Add a short result table for every published
experiment.
