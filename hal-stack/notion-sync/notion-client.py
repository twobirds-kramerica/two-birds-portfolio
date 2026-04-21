"""Notion API wrapper for HAL Stack sync layer.

Reads NOTION_API_KEY from the environment. Config lives in config.json next
to this file. All API calls have try/except; callers are expected to catch
NotionError and fall back to local files.

Usage:
    python notion-client.py --test
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print(
        "ERROR: the 'requests' library is not installed. Run: pip install requests",
        file=sys.stderr,
    )
    sys.exit(2)


HERE = Path(__file__).resolve().parent
CONFIG_PATH = HERE / "config.json"
SYNC_LOG_PATH = HERE / "SYNC-LOG.md"


class NotionError(Exception):
    """Raised when a Notion API call fails (network, auth, or non-2xx)."""


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_api_key() -> str:
    key = os.environ.get("NOTION_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "NOTION_API_KEY environment variable is not set. "
            "See hal-stack/notion-sync/SETUP.md."
        )
    return key


def log_sync_event(message: str) -> None:
    """Append a timestamped line to SYNC-LOG.md. Best-effort, never raises."""
    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")
    line = f"- {ts} — {message}\n"
    try:
        if not SYNC_LOG_PATH.exists():
            SYNC_LOG_PATH.write_text(
                "# Notion Sync Log\n\n"
                "Append-only record of sync events, errors, and completions.\n\n",
                encoding="utf-8",
            )
        with SYNC_LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass


class NotionClient:
    def __init__(self, api_key: str | None = None, config: dict | None = None):
        self.config = config or load_config()
        self.api_key = api_key or get_api_key()
        self.base_url = self.config.get("base_url", "https://api.notion.com/v1/")
        self.notion_version = self.config.get("notion_version", "2025-09-03")
        self.timeout = self.config.get("request_timeout_seconds", 15)

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
        }

    def _request(self, method: str, path: str, body: dict | None = None) -> dict:
        url = urljoin(self.base_url, path.lstrip("/"))
        try:
            resp = requests.request(
                method, url,
                headers=self._headers(),
                json=body,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            log_sync_event(f"API network error on {method} {path}: {e}")
            raise NotionError(f"Network error: {e}") from e
        if resp.status_code >= 400:
            snippet = resp.text[:300].replace("\n", " ")
            log_sync_event(f"API {resp.status_code} on {method} {path}: {snippet}")
            raise NotionError(f"{resp.status_code}: {snippet}")
        return resp.json()

    def query_data_source(
        self,
        data_source_id: str,
        filter_: dict | None = None,
        sorts: list | None = None,
    ) -> list[dict]:
        """Query a data source, handling pagination. Returns the list of pages."""
        body: dict[str, Any] = {}
        if filter_:
            body["filter"] = filter_
        if sorts:
            body["sorts"] = sorts
        path = f"data_sources/{data_source_id}/query"
        out: list[dict] = []
        while True:
            resp = self._request("POST", path, body)
            out.extend(resp.get("results", []))
            if not resp.get("has_more"):
                break
            body["start_cursor"] = resp.get("next_cursor")
        return out

    def get_page(self, page_id: str) -> dict:
        return self._request("GET", f"pages/{page_id}")

    def update_page_properties(self, page_id: str, properties: dict) -> dict:
        return self._request("PATCH", f"pages/{page_id}", {"properties": properties})

    def set_select(self, page_id: str, property_name: str, option_name: str) -> dict:
        return self.update_page_properties(
            page_id, {property_name: {"select": {"name": option_name}}}
        )

    def append_to_rich_text(
        self, page_id: str, property_name: str, text: str
    ) -> dict:
        """Fetch current rich_text, append `text` as a new block, PATCH back."""
        page = self.get_page(page_id)
        current = page.get("properties", {}).get(property_name, {})
        existing = current.get("rich_text", []) or []
        blocks = list(existing)
        prefix = "\n" if existing else ""
        blocks.append({"type": "text", "text": {"content": prefix + text}})
        return self.update_page_properties(
            page_id, {property_name: {"rich_text": blocks}}
        )

    def create_page(
        self,
        data_source_id: str,
        properties: dict,
        children: list | None = None,
    ) -> dict:
        """Create a new page (row) in a data source.

        Args:
            data_source_id: the Notion data source UUID.
            properties: dict of property name -> Notion property value shape.
                Example for the Product Backlog:
                    {
                        "Item":     {"title":     [{"text": {"content": "My sprint"}}]},
                        "Status":   {"select":    {"name": "Ready"}},
                        "Priority": {"select":    {"name": "P2"}},
                        "Owner":    {"select":    {"name": "Claude Code"}},
                        "Type":     {"select":    {"name": "Sprint"}},
                        "Notes":    {"rich_text": [{"text": {"content": "..."}}]},
                    }
            children: optional list of Notion block objects for the page body.

        Returns the created page object (including `id` and `url`).

        Raises NotionError on network or API failures.
        """
        body: dict[str, Any] = {
            "parent": {
                "type": "data_source_id",
                "data_source_id": data_source_id,
            },
            "properties": properties,
        }
        if children:
            body["children"] = children
        return self._request("POST", "pages", body)

    def build_page_body(
        self,
        data_source_id: str,
        properties: dict,
        children: list | None = None,
    ) -> dict:
        """Return the exact request body `create_page` would POST.

        Useful for dry-run / offline verification: callers can inspect the
        body before sending, log it into SYNC-LOG, or validate against a
        fixture. Never hits the network.
        """
        body: dict[str, Any] = {
            "parent": {
                "type": "data_source_id",
                "data_source_id": data_source_id,
            },
            "properties": properties,
        }
        if children:
            body["children"] = children
        return body


# --- Property extractors for Product Backlog rows --------------------------

def extract_title(page: dict, title_property: str = "Item") -> str:
    prop = page.get("properties", {}).get(title_property, {})
    parts = prop.get("title", [])
    return "".join(p.get("plain_text", "") for p in parts).strip()


def extract_select(page: dict, property_name: str) -> str | None:
    prop = page.get("properties", {}).get(property_name, {})
    sel = prop.get("select") or {}
    return sel.get("name")


def extract_rich_text(page: dict, property_name: str = "Notes") -> str:
    prop = page.get("properties", {}).get(property_name, {})
    parts = prop.get("rich_text", [])
    return "".join(p.get("plain_text", "") for p in parts).strip()


def normalize_page(page: dict) -> dict:
    return {
        "id": page.get("id", ""),
        "url": page.get("url", ""),
        "item": extract_title(page, "Item"),
        "status": extract_select(page, "Status"),
        "priority": extract_select(page, "Priority"),
        "product": extract_select(page, "Product"),
        "type": extract_select(page, "Type"),
        "owner": extract_select(page, "Owner"),
        "notes": extract_rich_text(page, "Notes"),
    }


# --- High-level: list Claude Code sprints ----------------------------------

def list_claude_code_sprints(
    client: NotionClient, exclude_done: bool = True
) -> list[dict]:
    """Return Product Backlog items where Type=Sprint and Owner=Claude Code."""
    cfg = client.config
    clauses = [
        {"property": "Type", "select": {"equals": cfg["filter_defaults"]["type_sprint"]}},
        {"property": "Owner", "select": {"equals": cfg["filter_defaults"]["owner_claude_code"]}},
    ]
    if exclude_done:
        clauses.append({"property": "Status", "select": {"does_not_equal": "Done"}})
    filter_ = {"and": clauses}
    pages = client.query_data_source(
        cfg["product_backlog_data_source"], filter_=filter_
    )
    return [normalize_page(p) for p in pages]


# --- High-level: create a Product Backlog row ------------------------------

def build_backlog_properties(
    item: str,
    priority: str = "P3",
    status: str = "Backlog",
    owner: str = "Claude Code",
    type_: str = "Sprint",
    product: str | None = None,
    notes: str | None = None,
) -> dict:
    """Construct a Notion `properties` dict for a Product Backlog row.

    Saves callers from having to remember the exact title/select/rich_text
    shape for each property. Unknown/empty values are omitted so the row
    uses the database's default for that property.
    """
    properties: dict[str, Any] = {
        "Item": {"title": [{"text": {"content": item}}]},
        "Status": {"select": {"name": status}},
        "Priority": {"select": {"name": priority}},
        "Owner": {"select": {"name": owner}},
        "Type": {"select": {"name": type_}},
    }
    if product:
        properties["Product"] = {"select": {"name": product}}
    if notes:
        properties["Notes"] = {"rich_text": [{"text": {"content": notes}}]}
    return properties


def create_backlog_item(
    client: NotionClient,
    item: str,
    priority: str = "P3",
    status: str = "Backlog",
    owner: str = "Claude Code",
    type_: str = "Sprint",
    product: str | None = None,
    notes: str | None = None,
) -> dict:
    """Create a new row in the Product Backlog data source.

    Returns the created page object. Logs success to SYNC-LOG.md.
    """
    cfg = client.config
    data_source_id = cfg["product_backlog_data_source"]
    properties = build_backlog_properties(
        item=item, priority=priority, status=status, owner=owner,
        type_=type_, product=product, notes=notes,
    )
    page = client.create_page(data_source_id, properties)
    log_sync_event(
        f"create_backlog_item: '{item}' "
        f"({priority} {type_} / {status} / {owner}) -> {page.get('id', '?')}"
    )
    return page


# --- High-level: create a DCC Kids Research Database row --------------------
# Schema captured 2026-04-21 from the live data source
# `kids_research_data_source` (e184382b-b59a-41e7-9152-d90fbee1abe6).
# 22 columns. Rich-text fields accept a single prose block; callers pass
# plain strings and the helper wraps them into Notion's rich_text shape.

RESEARCH_CATEGORIES   = {"Tech-Safety", "Learning", "Emotional-Safety",
                         "Critical-Thinking", "Creative-Making"}
RESEARCH_AGE_RANGES   = {"4-6", "7-9", "10-12", "13-15", "Flexible-Range"}
RESEARCH_PRIORITIES   = {"P0-Core", "P1-Important", "P2-Nice"}
RESEARCH_STATUSES     = {"Research", "Spec", "Ready-to-Build", "Built"}
RESEARCH_DEMO_METHODS = {"Drawing", "Play-Acting", "Song-or-Music",
                         "Art-Creation", "Show-and-Tell", "Multi-Modal"}
RESEARCH_LEARNING     = {"Standard", "ADHD", "Dyslexia", "Special-Needs"}
RESEARCH_LANGUAGES    = {"en-CA", "fr-QC"}
RESEARCH_AR_SHOWCASES = {"None", "Toy-to-Life", "Cup-Animation",
                         "Stuffed-Animal-Action"}


_NOTION_RICH_TEXT_CHUNK = 1900  # Notion limit is 2000; leave headroom.


def _rich_text(content: str | None):
    """Wrap plain text into the Notion rich_text block array.

    Notion enforces a 2000-char limit per text.content; longer strings
    are split across multiple blocks on the nearest newline/space to
    avoid cutting words. Callers still pass plain strings — chunking
    happens here.
    """
    if content is None or content == "":
        return []
    if len(content) <= _NOTION_RICH_TEXT_CHUNK:
        return [{"text": {"content": content}}]

    blocks: list[dict] = []
    remaining = content
    while remaining:
        if len(remaining) <= _NOTION_RICH_TEXT_CHUNK:
            blocks.append({"text": {"content": remaining}})
            break
        # Prefer to split on a newline; fall back to a space; last resort
        # a hard cut at the chunk boundary.
        window = remaining[:_NOTION_RICH_TEXT_CHUNK]
        split_at = window.rfind("\n\n")
        if split_at < _NOTION_RICH_TEXT_CHUNK // 2:
            split_at = window.rfind("\n")
        if split_at < _NOTION_RICH_TEXT_CHUNK // 2:
            split_at = window.rfind(" ")
        if split_at < _NOTION_RICH_TEXT_CHUNK // 2:
            split_at = _NOTION_RICH_TEXT_CHUNK
        blocks.append({"text": {"content": remaining[:split_at]}})
        remaining = remaining[split_at:].lstrip("\n ")
    return blocks


def build_research_row_properties(
    *,
    skill: str,
    category: str,
    age_ranges: list[str],
    priority: str = "P1-Important",
    status: str = "Research",
    description: str = "",
    research_source: str = "",
    threat_addressed: str = "",
    psychology_framework: str = "",
    creator_luring_awareness: str = "",
    example_activity: str = "",
    demonstration_method: str = "Multi-Modal",
    gamification_element: str = "",
    learning_profile: list[str] | None = None,
    screen_time_guidance: str = "",
    parental_controls_component: str = "",
    media_quality_rubric: str = "",
    language_version: list[str] | None = None,
    en_ca_content: str = "",
    fr_qc_content: str = "",
    ar_showcase: str = "None",
    ar_description: str = "",
) -> dict:
    """Build the Notion `properties` dict for one row of the DCC Kids
    Research Database.

    Values are passed as plain strings / list[str]; the helper wraps them
    into the Notion rich_text / select / multi_select shape. Enums are
    validated against the captured schema; invalid values raise ValueError
    with the list of valid options.

    Mandatory kwargs: `skill`, `category`, `age_ranges`.
    """
    if category not in RESEARCH_CATEGORIES:
        raise ValueError(f"category must be one of {RESEARCH_CATEGORIES}")
    if not age_ranges or any(a not in RESEARCH_AGE_RANGES for a in age_ranges):
        raise ValueError(f"age_ranges must be subset of {RESEARCH_AGE_RANGES}")
    if priority not in RESEARCH_PRIORITIES:
        raise ValueError(f"priority must be one of {RESEARCH_PRIORITIES}")
    if status not in RESEARCH_STATUSES:
        raise ValueError(f"status must be one of {RESEARCH_STATUSES}")
    if demonstration_method not in RESEARCH_DEMO_METHODS:
        raise ValueError(
            f"demonstration_method must be one of {RESEARCH_DEMO_METHODS}"
        )
    if ar_showcase not in RESEARCH_AR_SHOWCASES:
        raise ValueError(f"ar_showcase must be one of {RESEARCH_AR_SHOWCASES}")

    lp = learning_profile or ["Standard"]
    if any(p not in RESEARCH_LEARNING for p in lp):
        raise ValueError(f"learning_profile entries must be subset of {RESEARCH_LEARNING}")

    lv = language_version or ["en-CA"]
    if any(l not in RESEARCH_LANGUAGES for l in lv):
        raise ValueError(f"language_version entries must be subset of {RESEARCH_LANGUAGES}")

    return {
        "Skill / Feature":              {"title":        [{"text": {"content": skill}}]},
        "Category":                     {"select":       {"name": category}},
        "Age-Ranges":                   {"multi_select": [{"name": a} for a in age_ranges]},
        "Priority":                     {"select":       {"name": priority}},
        "Status":                       {"select":       {"name": status}},
        "Description":                  {"rich_text":    _rich_text(description)},
        "Research-Source":              {"rich_text":    _rich_text(research_source)},
        "Threat-Addressed":             {"rich_text":    _rich_text(threat_addressed)},
        "Psychology-Framework":         {"rich_text":    _rich_text(psychology_framework)},
        "Creator-Luring-Awareness":     {"rich_text":    _rich_text(creator_luring_awareness)},
        "Example-Activity":             {"rich_text":    _rich_text(example_activity)},
        "Demonstration-Method":         {"select":       {"name": demonstration_method}},
        "Gamification-Element":         {"rich_text":    _rich_text(gamification_element)},
        "Learning-Profile":             {"multi_select": [{"name": p} for p in lp]},
        "Screen-Time-Guidance":         {"rich_text":    _rich_text(screen_time_guidance)},
        "Parental-Controls-Component":  {"rich_text":    _rich_text(parental_controls_component)},
        "Media-Quality-Rubric":         {"rich_text":    _rich_text(media_quality_rubric)},
        "Language-Version":             {"multi_select": [{"name": l} for l in lv]},
        "en-CA-Content":                {"rich_text":    _rich_text(en_ca_content)},
        "fr-QC-Content":                {"rich_text":    _rich_text(fr_qc_content)},
        "AR-Showcase":                  {"select":       {"name": ar_showcase}},
        "AR-Description":               {"rich_text":    _rich_text(ar_description)},
    }


def create_research_row(client: NotionClient, **kwargs) -> dict:
    """Create a row in the DCC Kids Research Database.

    Accepts the same keyword args as `build_research_row_properties`.
    Returns the created Notion page object. Logs to SYNC-LOG.md.
    """
    cfg = client.config
    ds_id = cfg.get("kids_research_data_source")
    if not ds_id:
        raise NotionError(
            "config.json is missing 'kids_research_data_source' — "
            "cannot create a research row."
        )
    properties = build_research_row_properties(**kwargs)
    page = client.create_page(ds_id, properties)
    log_sync_event(
        f"create_research_row: '{kwargs.get('skill', '?')}' "
        f"({kwargs.get('category','?')} / {kwargs.get('age_ranges','?')}) "
        f"-> {page.get('id', '?')}"
    )
    return page


# --- Self-test -------------------------------------------------------------

def _self_test() -> int:
    try:
        cfg = load_config()
    except Exception as e:
        print(f"FAIL: could not load config.json: {e}")
        return 2
    try:
        client = NotionClient(config=cfg)
    except RuntimeError as e:
        print(f"FAIL: {e}")
        return 2
    print(f"Config loaded. Notion-Version: {client.notion_version}")
    print(f"Product Backlog data source: {cfg['product_backlog_data_source']}")
    try:
        sprints = list_claude_code_sprints(client, exclude_done=True)
    except NotionError as e:
        print(f"FAIL: Notion API error: {e}")
        return 1
    print(f"OK: found {len(sprints)} open Claude Code sprint(s).")
    for s in sprints[:10]:
        pri = s["priority"] or "--"
        status = s["status"] or "--"
        print(f"  [{pri}] {status:12s} — {s['item']}")
    log_sync_event(f"self-test OK — {len(sprints)} open sprint(s)")
    return 0


def _dry_run_create() -> int:
    """Offline verification: print two sample create_page request bodies —
    one for a Product Backlog row, one for a DCC Kids Research Database row.
    Does NOT hit the API. Used to verify the create_page helpers wire up
    cleanly before any live call.
    """
    try:
        cfg = load_config()
    except Exception as e:
        print(f"FAIL: could not load config.json: {e}")
        return 2

    backlog_ds = cfg.get("product_backlog_data_source", "<missing>")
    research_ds = cfg.get("kids_research_data_source", "<missing>")

    backlog_props = build_backlog_properties(
        item="SMOKE: notion-client.py create_page dry-run",
        priority="P3",
        status="Backlog",
        owner="Claude Code",
        type_="Sprint",
        product="HAL Stack",
        notes="Generated by `notion-client.py --dry-run-create`. Not posted.",
    )

    research_props = build_research_row_properties(
        skill="SMOKE: dry-run sample skill row",
        category="Learning",
        age_ranges=["7-9", "10-12"],
        priority="P2-Nice",
        status="Research",
        description="Sample row emitted by --dry-run-create.",
        research_source="N/A — smoke test.",
        psychology_framework="N/A — smoke test.",
        demonstration_method="Show-and-Tell",
        learning_profile=["Standard", "ADHD"],
        language_version=["en-CA"],
        ar_showcase="None",
    )

    try:
        client = NotionClient(config=cfg)
        build = client.build_page_body
    except RuntimeError:
        # No API key: inline the body shape
        def build(ds, props):
            return {
                "parent": {"type": "data_source_id", "data_source_id": ds},
                "properties": props,
            }

    out = {
        "product_backlog_example": build(backlog_ds, backlog_props),
        "kids_research_example":   build(research_ds, research_props),
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sys.exit(_self_test())
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run-create":
        sys.exit(_dry_run_create())
    print(
        "Usage: python notion-client.py [--test | --dry-run-create]",
        file=sys.stderr,
    )
    sys.exit(64)
