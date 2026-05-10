"""CoS Morning Briefing Generator.

Runs overnight (via run-overnight-build.bat) to pre-generate context
for the next day's `cos` check-in.

Delivers to THREE places:
  1. hal-stack/cos/morning-briefing.md  (Claude Code context file)
  2. Notion "Daily Briefing" page       (pin in browser, always fresh)
  3. Gmail inbox email                  (CEO treatment — needs GMAIL_APP_PASSWORD env var)

Gmail setup (one-time, 30 seconds):
  Google Account > Security > 2-Step Verification > App passwords
  > Generate for "Mail / Windows Computer"
  > Add to .env:  GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx

Usage: python hal-stack/cos/morning-briefing.py
"""
from __future__ import annotations

import importlib.util
import json
import os
import smtplib
import sys
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

HERE      = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
OUT_PATH  = HERE / "morning-briefing.md"
SS_PATH   = REPO_ROOT / "SESSION-STATE.md"

COMMANDS = [
    ("cos",        "Any morning",  "Full check-in: wins + calendar + email + priorities + energy"),
    ("cos-week",   "Monday",       "Weekly Priority Dashboard + overcommitment check"),
    ("cos-retro",  "Friday",       "Pattern review + weekly summary + Monday setup"),
    ("next sprint","Ready to build","Picks and locks next sprint from Notion backlog"),
    ("state",      "Feeling lost", "Top 3 next actions from SESSION-STATE"),
    ("just go",    "Quick build",  "One autonomous sprint, returns control after"),
]

# ── Load Notion client ────────────────────────────────────────────────────────

def load_notion():
    nc_path = REPO_ROOT / "hal-stack" / "notion-sync" / "notion-client.py"
    spec = importlib.util.spec_from_file_location("nc", nc_path)
    nc   = importlib.util.module_from_spec(spec); spec.loader.exec_module(nc)
    cfg    = nc.load_config()
    client = nc.NotionClient(config=cfg)
    return nc, cfg, client


# ── Fetch Notion P1 Aaron items ───────────────────────────────────────────────

def fetch_p1_items(nc, cfg, client) -> list[dict]:
    try:
        pages = client.query_data_source(
            cfg["product_backlog_data_source"],
            filter_={"and": [
                {"property": "Priority", "select": {"equals": "P1"}},
                {"property": "Owner",    "select": {"equals": "Aaron"}},
                {"property": "Status",   "select": {"does_not_equal": "Done"}},
            ]}
        )
        return [nc.normalize_page(p) for p in pages]
    except Exception as e:
        return [{"item": f"(Notion unavailable: {e})", "status": "?"}]


# ── Read SESSION-STATE tail ───────────────────────────────────────────────────

def read_ss_tail() -> str:
    if not SS_PATH.exists():
        return "(SESSION-STATE.md not found)"
    lines = SS_PATH.read_text(encoding="utf-8").splitlines()
    return "\n".join(lines[-50:]) if len(lines) > 50 else "\n".join(lines)


# ── Update Notion briefing page ───────────────────────────────────────────────

def update_notion_page(client, page_id: str, p1_items: list[dict], date_str: str, time_str: str) -> None:
    api_key = os.environ.get("NOTION_API_KEY", "").strip()
    if not api_key:
        print("SKIP  Notion page update — NOTION_API_KEY not set")
        return

    import urllib.request

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": client.notion_version,
        "Content-Type": "application/json",
    }

    def notion_request(method: str, path: str, body=None):
        url  = f"https://api.notion.com/v1/{path}"
        data = json.dumps(body).encode() if body else None
        req  = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.loads(r.read())
        except Exception as e:
            print(f"WARN  Notion API {method} {path}: {e}")
            return {}

    # Delete existing child blocks
    children_resp = notion_request("GET", f"blocks/{page_id}/children")
    for blk in children_resp.get("results", []):
        notion_request("DELETE", f"blocks/{blk['id']}")

    # Build new blocks
    def para(text):
        return {"object": "block", "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": text}}]}}

    def h2(text):
        return {"object": "block", "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": text}}]}}

    def bullet(text, bold=False):
        return {"object": "block", "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": text},
                    "annotations": {"bold": bold}}]}}

    def divider():
        return {"object": "block", "type": "divider", "divider": {}}

    blocks = [
        para(f"Generated {time_str}. Open Claude Code and type cos to add live calendar + email."),
        divider(),
        h2("Your Commands"),
    ]
    for cmd, when, what in COMMANDS:
        blocks.append(bullet(f"{cmd}   |   {when}   |   {what}"))

    blocks += [divider(), h2(f"P1 Open Actions ({len(p1_items)} items)")]
    for item in p1_items[:20]:  # cap at 20 for Notion block limits
        status = item.get("status") or "?"
        title  = item.get("item")   or "(untitled)"
        blocks.append(bullet(f"[{status}] {title}"))

    notion_request("PATCH", f"blocks/{page_id}/children", {"children": blocks})
    print(f"OK    Notion briefing page updated: https://www.notion.so/{page_id.replace('-','')}")


# ── Send Gmail email ──────────────────────────────────────────────────────────

def send_gmail(p1_items: list[dict], date_str: str, time_str: str, cfg: dict) -> None:
    app_password = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
    if not app_password:
        print("SKIP  Gmail email — GMAIL_APP_PASSWORD not set (see script header for setup)")
        return

    to_addr   = cfg.get("cos_email_to",   "getkramer@gmail.com")
    from_addr = cfg.get("cos_email_from", "getkramer@gmail.com")
    subject   = f"Good morning, Aaron. CoS Briefing — {date_str}"

    # Build HTML
    cmd_rows = "".join(
        f"<tr><td style='padding:8px 12px;font-family:monospace;background:#f0f4ff;border-radius:4px;'><strong>{c}</strong></td>"
        f"<td style='padding:8px 12px;color:#555'>{w}</td>"
        f"<td style='padding:8px 12px;color:#222'>{d}</td></tr>"
        for c, w, d in COMMANDS
    )
    p1_rows = "".join(
        f"<li style='margin:4px 0;color:#1a1a1a'>"
        f"<span style='background:#e5e7eb;border-radius:3px;padding:1px 6px;font-size:0.78em;margin-right:6px;'>{(i.get('status') or '?')}</span>"
        f"{i.get('item','(untitled)')}</li>"
        for i in p1_items[:25]
    )

    html = f"""
<html><body style="font-family:Georgia,serif;max-width:680px;margin:0 auto;padding:24px;color:#1a1a1a;line-height:1.7;">
<p style="color:#888;font-size:0.82em;margin-bottom:8px;">Two Birds Innovation · CoS Daily Briefing · {time_str}</p>
<h1 style="font-size:1.5rem;color:#0F1C35;border-bottom:3px solid #1D4ED8;padding-bottom:10px;margin-bottom:20px;">
Good morning, Aaron.</h1>

<h2 style="font-size:1rem;color:#374151;text-transform:uppercase;letter-spacing:0.05em;">Your Commands</h2>
<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:0.88rem;">
<thead><tr style="background:#0F1C35;color:white;">
<th style="padding:8px 12px;text-align:left;">Type this</th>
<th style="padding:8px 12px;text-align:left;">When</th>
<th style="padding:8px 12px;text-align:left;">What it does</th>
</tr></thead>
<tbody>{cmd_rows}</tbody>
</table>

<h2 style="font-size:1rem;color:#374151;text-transform:uppercase;letter-spacing:0.05em;">
P1 Open Actions — {len(p1_items)} items waiting for you</h2>
<ul style="padding-left:0;list-style:none;margin-bottom:24px;">{p1_rows}</ul>

<hr style="border:none;border-top:1px solid #e5e7eb;margin:24px 0;">
<p style="color:#888;font-size:0.8em;">
Open Claude Code and type <strong>cos</strong> to add live calendar + email to this context.<br>
<a href="https://www.notion.so/{cfg.get('cos_briefing_page','').replace('-','')}" style="color:#1D4ED8;">
Open Notion Daily Briefing page</a>
</p>
</body></html>"""

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = from_addr
    msg["To"]      = to_addr
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=20) as srv:
            srv.login(from_addr, app_password)
            srv.sendmail(from_addr, to_addr, msg.as_string())
        print(f"OK    Gmail briefing sent to {to_addr}")
    except Exception as e:
        print(f"WARN  Gmail send failed: {e}")


# ── Write local MD file ───────────────────────────────────────────────────────

def write_md(p1_items: list[dict], ss_tail: str, date_str: str, time_str: str) -> None:
    cmd_table = "\n".join(
        f"| `{c}` | {w} | {d} |" for c, w, d in COMMANDS
    )
    p1_list = "\n".join(
        f"- **[{i.get('status','?')}]** {i.get('item','(untitled)')}" for i in p1_items
    )

    content = f"""# CoS Morning Briefing — {date_str}
_Generated overnight at {time_str}._

---

## Your Commands (always here so you never have to remember)

| Type this | When | What it does |
|---|---|---|
{cmd_table}

---

## P1 Open Actions (Owner: Aaron) — {len(p1_items)} items

{p1_list if p1_list else "- (none)"}

---

## Recent Sprint Context (from SESSION-STATE)

```
{ss_tail.strip()}
```

---

## CoS Stale-Item Flags

_Filled in by Claude when `cos` runs — checks for items not mentioned in 3+ days._

---

_Type `cos` to add live calendar + email and run the full check-in._
"""
    OUT_PATH.write_text(content, encoding="utf-8")
    print(f"OK    MD briefing written: {OUT_PATH}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    print("CoS morning briefing starting...")
    now      = datetime.now(timezone.utc).astimezone()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M %Z")

    try:
        nc, cfg, client = load_notion()
        print(f"    Fetching Notion P1 items (Owner=Aaron)...")
        p1_items = fetch_p1_items(nc, cfg, client)
        print(f"    Found {len(p1_items)} P1 item(s).")
    except Exception as e:
        print(f"WARN  Notion load failed ({e}) — continuing with empty P1 list.")
        p1_items = [{"item": f"Notion unavailable: {e}", "status": "?"}]
        cfg = {}
        client = None

    print("    Reading SESSION-STATE...")
    ss_tail = read_ss_tail()

    # 1. Local MD file
    write_md(p1_items, ss_tail, date_str, time_str)

    # 2. Notion briefing page
    briefing_page_id = cfg.get("cos_briefing_page") if cfg else None
    if client and briefing_page_id:
        print("    Updating Notion briefing page...")
        update_notion_page(client, briefing_page_id, p1_items, date_str, time_str)
    else:
        print("SKIP  Notion page update — no page ID or client.")

    # 3. Gmail email
    print("    Sending Gmail briefing email...")
    send_gmail(p1_items, date_str, time_str, cfg or {})

    print("CoS morning briefing complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
