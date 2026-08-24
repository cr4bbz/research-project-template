# Paper module

`main.tex` is the sole LaTeX entry point. Put prose in `sections/`, generated TeX inputs
or graphics in `figures/generated/`, and bibliographic data in `../references/`.

Build locally with `latexmk -pdf -interaction=nonstopmode main.tex` from this directory,
or run `python ../scripts/check.py --paper` from the repository root.
