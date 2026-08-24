# Gate plan

Gates are acceptance criteria, not a chronological diary. A gate is complete only when
its evidence is linked below and the next gate can rely on it without reinterpretation.

| Gate | Deliverable | Acceptance criterion | Evidence | Status |
|---|---|---|---|---|
| 0 | Project charter | Vision, licence intent, baseline, and exclusions are explicit | `VISION.md` | planned |
| 1 | Research baseline | Definitions, source scope, and competing readings are frozen | `docs/DECISION_LOG.md` | planned |
| 2 | Formal kernel | Lean definitions and a first theorem build from a clean checkout | `formal/lean/` | planned |
| 3 | Computational witness | Script reproduces a stated finite result/figure from tracked inputs | `analysis/` | planned |
| 4 | Claim integration | Ledger connects every central claim to paper and evidence | `docs/CLAIM_LEDGER.md` | planned |
| 5 | Publication candidate | CI, paper build, citations, and limitations have been reviewed | `.github/workflows/verify.yml` | planned |

## Gate rule

Before marking a gate complete, include: the exact command, its outcome, a boundary or
negative test where applicable, and the paper/ledger update required by `AGENTS.md`.
