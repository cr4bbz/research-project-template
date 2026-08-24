# Project maintenance contract

## Authority and scope

- VISION.md is the stable promise; GATE_PLAN.md is the changeable plan.
- PROJECT_PROFILE.toml declares active modules. Update it before adding or removing formal/lean, analysis, or paper.
- docs/DECISION_LOG.md records changes of semantics, scope, dependencies, or publication claims.
- references/working is exploratory material, never a citable source without human verification.

## Evidence discipline

- State the research claim before formalising it.
- Keep definitions, assumptions, theorems, executable checks, and interpretation distinct.
- Every non-trivial result has a docs/CLAIM_LEDGER.md row.
- Every ledger row declares evidence type, assumptions, and scope. Finite exhaustive searches are bounded results, never unrestricted necessity.
- Add counterexamples, boundary cases, or negative tests where a nearby invalid reading could look valid.

## Successful-build-to-paper protocol

After a successful Lean build, CI run, or computational check that changes a result:

1. update the ledger row and evidence path;
2. update paper prose when a definition, result, limitation, or conclusion changes;
3. record a decision when scope or interpretation changes; and
4. mention the documentation update in the same or immediately following commit.

A green infrastructure-only check does not require manufactured paper prose.

## Reproducibility

- Pin toolchains; never rely on global latest versions.
- Generate figures from tracked scripts and tracked inputs.
- Keep the default verification command cross-platform: python scripts/check.py.
- Never commit caches, local environments, TeX intermediates, or secrets.
- When the analysis module is active, declare its tracked Python entry point and every
  expected generated output in `PROJECT_PROFILE.toml`; the normal checker executes this
  contract. A disabled paper module uses `—` rather than a dormant paper link in the
  claim ledger.
- When the paper module is active, give every ledger claim one decision in
  `docs/VISUALIZATION_PLAN.md`: figure, table, diagram, or a reasoned `no-figure`.
  Add a visual only when it improves inspection of the claim rather than decorating it;
  generated outputs must remain linked to their source, claim, and paper location.
- Treat `docs/PAPER_RENDER_CONTRACT.md` as the publication handoff contract. Before a
  shareable render, set a deliberate paper version in both canonical locations and create
  the dated filename through `python scripts/check.py --paper`; log external handoffs in
  `docs/RENDER_LOG.md`. Never overwrite a dated render with changed sources; increment
  the version instead.
- Before a public research release, set release.enabled to true in PROJECT_PROFILE.toml, complete RELEASE_CHECKLIST.md, and require python scripts/check.py --release to pass.
