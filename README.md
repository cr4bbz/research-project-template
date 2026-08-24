# Research Project Template

Template for projects in which an academic argument, formalisation, computation, and publication artefacts must remain mutually checkable.

The template is modular. Select only the paper, Lean, and analysis modules needed by a project in PROJECT_PROFILE.toml before deleting unused directories. Use GitHub's **Use this template** action to create a new repository; the template itself remains a maintenance baseline, not a research result.

## Contract

1. VISION.md records stable purpose and exclusions.
2. GATE_PLAN.md records falsifiable development commitments.
3. Every central claim is in docs/CLAIM_LEDGER.md with evidence, assumptions, scope, and paper location.
4. docs/VISUALIZATION_PLAN.md records whether each claim needs a figure, table, diagram, or deliberately none.
5. Lean theorems, computational outputs, and paper prose remain distinct linked artefacts.
6. A green research-facing check updates the ledger and, where relevant, the paper.

## Start a derived project

1. Replace PROJECT_NAME and complete VISION.md.
2. Select active modules in PROJECT_PROFILE.toml.
3. Record the first baseline and gate.
4. Rename TemplateFormalization if Lean is active.
5. Replace sample claim C-001.
6. Replace the example analysis contract if analysis is active; every generated output must be declared in PROJECT_PROFILE.toml.
7. Before public release, create CITATION.cff from CITATION.cff.example and complete RELEASE_CHECKLIST.md.

## Verification

Requires Python 3.11 or newer. Run `python scripts/check.py` for all active modules; this also executes the declared analysis contract and verifies its outputs. Run `python scripts/check.py --paper` to regenerate active analysis outputs and build the paper. Run `python scripts/check.py --static` for profile, ledger, and Python-source checks without running Lean, analysis, or LaTeX. Run `python scripts/check.py --release` only when release mode is enabled.

Lean is pinned in formal/lean/lean-toolchain. The paper command requires latexmk. See TEMPLATE_STATUS.md for the template's own maintenance status and compatibility promise.

## Deliberate exclusions

This template does not imply a web app, dataset, AI integration, package manager, or a claim that formal verification completes a paper. It does not treat working notes or generated figures as primary evidence.
