# Analysis and visualisation

Put deterministic, reviewable computation here. The active analysis module declares one
tracked Python entry point and its expected outputs in `PROJECT_PROFILE.toml`. The normal
checker runs that entry point, then requires every declared output; `--static` only checks
that the sources compile.

A script that generates a paper figure must document its inputs, output path, parameters,
and the claim ledger entry it supports. If it uses randomness, fix and record the seed.

Do not hand-edit files in `paper/figures/generated/`; regenerate them instead.
