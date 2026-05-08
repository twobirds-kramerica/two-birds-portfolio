# Loop: Notion Backlog Health Check
**Pattern:** Boris Cherny — recurring monitoring job that clusters signals on an interval
**Interval:** Weekly (Sunday evening recommended)
**Source:** Notion Product Backlog `dee08637-7122-46cd-bc29-7775ce3ab8f6`

---

## Prompt (paste at session start)

```
BACKLOG HEALTH LOOP — Two Birds Innovation
Read SESSION-STATE.md before starting.
Run: python hal-stack/notion-sync/next-sprint.py — note exit code.

PHASE 1 — PULL BACKLOG SNAPSHOT

Use Notion MCP (notion-search or notion-fetch) to read the Product Backlog
data source: dee08637-7122-46cd-bc29-7775ce3ab8f6

Build a working list of all items where Status != Done.

PHASE 2 — HEALTH CHECKS

Flag items that match any of these conditions:

[STALE-P1] Priority=P1, Status=Backlog, created >7 days ago with no movement
  → These are rotting. Surface to Aaron as "P1 items going cold."

[STALE-READY] Status=Ready for >14 days with no sprint started
  → Either the sprint got done without Notion being updated, or it's genuinely stuck.

[ORPHANED] Status=In Progress with no recent SESSION-STATE entry mentioning the sprint ID
  → Probably stale In Progress. Needs cleanup.

[P0-EXISTS] Any item at P0 that is not In Progress
  → P0 should never sit idle. Flag immediately.

PHASE 3 — REPORT

Append to SESSION-STATE.md:
---
## Backlog Health — [DATE]
- Total open items: N
- [STALE-P1] items: list sprint IDs
- [STALE-READY] items: list sprint IDs
- [ORPHANED] items: list sprint IDs
- [P0-EXISTS] items: list sprint IDs
- Recommended next sprint: [ID] ([priority] — reason)
---

Do NOT move any items in Notion without Aaron's confirmation.
Only report. Aaron decides what to act on.

Commit: chore(loop): backlog-health run [DATE]
Push to master.
```

---

## Notes
- This loop is read-only in Notion. Never write to the backlog from this loop.
- If Notion MCP returns errors, fall back to reading hal-stack/sprint-system/sprint-queue.md.
- Ideal to run Sunday evening so Aaron starts Monday with a clear backlog picture.
