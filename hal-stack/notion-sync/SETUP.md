# Notion Sync — First-Time Setup

One-time-per-machine setup to connect Claude Code to the Notion Command Center.

## Why this is needed
The sync scripts in this folder talk to Notion via the Notion API. The API needs an integration token. You generate the token once in Notion, store it as the `NOTION_API_KEY` environment variable on each machine, and share the Command Center page with the integration so it can read + update items.

---

## Step 1 — Create a Notion integration

1. Open https://www.notion.so/my-integrations in a browser, signed in as the same Notion account that owns the Command Center.
2. Click **New integration**.
3. Fill in:
   - **Name:** `Two Birds — Claude Code Sync`
   - **Associated workspace:** select the workspace that contains the Command Center.
   - **Type:** Internal integration.
4. On the **Capabilities** tab, enable:
   - Read content
   - Update content
   - Insert content
   (Leave "User information" disabled — not needed.)
5. Click **Submit**. You now land on the integration settings page.
6. Click **Show** next to the **Internal Integration Secret**. Copy the value that starts with `secret_` or `ntn_`. That is your `NOTION_API_KEY`. Keep the browser tab open for Step 3.

## Step 2 — Share the Command Center with the integration

The integration can only see pages that have been explicitly shared with it.

1. In Notion, open the Command Center page (`347a09cf-876a-81fb-9a5c-eca696fb585b`).
2. Click the `⋯` menu in the top right → **Connect to** (or **Add connections**).
3. Select **Two Birds — Claude Code Sync**.
4. Confirm.
5. Sharing propagates to all child pages and databases, so the Product Backlog and Job Pipeline data sources are reachable automatically.

## Step 3 — Set `NOTION_API_KEY` on each machine

Run all commands as the Aaron user (not Administrator — user env vars are per-user).

### Windows (PowerShell)
Persistent (survives reboots):
```powershell
[Environment]::SetEnvironmentVariable("NOTION_API_KEY", "paste-your-token-here", "User")
```
Then close and reopen the terminal for the new value to be visible.

Verify:
```powershell
echo $env:NOTION_API_KEY
```

### macOS / Linux (bash / zsh)
Persistent:
```bash
echo 'export NOTION_API_KEY="paste-your-token-here"' >> ~/.bashrc
source ~/.bashrc
```

Verify:
```bash
echo "$NOTION_API_KEY"
```

### Repeat on all three machines
- EZbook
- ThinkPad
- Pentium Silver

The same token works everywhere. No need to generate a separate token per machine.

## Step 4 — Install the one Python dependency

Once per machine:
```
pip install requests
```

Verify Python version is 3.10+:
```
python --version
```

## Step 5 — Test the connection

From the repo root:
```
python hal-stack/notion-sync/notion-client.py --test
```

Expected output:
```
Config loaded. Notion-Version: 2025-09-03
Product Backlog data source: dee08637-7122-46cd-bc29-7775ce3ab8f6
OK: found N open Claude Code sprint(s).
  [P1] Ready        — <sprint name>
  ...
```

If you see `FAIL: 401` → the token is wrong. Re-copy from the integration page.
If you see `FAIL: 404` → the Command Center is not shared with the integration. Redo Step 2.
If you see `FAIL: Network error` → check internet, then try again.

## Step 6 — Test the full flow (optional, recommended)

1. Pull the queue: `python hal-stack/notion-sync/sync-queue.py`
   - Writes `hal-stack/sprint-system/sprint-queue-from-notion.md`.
2. Lock the next sprint: `python hal-stack/notion-sync/next-sprint.py`
   - Picks the highest-priority Ready item and marks it In Progress in Notion.
   - In Notion, confirm the item moved to In Progress.
3. Mark it complete (test only — pick a throwaway item first): `python hal-stack/notion-sync/complete-sprint.py "<item name>" "test-commit-hash"`
   - In Notion, confirm the item is now Done and Notes has the timestamped entry.

## Key rotation
If the token leaks, rotate it:
1. Back to https://www.notion.so/my-integrations → select the integration → **Rotate secret**.
2. Update `NOTION_API_KEY` on every machine (Step 3).

## Security notes
- The token grants read/write to every page shared with the integration. Only share the Command Center and its children.
- `NOTION_API_KEY` is gitignored via the existing `.env` exclusion. Never put it in a file inside the repo.
- `.env.example` in the repo root lists the expected variable name, with a placeholder — never a real value.
