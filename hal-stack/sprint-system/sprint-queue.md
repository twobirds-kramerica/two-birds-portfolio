<!--
STATUS: LIVE — THIS IS THE ACTIVE SPRINT QUEUE
Created: 2026-04-11 16:15 EST (Toronto)
Updated: 2026-04-11 16:15 EST (Toronto)
-->

# Sprint Queue

Sorted by priority. Top non-blocked sprint runs next.

**Status key:** READY = run anytime | BLOCKED = waiting on something | DONE = completed

---

## S-001: Voice Layer — Keyword Command Map (L4)

**Priority:** P1
**Duration:** 45 min
**Status:** READY
**Blocked by:** —
**Layer:** L4-native
**Story refs:** S3.3

### Prompt

```
AUTONOMOUS SPRINT — VOICE KEYWORD COMMAND MAP
Repo: C:\twobirds\two-birds-portfolio\
Read SESSION-STATE.md before starting. Commit after each phase.

PHASE 1 — BUILD KEYWORD MAP (30 min)

Create hal-stack/voice-layer/src/command-map.json

Map Aaron's trigger commands to structured intents:
{
  "next sprint": { "action": "sprint", "target": "next" },
  "retro": { "action": "retro" },
  "state": { "action": "state" },
  "dashboard": { "action": "dashboard" },
  "hal": { "action": "hal" },
  "journey": { "action": "journey" },
  "stop": { "action": "stop" },
  "status": { "action": "status" },
  "commit": { "action": "commit" },
  "push": { "action": "push" }
}

Create hal-stack/voice-layer/src/command-matcher.js
- Takes a text string, fuzzy-matches against command-map.json
- Returns the matched intent or null
- Handles partial matches ("run next sprint" contains "next sprint")
- Pure JavaScript, no dependencies, works at L4

Test with 10 sample inputs, log results to console.

PHASE 2 — WIRE TO EXISTING CLAUDE.MD TRIGGERS (15 min)

Document in hal-stack/voice-layer/src/README.md how the keyword
matcher connects to the CLAUDE.md trigger commands. The matcher
outputs an action; the action maps to reading a specific file or
running a specific command.

Commit per phase. Update SESSION-STATE.md, auto-generate context
export, push to master.
```

### Expected Outputs
- `hal-stack/voice-layer/src/command-map.json`
- `hal-stack/voice-layer/src/command-matcher.js`
- `hal-stack/voice-layer/src/README.md`

---

## S-002: DCC Logo Finalization (after Aaron picks)

**Priority:** P2
**Duration:** 30 min
**Status:** BLOCKED
**Blocked by:** Aaron selects DCC logo variation (S5.4)
**Layer:** L1
**Story refs:** S5.5, S5.6

### Prompt

```
AUTONOMOUS SPRINT — DCC LOGO FINALIZATION
Repo: C:\twobirds\two-birds-portfolio\ and C:\twobirds\digital-confidence\
Read SESSION-STATE.md before starting. Commit after each phase.

Aaron has selected DCC logo variation V[XX]. Finalize it.

PHASE 1 — GENERATE ALL DCC LOGO FORMATS (15 min)

From the selected variation SVG, generate:
- dcc-logo.svg (canonical)
- dcc-1024.png, dcc-512.png, dcc-256.png, dcc-128.png, dcc-64.png
- dcc-favicon.ico (16/32/48)
- dcc-og.png (1200x630, teal background)

Save to: assets/logos/dcc/

PHASE 2 — REPLACE DCC SITE FAVICON (15 min)

In the digital-confidence repo:
- Replace existing favicon with the new DCC favicon
- Update all HTML files with correct <link rel="icon"> tags
- Verify no broken references

Commit per phase per repo. Update SESSION-STATE.md, push both repos.
```

### Expected Outputs
- `assets/logos/dcc/dcc-logo.svg` + all format PNGs
- `digital-confidence/` favicon updated across all HTML files

---

## S-003: DCC Content Freshness Rules + Script

**Priority:** P2
**Duration:** 1 hour
**Status:** READY
**Blocked by:** —
**Layer:** L4-native
**Story refs:** S6.1, S6.2

### Prompt

```
AUTONOMOUS SPRINT — CONTENT FRESHNESS SYSTEM
Repo: C:\twobirds\two-birds-portfolio\
Read SESSION-STATE.md before starting. Commit after each phase.

Content freshness has been a Day 1 HAL requirement (March 6) and
is still not built. This sprint delivers a working system.

PHASE 1 — DEFINE STALENESS RULES (20 min)

Create hal-stack/content-freshness/staleness-rules.md

For each content type, define when it's "stale":
- DCC modules: stale if lastmod > 90 days
- DCC resources page: stale if lastmod > 60 days
- Company sites (TBI, Aaron P): stale if lastmod > 180 days
- Backlog/session state: stale if > 14 days with no update
- LinkedIn content: stale if no post in > 7 days

PHASE 2 — BUILD FRESHNESS CHECK SCRIPT (30 min)

Create hal-stack/content-freshness/check-freshness.js

Node.js script (no npm dependencies) that:
1. Reads all HTML files in digital-confidence repo
2. Extracts lastmod from meta tags or sitemap
3. Compares against staleness rules
4. Outputs a report: fresh / warning / stale per file
5. Prints summary: X fresh, Y warning, Z stale

PHASE 3 — REPORT TEMPLATE (10 min)

Create hal-stack/content-freshness/README.md
- How to run the script
- How to read the report
- How to update staleness rules

Commit per phase. Update SESSION-STATE.md, push to master.
```

### Expected Outputs
- `hal-stack/content-freshness/staleness-rules.md`
- `hal-stack/content-freshness/check-freshness.js`
- `hal-stack/content-freshness/README.md`

---

## S-004: Context Export to CLAUDE.md Workflow

**Priority:** P2
**Duration:** 20 min
**Status:** READY
**Blocked by:** —
**Layer:** L1-L4
**Story refs:** S2.1

### Prompt

```
AUTONOMOUS SPRINT — ADD CONTEXT EXPORT TO CLAUDE.MD
Repo: C:\twobirds\two-birds-portfolio\
Read SESSION-STATE.md and hal-stack/context-system/claude-code-auto-export.md.

PHASE 1 — UPDATE CLAUDE.MD (10 min)

Add to the STANDING RULES section of CLAUDE.md:
- After updating SESSION-STATE.md at session end, also auto-generate
  a context export using the template in
  hal-stack/context-system/context-export-template.md
- Save as hal-stack/context-system/exports/[date]-[title].md
- Add one-line entry to context-index.md

Keep the addition minimal — 3-4 lines max. Don't restructure CLAUDE.md.

PHASE 2 — VERIFY (10 min)

Read the updated CLAUDE.md, verify the new rule doesn't conflict
with existing rules. Check that file paths are correct.

Commit. Update SESSION-STATE.md, push to master.
```

### Expected Outputs
- Updated `CLAUDE.md` with context export rule

---

## S-005: Test Aider as L2 Claude Code Fallback

**Priority:** P2
**Duration:** 1 hour
**Status:** READY
**Blocked by:** —
**Layer:** L2
**Story refs:** Decapitation audit action item

### Prompt

```
AUTONOMOUS SPRINT — AIDER L2 EVALUATION
Repo: C:\twobirds\two-birds-portfolio\
Read SESSION-STATE.md before starting. Commit after each phase.

PHASE 1 — INSTALL AIDER (15 min)

Install Aider on the current machine:
  pip install aider-chat (or pipx install aider-chat)
If pip not available, document the blocker and skip to Phase 3.

PHASE 2 — TEST WITH SMALL EDIT (30 min)

Use Aider to make one small, safe edit to a non-critical file:
- Target: hal-stack/architecture/decapitation-checklist.md
- Task: Update the Claude Code entry with the Aider test results
- Use whatever LLM backend is available (BYOK or free tier)

Document: did it work? Quality vs Claude Code? Setup friction?

PHASE 3 — DOCUMENT RESULTS (15 min)

Create hal-stack/architecture/aider-evaluation.md
- Installation steps (what worked, what didn't)
- Test results (quality, speed, usability)
- Recommendation: viable L2 fallback? (yes/no/maybe)
- Update decapitation-checklist.md Claude Code entry

Commit. Update SESSION-STATE.md, push to master.
```

### Expected Outputs
- Aider installed (or blocker documented)
- `hal-stack/architecture/aider-evaluation.md`
- Updated decapitation checklist

---

## S-006: Local Git Backup Setup on Pentium Silver

**Priority:** P2
**Duration:** 30 min
**Status:** BLOCKED
**Blocked by:** Physical access to Pentium Silver
**Layer:** L4
**Story refs:** E11

### Prompt

```
AUTONOMOUS SPRINT — LOCAL GIT BACKUP SETUP
Machine: Pentium Silver
Read hal-stack/architecture/local-backup.md for the full plan.

PHASE 1 — CLONE ALL REPOS (15 min)

Run the clone commands from local-backup.md for all 10 repos.
If any fail, document which ones and why.

PHASE 2 — INSTALL SYNC SCRIPT (10 min)

Copy sync-from-github.bat to C:\twobirds\
Set up Windows Task Scheduler to run every 4 hours.
Test one manual run.

PHASE 3 — VERIFY (5 min)

Check sync-log.txt. Confirm all repos pulled successfully.
Commit verification results to two-birds-portfolio.
Push from EZbook (not from Pentium — it's pull-only).
```

### Expected Outputs
- All repos cloned on Pentium Silver
- Sync script scheduled every 4 hours
- Verification in sync-log.txt

---

## S-007: CIPO Trademark Research

**Priority:** P3
**Duration:** 30 min
**Status:** READY
**Blocked by:** —
**Layer:** L1
**Story refs:** S5.8

### Prompt

```
AUTONOMOUS SPRINT — CIPO TRADEMARK RESEARCH
Repo: C:\twobirds\two-birds-portfolio\
Read SESSION-STATE.md before starting.

PHASE 1 — RESEARCH (20 min)

Search the Canadian Intellectual Property Office (CIPO) database
for existing "Two Birds" trademarks in relevant categories.

Document in hal-stack/branding/cipo-trademark-research.md:
- Search results (any existing "Two Birds" marks in Canada)
- Registration process steps
- Cost breakdown (filing fees, agent fees if applicable)
- Timeline (how long registration takes)
- DIY vs. hiring a trademark agent
- Risk assessment: is the name registrable?

PHASE 2 — RECOMMENDATION (10 min)

Add a recommendation section:
- Should Aaron register now, later, or not at all?
- What category/class to file under?
- Priority relative to other business needs

Commit. Update SESSION-STATE.md, push to master.
```

### Expected Outputs
- `hal-stack/branding/cipo-trademark-research.md`

---

## S-008: DCC Site CSS Update to Brand Guidelines

**Priority:** P3
**Duration:** 1 hour
**Status:** BLOCKED
**Blocked by:** S-002 (DCC logo must be finalized first)
**Layer:** L1
**Story refs:** S5.7

### Prompt

```
AUTONOMOUS SPRINT — DCC CSS BRAND ALIGNMENT
Repo: C:\twobirds\digital-confidence\
Read hal-stack/branding/dcc-brand-guidelines.md before starting.

PHASE 1 — AUDIT CURRENT CSS (20 min)

Compare css/main.css against DCC brand guidelines:
- Are colours matching? Flag deviations.
- Is font sizing senior-friendly (18px body min)?
- Are tap targets 44px+?
- Is contrast WCAG AA?

PHASE 2 — UPDATE CSS (30 min)

Fix any deviations found. Don't redesign — just align to spec.

PHASE 3 — VERIFY (10 min)

Run axe-core via ?qa=true on index.html. Report results.

Commit per phase. Push to main.
```

### Expected Outputs
- Updated `css/main.css` aligned to brand guidelines
- axe-core QA results

---

## BLOCKED SPRINTS (waiting on Aaron)

These sprints have ready prompts but can't run until Aaron does something.

| Sprint | Blocked By | Aaron Action | Time |
|--------|-----------|-------------|------|
| S-002 | Aaron picks DCC logo | Review 8 variations, tell Claude Code which one | 5 min |
| S-006 | Physical access to Pentium Silver | Be at the Pentium Silver machine | — |

## DONE

_(Completed sprints moved here with date)_
