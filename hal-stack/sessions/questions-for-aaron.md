<!--
STATUS: v0.1 — QUESTIONS — AARON ANSWERS THESE BEFORE NEXT SPRINT
Created: 2026-04-10 21:00 EST (Toronto)
Purpose: Unblock the next build sprint with minimum Aaron effort
-->

# Questions for Aaron

Most blocking first. Answer these before the next build sprint.

---

### Q1. Is voice a priority right now?

The voice layer research is done — signup checklist, build plan, sovereignty notes, the works. But building it takes 2-3 hours and requires an OpenAI account (CA$5).

**Why it matters:** If voice is not a near-term priority, the next sprint should focus elsewhere (branding rework, content freshness, decapitation checklists). If voice IS a priority, the next sprint starts with "create OpenAI account."

**Suggested answer:** Park voice until the desktop arrives (L4 STT will be too slow on EZbook's Celeron anyway). Focus next sprint on revenue-adjacent work.
**Confidence:** LOW — I don't know Aaron's current priority. This is a guess.

**Files affected:** `voice-layer/build-sprint-plan.md`, `backlog/epics.md` (E3 priority), `backlog/stories.md` (S3.x sequence)

---

### Q2. What's wrong with logo v1.1?

You said it's "not quite the spec." I need specific feedback to do a v1.2 rework.

**Why it matters:** Logo is blocked until you say what to change. LinkedIn upload is on hold.

**Suggested answer:** n/a — only Aaron can answer this.
**Confidence:** n/a

**Files affected:** `assets/logos/two-birds/`, `backlog/epics.md` (E5), `backlog/stories.md` (S5.1, S5.2)

---

### Q3. Is the four-layer sovereignty model the right level of rigour?

The overnight sprint built a full framework: principles doc, layer tags, decapitation checklists, ADRs. This is thorough architecture for a solo consultancy that's three months old.

**Why it matters:** If it's over-engineered, we're spending documentation time that could go to revenue work. If it's right-sized, it prevents a future crisis. Only Aaron knows where the line is.

**Suggested answer:** The principles are right. The decapitation checklist template is useful. The layer tags might be overkill — consider only applying them to new decisions rather than retroactively tagging everything.
**Confidence:** MEDIUM — the framework feels right-sized to me but I built it.

**Files affected:** `architecture/sovereignty-principles.md`, `architecture/layer-tags.md`, `architecture/decapitation-checklist.md`

---

### Q4. Should "fill out context export template" be added to the post-session workflow?

The context bridge system includes a template to fill out after each session. This takes about 5 minutes. It means future sessions start with full context instead of cold.

**Why it matters:** If added to CLAUDE.md, every session ends with a context export. If not, the context system exists but doesn't get populated. Without data, the system is an empty container.

**Suggested answer:** Yes, but keep it lightweight — only fill it out for significant sessions (new architecture, major decisions, research findings). Skip it for routine sprints that are already captured in SESSION-STATE.md.
**Confidence:** MEDIUM — the suggested answer tries to balance overhead vs value.

**Files affected:** `CLAUDE.md`, `context-system/retroactive-catchup-plan.md`

---

### Q5. Does the "no Node frameworks" principle apply only to products, or to everything?

`architecture/principles.md` says "No Node frameworks" but the voice layer build plan uses Node.js scripts. The DCC and other products are static HTML/CSS/JS — that's clear. But HAL Stack internal tools might need Node.

**Why it matters:** If the principle applies everywhere, the voice layer can't use Node and must be built in PowerShell or batch scripts. If it applies only to products, Node is fine for internal infrastructure.

**Suggested answer:** Products only. Internal tools can use whatever works.
**Confidence:** HIGH — this is almost certainly what Aaron means, but it's worth confirming.

**Files affected:** `architecture/principles.md` (needs one clarifying sentence), `voice-layer/build-sprint-plan.md`

---

### Q6. What should the next build sprint focus on?

Options, ranked by my assessment of value:

a. **Voice layer build** (2.5 hours, needs OpenAI account) — cool, sovereignty-aligned, but not revenue-generating
b. **Logo v1.2 rework** (30-60 min, needs Q2 answered) — unblocks LinkedIn presence
c. **Decapitation checklists for GitHub/Formspree/Cloudflare** (1 hour) — sovereignty hygiene
d. **Content freshness script** (1-2 hours) — operational hygiene for DCC
e. **Retroactive context recovery** (2 hours, manual) — fills the context bridge with past decisions

**Why it matters:** Aaron's time is the scarcest resource. Choosing the wrong next sprint wastes it.

**Suggested answer:** (b) then (c). Logo rework is fast and unblocks LinkedIn. Decapitation checklists are quick documentation that compound in value.
**Confidence:** LOW — I don't know Aaron's current revenue priorities or calendar.

**Files affected:** All backlog files

---

### Q7. Is the Pentium Silver still in active use?

machines.json lists it as "active" with almost no specs filled in. If Aaron hasn't used it in weeks, it could be marked "standby" and the unknown specs stop being a gap.

**Why it matters:** Minor — just cleanup. If it's active, we should fill in specs next time Aaron's on it.

**Suggested answer:** Mark as "standby" unless Aaron uses it regularly.
**Confidence:** MEDIUM

**Files affected:** `machine-profile/machines.json`

---

### Q8. Do you want me to check Claude.ai for a data export option?

The retroactive catchup plan says to check claude.ai settings. I can't do this from Claude Code (no browser access to your account), but I can describe exactly where to look.

**Why it matters:** If data export exists, we can recover context from 3 months of Claude Web sessions. If it doesn't, manual recovery is the only path.

**Suggested answer:** Aaron checks next time he's on claude.ai. Takes 2 minutes: Settings → Account → look for "Export" or "Download my data."

**Files affected:** `context-system/retroactive-catchup-plan.md`
