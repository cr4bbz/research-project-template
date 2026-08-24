# Research Project Template

Template for projects in which an academic argument, formalisation, computation, and
publication-quality artefacts must remain mutually checkable.

It is intentionally **modular**: a project may use only the paper, only Lean, or the
entire evidence pipeline. Delete unused modules at the first project commit; do not
leave fictional plans or placeholder claims behind.

## The contract

1. `VISION.md` records the stable purpose and exclusions.
2. `GATE_PLAN.md` records falsifiable, time-local development commitments.
3. Every central claim belongs in `docs/CLAIM_LEDGER.md`, with its evidence and paper
   location.
4. Lean theorems, computational results, and paper prose are separate artefacts linked
   by that ledger; none silently substitutes for another.
5. A green check is a release event: update the claim ledger and the paper when the
   result changes the research record.

## Repository map

```text
.
├── paper/                 # LaTeX source and generated publication artefacts
├── formal/lean/           # independent Lean/Lake project
├── analysis/              # deterministic computations and figure generators
├── docs/                  # research contracts, decisions, reproducibility record
├── references/            # curated bibliography and explicitly non-authoritative notes
├── scripts/               # cross-platform verification entry points
└── .github/               # CI and contribution templates
```

`paper/figures/generated/` contains generated inputs only. Source data, scripts, and
the command that produced an illustration are versioned; PDFs and build by-products are
not.

## First 30 minutes

1. Replace `PROJECT_NAME` and complete `VISION.md`.
2. Record the first immutable baseline and the first gate.
3. Keep or delete `formal/lean/`, `analysis/`, and `paper/` deliberately.
4. Rename the Lean package and module (`TemplateFormalization`) if you retain it.
5. Replace the sample claim `C-001`; do not carry it into the actual project.

## Verification

The portable command is:

```text
python scripts/check.py
```

It checks claim links and runs `lake build` in `formal/lean`. To build the paper too:

```text
python scripts/check.py --paper
```

The latter needs `latexmk`. Lean is pinned in `formal/lean/lean-toolchain`; install
the pinned toolchain with `elan` and run `lake exe cache get` when a project later adds
Mathlib.

## What this template deliberately does not do

- It does not equate a successful Lean build with a completed paper.
- It does not add a web app, datasets, AI integrations, or package managers by default.
- It does not treat working notes as sources or generated figures as primary evidence.
- It does not force a single research methodology on projects that only need one module.

See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for the evidence pipeline and
[`AGENTS.md`](AGENTS.md) for the standing maintenance contract.
