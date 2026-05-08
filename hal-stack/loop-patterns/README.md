# HAL Stack — Loop Patterns
**Created:** 2026-05-08 | **Updated:** 2026-05-08 (research correction)
**Source:** Boris Cherny /loop — AI Ascent 2026 + official Threads post

Boris Cherny's actual commands (cited — Threads `@boris_cherny/post/DWfjpUNlKzx`):
- **`/loop 5m /babysit`** — auto-address code review, auto-rebase PRs
- **`/loop 30m /slack-feedback`** — create PRs for Slack feedback every 30 min

Pattern: **skill = logic, loop = scheduler, loop.md = default**.
Named skills live in `hal-stack/skills/`. Loops call them.

---

## ⚠️ Critical: /loop is session-scoped

> *"Tasks only fire while Claude Code is running and idle. Closing the terminal or letting the session exit stops them firing."*
> — [Official docs, code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)

**`/loop` requires an open Claude Code terminal.** It is NOT a background daemon.
For overnight or unattended jobs, use **Task Scheduler** or **GitHub Actions** instead.

## Automation tiers — choose the right one

| Tier | Tool | Needs open session | Local files | Min interval | Use for |
|------|------|--------------------|-------------|--------------|---------|
| **1 — Active session** | `/loop` + skills | **Yes** | Yes | 1 min | PR babysitting, CI watching, deploy polling during active work |
| **2 — Machine unattended** | Task Scheduler + `run-overnight-build.bat` | No | Yes | 1 min | Nightly git sync, Lighthouse audits, weekly reports |
| **3 — Cloud CI** | GitHub Actions | No | No (clone) | On push / cron | Link checker, axe-core, gitleaks, build health reports |
| **4 — Anthropic cloud** | `/schedule` (Routines) | No | No | **1 hour min** | High-value jobs when machine is off |

---

## Boris's pattern in Three Steps

**Step 1 — Write the skill** (`hal-stack/skills/babysit.md`)
The skill is the logic. Concise instructions Claude follows each iteration.

**Step 2 — Wire a loop** (`/loop 5m /babysit`)
The loop is just the scheduler. Interval + skill name = done.

**Step 3 — Bake into loop.md** (`.claude/loop.md`)
Bare `/loop` (no args) now runs your project maintenance default automatically.

---

## Loop inventory

| File | Named Skill | Loop Command | Tier | Interval |
|------|-------------|-------------|------|----------|
| `loop-pr-babysitter.md` | `/babysit` | `/loop 5m /babysit` | 1 — Active session | 5 min during active work |
| `loop-backlog-health.md` | `/backlog-triage` | `/loop 60m /backlog-triage` | 1 or 2 | 60 min session / weekly Task Scheduler |
| `loop-content-freshness.md` | `/freshness-check` | `/loop /freshness-check` | 2 — Task Scheduler | Weekly (Sunday 8 PM) |
| `loop-notion-sync-verify.md` | _(inline prompt)_ | Task Scheduler only | 2 — Task Scheduler | Daily 6 AM |

See `AUTOMATION-MAP.md` for the full HAL Stack job-to-tier mapping.

---

## Boris Cherny pattern principles (verified)

1. **Skill first, loop second** — build the skill, then the loop calls it. Never inline long prompts in loop commands.
2. **One job per loop** — narrow focus. Don't build one loop that does everything.
3. **loop.md is your maintenance default** — bare `/loop` should "just work" for the current project.
4. **Session-tier for active work; machine-tier for overnight** — don't fight the architecture.
5. **Sovereign** — `/loop` is built into Claude Code. Zero external dependencies, zero cost.
