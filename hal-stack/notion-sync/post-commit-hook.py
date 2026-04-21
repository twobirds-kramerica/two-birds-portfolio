#!/usr/bin/env python3
"""post-commit-hook.py — Claude Code PostToolUse hook.

Fires after Claude Code runs a Bash `git commit *` command. Appends a
bulleted-list-item block describing the commit to the Notion page
"SESSION-STATE (Live)" (348a09cf-876a-815c-a9ed-cd8a4ab2767e).

Mechanical data only (hash / subject / author / files / timestamp). The
"Next Action: [blocker analysis]" semantic field is written by Claude at
sprint-completion time via SESSION-STATE.md, not by this hook.

Fails soft: any missing dependency, missing API key, network error, or
Notion API error exits 0 silently. The hook never blocks a commit.

Invoked by .claude/settings.json PostToolUse hook with matcher="Bash" and
if="Bash(git commit*)".
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib import error as urlerror
from urllib import request as urlrequest

NOTION_PAGE_ID = "348a09cf-876a-815c-a9ed-cd8a4ab2767e"
NOTION_VERSION = "2025-09-03"
TIMEOUT = 10

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SYNC_LOG = REPO_ROOT / "hal-stack" / "notion-sync" / "SYNC-LOG.md"


def _exit(code: int = 0) -> None:
    sys.exit(code)


def _log_failure(ts: str, http: str, short: str, subject: str) -> None:
    """Best-effort: append a line to SYNC-LOG.md. Never raises."""
    try:
        SYNC_LOG.parent.mkdir(parents=True, exist_ok=True)
        with SYNC_LOG.open("a", encoding="utf-8") as f:
            f.write(f"- {ts} — post-commit-hook: HTTP {http} on commit {short} ({subject})\n")
    except OSError:
        pass


def _run(cmd: list[str], cwd: str | None = None) -> str | None:
    """Run a git subcommand; return stdout stripped or None on failure."""
    try:
        r = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=5, check=False
        )
        if r.returncode != 0:
            return None
        return (r.stdout or "").strip()
    except (OSError, subprocess.TimeoutExpired):
        return None


def main() -> int:
    # --- Guards ---
    api_key = os.environ.get("NOTION_API_KEY", "").strip()
    if not api_key:
        return 0

    # --- Read stdin (Claude hook JSON) ---
    try:
        stdin_raw = sys.stdin.read()
    except (OSError, ValueError):
        return 0
    if not stdin_raw:
        return 0

    try:
        hook = json.loads(stdin_raw)
    except json.JSONDecodeError:
        return 0

    cmd = (hook.get("tool_input") or {}).get("command") or ""
    if "git commit" not in cmd:
        # defensive: the settings.json `if` filter should already prevent this
        return 0

    # Claude Code runs this hook as a subprocess of itself — our os.getcwd()
    # is already the repo dir Claude was invoked from. No need to parse the
    # JSON 'cwd' field (which would require careful Windows escape handling).
    cwd = os.getcwd()

    # --- Collect git metadata ---
    if _run(["git", "rev-parse", "--verify", "HEAD"], cwd=cwd) is None:
        return 0

    short   = _run(["git", "rev-parse", "--short", "HEAD"], cwd=cwd) or "?"
    subject = _run(["git", "log", "-1", "--format=%s"], cwd=cwd) or "(no subject)"
    author  = _run(["git", "log", "-1", "--format=%an"], cwd=cwd) or "?"
    branch  = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd) or "?"
    repo_root = _run(["git", "rev-parse", "--show-toplevel"], cwd=cwd) or cwd
    repo = Path(repo_root).name or "?"

    files_raw = _run(["git", "show", "--name-only", "--format=", "HEAD"], cwd=cwd) or ""
    files_list = [f for f in files_raw.splitlines() if f.strip()][:6]
    files = ", ".join(files_list) if files_list else "(no files)"

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # --- Build Notion PATCH payload ---
    body = {
        "children": [
            {
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {"type": "text", "text": {"content": f"{ts}  "}},
                        {
                            "type": "text",
                            "text": {"content": short},
                            "annotations": {"code": True},
                        },
                        {
                            "type": "text",
                            "text": {
                                "content": f"  {subject}  —  {author} on {repo}/{branch}"
                            },
                        },
                        {
                            "type": "text",
                            "text": {"content": f"  [{files}]"},
                            "annotations": {"italic": True, "color": "gray"},
                        },
                    ]
                },
            }
        ]
    }

    # --- POST to Notion via stdlib (avoids requests dependency for hooks) ---
    req = urlrequest.Request(
        url=f"https://api.notion.com/v1/blocks/{NOTION_PAGE_ID}/children",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
        method="PATCH",
    )
    http = "000"
    try:
        with urlrequest.urlopen(req, timeout=TIMEOUT) as resp:
            http = str(resp.status)
    except urlerror.HTTPError as e:
        http = str(e.code)
    except (urlerror.URLError, OSError, TimeoutError):
        http = "000"

    if http not in ("200", "201"):
        _log_failure(ts, http, short, subject)

    return 0


if __name__ == "__main__":
    try:
        _exit(main())
    except Exception:
        # Belt-and-suspenders: never surface an error to Claude Code.
        _exit(0)
