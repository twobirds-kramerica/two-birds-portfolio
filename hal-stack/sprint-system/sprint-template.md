<!--
STATUS: v0.2 — TEMPLATE
Created: 2026-04-11 16:10 EST (Toronto)
Updated: 2026-04-11 22:58 EST (Toronto)
-->

# Sprint Template

Copy this template to add a new sprint to `sprint-queue.md`.

---

```
## S-[NNN]: [Title]

**Priority:** P[1/2/3]
**Duration:** [estimate]
**Status:** READY / BLOCKED / DONE
**Blocked by:** [what must happen first, or "—"]
**Layer:** [L1-L4]
**Story refs:** [S1.1, S5.6, etc.]

### Prompt

AUTONOMOUS SPRINT — [TITLE]
Repo: C:\twobirds\two-birds-portfolio\
Read SESSION-STATE.md before starting. Commit after each phase.

PHASE 0 — PROCESS PENDING CAPTURES (mandatory)

Read hal-stack/sprint-system/pending-capture.md.
If the "Current Queue" section contains any items:
1. For each item, route to destination based on TYPE:
   - human-backlog → append to sprint-system/human-backlog.md
   - story → append to backlog/stories.md
   - epic → append to backlog/epics.md
   - blocker → flag at top of session results as highest priority
   - issue → append to backlog/stories.md as P1 bug
2. Preserve priority, category, context, and action
3. Clear merged items from pending-capture.md (keep header, empty queue)
4. Commit: "chore(hal): merged [N] captured items from pending queue"
If pending-capture is empty, skip to Phase 1.

PHASE 0.5 — DREW INTAKE (recommended for Stage 2+)

Drew (Program Director) reviews sprint scope:
- Confirms maturity stage (see personas/maturity-stages.md)
- Selects review panel (see personas/review-panels.md)
- Flags concerns before work begins
For Stage 1 prototype work, Aaron can say "standard intake" to skip.

[PHASE 1+ — Sprint-specific work here]

PHASE N-1 — PANEL REVIEW (required for Stage 3+)

Each panel member reviews sprint output against DoD:
- Reviews logged to hal-stack/personas/review-log/
- Drew synthesizes verdict: APPROVED or REWORK
- If REWORK: sprint status → BLOCKED, fix list documented
- If APPROVED: sprint status → READY TO SHIP
- Aaron makes final call (SHIP / ACCEPT REWORK / OVERRIDE)
For Stage 1-2, panel review is optional (Drew decides).

FINAL STEP: Update SESSION-STATE.md, auto-generate context export,
commit, push to master.

### Expected Outputs
- [file or commit expected]
- [file or commit expected]
```

---

## Mandatory Standards Checklist

Every sprint that produces code or user-facing changes must verify these before marking DONE:

```
### Standards Compliance (check before DONE)

- [ ] HTML: semantic elements, heading hierarchy, alt text, linked labels
- [ ] CSS: tokens.css variables used (no hardcoded colours), mobile-first
- [ ] Accessibility: WCAG AA contrast, 44px tap targets, focus indicators, keyboard nav
- [ ] Performance: page weight < 500KB, no render-blocking JS, images lazy-loaded
- [ ] SEO: unique title + meta description, canonical, OG tags
- [ ] Security: no secrets in repo, CDN libs pinned with SRI, CSP present
- [ ] Dependencies: zero npm, CDN fallbacks documented, decapitation-safe
- [ ] Testing: axe-core 0 critical/serious, links work, mobile viewport OK
- [ ] CHANGELOG.md updated (if user-facing changes)
```

Sprints that are documentation-only or internal tooling may skip this checklist but must note "Standards checklist: N/A (no code changes)" in the commit.

---

## Rules Every Sprint Prompt Must Include

1. **PHASE 0 — Process pending captures.** NON-NEGOTIABLE. Every sprint checks `pending-capture.md` first so nothing Aaron logged gets lost.
2. `Read SESSION-STATE.md before starting`
3. `Commit after each phase`
4. `Update SESSION-STATE.md` at the end
5. `Auto-generate context export` at the end
6. `Push to master` at the end
7. Quality over completeness
8. No scope creep — improvements go to backlog
9. Plain language, timestamps on all files
10. **Standards compliance checklist** verified before DONE (see above)
11. **GitHub Projects:** New sprints should create a GitHub Issue first (use sprint template), then reference the issue number in the sprint prompt. Close the issue when the sprint is DONE. The project board at https://github.com/users/twobirds-kramerica/projects/1 is the visibility layer; sprint-queue.md remains the execution queue.
