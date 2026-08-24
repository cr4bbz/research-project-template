# Paper integration and visualisation plan

Every central claim receives an explicit decision: a figure, table, diagram, or a
reasoned `no-figure` choice. The purpose is not decoration. A visual is used only when it
makes a relationship, comparison, distribution, parameter dependence, counterexample, or
proof architecture easier to inspect than prose alone.

| Claim ID | Decision | Form | Reader question answered | Source / generator | Output | Paper location |
|---|---|---|---|---|---|---|
| C-001 | no-figure | formal statement and prose | Which exact theorem follows from the stated kernel? | — | — | paper/sections/03_formalisation.tex |
| C-002 | figure | generated figure | Does the tracked analysis contract produce a paper-facing artefact? | analysis/generate_figure.py | paper/figures/generated/example-data.tex | paper/sections/02_method.tex |

## Decision rule

Use a figure for a numerical trend, distribution, spatial relation, or parameter sweep;
a table for exact comparisons, finite cases, or mappings; and a diagram for dependencies,
construction steps, or semantic structure. Prefer a formal statement, compact example, or
prose when it is clearer than a visual. A `no-figure` entry is therefore a positive
editorial decision, not a missing task.

For a visual decision, keep the source/generator and output repository-relative, declare
the output in `PROJECT_PROFILE.toml`, cite the supported claim in the ledger, and explain
the visual's interpretive limit in the paper when a nearby over-reading is plausible.

## Integration protocol

Before marking a claim `established`, update its ledger row, this plan, and the named
paper location if the result changes a definition, theorem, example, limitation, or
conclusion. Infrastructure-only checks do not require prose, but any paper-facing output
still needs a visualization-plan row. Record a decision-log entry when the choice changes
the project scope, methodology, or publication claim.
