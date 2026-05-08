"""Overnight backlog health check for HAL Stack.

Queries the Notion Product Backlog, applies four health rules, and appends
a timestamped report to SESSION-STATE.md.

Exit codes:
  0 — ran successfully (findings may exist)
  1 — Notion API unreachable
  2 — config/auth error
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
SESSION_STATE_PATH = REPO_ROOT / "SESSION-STATE.md"

_spec = importlib.util.spec_from_file_location("notion_client", HERE / "notion-client.py")
_nc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_nc)  # type: ignore[attr-defined]

NotionClient = _nc.NotionClient
NotionError = _nc.NotionError
log_sync_event = _nc.log_sync_event
normalize_page = _nc.normalize_page

DATABASE_ID = "dee08637-7122-46cd-bc29-7775ce3ab8f6"
STALE_P1_DAYS   = 7
STALE_READY_DAYS = 14
ORPHANED_DAYS   = 14


def days_since(iso: str) -> int:
    if not iso:
        return 0
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - dt).days


def recent_git_mention(text: str) -> bool:
    """True if a git commit in the last ORPHANED_DAYS days mentions this string."""
    try:
        result = subprocess.run(
            ["git", "log", f"--since={ORPHANED_DAYS} days ago", "--oneline", "--all"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        return text.lower() in result.stdout.lower()
    except Exception:
        return False


def run() -> int:
    try:
        client = NotionClient()
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    try:
        raw_pages = client.query_data_source(
            DATABASE_ID,
            filter_={"property": "Status", "select": {"does_not_equal": "Done"}},
        )
    except NotionError as e:
        print(f"Notion API error: {e}", file=sys.stderr)
        log_sync_event(f"backlog-health FAILED — {e}")
        return 1

    stale_p1, stale_ready, orphaned, p0_not_running = [], [], [], []

    for raw in raw_pages:
        page = normalize_page(raw)
        name    = page["item"] or page["id"]
        status  = page["status"] or ""
        priority = page["priority"] or ""
        age     = days_since(raw.get("created_time", ""))

        if priority == "P1" and status == "Backlog" and age >= STALE_P1_DAYS:
            stale_p1.append(f"{name} ({age}d old)")

        if status == "Ready" and age >= STALE_READY_DAYS:
            stale_ready.append(f"{name} ({age}d old)")

        if status == "In Progress" and not recent_git_mention(name[:30]):
            orphaned.append(f"{name} (no git mention in {ORPHANED_DAYS}d)")

        if priority == "P0" and status != "In Progress":
            p0_not_running.append(f"{name} (status: {status})")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    findings = any([stale_p1, stale_ready, orphaned, p0_not_running])

    def fmt(lst: list[str]) -> str:
        return ", ".join(lst) if lst else "none"

    lines = [
        "",
        f"## /backlog-triage (overnight) — {now}",
        f"- Total open items: {len(raw_pages)}",
        f"- [STALE-P1] (P1 Backlog >{STALE_P1_DAYS}d): {fmt(stale_p1)}",
        f"- [STALE-READY] (Ready >{STALE_READY_DAYS}d): {fmt(stale_ready)}",
        f"- [ORPHANED] (In Progress, no git {ORPHANED_DAYS}d): {fmt(orphaned)}",
        f"- [P0-NOT-RUNNING]: {fmt(p0_not_running)}",
        "- ACTION NEEDED — review at next session start" if findings else "- All clear",
    ]
    report = "\n".join(lines) + "\n"

    try:
        with SESSION_STATE_PATH.open("a", encoding="utf-8") as f:
            f.write(report)
        print(report)
    except OSError as e:
        print(f"Could not write SESSION-STATE.md: {e}", file=sys.stderr)
        return 1

    log_sync_event(f"backlog-health complete — {len(raw_pages)} open, findings={findings}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
