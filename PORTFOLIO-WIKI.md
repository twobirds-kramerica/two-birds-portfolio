<!--
  Portfolio Site Wiki — produced by S-ARCHAEOLOGY-005 (2026-04-23 ~00:35 EST)
  Status: MVP. Covers the full Two Birds Innovation portfolio (not just
  two-birds-portfolio repo — also aaron-patzalek, two-birds-innovation,
  two-birds-command-centre, etc). Sources: Two Birds Command project_memory
  (019d87ad), HAL Stack project_memory (019cc3d2), portfolio README.md
  (shipped S-039 this session), direct repo inspection.
-->

# Two Birds Portfolio Wiki — v0.1 MVP

**Last updated:** 2026-04-23 00:35 EST (Toronto)
**Source:** Two Birds Command project_memory (019d87ad) + HAL Stack project_memory + portfolio-root files + ls of `C:\twobirds\`
**Status:** Living document.

## 1. What the Portfolio Is

**Two Birds Innovation** — Aaron Patzalek's Canadian solo-founder tech company, based in St. Thomas, Ontario. Combines:

- A set of owned products (DCC, Clarity, Career Coach, Kevin's Apartment Search)
- Brand/marketing sites (aaron-patzalek, two-birds-innovation)
- Operations infrastructure (two-birds-portfolio = HAL Stack governance; two-birds-command-centre = executive dashboard; quality-dashboard = portfolio health monitor)
- Templates + tooling (two-birds-project-template; career-ops; HAL Stack autonomy layer)

Per Two Birds Command project_memory:
> "Aaron runs a consulting and product business called **Two Birds** (Two Birds Innovation), supported by an AI assistant system called **HAL** that uses Claude Code with remote control, GitHub for version control, and Notion as a sprint management database. The overarching goal is a fully automated, Notion-first sprint workflow where HAL can autonomously pull, execute, and complete sprints with minimal manual intervention."

Revenue target: **CAD $10,000 / month by August/September 2026** (per DCC + HAL Stack memories).

## 2. The Portfolio Sites (user-facing)

| Repo | Purpose | Live URL |
|---|---|---|
| `aaron-patzalek` | Personal brand / solopreneur site | `https://twobirds-kramerica.github.io/aaron-patzalek/` |
| `two-birds-innovation` | Company brand site | `https://twobirds-kramerica.github.io/two-birds-innovation/` |
| `digital-confidence` | DCC (flagship product) | `https://twobirds-kramerica.github.io/digital-confidence/` |
| `clarity` | SME AI-readiness diagnostic | `https://twobirds-kramerica.github.io/clarity/` |
| `career-coach` | Job-app tooling | `https://twobirds-kramerica.github.io/career-coach/` |
| `kevins-apartment-search` | Private tool for Kevin Burnett (Aaron's uncle) | private-link / noindex |
| `quality-dashboard` | Portfolio health monitor (internal) | `https://twobirds-kramerica.github.io/quality-dashboard/` |
| `two-birds-command-centre` | Executive dashboard + project hub | `https://twobirds-kramerica.github.io/two-birds-command-centre/` |
| `elite-karate-site` | Client site for Kirk's Elite Karate Club (St. Thomas ON) — client-pending, do-not-touch | `https://twobirds-kramerica.github.io/elite-karate-site/` |

GitHub org: **`twobirds-kramerica`**.

## 3. The Portfolio Infrastructure (governance layer)

| Repo / file | Role |
|---|---|
| `two-birds-portfolio` (this repo) | Master governance + HAL Stack; CLAUDE.md, SESSION-STATE, RETRO, RELIABILITY-ISSUES, product wikis (new this session) |
| `two-birds-project-template` | Starting point every new product clones; ships a11y + SEO + sovereignty baseline |
| `career-ops` | UNKNOWN scope — not in the memory; present at `C:\twobirds\career-ops` with 281-line README. Aaron to summarise. |
| `hal-stack/` (inside two-birds-portfolio) | HAL Stack autonomy layer — personas, governance docs, sprint system, notion-sync, architecture |

## 4. Notion Architecture (authoritative)

From HAL Stack memory + Two Birds Command memory:

| Surface | Notion ID |
|---|---|
| Command Center page | `347a09cf-876a-81fb-9a5c-eca696fb585b` |
| Product Backlog data source | `dee08637-7122-46cd-bc29-7775ce3ab8f6` |
| Sprint Queue Manager data source | `a297b04c-7887-42d1-b73b-21af94d57cd8` |
| Job Pipeline data source | `92415698-9009-4d74-b86b-ad23f5afe475` |
| Glossary / Command Reference page | `348a09cf-876a-815a-802c-c9c182167749` |
| Kids Research DB | `e184382b-b59a-41e7-9152-d90fbee1abe6` |

**Integration name (in Notion's settings):** "Two Birds — Claude Code Sync" in TwoBirds workspace.

## 5. Workflow (session startup pattern)

Per Two Birds Command memory:
> "When I say 'retro,' fetch SESSION-STATE.md from the HAL Stack repo before responding. When I say 'next sprint,' fetch sprint-queue.md. Never reconstruct status from memory — only report what the live files confirm."

This is the **origin** of the portfolio's trigger command system as it appears in CLAUDE.md today.

## 6. Key People (portfolio-level)

From memories:
- **Brenda Bender** — step-mother, real person, DCC beta tester
- **Trish Patzalek** — DCC beta tester
- **Kevin Burnett** — uncle; Kevin's Apartment Search is built for him
- **Mike Kerkvliet** — St. Thomas Economic Development; Paperwork Labs + role opportunity
- **Phil Butler** — Employment Services Elgin; EZbook provider
- **Davie Lee** — interVal / TechAlliance St. Thomas
- **Alicia Patzalek** — Aaron's wife (Alicia Patzalek project, 019bde6a, for her re-entry resume work)

## 7. Stack Rules (portfolio-wide)

Inherited from CLAUDE.md STANDING RULES:
- Static HTML/CSS/JS only (no npm, no Node frameworks)
- Canadian English in all visible content
- Self-hosted fonts (no Google CDN)
- Commit after every phase
- `git log --oneline -30` before touching any repo
- Session-start: read SESSION-STATE.md before working
- End-of-session: overwrite RETRO.md + push
- Pattern Counter Rule: same question 3x → declare pattern broken + log to RELIABILITY-ISSUES.md
- Sprint Completion Rule: every sprint ends with SESSION-STATE update + git push
- Timestamp Rule: RETRO/SESSION-STATE/log end with mandatory two-line footer
- (new 2026-04-22) Session Length Rule: ~3h / ~40 tool calls per session
- (new 2026-04-22) MCP Write Safety Rule: `safe_notion_write()` wrapper around Notion writes
- (new 2026-04-22) `just go` trigger: single-sprint normal-mode autonomous authorisation

## 8. Sovereignty (Float Free Index 48/100)

Every component designed to drop between layers (L1 commercial → L4 air-gapped local) as a config change, not a rebuild.

Per HAL Stack memory: **Float Free Index 48/100** with documented path to 80/100.

**Explicitly rejected:**
- React / Vue / Svelte (violates static-only)
- npm / yarn / pnpm (violates no-frameworks)
- Google Fonts CDN (self-host instead)
- Supabase, Vercel, Resend (closed per audit)

## 9. Open Questions

1. **Company name decision** — Two Birds Innovation vs ALOFT (memory 2026-04-04: "domain purchase blocked on this decision"). Status?
2. **career-ops scope** — 281-line README in `C:\twobirds\career-ops\README.md`; not in DCC or HAL Stack memories. What is it, and why separate from career-coach?
3. **Elite Karate status** — client site, pending feedback per CLAUDE.md. Any update?
4. **Domain strategy** — 2 `.ai` domains Aaron owns; Two Birds Command memory flagged as "quick-sell / price-drop / auction-list" pending decision.
5. **EI runway** — HAL Stack memory dated 2026-04-04: "Aaron is on employment insurance with limited runway." Still the case?
6. **Gig work applications + domain purchases** — active backlog items per Two Birds Command memory; status?

## 10. Decision Log (portfolio-wide, chronological highlights)

| Date | Decision | Source |
|---|---|---|
| 2026-02-16 | DCC founded | projects.json[019c67c5] |
| 2026-02-19 | Job Apps Suite (precursor to Career Coach) | projects.json[019c784a] |
| 2026-03-06 | HAL Stack project created | projects.json[019cc3d2] |
| 2026-04-04 | HAL Stack memory last updated; audit finding "stop orchestrating the orchestrator" | memory |
| 2026-04-11 | DCC V07 heart-bulb logo selected | portfolio RETRO |
| 2026-04-13 | Two Birds — Command project created | projects.json[019d87ad] |
| 2026-04-19 | Warm Hearth palette voted winner (org vote, 65.5%) | tokens.css + HAL Stack memory |
| 2026-04-21 | Max-mode 75-sprint session; 8/9 repos have axe-core + AUDIT.md; DCC Kids DB 20 rows | portfolio RETRO |
| 2026-04-22 | Max-mode 18-sprint session; S-DCC-V2 /v2/ POC; S-MCP-RELIABILITY-001; RI-006 'just go' trigger | portfolio SESSION-STATE |
| 2026-04-23 | S-ARCHAEOLOGY-001 through 005 wikis produced (this pass) | portfolio commit log |

## 11. Pointers

- Master README (human-landing): `README.md` (portfolio root, shipped S-039)
- Auto-loaded for Claude: `CLAUDE.md`
- Per-product wikis (new this session): `DCC-PRODUCT-WIKI.md`, `HAL-STACK-WIKI.md`, `CLARITY-PRODUCT-WIKI.md`, `CAREER-COACH-WIKI.md`, this file
- HAL Stack internals: `hal-stack/README.md` + subdirs (architecture, personas, sprint-system, notion-sync, governance, mcp-reliability)
- Reliability log: `RELIABILITY-ISSUES.md` (7 RIs as of 2026-04-22)
- Last retro: `logs/RETRO.md` (2026-04-21 session)

## 12. How to Navigate (for a fresh Claude Code instance)

1. Read `CLAUDE.md` (auto-loaded)
2. Read `SESSION-STATE.md`
3. Read `logs/RETRO.md` for most-recent session summary
4. Read the relevant per-product wiki (this file for portfolio-wide view; specific wikis for DCC / HAL / Clarity / Career Coach)
5. Before proposing a sprint: `git log --all --grep=<SPRINT-ID>` per feedback memory — prevents duplicate work
6. Before asserting anything about Notion state: query the authoritative data sources (Sprint Queue `a297b04c-...`, Product Backlog `dee08637-...`)
