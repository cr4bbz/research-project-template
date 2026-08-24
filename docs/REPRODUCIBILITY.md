# Reproducibility record

## Evidence pipeline

sources and assumptions -> formal definitions or data -> Lean or analysis check -> claim ledger -> paper

Each arrow must be inspectable. The paper may interpret a result, but cannot claim more than the recorded evidence supports.

PROJECT_PROFILE.toml declares which arrows exist. A missing module is a deliberate scope choice, not a failed build. Record toolchain, inputs, parameters, seeds, and output hashes for every published computational result.

## Clean-checkout commands

python scripts/check.py
python scripts/check.py --paper

Record project-specific prerequisites, platform limits, data versions, and expected hashes here.

