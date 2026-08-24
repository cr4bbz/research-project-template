# Versioned paper-render contract

Every paper render intended for review, sharing, archival, or release has exactly this
repository-relative filename:

```text
paper/renders/<slug>-v<version>-<YYYY-MM-DD>.pdf
```

For the template baseline, the first render is therefore
`paper/renders/project-name-v0.1.0-YYYY-MM-DD.pdf`. The date is the local ISO-8601 date
on which `python scripts/check.py --paper` creates the render. The same paper version is
shown on the title page through `paper/PAPER_VERSION.tex`; the checker requires it to
match `[paper].version` in `PROJECT_PROFILE.toml`.

## Version rule

Use `MAJOR.MINOR.PATCH` without a leading `v` in the source metadata.

- Increment `PATCH` for corrections that leave the stated contribution, claims, and
  interpretation unchanged.
- Increment `MINOR` when a new result, evidence path, substantial section, or visual
  argument changes what the paper contributes.
- Increment `MAJOR` when the central question, semantic framework, or interpretation is
  no longer compatible with the prior paper. Before a 1.0.0 publication, use a new
  `0.MINOR.0` for such a breaking research revision.

Set the version **before** producing a render that will be shared. A changed PDF must not
silently reuse an earlier version number. For a public release, this version, the Git tag
(`v<version>`), and `CITATION.cff` must agree.

## Render procedure

1. Update the paper version in `PROJECT_PROFILE.toml` and `paper/PAPER_VERSION.tex`.
2. Run `python scripts/check.py --paper` from a clean checkout.
3. Verify the new file in `paper/renders/` and record a shareable or archival render in
   `docs/RENDER_LOG.md`.
4. Attach that exact PDF to the review, release, or archive. Never hand-edit a file in
   `paper/renders/`.

The unversioned `paper/main.pdf` is only a LaTeX build intermediate. The versioned render
is the handoff artefact; both remain untracked until deliberately attached to a release or
archive.
