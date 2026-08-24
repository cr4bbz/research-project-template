#!/usr/bin/env python3
"""Cross-platform project verification for a clean checkout."""
from __future__ import annotations

import argparse
import compileall
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "CLAIM_LEDGER.md"
PROFILE = ROOT / "PROJECT_PROFILE.toml"
EVIDENCE_TYPES = {"formal-theorem", "bounded-exhaustive-check", "computational-experiment", "worked-example", "interpretation"}
STATUSES = {"planned", "checked", "established", "withdrawn"}


def run(command, cwd):
    print("+", " ".join(command))
    try:
        subprocess.run(command, cwd=cwd, check=True)
    except FileNotFoundError as error:
        raise RuntimeError("required command not found on PATH: " + command[0]) from error


def read_profile():
    if not PROFILE.is_file():
        raise RuntimeError("missing PROJECT_PROFILE.toml")
    profile = tomllib.loads(PROFILE.read_text(encoding="utf-8"))
    if profile.get("profile_version") != 1:
        raise RuntimeError("unsupported PROJECT_PROFILE.toml version")
    modules = profile.get("modules")
    if not isinstance(modules, dict) or any(not isinstance(modules.get(name), bool) for name in ("formal", "analysis", "paper")):
        raise RuntimeError("profile must declare boolean formal, analysis, and paper modules")
    return profile


def rows():
    result = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and "---" not in line:
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if cells[0] != "ID":
                result.append(cells)
    return result


def check_ledger():
    claims = rows()
    if not claims:
        raise RuntimeError("claim ledger contains no claim rows")
    links = []
    for claim in claims:
        if len(claim) != 8 or any(not value for value in claim):
            raise RuntimeError("each claim row needs eight non-empty columns")
        claim_id, kind, _, _, scope, evidence, paper, status = claim
        if not re.fullmatch(r"C-[0-9]{3,}", claim_id):
            raise RuntimeError("invalid claim id: " + claim_id)
        if kind not in EVIDENCE_TYPES or status not in STATUSES:
            raise RuntimeError("invalid evidence type or status for " + claim_id)
        if kind == "bounded-exhaustive-check" and "bound" not in scope.lower():
            raise RuntimeError("bounded evidence must state bounded scope: " + claim_id)
        if not (ROOT / paper).is_file():
            raise RuntimeError("missing paper location: " + paper)
        match = re.fullmatch(r"(formal/lean/[^#]+)#([A-Za-z_][A-Za-z0-9_]*)", evidence)
        if kind == "formal-theorem":
            if not match:
                raise RuntimeError("formal theorem needs Lean declaration link: " + claim_id)
            links.append(match.groups())
    for relative, declaration in links:
        source = ROOT / relative
        if not source.is_file() or not re.search(r"\b(?:theorem|lemma|def)\s+" + re.escape(declaration) + r"\b", source.read_text(encoding="utf-8")):
            raise RuntimeError("missing formal declaration: " + relative + "#" + declaration)
    print("claim ledger:", len(claims), "row(s),", len(links), "formal link(s) verified")


def check_release(profile):
    release = profile.get("release", {})
    if not release.get("enabled", False):
        raise RuntimeError("release checks disabled; set release.enabled = true when ready")
    required = [ROOT / "LICENSE"]
    if release.get("require_content_license", True):
        required.append(ROOT / "LICENSE-CONTENT")
    if release.get("require_citation", True):
        required.append(ROOT / "CITATION.cff")
    for path in required:
        if not path.is_file():
            raise RuntimeError("release metadata missing: " + str(path.relative_to(ROOT)))
        if re.search(r"PROJECT_NAME|AUTHOR_|YYYY-MM-DD", path.read_text(encoding="utf-8")):
            raise RuntimeError("release metadata contains placeholders: " + str(path.relative_to(ROOT)))
    print("release metadata verified")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", action="store_true")
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--static", action="store_true")
    args = parser.parse_args()
    profile = read_profile()
    check_ledger()
    if profile["modules"]["analysis"]:
        if not compileall.compile_dir(ROOT / "analysis", quiet=1):
            raise RuntimeError("analysis sources do not compile")
        print("analysis sources compile")
    if profile["modules"]["formal"] and not args.static:
        run(["lake", "build"], ROOT / "formal" / "lean")
    if args.paper and not profile["modules"]["paper"]:
        raise RuntimeError("paper requested but disabled by profile")
    if args.paper and not args.static:
        if not shutil.which("latexmk"):
            raise RuntimeError("--paper requires latexmk")
        run(["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"], ROOT / "paper")
    if args.release:
        check_release(profile)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print("check failed:", error, file=sys.stderr)
        raise SystemExit(1)

