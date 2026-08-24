#!/usr/bin/env bash
set -euo pipefail

sudo apt-get update
sudo env DEBIAN_FRONTEND=noninteractive apt-get install -y \
  curl \
  git \
  latexmk \
  lmodern \
  texlive-latex-extra \
  texlive-pictures

if [ ! -x "$HOME/.elan/bin/elan" ]; then
  curl https://elan.lean-lang.org/elan-init.sh -sSf | sh -s -- -y --default-toolchain none
fi

grep -qxF 'export PATH="$HOME/.elan/bin:$PATH"' "$HOME/.bashrc" || \
  echo 'export PATH="$HOME/.elan/bin:$PATH"' >> "$HOME/.bashrc"
export PATH="$HOME/.elan/bin:$PATH"

toolchain="$(tr -d '\r\n' < formal/lean/lean-toolchain)"
elan toolchain install "$toolchain"
lake --version
python scripts/check.py --static
