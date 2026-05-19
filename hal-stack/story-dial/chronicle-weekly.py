#!/usr/bin/env python3
"""
Story Dial — Chronicle Weekly (Layer 1)
Autonomous Thursday script: pulls git commits → creates Notion stub.
No Claude API needed. Raw data only.
Run: python hal-stack/story-dial/chronicle-weekly.py
Scheduled: Thursday 2am via run-overnight-build.bat
"""

import os
import sys
import subprocess
import json
import re
import importlib.util
from datetime import datetime, timezone

# ── Config ──────────────────────────────────────────────────────────────────

REPOS = [
    r"C:\twobirds\two-birds-portfolio",
    r"C:\twobirds\digital-confidence",
    r"C:\twobirds\career-coach",
    r"C:\twobirds\clarity",
    r"C:\twobirds\two-birds-innovation",
    r"C:\twobirds\aaron-patzalek",
    r"C:\twobirds\kevins-apartment-search",
]

STORY_COMMIT_PREFIXES = ("feat:", "fix:", "log(SESSION-STATE):", "feat(hal):", "feat(dcc):")
DAYS_BACK = 7

# Notion Agency Log database ID (from SESSION-STATE / existing chronicle sprints)
# This is the parent page where new entries are created as sub-pages
AGENCY_LOG_PARENT_ID = "347a09cf-876a-81fb-9a5c-eca696fb585b"  # Command Center

LOG_PATH = r"C:\twobirds\two-birds-portfolio\logs\automated-run-log.md"
SYNC_LOG = r"C:\twobirds\two-birds-portfolio\hal-stack\notion-sync\SYNC-LOG.md"

# ── Notion client loader ─────────────────────────────────────────────────────

def _load_notion_client():
    """Load notion-client.py (hyphen filename) via importlib."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    client_path = os.path.join(base, "notion-sync", "notion-client.py")
    spec = importlib.util.spec_from_file_location("notion_client", client_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# ── Git helpers ───────────────────────────────────────────────────────────────

def get_commits_since(repo_path: str, days: int) -> list[dict]:
    """Return list of {hash, date, message, repo} for story-worthy commits."""
    if not os.path.isdir(repo_path):
        return []
    try:
        result = subprocess.run(
            ["git", "log", f"--since={days} days ago", "--no-merges",
             "--format=%H|%ad|%s", "--date=short"],
            cwd=repo_path, capture_output=True, text=True, timeout=15
        )
        commits = []
        for line in result.stdout.strip().splitlines():
            parts = line.split("|", 2)
            if len(parts) != 3:
                continue
            h, date, msg = parts
            if msg.startswith(STORY_COMMIT_PREFIXES):
                repo_name = os.path.basename(repo_path)
                commits.append({"hash": h[:8], "date": date, "message": msg, "repo": repo_name})
        return commits
    except Exception:
        return []


def collect_all_commits(days: int = DAYS_BACK) -> list[dict]:
    all_commits = []
    for repo in REPOS:
        all_commits.extend(get_commits_since(repo, days))
    all_commits.sort(key=lambda c: c["date"], reverse=True)
    return all_commits


# ── Story candidate selection ─────────────────────────────────────────────────

STORY_SIGNALS = [
    "S-CHRONICLE", "S-VOICE", "S-SME", "S-DCC", "feat(hal)",
    "founding-board", "persona", "boardroom", "loop", "discovery",
]

def identify_story_candidates(commits: list[dict]) -> list[dict]:
    """Heuristically rank commits by story potential."""
    scored = []
    for c in commits:
        score = 0
        msg_lower = c["message"].lower()
        for signal in STORY_SIGNALS:
            if signal.lower() in msg_lower:
                score += 2
        if "log(SESSION-STATE)" in c["message"]:
            score += 1
        if "feat:" in c["message"] or "feat(" in c["message"]:
            score += 1
        scored.append((score, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for score, c in scored[:3] if score > 0]


# ── SESSION-STATE reader ──────────────────────────────────────────────────────

def read_recent_session_state_entries() -> str:
    """Extract the last 1-2 sprint entries from SESSION-STATE.md."""
    ss_path = r"C:\twobirds\two-birds-portfolio\SESSION-STATE.md"
    if not os.path.isfile(ss_path):
        return "(SESSION-STATE.md not found)"
    with open(ss_path, encoding="utf-8") as f:
        content = f.read()
    # Find all sprint headers
    sections = re.split(r"(?=## ⚡ 2026-)", content)
    recent = sections[-2:] if len(sections) >= 2 else sections
    excerpt = "\n---\n".join(s[:1200] for s in recent)
    return excerpt[:3000]


# ── Get next entry number ─────────────────────────────────────────────────────

def get_next_entry_number() -> int:
    """Read existing entry numbers from Notion, return next."""
    # Simple heuristic: read SYNC-LOG for chronicle entries
    try:
        with open(SYNC_LOG, encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(r"chronicle.*?#(\d+)", content, re.IGNORECASE)
        if matches:
            return max(int(m) for m in matches) + 1
    except Exception:
        pass
    # Fallback: assume #006 was last, so next is #007
    return 7


# ── Build Notion page content ─────────────────────────────────────────────────

def build_notion_page_blocks(
    entry_num: int,
    commits: list[dict],
    candidates: list[dict],
    session_excerpt: str,
    week_of: str,
) -> list[dict]:
    """Build Notion block array for the raw data stub."""

    def para(text: str, bold: bool = False) -> dict:
        rt = {"type": "text", "text": {"content": text}}
        if bold:
            rt["annotations"] = {"bold": True}
        return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [rt]}}

    def heading(text: str, level: int = 2) -> dict:
        htype = f"heading_{level}"
        return {"object": "block", "type": htype, htype: {
            "rich_text": [{"type": "text", "text": {"content": text}}]
        }}

    def bullet(text: str) -> dict:
        return {"object": "block", "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text}}]}}

    def divider() -> dict:
        return {"object": "block", "type": "divider", "divider": {}}

    def code_block(text: str) -> dict:
        return {"object": "block", "type": "code",
                "code": {"rich_text": [{"type": "text", "text": {"content": text[:1900]}}],
                         "language": "plain text"}}

    blocks = []

    # Status callout
    blocks.append({
        "object": "block", "type": "callout",
        "callout": {
            "rich_text": [{"type": "text", "text": {"content": f"Status: Raw Data Ready — Week of {week_of} | Awaiting Chronicle session (dial 3 default)"}}],
            "icon": {"emoji": "📋"}, "color": "yellow_background"
        }
    })

    blocks.append(divider())

    # Metadata
    blocks.append(heading("Metadata", 2))
    blocks.append(bullet(f"Entry: #{entry_num:03d}"))
    blocks.append(bullet(f"Week of: {week_of}"))
    blocks.append(bullet(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} EST"))
    blocks.append(bullet("Scribe Rules: scribe-rules.md (honesty + receipts)"))
    blocks.append(bullet("Dial default: 3 (LinkedIn Long)"))

    blocks.append(divider())

    # Commits
    blocks.append(heading("Commits This Week", 2))
    if commits:
        for c in commits[:15]:
            blocks.append(bullet(f"[{c['repo']}] {c['hash']} ({c['date']}) — {c['message']}"))
    else:
        blocks.append(para("No story-worthy commits found this week."))

    blocks.append(divider())

    # Story candidates
    blocks.append(heading("Story Candidates (top picks)", 2))
    if candidates:
        for i, c in enumerate(candidates, 1):
            blocks.append(bullet(f"{i}. [{c['repo']}] {c['hash']} — {c['message']}"))
    else:
        blocks.append(para("No strong candidates identified — review commits above and select manually."))

    blocks.append(divider())

    # SESSION-STATE excerpt
    blocks.append(heading("SESSION-STATE — Recent Sprints", 2))
    blocks.append(para("(Excerpt — for full context read SESSION-STATE.md)"))
    if len(session_excerpt) > 1900:
        chunks = [session_excerpt[i:i+1900] for i in range(0, min(len(session_excerpt), 5700), 1900)]
        for chunk in chunks:
            blocks.append(code_block(chunk))
    else:
        blocks.append(code_block(session_excerpt))

    blocks.append(divider())

    # Scribe rules reminder
    blocks.append(heading("Scribe Rules (applied at Chronicle time)", 2))
    blocks.append(bullet("Rule 1: Honest, humble, defensible — qualify all projections and estimates"))
    blocks.append(bullet("Rule 2: Keep receipts — every claim traces to a commit hash, Notion ID, or file path"))
    blocks.append(bullet("Standard: 'based on a true story, with receipts available on request'"))

    blocks.append(divider())

    # Placeholder sections for Claude to fill
    blocks.append(heading("Raw Story (fill in Chronicle session)", 2))
    blocks.append(para("← Claude Code fills this in during the Chronicle session"))

    blocks.append(heading("Format 1: LinkedIn Short (~200 words)", 2))
    blocks.append(para("← Dial 2 output"))

    blocks.append(heading("Format 2: LinkedIn Long (~600 words)", 2))
    blocks.append(para("← Dial 3 output (default)"))

    blocks.append(heading("Format 3: Blog Post Outline", 2))
    blocks.append(para("← Dial 4 outline"))

    blocks.append(heading("Evidence", 2))
    blocks.append(para("Source commits and Notion IDs used to produce this entry:"))
    for c in candidates[:5]:
        blocks.append(bullet(f"{c['repo']} / {c['hash']} — {c['message']}"))

    return blocks


# ── Notion API call ───────────────────────────────────────────────────────────

def create_notion_stub(entry_num: int, week_of: str, blocks: list[dict]) -> str | None:
    """Create the Notion page stub. Returns page ID or None on failure."""
    api_key = os.environ.get("NOTION_API_KEY", "")
    if not api_key:
        print("ERROR: NOTION_API_KEY not set", file=sys.stderr)
        return None

    import urllib.request
    import urllib.error

    title = f"Agency Log #{entry_num:03d} — (Week of {week_of}) — RAW DATA"

    payload = {
        "parent": {"type": "page_id", "page_id": AGENCY_LOG_PARENT_ID},
        "properties": {
            "title": {"title": [{"text": {"content": title}}]}
        },
        "children": blocks[:99],  # Notion max 100 children per request
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.notion.com/v1/pages",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
            return result.get("id", "")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"ERROR creating Notion page: {e.code} — {body[:300]}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return None


# ── Logging ───────────────────────────────────────────────────────────────────

def log(msg: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"- {ts} EST — chronicle-weekly: {msg}\n"
    try:
        with open(SYNC_LOG, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass
    print(msg)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    week_of = datetime.now().strftime("%Y-%m-%d")
    print(f"[Story Dial] Chronicle Weekly — Layer 1 — {week_of}")

    # Collect commits
    commits = collect_all_commits(DAYS_BACK)
    print(f"  Found {len(commits)} story-worthy commits across all repos")

    # Identify candidates
    candidates = identify_story_candidates(commits)
    print(f"  Identified {len(candidates)} story candidate(s)")

    # Read SESSION-STATE
    session_excerpt = read_recent_session_state_entries()

    # Get next entry number
    entry_num = get_next_entry_number()
    print(f"  Next entry: #{entry_num:03d}")

    # Build blocks
    blocks = build_notion_page_blocks(entry_num, commits, candidates, session_excerpt, week_of)

    # Create Notion stub
    page_id = create_notion_stub(entry_num, week_of, blocks)
    if page_id:
        notion_url = f"https://www.notion.so/{page_id.replace('-', '')}"
        log(f"Agency Log #{entry_num:03d} stub created — Raw Data Ready — {notion_url}")
        print(f"\n  Notion stub created: {notion_url}")
        print(f"  Status: Raw Data Ready")
        print(f"  Next: In a Claude Code session, type: 'Chronicle this week\\'s entry at dial 3'")
    else:
        log(f"Agency Log #{entry_num:03d} stub FAILED — check NOTION_API_KEY and parent page ID")
        print("\n  ERROR: Failed to create Notion stub. Check NOTION_API_KEY.")
        sys.exit(1)


if __name__ == "__main__":
    main()
