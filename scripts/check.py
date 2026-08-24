#!/usr/bin/env python3
"""Cross-platform project verification for a clean checkout."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "CLAIM_LEDGER.md"


def run(command: list[str], cwd: Path) -> None:
    print("+", " ".join(command))
    try:
        subprocess.run(command, cwd=cwd, check=True)
    except FileNotFoundError as error:
        raise RuntimeError(f"required command not found on PATH: {command[0]}") from error


def check_claim_ledger() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    matches = re.findall(r"`(formal/lean/[^`#]+)#([A-Za-z_][A-Za-z0-9_]*)`", text)
    if not matches:
        raise RuntimeError("claim ledger contains no formal evidence links")
    for relative_path, declaration in matches:
        source = ROOT / relative_path
        if not source.is_file():
            raise RuntimeError(f"missing formal evidence file: {relative_path}")
        if not re.search(rf"\b(?:theorem|lemma|def)\s+{re.escape(declaration)}\b", source.read_text(encoding="utf-8")):
            raise RuntimeError(f"missing declaration {declaration} in {relative_path}")
    print(f"claim ledger: {len(matches)} formal evidence link(s) verified")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", action="store_true", help="also build the LaTeX paper")
    args = parser.parse_args()
    check_claim_ledger()
    run(["lake", "build"], ROOT / "formal" / "lean")
    if args.paper:
        if not shutil.which("latexmk"):
            raise RuntimeError("--paper requires latexmk on PATH")
        run(["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"], ROOT / "paper")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f"check failed: {error}", file=sys.stderr)
        raise SystemExit(1)
