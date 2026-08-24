# Gate plan

Gates are acceptance criteria, not a diary. A gate is complete only when later work can rely on its evidence without reinterpretation.

This plan is copied into a derived research project. It records that project's evidence,
not the maturity of this template; see TEMPLATE_STATUS.md and CHANGELOG.md for template
maintenance.

| Gate | Deliverable | Acceptance criterion | Evidence | Status |
|---|---|---|---|---|
| 0 | Project charter | Vision, active profile, licences, baseline, and exclusions are explicit | VISION.md; PROJECT_PROFILE.toml | planned |
| 1 | Research baseline | Definitions, source scope, and competing readings are frozen | docs/DECISION_LOG.md | planned |
| 2 | Formal kernel | Lean definitions and first theorem build from clean checkout | formal/lean | planned |
| 3 | Computational witness | Script reproduces a stated finite result or figure from tracked inputs | analysis | planned |
| 4 | Claim integration | Ledger and visualisation plan connect each central claim to evidence, assumptions, scope, paper, and an explicit presentation decision | docs/CLAIM_LEDGER.md; docs/VISUALIZATION_PLAN.md | planned |
| 5 | Publication candidate | CI, licences, citation, release check, paper build, and limitations are reviewed | RELEASE_CHECKLIST.md | planned |

Before completion, record the exact command, its outcome, a boundary or negative test where applicable, and the required paper or ledger update.
