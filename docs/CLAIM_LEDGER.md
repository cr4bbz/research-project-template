# Claim ledger

This ledger prevents a polished sentence, a Lean theorem, and a script output from
drifting into different claims. `status` is one of `planned`, `checked`, `established`,
or `withdrawn`.

| ID | Research claim | Formal / computational evidence | Paper location | Status |
|---|---|---|---|---|
| C-001 | Modus ponens is derivable in the sample propositional kernel. | `formal/lean/TemplateFormalization/Basic.lean#modus_ponens` | `paper/sections/03_formalisation.tex` | checked |

Replace the sample row before the first substantive release. Evidence locations must be
repository-relative paths. The checker verifies that the cited file and Lean declaration
exist; it does not decide whether prose philosophically overstates the result.
