# Claim ledger

This ledger prevents prose, Lean theorems, and script outputs from drifting into different claims. Status is planned, checked, established, or withdrawn.

Evidence type is formal-theorem, bounded-exhaustive-check, computational-experiment, worked-example, or interpretation. Scope starts with `bounded:` or `unbounded:` and states exactly what follows; finite searches must use `bounded:`. When the paper module is disabled, use `—` as the paper location rather than a dormant link.

| ID | Evidence type | Research claim | Assumptions | Scope | Evidence | Paper location | Status |
|---|---|---|---|---|---|---|---|
| C-001 | formal-theorem | Modus ponens is derivable in the sample propositional kernel. | Lean Prop; implication has its standard meaning. | unbounded: over propositions in the Lean kernel; not an interpretation of a substantive logic. | formal/lean/TemplateFormalization/Basic.lean#modus_ponens | paper/sections/03_formalisation.tex | checked |
| C-002 | computational-experiment | The example analysis contract deterministically produces its linked paper figure. | Python standard library; tracked generator source. | bounded: exact template generator and declared output path. | analysis/generate_figure.py | paper/sections/02_method.tex | checked |

Replace C-001 before substantive release. Evidence and paper locations are repository-relative. Escape a literal pipe within a cell as `\|`. The checker verifies the schema and Lean links; it does not judge whether prose overstates a result.
