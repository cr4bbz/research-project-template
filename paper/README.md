# Paper module

main.tex is the LaTeX entry point. Put prose in sections, generated inputs in figures/generated, and bibliography data in ../references.

Build with latexmk -pdf -interaction=nonstopmode main.tex here, or python ../scripts/check.py --paper at repository root.

For a public release, attach the generated PDF to the tagged release. Tracked TeX remains the authoritative artefact.

