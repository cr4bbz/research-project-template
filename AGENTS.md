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
- Before a public research release, set release.enabled to true in PROJECT_PROFILE.toml, complete RELEASE_CHECKLIST.md, and require python scripts/check.py --release to pass.

