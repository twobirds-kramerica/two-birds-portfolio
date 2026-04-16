# Sprint Intake Interview

**Version:** 1.0 | **Created:** 2026-04-16
**Conducted by:** Drew (Program Director)

Drew asks these questions before any sprint is scope-locked. Aaron answers, Drew synthesizes into a sprint brief.

---

## Standard Intake (7 Questions)

### 1. What is this sprint's product/deliverable?
_One sentence. What are we building or fixing?_

### 2. What maturity stage is this? (1-5)
_See `maturity-stages.md`. This determines the review panel._
- 1 = Prototype (internal, throwaway OK)
- 2 = Alpha (internal, not throwaway)
- 3 = Beta (trusted testers / Brenda)
- 4 = Production (public / paying users)
- 5 = Scale (revenue-critical)

### 3. Who are the target users?
_Be specific. "Seniors in Ontario" not "users." "Aaron only" is valid for prototype._

### 4. What's the business risk if this ships broken?
- **None** — it's a prototype, nobody sees it
- **Low** — internal tool, easy to fix
- **Medium** — real users see it, trust affected
- **High** — revenue or partnership depends on it
- **Critical** — legal, financial, or safety consequences

### 5. What are your acceptance criteria in plain language?
_What does "done" look like? Not technical spec — Aaron's words._

### 6. Any known constraints?
_Time, cost, dependencies, blockers, Aaron's energy level._

### 7. Do you want Scrappy Pack on standard friction or heavy challenge mode?
- **Standard** — Scrappy Pack reviews output, flags concerns
- **Heavy challenge** — Scrappy Pack actively argues against the approach, looking for reasons NOT to ship

---

## Quick Intake (Skip Interview)

For small prototype work (Stage 1), Aaron can say **"standard intake"** and Drew will:
1. Set maturity stage to 1
2. Assign Scrappy Pack review only
3. Apply baseline DoD
4. Skip the full interview

Aaron can also say **"stage N, standard"** to set the stage directly and skip questions 1-6.

---

## Drew's Sprint Brief (Output)

After intake, Drew produces:

```
### DREW — SPRINT BRIEF

**Sprint:** [ID or title]
**Stage:** [1-5]
**Risk:** [None / Low / Medium / High / Critical]
**Review panel:** [list of names]
**Scrappy Pack mode:** [Standard / Heavy challenge]
**Acceptance criteria:** [Aaron's words, verbatim]
**Constraints:** [time, dependencies, blockers]
**Drew's concerns:** [anything flagged before work starts]
```

This brief is included at the top of the sprint prompt before Claude Code executes.
