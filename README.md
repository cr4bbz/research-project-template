# Research Project Template

Template for projects in which an academic argument, formalisation, computation, and publication artefacts must remain mutually checkable.

The template is modular. Select only the paper, Lean, and analysis modules needed by a project in PROJECT_PROFILE.toml before deleting unused directories.

## Contract

1. VISION.md records stable purpose and exclusions.
2. GATE_PLAN.md records falsifiable development commitments.
3. Every central claim is in docs/CLAIM_LEDGER.md with evidence, assumptions, scope, and paper location.
4. Lean theorems, computational outputs, and paper prose remain distinct linked artefacts.
5. A green research-facing check updates the ledger and, where relevant, the paper.

## Start a derived project

1. Replace PROJECT_NAME and complete VISION.md.
2. Select active modules in PROJECT_PROFILE.toml.
3. Record the first baseline and gate.
4. Rename TemplateFormalization if Lean is active.
5. Replace sample claim C-001.
6. Before public release, create CITATION.cff from CITATION.cff.example and complete RELEASE_CHECKLIST.md.

## Verification

Run python scripts/check.py for all active modules. Run python scripts/check.py --paper to build the paper. Run python scripts/check.py --static for profile, ledger, and Python-source checks without Lean or LaTeX. Run python scripts/check.py --release only when release mode is enabled.

Lean is pinned in formal/lean/lean-toolchain. The paper command requires latexmk.

## Deliberate exclusions

This template does not imply a web app, dataset, AI integration, package manager, or a claim that formal verification completes a paper. It does not treat working notes or generated figures as primary evidence.

