# Decision log

| Date | Decision | Why | Consequences / revisiting condition |
|---|---|---|---|
| 2026-08-24 | Require an explicit paper-integration and visualisation decision for every claim when the paper module is active. | A generated figure is not automatically an explanatory figure, and omission can be the clearest editorial choice. | `docs/VISUALIZATION_PLAN.md` links each claim to a figure, table, diagram, or reasoned no-figure decision. Revisit if a project has no claim ledger or uses a non-paper publication medium. |
| 2026-08-24 | Use profile-governed evidence links and an executable analysis contract. | A module must be removable without leaving false paper or Lean dependencies; generated research artefacts must be checked, not merely stored. | Claims use `—` for unavailable modules and explicit `bounded:`/`unbounded:` scope. Active analysis declares a Python entry point and outputs. Revisit if a project needs multi-command, non-Python, or data-heavy workflows. |
| YYYY-MM-DD | Initial project baseline | Replace before first gate | What would make this baseline inadequate? |

Use this for semantic and methodological choices, not routine implementation details.
