# Template status

## Current maintenance baseline

This repository is a reusable, pre-release baseline rather than a citable research
artefact. Its purpose is to provide a small default that can be copied and then reduced
to the modules a research project actually uses.

## Compatibility promise

- Python 3.11 or newer is required for `tomllib` and the default checker.
- Lean projects use the version pinned in `formal/lean/lean-toolchain`.
- An active analysis module declares one tracked Python entry point and one or more
  deterministic outputs in `PROJECT_PROFILE.toml`.
- A derived project may disable formal, analysis, or paper. Its claim ledger must use
  `—` for the paper location when the paper module is disabled; formal-theorem claims
  require the formal module.

## Template change policy

Changes to contracts, default tools, licence boundaries, or release semantics require a
decision-log entry and a changelog entry. Changes to this file describe the template's
maintenance state; GATE_PLAN.md remains reserved for the derived research project.
