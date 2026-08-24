# Changelog

This file records changes to the template itself. Derived research projects should use
their own release notes for research claims and results.

## Unreleased

- Made paper links, formal claims, and module selection mutually consistent.
- Added an executable analysis contract with declared outputs and a generated-paper
  example.
- Added structured scope markers, stronger citation metadata checks, and checker tests.
- Separated template maintenance status from derived-project gates.
- Added a versioned paper-render contract with dated filenames, in-PDF version display,
  citation consistency checks, and an external-handoff log.
- Made render identities immutable with source-fingerprint manifests; release preflight
  now requires a matching render-log row, while CI exports the versioned render artifact.
- Added mathematical-proof as an explicit evidence type, PDF metadata placeholders,
  and a paper-quality checklist with visual-render review requirements.
- Added a Codespaces/dev-container bootstrap and root-pinned VS Code verification tasks.
