"""CoS Morning Briefing Generator.

Runs overnight (via run-overnight-build.bat) to pre-generate context
for the next day's `cos` check-in. Reads SESSION-STATE.md and Notion
P1 backlog; writes hal-stack/cos/morning-briefing.md.

When Aaron types `cos`, Claude reads this file first before pulling
live calendar/email — the task context is already prepared.

Usage: python hal-stack/cos/morning-briefing.py
"""
from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE      = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
OUT_PATH  = HERE / "morning-briefing.md"
SS_PATH   = REPO_ROOT / "SESSION-STATE.md"

# ── Load Notion client ────────────────────────────────────────────────────────

def load_notion_client():
    nc_path = REPO_ROOT / "hal-stack" / "notion-sync" / "notion-client.py"
    spec = importlib.util.spec_from_file_location("notion_client", nc_path)
    nc   = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nc)
    return nc


# ── Fetch Notion P1 items (Owner=Aaron) ──────────────────────────────────────

def fetch_p1_items(nc) -> list[dict]:
    try:
        cfg    = nc.load_config()
        client = nc.NotionClient(config=cfg)
        pages  = client.query_data_source(
            cfg["product_backlog_data_source"],
            filter_={
                "and": [
                    {"property": "Priority", "select": {"equals": "P1"}},
                    {"property": "Owner",    "select": {"equals": "Aaron"}},
                    {"property": "Status",   "select": {"does_not_equal": "Done"}},
                ]
            }
        )
        return [nc.normalize_page(p) for p in pages]
    except Exception as e:
        return [{"item": f"(Notion unavailable: {e})", "status": "?", "priority": "P1"}]


# ── Read recent SESSION-STATE context ─────────────────────────────────────────

def read_session_state_tail() -> str:
    if not SS_PATH.exists():
        return "(SESSION-STATE.md not found)"
    text = SS_PATH.read_text(encoding="utf-8")
    # Return the last ~60 lines — the most recent sprint entry
    lines = text.splitlines()
    return "\n".join(lines[-60:]) if len(lines) > 60 else text


# ── Write briefing ────────────────────────────────────────────────────────────

def write_briefing(p1_items: list[dict], ss_tail: str) -> None:
    now      = datetime.now(timezone.utc).astimezone()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M %Z")

    lines = [
        f"# CoS Morning Briefing — {date_str}",
        f"_Generated overnight at {time_str}._",
        "",
        "---",
        "",
        "## Your Commands (always here so you never have to remember)",
        "",
        "| Type this | When | What it does |",
        "|---|---|---|",
        "| `cos` | Any morning | Full check-in: wins + calendar + email + priorities + energy |",
        "| `cos-week` | Monday | Weekly Priority Dashboard + overcommitment check |",
        "| `cos-retro` | Friday | Pattern review + weekly summary + Monday setup |",
        "| `next sprint` | Ready to build | Picks and locks next sprint from Notion backlog |",
        "| `state` | Feeling lost | Top 3 next actions from SESSION-STATE |",
        "| `just go` | Quick autonomous build | One sprint, no chaining, returns control after |",
        "",
        "---",
        "",
        "## P1 Open Actions (Owner: Aaron)",
        "",
    ]

    if p1_items:
        for item in p1_items:
            status = item.get("status") or "?"
            title  = item.get("item")   or "(untitled)"
            lines.append(f"- **[{status}]** {title}")
    else:
        lines.append("- (none — all P1 items are complete or unassigned)")

    lines += [
        "",
        "---",
        "",
        "## Recent Sprint Context (from SESSION-STATE)",
        "",
        "```",
        ss_tail.strip(),
        "```",
        "",
        "---",
        "",
        "## CoS Stale-Item Flags",
        "",
        "_Filled in by Claude when `cos` runs — checks for items not mentioned in 3+ days._",
        "",
        "---",
        "",
        f"_Next step: type `cos` to add live calendar + email and run the full check-in._",
    ]

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"OK  CoS morning briefing written: {OUT_PATH}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    print("CoS morning briefing generator starting...")

    try:
        nc = load_notion_client()
        print("    Loading Notion P1 items (Owner=Aaron)...")
        p1_items = fetch_p1_items(nc)
        print(f"    Found {len(p1_items)} P1 item(s).")
    except Exception as e:
        print(f"WARN  Notion unavailable ({e}) — briefing will note this.")
        p1_items = [{"item": f"Notion unavailable: {e}", "status": "?"}]

    print("    Reading SESSION-STATE tail...")
    ss_tail = read_session_state_tail()

    write_briefing(p1_items, ss_tail)
    return 0


if __name__ == "__main__":
    sys.exit(main())
