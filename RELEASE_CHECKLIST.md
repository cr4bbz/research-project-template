# Release checklist

Use this only after the research project itself, not merely this template, is ready for
a public release. Set `[release].enabled = true` in `PROJECT_PROFILE.toml` first.

- [ ] `python scripts/check.py` succeeds from a clean checkout.
- [ ] `python scripts/check.py --paper` succeeds when the paper module is active.
- [ ] `python scripts/check.py --release` succeeds.
- [ ] Every central claim has a complete ledger row with evidence type, assumptions,
  and scope; bounded computations are explicitly labelled as bounded.
- [ ] `CITATION.cff`, `[paper].version`, `paper/PAPER_VERSION.tex`, and the release tag
  agree; `CITATION.cff` has real authors and a valid release date.
- [ ] Licences cover code, formalisation, prose, graphics, data, and third-party assets.
- [ ] The release notes state the research contribution, toolchain versions, known
  limitations, and any archived paper/result artefacts.
- [ ] Tag the exact commit (`vMAJOR.MINOR.PATCH`); attach the exact dated and versioned
  PDF from `paper/renders/` when the paper module is active, plus result artefacts, to the
  GitHub release or a suitable long-term archive.
