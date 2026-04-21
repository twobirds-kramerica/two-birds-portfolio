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
    """Offline verification: construct the create_page request body for a
    sample Product Backlog row and print it as JSON. Does NOT hit the API.
    Used to verify the create_page / build_backlog_properties helpers wire
    up cleanly before any live call."""
    try:
        cfg = load_config()
    except Exception as e:
        print(f"FAIL: could not load config.json: {e}")
        return 2

    ds_id = cfg.get("product_backlog_data_source", "<missing>")
    properties = build_backlog_properties(
        item="SMOKE: notion-client.py create_page dry-run",
        priority="P3",
        status="Backlog",
        owner="Claude Code",
        type_="Sprint",
        product="HAL Stack",
        notes="Generated by `notion-client.py --dry-run-create`. Not posted.",
    )
    # Use build_page_body so we don't need NOTION_API_KEY for an offline check
    try:
        client = NotionClient(config=cfg)
    except RuntimeError:
        # No API key: build the body without instantiating a network client
        body = {
            "parent": {"type": "data_source_id", "data_source_id": ds_id},
            "properties": properties,
        }
    else:
        body = client.build_page_body(ds_id, properties)

    print(json.dumps(body, indent=2, ensure_ascii=False))
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
