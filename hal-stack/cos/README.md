# HAL Stack — Chief of Staff (CoS) Layer
**Integrated:** 2026-05-10
**Source:** Logan Currie CoS v3 (logancurrie.com/chief-of-staff) + HAL Stack adaptation
**Trigger word:** `cos`

---

## What This Does

When Aaron types `cos`, Claude runs a structured daily ops check-in using live data from four sources:

1. **Google Calendar** (via MCP) — today + tomorrow's events, deep work windows, meeting blocks
2. **Gmail** (via MCP) — scan last 48h for urgent/unread items requiring same-day response
3. **Notion P1 backlog** (via MCP) — current P1 items by Owner=Aaron
4. **SESSION-STATE.md** — recent sprint completions, open actions, last recommended next step

Then outputs the full CoS check-in structure (see below).

## How to Run

In any Claude Code or Claude.ai session, just type:

```
cos
```

Claude will pull the live data and return the check-in. No other input required.

For the procrastination diagnostic (Head/Heart/Hand), Claude will trigger it automatically when resistance signals are detected. Do not ask for it explicitly — Logan's protocol says naming resistance directly works better than asking.

---

## Daily Check-In Structure

Every `cos` run produces:

### 1. Wins
- What shipped recently (from SESSION-STATE)
- Pattern observation if visible

### 2. Today's Landscape
- Calendar: meetings, deep work windows, gaps
- Email: anything urgent flagged
- Energy check: one question about current state

### 3. Brain Dump → Organize
From SESSION-STATE + Notion P1, identify:
- **2-minute tasks** (do NOW)
- **Batchable clusters**
- **Today's realistic focus** (1–3 items max)
- **This week** (important but not today)
- **Parking lot** (genuinely set aside)

### 4. Today's Focus
- Max 3 tasks with concrete next actions
- Batching opportunities
- ADHD technique suggestion when relevant

### 5. Accountability
- One specific thing to report back on next check-in
- No guilt, just clarity

---

## Weekly Rhythm

| Day | CoS Action |
|---|---|
| Monday | `cos-week` — Priority Dashboard for the week, mid-week review reminder |
| Tue–Thu | `cos` — daily check-in in same thread |
| Wed or Thu | Mid-week parking lot review: "what lower-priority items can fit this week?" |
| Friday | `cos-retro` — light pattern observation, setup for Monday |

*(These sub-triggers will be added as usage patterns emerge.)*

---

## Procrastination Protocol

When resistance signals appear (see `hal-stack/reference/logan-currie-procrastination-protocol.md`), Claude runs the diagnostic **before** suggesting any execution tactics:

1. **HEAD** — Is this task strategically appropriate? Should it be done at all?
2. **HEART** — Is there emotional resistance? What is the feeling?
3. **HAND** — Is there a genuine capability gap?

Sequence: **Diagnose → Address root cause → THEN apply execution tactics.**

Do NOT default to Pomodoro/2-minute-rule until after the diagnostic. Applying productivity tactics to a Heart problem adds shame.

---

## Reference Files

| File | Purpose |
|---|---|
| `hal-stack/reference/logan-currie-cos-prompt-v3.md` | Full CoS system prompt (verbatim, ADHD framing preserved) |
| `hal-stack/reference/logan-currie-procrastination-protocol.md` | Head/Heart/Hand diagnostic framework |
| `hal-stack/cos/README.md` | This file — HAL Stack integration notes |

---

## HAL Stack Integration Notes

**What CoS adds that HAL didn't have:**
- Structured daily check-in ritual (HAL had sprint execution but no daily human-facing ops moment)
- Procrastination diagnostic (HAL had pattern detection but no root-cause framework)
- Energy-aware task matching (Love Balance Advisor flagged overload; CoS matches tasks to energy level)
- Weekly human rhythm (overnight automation covered machine-side; CoS covers human-side cadence)

**What HAL adds that Logan's standard CoS doesn't have:**
- Live MCP integrations (Gmail + Calendar vs. simulated in Logan's version)
- Notion backlog as the Task Master List (automated, version-controlled)
- SESSION-STATE as institutional memory (persistent across sessions)
- Sovereignty layer (L1-L4 escape paths — no Discord dependency)

**ADHD framing:** Preserve fully. Aaron confirmed this framing is intentional and is exactly why the system works for him. Do not strip ADHD language from CoS outputs.
