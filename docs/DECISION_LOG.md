# Decision log

| Date | Decision | Why | Consequences / revisiting condition |
|---|---|---|---|
| 2026-08-24 | Make paper renders immutable within one slug/version/date identity. | A mutable handoff PDF destroys the ability to identify which research state was reviewed or archived. | A manifest fingerprints paper sources; changed sources fail rather than overwrite an existing render. Releases require the render, manifest, and a matching log row. Revisit if release dates must be user-selected rather than build dates. |
| 2026-08-24 | Treat versioned paper renders as named publication artefacts. | An unversioned `main.pdf` cannot reliably identify the paper state shared with reviewers or archives. | `PROJECT_PROFILE.toml` and `paper/PAPER_VERSION.tex` define one paper version; the checker copies each paper build to a dated `paper/renders/<slug>-v<version>-<date>.pdf`. Revisit if the project needs pre-release identifiers or multiple publication formats. |
| 2026-08-24 | Require an explicit paper-integration and visualisation decision for every claim when the paper module is active. | A generated figure is not automatically an explanatory figure, and omission can be the clearest editorial choice. | `docs/VISUALIZATION_PLAN.md` links each claim to a figure, table, diagram, or reasoned no-figure decision. Revisit if a project has no claim ledger or uses a non-paper publication medium. |
| 2026-08-24 | Use profile-governed evidence links and an executable analysis contract. | A module must be removable without leaving false paper or Lean dependencies; generated research artefacts must be checked, not merely stored. | Claims use `—` for unavailable modules and explicit `bounded:`/`unbounded:` scope. Active analysis declares a Python entry point and outputs. Revisit if a project needs multi-command, non-Python, or data-heavy workflows. |
| YYYY-MM-DD | Initial project baseline | Replace before first gate | What would make this baseline inadequate? |

Use this for semantic and methodological choices, not routine implementation details.
