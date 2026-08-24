# Project maintenance contract

## Authority and scope

- `VISION.md` is the stable project promise. `GATE_PLAN.md` is the changeable plan.
- `docs/DECISION_LOG.md` records decisions that alter semantics, scope, dependencies,
  or publication claims. Do not bury such decisions in commits or chat summaries.
- `references/working/` is exploratory material, never a citable source without being
  promoted to the bibliography and checked by a human.

## Evidence discipline

- State the mathematical/research claim before attempting its formalisation.
- Keep definitions, assumptions, theorems, executable checks, and interpretive prose
  distinguishable. A theorem can support a claim without exhausting its meaning.
- For each non-trivial result, add or update one row in `docs/CLAIM_LEDGER.md`.
- Add counterexamples, boundary cases, or negative tests whenever an invalid nearby
  interpretation could appear to satisfy the intended result.

## Successful-build-to-paper protocol

After every successful Lean build, CI run, or computational check that establishes a
new result or changes an existing result:

1. update the relevant claim-ledger row and its evidence path;
2. update the paper section if the result affects a stated definition, theorem,
   example, limitation, or conclusion;
3. record a decision when the result changes scope or interpretation; and
4. mention the paper/ledger update in the same commit or in the immediately following
   documentation commit.

Do not manufacture prose merely because a build is green. If a successful check changes
no research-facing claim, note that the result is infrastructure-only in the commit.

## Reproducibility

- Pin toolchains; do not rely on a globally installed “latest” version.
- Put generated files under `paper/figures/generated/` and generate them from tracked
  scripts and tracked inputs.
- Keep the default verification command cross-platform: `python scripts/check.py`.
- Never commit caches, local environments, TeX intermediates, or secrets.
