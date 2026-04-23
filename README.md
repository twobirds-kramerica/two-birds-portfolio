# Two Birds Portfolio — Master Index

Infrastructure and operations repo for Two Birds Innovation. This is the hub: it holds the cross-cutting governance (CLAUDE.md, SESSION-STATE.md, RETRO.md), the HAL Stack autonomy layer, the sprint system, and the Notion sync helpers used by every other sibling repo in the portfolio.

It is **not** a product repo. Products live in their own repositories; this one coordinates the work across them.

## Orient in 60 seconds

If you're returning after time away (or picking this up cold), read these files in order:

1. **[CLAUDE.md](CLAUDE.md)** — auto-loaded by Claude Code on every session; the canonical index of standing rules, trigger commands, sibling repos, governance links, and workflow
2. **[SESSION-STATE.md](SESSION-STATE.md)** — per-sprint running log. Latest block at the top. Always ends with a TIMESTAMP RULE footer so you can tell how fresh it is
3. **[logs/RETRO.md](logs/RETRO.md)** — the most-recent session retrospective. Overwritten at session end; pair it with SESSION-STATE for a full picture
4. **[hal-stack/HAL-BACKLOG.md](hal-stack/HAL-BACKLOG.md)** — infrastructure backlog (HAL Stack sprint queue is separate from product sprints)

Four files, ~2 minutes. You will know: what Two Birds is, what shipped last, what's ready to ship, and what's blocked on human input.

## The Two Birds portfolio (sibling repos)

The canonical list with one-liner descriptions lives in `CLAUDE.md` under the **ALL REPOS** section. The portfolio is roughly:

- **Products:** Digital Confidence Centre (DCC), Career Coach, Clarity, Kevin's Apartment Search
- **Brand sites:** Aaron Patzalek (solopreneur portfolio), Two Birds Innovation (company)
- **Ops:** Quality Dashboard, Two Birds Command Centre
- **Client work:** Elite Karate (pending feedback)
- **Template:** Two Birds Project Template (every new repo clones from this — ships a11y baseline, axe-core CI, AUDIT.md structure, self-hosted fonts, etc.)

Each repo is static HTML/CSS/JS — **no npm, no Node frameworks** — per the standing rule in CLAUDE.md.

## How work happens

### Sprint loop

1. **Pending capture** — `hal-stack/sprint-system/pending-capture.md` holds items dropped in from Claude.ai chats. Every sprint starts by merging this file
2. **Notion is source of truth for sprint state** — `hal-stack/notion-sync/next-sprint.py` pulls the top Ready item. Fallback: `hal-stack/sprint-system/sprint-queue.md` when Notion is unreachable
3. **Execute → commit per phase → update SESSION-STATE → push** — every sprint ends that way; no exceptions per CLAUDE.md's SPRINT COMPLETION RULE
4. **Retro-file to Notion at session close** — pattern: `hal-stack/notion-sync/_retrofile_*.py` helpers (see `_retrofile_sprints_48_63.py` for the canonical shape)

### Trigger commands (in Claude Code)

CLAUDE.md defines these, but the common ones:

| Trigger | What it does |
|---|---|
| `next sprint` | Run `next-sprint.py` → execute top Ready item |
| `just go` | Single-sprint autonomous authorization in normal mode (added 2026-04-22 as RI-006 Fix #1) |
| `max mode` | Activate chained autonomous posture per `hal-stack/governance/max-mode.md` |
| `state` | Read SESSION-STATE and report top 3 next actions |
| `retro` | Read and report `logs/RETRO.md` |
| `dashboard` | Read `WIP-DASHBOARD.md` and report portfolio status |
| `hal` | Read `hal-stack/HAL-BACKLOG.md` and report next infra item |

### Governance

- **Standing rules** in CLAUDE.md are non-negotiable (static-only, Canadian English, commit after every phase, etc.)
- **Max mode** (`hal-stack/governance/max-mode.md`) overrides normal-mode pauses; activation is explicit by phrase or timestamp
- **Pattern Counter Rule** — if the same question is asked 3+ times in a session, stop troubleshooting instances and declare the pattern broken; log to [RELIABILITY-ISSUES.md](RELIABILITY-ISSUES.md)
- **Voice-check protocol** — scan all externally-facing written content for banned words (see `hal-stack/sprint-system/backlog/P2-voice-check-protocol.md`)

## HAL Stack (autonomy layer)

Local-first, sovereign-by-design development + automation infrastructure. See **[hal-stack/README.md](hal-stack/README.md)** for the full spec: sovereignty model (L1-L4), machine roster (Pentium Silver, ThinkPad i5, EZbook), persona system (Scrappy Pack + Founding Board), and architectural details.

The **Sovereignty Float Model** (L1-L4): every component must be designed so dropping between layers is a configuration change, not a rebuild. L1 = commercial cloud (default), L4 = air-gapped local.

## Notion sync

Product Backlog (Notion data source `dee08637-7122-46cd-bc29-7775ce3ab8f6`) is the canonical sprint state. See **[hal-stack/notion-sync/README.md](hal-stack/notion-sync/README.md)** for architecture and **[hal-stack/notion-sync/SETUP.md](hal-stack/notion-sync/SETUP.md)** for first-time setup.

Requires `NOTION_API_KEY` environment variable. Never committed.

## Key files reference

| File | Purpose |
|---|---|
| `CLAUDE.md` | Auto-loaded rules + trigger index for Claude Code sessions |
| `SESSION-STATE.md` | Per-sprint running log (latest at top) |
| `logs/RETRO.md` | Most-recent session retrospective |
| `RELIABILITY-ISSUES.md` | Log of systemic failures + their fixes (RI-001 through RI-007 at time of writing) |
| `NEXT-SPRINT-QUEUE.md` | Human-maintained backlog preview |
| `WIP-DASHBOARD.md` | Portfolio status dashboard |
| `hal-stack/HAL-BACKLOG.md` | Infrastructure backlog |
| `hal-stack/sprint-system/sprint-queue.md` | Local sprint queue (Notion fallback) |
| `hal-stack/sprint-system/pending-capture.md` | Inbox from Claude.ai chats |
| `hal-stack/governance/max-mode.md` | Autonomous posture governance |
| `journey/` | Archived journey entries (project history) |

## Contributing / session-start checklist

Before making changes in any repo in this portfolio:

1. Run `git log --oneline -30` — confirm you understand current state (per CLAUDE.md standing rule: *never rebuild something already built*)
2. Read SESSION-STATE.md — understand what shipped last and what's in-flight
3. Check `pending-capture.md` — merge any queued items first
4. Run PowerShell as Administrator if you'll need filesystem writes (Windows permission quirks, per CLAUDE.md)
5. End every work unit with SESSION-STATE update + `git push`

## Who + context

Aaron Patzalek. St. Thomas, Ontario. Solo parent of 6-year-old twins. 20+ years Senior Product Manager, most recently at Telus. Founded Two Birds Innovation early 2026. Revenue target: $10,000/month by August/September 2026.

The **Scrappy Pack** (five sub-personas: The Researcher, Why Not, The Fifth Why, The Ripper, Sovereignty Check) reviews Claude output as a filter — they're the "why guys" that challenge soft answers and surface cheaper-stronger alternatives.

The **Founding Board** (22 personas, 6 departments — see `hal-stack/personas/`) only runs when the sprint queue is empty; Legal (Helen) and CTO/Engineering (Naveen) hold veto cards.

## License

This repository contains governance, operations, and automation infrastructure. Individual product repos declare their own licenses.
