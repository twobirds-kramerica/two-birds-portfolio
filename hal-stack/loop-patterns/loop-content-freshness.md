# Loop: Content Freshness Alert
**Pattern:** Boris Cherny — "clusters it for me every 30 minutes" (adapted to weekly for content)
**Interval:** Weekly (Monday morning recommended — flags stale content for the week)
**Repos:** digital-confidence (DCC), two-birds-innovation, clarity, aaron-patzalek

---

## Prompt (paste at session start)

```
CONTENT FRESHNESS LOOP — Two Birds Innovation
Read SESSION-STATE.md before starting.

PHASE 1 — RUN DCC FRESHNESS SCRIPT

cd C:\twobirds\digital-confidence
node C:\twobirds\two-birds-portfolio\hal-stack\content-freshness\check-freshness.js

Capture output. Note: X fresh, Y warning, Z stale.

PHASE 2 — BRAND SITE CHECK

For two-birds-innovation/index.html and aaron-patzalek/index.html:
  - Check git log --follow -1 -- [file] for last modification date
  - Flag if last commit to the file is >180 days ago (per staleness-rules.md)

For clarity/index.html:
  - Same check, threshold 180 days

PHASE 3 — SESSION-STATE CHECK

Read SESSION-STATE.md last-updated date.
Flag if >14 days since last sprint entry.

PHASE 4 — REPORT

Append to SESSION-STATE.md:
---
## Content Freshness — [DATE]
### DCC
- Fresh: N modules
- Warning (60-90 days): list modules
- Stale (>90 days): list modules — ACTION NEEDED

### Brand Sites
- two-birds-innovation: last updated [DATE] — [OK / STALE]
- aaron-patzalek: last updated [DATE] — [OK / STALE]
- clarity: last updated [DATE] — [OK / STALE]

### SESSION-STATE
- Last sprint: [DATE] — [OK / STALE]
---

If any DCC module is STALE, create a Notion backlog item:
  Item: "S-FRESHNESS-[MODULE] — update [module name] content"
  Priority: P2, Status: Backlog, Product: DCC, Type: Sprint
  Notes: "Content freshness loop flagged [module] as stale on [DATE]. Last updated [DATE]."

Commit: chore(loop): content-freshness run [DATE]
Push to master.
```

---

## Notes
- Staleness thresholds are in hal-stack/content-freshness/staleness-rules.md
- Only create Notion items for STALE (not Warning). Warning = monitor next week.
- Do NOT update content in this loop. Flag only. Content updates are separate sprints.
