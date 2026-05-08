# Loop: Notion Sync Verify
**Pattern:** Boris Cherny — server-side monitoring ("which is the same thing but kind of on the server")
**Interval:** Daily (best run at 6 AM via Task Scheduler before Aaron's first session)
**Purpose:** Ensure Notion sync is healthy so `next sprint` always works reliably

---

## Prompt (paste at session start)

```
NOTION SYNC VERIFY LOOP — Two Birds Innovation
Read SESSION-STATE.md before starting.

PHASE 1 — CHECK SYNC LOG

Read hal-stack/notion-sync/SYNC-LOG.md
Find the most recent successful sync timestamp.

If last sync > 48 hours ago:
  → Flag as STALE in report
  → Attempt re-sync: python hal-stack/notion-sync/next-sprint.py
  → Log result (exit code 0 = sprint found, exit code 3 = queue empty, exit code 1 = error)

If last sync is recent (< 48 hours):
  → Log as HEALTHY

PHASE 2 — TEST NOTION MCP CONNECTIVITY

Run a lightweight Notion read: fetch the Product Backlog database
  data source: dee08637-7122-46cd-bc29-7775ce3ab8f6

If fetch fails:
  → Log "Notion MCP unreachable at [TIME]"
  → Check logs/mcp-write-log.txt for recent errors
  → Do NOT attempt writes — read failure likely means write failure too

If fetch succeeds:
  → Log "Notion MCP healthy at [TIME]"

PHASE 3 — VERIFY NOTION_API_KEY ENV VAR

python -c "import os; print('SET' if os.environ.get('NOTION_API_KEY') else 'MISSING')"

If MISSING: log warning. next-sprint.py will fail until key is set.

PHASE 4 — REPORT

Append one line to hal-stack/notion-sync/SYNC-LOG.md:
[DATE TIME] VERIFY-LOOP: sync=[HEALTHY/STALE], mcp=[HEALTHY/UNREACHABLE], key=[SET/MISSING]

If any check FAILED, also append to SESSION-STATE.md:
---
## Notion Sync Alert — [DATE]
- Sync log status: [result]
- MCP connectivity: [result]
- API key: [result]
- Action taken: [none / re-sync attempted / manual intervention needed]
---

Commit only if SYNC-LOG.md was updated.
chore(loop): notion-sync-verify [DATE]
Push to master.
```

---

## Notes
- This loop is the canary. If it fails, all other loops that depend on Notion will also fail.
- Ideal to add to run-overnight-build.bat so it runs at 2 AM alongside the main overnight job.
- Failure here should wake Aaron with a SESSION-STATE entry before his first morning sprint.
