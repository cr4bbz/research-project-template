# Reproducibility record

## Evidence pipeline

sources and assumptions -> formal definitions or data -> Lean or analysis check -> claim ledger -> visualization decision -> paper

Each arrow must be inspectable. The paper may interpret a result, but cannot claim more than the recorded evidence supports. `docs/VISUALIZATION_PLAN.md` records whether a result needs a figure, table, diagram, or deliberately none.

PROJECT_PROFILE.toml declares which arrows exist. A missing module is a deliberate scope choice, not a failed build. For an active analysis module, it also declares a tracked Python entry point and its expected outputs; the normal checker executes it. Record toolchain, inputs, parameters, seeds, and output hashes for every published computational result.

## Clean-checkout commands

python scripts/check.py
python scripts/check.py --paper

`--paper` creates a dated, versioned PDF according to `docs/PAPER_RENDER_CONTRACT.md`.
Record project-specific prerequisites, platform limits, data versions, expected hashes,
and externally shared renders in `docs/RENDER_LOG.md`.

Before sharing a render outside the working team, complete the applicable checks in
`docs/PAPER_QUALITY_CHECKLIST.md`; this includes a visual PNG review, not only a
successful LaTeX exit code.
