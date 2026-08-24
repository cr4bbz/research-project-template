# Paper module

main.tex is the LaTeX entry point. Put prose in sections, generated inputs in figures/generated, and bibliography data in ../references.

Build with latexmk -pdf -interaction=nonstopmode main.tex here, or python ../scripts/check.py --paper at repository root.

`python ../scripts/check.py --paper` also copies the result to the versioned handoff path
defined in `docs/PAPER_RENDER_CONTRACT.md`. `main.pdf` is only an intermediate; attach the
versioned render to a review, release, or archive and record external handoffs in
`docs/RENDER_LOG.md`. Tracked TeX remains the authoritative artefact.
