"""Scan sprint output for human-action markers; auto-file matches to Notion.

Pattern-matches any of the following markers (case-insensitive) in a text blob
and creates a Notion Product Backlog entry for each distinct finding:

  TODO:
  BLOCKED:
  HUMAN NEEDED:
  MANUAL STEP:
  NEEDS AARON:
  AARON TO DO:

For each match, captures the rest of the line (up to 300 chars) as the item
title and the next 3 lines as context. Deduplicates within a single run.

This is the automated-capture complement to the existing convention of
writing `- [ ] **Item** notes` entries into aaron-todos-YYYY-MM-DD.md — it
protects against the failure mode where a TODO surfaces in a sprint output
(e.g. in a commit message, SESSION-STATE entry, or git diff) and nobody
notices because Claude Code's output wasn't read end-to-end.

USAGE (CLI, for piping Claude Code session output):

    some-sprint-script.py | python hal-stack/sprint-system/human-task-capture.py --source S-FOO-BAR

USAGE (import):

    from human_task_capture import scan_and_file
    n_filed = scan_and_file(text, source="S-FOO-BAR", product="DCC")

Deliberately conservative: matches an exact marker + colon only, to avoid
false positives on prose like "TODO list" or "blocked today". Dedupes on
(marker, first 120 chars of following text).

Exit codes:
  0 — scan complete (prints N entries filed; N=0 is OK — not every sprint has markers)
  1 — Notion unreachable (nothing filed; matches still printed to stdout)
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent

_nc_spec = importlib.util.spec_from_file_location(
    "notion_client_mod", REPO_ROOT / "hal-stack" / "notion-sync" / "notion-client.py"
)
_nc = importlib.util.module_from_spec(_nc_spec)  # type: ignore
_nc_spec.loader.exec_module(_nc)  # type: ignore


# Marker → display label. Colon is required to prevent prose false-positives.
MARKERS = {
    r"\bTODO:": "TODO",
    r"\bBLOCKED:": "BLOCKED",
    r"\bHUMAN NEEDED:": "HUMAN NEEDED",
    r"\bMANUAL STEP:": "MANUAL STEP",
    r"\bNEEDS AARON:": "NEEDS AARON",
    r"\bAARON TO DO:": "AARON TO DO",
}

COMBINED_RE = re.compile(
    "(" + "|".join(MARKERS.keys()) + r")\s*(.*)",
    re.IGNORECASE,
)


def _extract(text: str) -> list[dict]:
    """Walk text line-by-line; return list of {marker, title, context}."""
    lines = text.splitlines()
    seen: set[tuple[str, str]] = set()
    findings: list[dict] = []

    for i, line in enumerate(lines):
        m = COMBINED_RE.search(line)
        if not m:
            continue
        marker_raw = m.group(1).upper().rstrip(":")
        # Normalize marker to canonical label
        marker = next(
            (label for pattern, label in MARKERS.items() if re.search(pattern, marker_raw + ":", re.IGNORECASE)),
            marker_raw,
        )
        tail = (m.group(2) or "").strip()
        if not tail:
            # Marker on its own line — grab next non-blank line as the title
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].strip():
                    tail = lines[j].strip()
                    break

        title = tail[:300]
        key = (marker, title[:120].lower())
        if key in seen:
            continue
        seen.add(key)

        # Context: the 3 surrounding lines after the marker
        ctx = "\n".join(lines[i:i + 4]).strip()
        findings.append({"marker": marker, "title": title, "context": ctx, "line_no": i + 1})

    return findings


def scan_and_file(
    text: str, source: str = "unknown", product: str | None = None
) -> int:
    """Scan text and file each finding. Returns count filed to Notion."""
    findings = _extract(text)
    if not findings:
        print(f"HUMAN-TASK-CAPTURE: no markers found in {source}")
        return 0

    print(f"HUMAN-TASK-CAPTURE: found {len(findings)} marker(s) in {source}:")
    for f in findings:
        print(f"  [{f['marker']}] line {f['line_no']}: {f['title'][:80]}")

    try:
        client = _nc.NotionClient()
    except Exception as e:
        print(f"HUMAN-TASK-CAPTURE: Notion unreachable ({e}); matches printed but NOT filed", file=sys.stderr)
        return 0

    filed = 0
    for f in findings:
        try:
            page = _nc.create_backlog_item(
                client,
                item=f"[{f['marker']}] {f['title'][:120]}",
                priority="P2",
                status="Blocked" if f["marker"] in ("BLOCKED", "HUMAN NEEDED", "MANUAL STEP") else "Backlog",
                owner="Aaron",
                type_="Human Action",
                product=product,
                notes=(
                    f"Auto-captured by human-task-capture.py at {datetime.now().strftime('%Y-%m-%d %H:%M')} EST "
                    f"from source={source}, line {f['line_no']}.\n\n"
                    f"**Marker:** {f['marker']}\n"
                    f"**Full title:** {f['title']}\n\n"
                    f"**Surrounding context:**\n```\n{f['context']}\n```"
                ),
            )
            print(f"  -> filed {page.get('id')}")
            filed += 1
        except Exception as e:
            print(f"  -> FAIL: {e}", file=sys.stderr)

    return filed


def _cli() -> int:
    p = argparse.ArgumentParser(description="Scan stdin for TODO/BLOCKED/etc markers; file to Notion.")
    p.add_argument("--source", default="stdin", help="Identifier for this scan (sprint ID, file path, etc.)")
    p.add_argument("--product", default=None, help="Notion Product select value")
    p.add_argument("--file", default=None, help="Read from file instead of stdin")
    args = p.parse_args()

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8", errors="replace")
    else:
        text = sys.stdin.read()

    filed = scan_and_file(text, source=args.source, product=args.product)
    print(f"HUMAN-TASK-CAPTURE: filed {filed} entries")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
