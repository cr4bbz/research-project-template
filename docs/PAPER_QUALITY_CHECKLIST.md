# Paper quality checklist

Use this checklist before an external review, submission, archive, or public release.
It complements `python scripts/check.py --paper`; a green build alone is not a visual or
editorial assessment.

## Claims and evidence

- Each stated result has a claim-ledger row with assumptions, bounded or unbounded scope,
  evidence path, and paper location.
- Definitions, mathematical proofs, Lean theorems, executable checks, and interpretation
  are clearly distinguished.
- The paper states nearby limitations or counterexamples where a reader could otherwise
  over-generalise a result.

## Figures and tables

- Each figure answers the reader question recorded in `docs/VISUALIZATION_PLAN.md`.
- Labels, legends, axes, units, and captions remain readable at normal page size; no text
  overlaps or is clipped.
- A table or appendix carries exact values whenever a chart is primarily comparative.
- The caption states what is compared and the visual's interpretive limit where needed.

## Render and release

- Render the current paper with `python scripts/check.py --paper`.
- Convert every PDF page to an image and inspect page balance, section transitions,
  headers/footers, numbering, tables, and figures.
- Check title, author, subject, version, date, and citations; remove placeholders.
- Log an externally shared versioned render in `docs/RENDER_LOG.md` with its source
  commit or archive identifier.
