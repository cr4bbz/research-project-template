#!/usr/bin/env python3
"""Cross-platform project verification for a clean checkout."""
from __future__ import annotations

import argparse
import compileall
from datetime import date
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "CLAIM_LEDGER.md"
VISUALIZATION_PLAN = ROOT / "docs" / "VISUALIZATION_PLAN.md"
PROFILE = ROOT / "PROJECT_PROFILE.toml"
PAPER_VERSION = ROOT / "paper" / "PAPER_VERSION.tex"
RENDERS = ROOT / "paper" / "renders"
RENDER_LOG = ROOT / "docs" / "RENDER_LOG.md"
EVIDENCE_TYPES = {"formal-theorem", "mathematical-proof", "bounded-exhaustive-check", "computational-experiment", "worked-example", "interpretation"}
STATUSES = {"planned", "checked", "established", "withdrawn"}
SCOPE_PREFIXES = {"bounded", "unbounded"}
NOT_APPLICABLE = "—"


def run(command, cwd):
    print("+", " ".join(command))
    try:
        subprocess.run(command, cwd=cwd, check=True)
    except FileNotFoundError as error:
        hints = {
            "lake": "Reopen the repository in its Codespace/dev container or install elan.",
            "latexmk": "Reopen the repository in its Codespace/dev container or install latexmk.",
        }
        message = "required command not found on PATH: " + command[0]
        if command[0] in hints:
            message += ". " + hints[command[0]]
        raise RuntimeError(message) from error


def read_profile():
    if not PROFILE.is_file():
        raise RuntimeError("missing PROJECT_PROFILE.toml")
    profile = tomllib.loads(PROFILE.read_text(encoding="utf-8"))
    if profile.get("profile_version") not in {1, 2, 3}:
        raise RuntimeError("unsupported PROJECT_PROFILE.toml version")
    modules = profile.get("modules")
    if not isinstance(modules, dict) or any(not isinstance(modules.get(name), bool) for name in ("formal", "analysis", "paper")):
        raise RuntimeError("profile must declare boolean formal, analysis, and paper modules")
    if profile["modules"]["analysis"] and profile["profile_version"] >= 2:
        analysis = profile.get("analysis")
        if not isinstance(analysis, dict) or not isinstance(analysis.get("command"), str):
            raise RuntimeError("active analysis module needs analysis.command")
        if not isinstance(analysis.get("outputs"), list) or not analysis["outputs"] or not all(isinstance(path, str) for path in analysis["outputs"]):
            raise RuntimeError("active analysis module needs non-empty analysis.outputs")
    if profile["modules"]["paper"] and profile["profile_version"] >= 3:
        paper = profile.get("paper")
        if not isinstance(paper, dict):
            raise RuntimeError("active paper module needs [paper] metadata")
        if not isinstance(paper.get("slug"), str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", paper["slug"]):
            raise RuntimeError("paper.slug must use lowercase kebab-case")
        if not isinstance(paper.get("version"), str) or not re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", paper["version"]):
            raise RuntimeError("paper.version must use MAJOR.MINOR.PATCH")
    return profile


def repository_path(value, label):
    path = Path(value)
    if not value or path.is_absolute() or ".." in path.parts:
        raise RuntimeError(label + " must be a safe repository-relative path: " + value)
    return ROOT / path


def rows():
    result = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and "---" not in line:
            cells = []
            cell = []
            escaped = False
            for character in line.strip().strip("|"):
                if escaped:
                    cell.append(character)
                    escaped = False
                elif character == "\\":
                    escaped = True
                elif character == "|":
                    cells.append("".join(cell).strip())
                    cell = []
                else:
                    cell.append(character)
            if escaped:
                cell.append("\\")
            cells.append("".join(cell).strip())
            if cells[0] != "ID":
                result.append(cells)
    return result


def visualization_rows():
    result = []
    for line in VISUALIZATION_PLAN.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and "---" not in line:
            cells = []
            cell = []
            escaped = False
            for character in line.strip().strip("|"):
                if escaped:
                    cell.append(character)
                    escaped = False
                elif character == "\\":
                    escaped = True
                elif character == "|":
                    cells.append("".join(cell).strip())
                    cell = []
                else:
                    cell.append(character)
            if escaped:
                cell.append("\\")
            cells.append("".join(cell).strip())
            if cells[0] != "Claim ID":
                result.append(cells)
    return result


def check_ledger(profile):
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
        scope_prefix, separator, scope_detail = scope.partition(":")
        if scope_prefix not in SCOPE_PREFIXES or not separator or not scope_detail.strip():
            raise RuntimeError("scope must start with bounded: or unbounded: " + claim_id)
        if kind == "bounded-exhaustive-check" and scope_prefix != "bounded":
            raise RuntimeError("bounded evidence needs a bounded: scope: " + claim_id)
        if profile["modules"]["paper"]:
            if paper == NOT_APPLICABLE or not repository_path(paper, "paper location").is_file():
                raise RuntimeError("active paper module needs an existing paper location: " + claim_id)
        elif paper != NOT_APPLICABLE:
            raise RuntimeError("disabled paper module requires — as paper location: " + claim_id)
        match = re.fullmatch(r"(formal/lean/[^#]+)#([A-Za-z_][A-Za-z0-9_]*)", evidence)
        if kind == "formal-theorem":
            if not profile["modules"]["formal"]:
                raise RuntimeError("formal theorem claim requires active formal module: " + claim_id)
            if not match:
                raise RuntimeError("formal theorem needs Lean declaration link: " + claim_id)
            links.append(match.groups())
    for relative, declaration in links:
        source = ROOT / relative
        if not source.is_file() or not re.search(r"\b(?:theorem|lemma|def)\s+" + re.escape(declaration) + r"\b", source.read_text(encoding="utf-8")):
            raise RuntimeError("missing formal declaration: " + relative + "#" + declaration)
    print("claim ledger:", len(claims), "row(s),", len(links), "formal link(s) verified")
    return claims


def check_visualization_plan(profile, claims):
    if not profile["modules"]["paper"]:
        return
    if not VISUALIZATION_PLAN.is_file():
        raise RuntimeError("active paper module needs docs/VISUALIZATION_PLAN.md")
    claim_papers = {claim[0]: claim[6] for claim in claims}
    planned = visualization_rows()
    if not planned:
        raise RuntimeError("visualization plan contains no decision rows")
    seen = set()
    decisions = {"figure", "table", "diagram", "no-figure"}
    for row in planned:
        if len(row) != 7 or any(not value for value in row):
            raise RuntimeError("each visualization row needs seven non-empty columns")
        claim_id, decision, _, _, source, output, paper = row
        if claim_id not in claim_papers or claim_id in seen:
            raise RuntimeError("visualization plan needs one unique row per ledger claim: " + claim_id)
        if decision not in decisions:
            raise RuntimeError("invalid visualization decision for " + claim_id)
        if paper != claim_papers[claim_id]:
            raise RuntimeError("visualization paper location must match ledger: " + claim_id)
        if decision == "no-figure":
            if source != NOT_APPLICABLE or output != NOT_APPLICABLE:
                raise RuntimeError("no-figure decision must use — for source and output: " + claim_id)
        else:
            if not profile["modules"]["analysis"]:
                raise RuntimeError("visual output requires active analysis module: " + claim_id)
            if not repository_path(source, "visualization source").is_file():
                raise RuntimeError("missing visualization source: " + source)
            if profile["profile_version"] >= 2 and output not in profile["analysis"]["outputs"]:
                raise RuntimeError("visualization output is not declared by analysis contract: " + output)
        seen.add(claim_id)
    missing = set(claim_papers) - seen
    if missing:
        raise RuntimeError("visualization plan missing ledger claim(s): " + ", ".join(sorted(missing)))
    print("visualization plan:", len(planned), "decision(s) verified")


def check_paper_metadata(profile):
    if not profile["modules"]["paper"] or profile["profile_version"] < 3:
        return
    if not PAPER_VERSION.is_file():
        raise RuntimeError("active paper module needs paper/PAPER_VERSION.tex")
    source = PAPER_VERSION.read_text(encoding="utf-8")
    match = re.search(r"\\newcommand\{\\paperversion\}\{([^}]+)\}", source)
    if not match:
        raise RuntimeError("paper/PAPER_VERSION.tex must define \\paperversion")
    if match.group(1) != profile["paper"]["version"]:
        raise RuntimeError("paper version differs between PROJECT_PROFILE.toml and PAPER_VERSION.tex")
    print("paper metadata:", profile["paper"]["slug"], "v" + profile["paper"]["version"])


def check_analysis(profile, execute):
    if not profile["modules"]["analysis"]:
        return
    if not compileall.compile_dir(ROOT / "analysis", quiet=1):
        raise RuntimeError("analysis sources do not compile")
    print("analysis sources compile")
    if not execute or profile["profile_version"] == 1:
        return
    analysis = profile["analysis"]
    command = repository_path(analysis["command"], "analysis.command")
    if not command.is_file() or command.suffix != ".py":
        raise RuntimeError("analysis.command must name a tracked Python source")
    run([sys.executable, str(command.relative_to(ROOT))], ROOT)
    for output in analysis["outputs"]:
        output_path = repository_path(output, "analysis output")
        if not output_path.is_file() or output_path.stat().st_size == 0:
            raise RuntimeError("analysis did not produce declared output: " + output)
    print("analysis outputs verified:", len(analysis["outputs"]))


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
    citation = ROOT / "CITATION.cff"
    if citation in required:
        content = citation.read_text(encoding="utf-8")
        for field in ("cff-version", "title", "version", "date-released"):
            if not re.search(r"^" + re.escape(field) + r":\s*\S", content, re.MULTILINE):
                raise RuntimeError("CITATION.cff missing required field: " + field)
        author_entry = re.search(r"^authors:\s*\n(?:^[ \t]+.*\n)*?^[ \t]+-\s+(?:family-names|name):\s*\S", content, re.MULTILINE)
        if not author_entry:
            raise RuntimeError("CITATION.cff needs at least one named author")
        date_match = re.search(r"^date-released:\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})", content, re.MULTILINE)
        if not date_match:
            raise RuntimeError("CITATION.cff date-released must use YYYY-MM-DD")
        try:
            date.fromisoformat(date_match.group(1))
        except ValueError as error:
            raise RuntimeError("CITATION.cff date-released is not a real date") from error
        if profile["modules"]["paper"] and profile["profile_version"] >= 3:
            version_match = re.search(r"^version:\s*['\"]?([^\s'\"]+)", content, re.MULTILINE)
            if not version_match or version_match.group(1) != profile["paper"]["version"]:
                raise RuntimeError("CITATION.cff version must match paper.version")
    if profile["modules"]["paper"] and profile["profile_version"] >= 3:
        expected = RENDERS / render_name(profile, date.today())
        if not expected.is_file():
            raise RuntimeError("release needs today's versioned paper render: " + str(expected.relative_to(ROOT)))
        manifest = render_manifest_path(expected)
        if not manifest.is_file():
            raise RuntimeError("release needs render manifest: " + str(manifest.relative_to(ROOT)))
        if not render_log_contains(expected, profile, date.today()):
            raise RuntimeError("release needs matching render-log entry: " + str(expected.relative_to(ROOT)))
    print("release metadata verified")


def render_name(profile, render_date):
    if profile["profile_version"] < 3:
        return None
    return profile["paper"]["slug"] + "-v" + profile["paper"]["version"] + "-" + render_date.isoformat() + ".pdf"


def render_manifest_path(render):
    return render.with_suffix(render.suffix + ".json")


def render_source_fingerprint():
    digest = hashlib.sha256()
    excluded_suffixes = {".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out", ".pdf"}
    sources = []
    for path in (ROOT / "paper").rglob("*"):
        if path.is_file() and RENDERS not in path.parents and path.suffix not in excluded_suffixes:
            sources.append(path)
    bibliography = ROOT / "references" / "bibliography.bib"
    if bibliography.is_file():
        sources.append(bibliography)
    for path in sorted(sources, key=lambda item: item.relative_to(ROOT).as_posix()):
        relative = path.relative_to(ROOT).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(4, "big"))
        digest.update(relative)
        content = path.read_bytes()
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest()


def render_log_contains(render, profile, render_date):
    if not RENDER_LOG.is_file():
        return False
    expected = render.relative_to(ROOT).as_posix()
    for line in RENDER_LOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and "---" not in line:
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) == 6 and cells[0] == expected:
                return cells[1] == profile["paper"]["version"] and cells[2] == render_date.isoformat() and cells[3] != NOT_APPLICABLE
    return False


def store_versioned_render(profile):
    name = render_name(profile, date.today())
    if name is None:
        return
    source = ROOT / "paper" / "main.pdf"
    if not source.is_file() or source.stat().st_size == 0:
        raise RuntimeError("LaTeX did not produce paper/main.pdf")
    RENDERS.mkdir(parents=True, exist_ok=True)
    target = RENDERS / name
    fingerprint = render_source_fingerprint()
    manifest = render_manifest_path(target)
    if target.is_file():
        if not manifest.is_file():
            raise RuntimeError("existing versioned render has no manifest; increment paper.version before rendering")
        try:
            prior = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise RuntimeError("existing versioned render has invalid manifest; increment paper.version before rendering") from error
        if prior.get("source_fingerprint") != fingerprint:
            raise RuntimeError("existing versioned render belongs to different sources; increment paper.version before rendering")
        print("versioned paper render already matches sources:", target.relative_to(ROOT))
        return target
    shutil.copy2(source, target)
    manifest.write_text(
        json.dumps(
            {
                "render": target.name,
                "paper_version": profile["paper"]["version"],
                "render_date": date.today().isoformat(),
                "source_fingerprint": fingerprint,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print("versioned paper render:", target.relative_to(ROOT))
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", action="store_true")
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--render-existing-paper", action="store_true")
    parser.add_argument("--static", action="store_true")
    args = parser.parse_args()
    if args.paper and args.render_existing_paper:
        raise RuntimeError("use either --paper or --render-existing-paper")
    if args.release and args.static:
        raise RuntimeError("--release requires a full check; do not combine it with --static")
    profile = read_profile()
    claims = check_ledger(profile)
    check_visualization_plan(profile, claims)
    check_paper_metadata(profile)
    check_analysis(profile, execute=not args.static)
    if profile["modules"]["formal"] and not args.static:
        run(["lake", "build"], ROOT / "formal" / "lean")
    render_requested = args.paper or args.render_existing_paper
    if render_requested and not profile["modules"]["paper"]:
        raise RuntimeError("paper requested but disabled by profile")
    if args.render_existing_paper:
        store_versioned_render(profile)
    elif (args.paper or (args.release and profile["modules"]["paper"])) and not args.static:
        if not shutil.which("latexmk"):
            raise RuntimeError("paper render requires latexmk")
        run(["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"], ROOT / "paper")
        store_versioned_render(profile)
    if args.release:
        check_release(profile)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print("check failed:", error, file=sys.stderr)
        raise SystemExit(1)
