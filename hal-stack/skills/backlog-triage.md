# Skill: /backlog-triage
**Domain:** HAL Stack / Notion
**Layer Compatibility:** L1-L4
**Loop command:** `/loop 60m /backlog-triage` or Task Scheduler weekly
**Source:** Boris Cherny cluster/feedback pattern adapted for Notion backlog

## What It Does
Reads the Notion Product Backlog, applies four health rules, and reports findings
to SESSION-STATE.md. Read-only in Notion — never moves or changes items.

## Instructions

1. **Pull backlog snapshot** via Notion MCP
   - Data source: `dee08637-7122-46cd-bc29-7775ce3ab8f6`
   - Fetch all items where Status != Done

2. **Apply health rules**

   **[STALE-P1]** Priority=P1, Status=Backlog, created >7 days ago
   → P1s should never sit idle. Surface immediately.

   **[STALE-READY]** Status=Ready, unchanged for >14 days
   → Either completed without Notion update, or genuinely stuck.

   **[ORPHANED]** Status=In Progress, no matching SESSION-STATE sprint entry in last 14 days
   → Probably stale In Progress. Needs cleanup.

   **[P0-NOT-RUNNING]** Any item at Priority=P0 and Status != In Progress
   → P0 should never sit idle. Flag immediately.

3. **Recommend next sprint**
   From the Ready items, recommend the highest-priority Ready item that is not blocked.
   One recommendation only.

4. **Report** (append to SESSION-STATE.md)
   ```
   ## /backlog-triage — [DATE]
   - [STALE-P1]: [none / list sprint IDs]
   - [STALE-READY]: [none / list sprint IDs]
   - [ORPHANED]: [none / list sprint IDs]
   - [P0-NOT-RUNNING]: [none / list sprint IDs]
   - Recommended next sprint: [ID] ([priority] — [one-line reason])
   ```

5. **Commit** if SESSION-STATE.md was updated
   ```
   git commit -m "chore(loop): backlog-triage run [DATE]"
   git push origin master
   ```

## Quality Checklist
- [ ] Notion MCP fetch succeeded (if failed: log error, skip Notion checks)
- [ ] No items moved or updated in Notion
- [ ] Recommendation is one item only, with justification
- [ ] SESSION-STATE.md updated

## Referenced By
- `loop-backlog-health.md` — schedule wrapper
- `.claude/loop.md` — runs as section 3 of the default maintenance loop (lightweight mode)
