# Skill: /freshness-check
**Domain:** Content / DCC
**Layer Compatibility:** L1-L3
**Loop command:** `/loop /freshness-check` (dynamic interval, or Task Scheduler weekly)
**Source:** hal-stack/content-freshness/check-freshness.js (already built)

## What It Does
Runs the DCC content freshness script and checks brand site lastmod dates.
Flags stale modules and auto-creates Notion backlog items for anything crossing the STALE threshold.

## Instructions

1. **Run DCC freshness script**
   ```
   cd C:\twobirds\digital-confidence
   node C:\twobirds\two-birds-portfolio\hal-stack\content-freshness\check-freshness.js
   ```
   Capture: X fresh, Y warning, Z stale.

2. **Brand site lastmod check**
   For each: `two-birds-innovation/index.html`, `aaron-patzalek/index.html`, `clarity/index.html`
   ```
   git log --follow -1 --format="%ci" -- [file]
   ```
   Flag if last commit >180 days ago (per `staleness-rules.md`).

3. **Classify results**
   - Fresh (< 60 days): log only
   - Warning (60-90 days): log, no action
   - Stale (> 90 days for DCC, > 180 days for brand sites): create Notion item

4. **For each STALE module**, create Notion backlog item:
   - Data source: `dee08637-7122-46cd-bc29-7775ce3ab8f6`
   - Item: `S-FRESHNESS-[MODULE] — update [module] content`
   - Priority: P2, Status: Backlog, Product: DCC or relevant product, Type: Sprint
   - Notes: "Content freshness loop flagged [module] as stale on [DATE]. Last updated [DATE]."

5. **Report** (append to SESSION-STATE.md)
   ```
   ## /freshness-check — [DATE]
   - DCC: N fresh, N warning, N stale
   - Brand sites: [OK / list stale]
   - Notion items created: N (list IDs)
   ```

6. **Commit** if SESSION-STATE.md was updated
   ```
   git commit -m "chore(loop): freshness-check run [DATE]"
   git push origin master
   ```

## Quality Checklist
- [ ] Script ran without errors (or error was logged)
- [ ] No Notion items created for Warning (only STALE)
- [ ] Brand site dates pulled from `git log`, not estimated
- [ ] SESSION-STATE.md updated

## Referenced By
- `loop-content-freshness.md` — schedule wrapper
- `hal-stack/content-freshness/staleness-rules.md` — threshold definitions
