# Claim ledger

This ledger prevents prose, Lean theorems, and script outputs from drifting into different claims. Status is planned, checked, established, or withdrawn.

Evidence type is formal-theorem, bounded-exhaustive-check, computational-experiment, worked-example, or interpretation. Scope states exactly what follows; finite searches must state that their scope is bounded.

| ID | Evidence type | Research claim | Assumptions | Scope | Evidence | Paper location | Status |
|---|---|---|---|---|---|---|---|
| C-001 | formal-theorem | Modus ponens is derivable in the sample propositional kernel. | Lean Prop; implication has its standard meaning. | Unbounded over propositions in Lean kernel; not an interpretation of a substantive logic. | formal/lean/TemplateFormalization/Basic.lean#modus_ponens | paper/sections/03_formalisation.tex | checked |

Replace C-001 before substantive release. Evidence and paper locations are repository-relative. The checker verifies the schema and Lean links; it does not judge whether prose overstates a result.

