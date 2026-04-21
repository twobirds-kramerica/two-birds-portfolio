# DCC — Candidate New Accessibility Components (Scope Proposal)

**Status:** PROPOSAL — for Aaron review. No code.
**Source context:** S-025 benchmark research + Warm Hearth design system (shipped) + competitive-audit findings (`hal-stack/research/dcc-ui-benchmarks.md`) + the Notion Backlog item "DCC new accessibility components sprint" (P2, Backlog, Claude Code).

Propose 4 candidate components, each with: user need, implementation sketch, LOE, and a defensible reason to ship (or skip) it.

Your action: approve 0-4 of these for S-030. Any subset I can execute immediately after your flip-to-Ready. If none feel right, paste a spec for a different component and I'll build that instead.

---

## Candidate 1 — Read-Aloud button (page-level)

**User need.** Seniors with low vision or cognitive fatigue benefit enormously from having long content read aloud. Competitive audit finding: MyChart and Be Connected both offer this; we flagged it as a recommendation in S-025 Part 9 ("add a read-aloud control to each module page"). Codified in `digital-confidence/styleguide/MAINTENANCE.md` Audio & Voice spec.

**Implementation sketch.** A single button at the top of each module / article page: `▶ Read this aloud`. Clicking it starts the Web Speech API's `speechSynthesis.speak()` on the main content (`<main>` innerText, minus nav and footer). Second click pauses; third resumes. A second control cycles voice preference (system default / Canadian English female / Canadian French female). Preference persists in localStorage.

**Files touched.** New `js/read-aloud.js` (~80 lines). New `css/components.css` rule for `.read-aloud-btn` (~15 lines). Each DCC page gets one `<button class="read-aloud-btn">` placed after `<h1>`. For mass rollout across 29 modules: a `sed` loop similar to the S-028 palette swap.

**LOE.** 2-3 hours including the 29-module injection + per-page smoke test.

**Why ship.** Highest user-visible payoff of the four. Web Speech API is on every modern browser for free. No external dependency.

**Why not ship yet.** Voice quality varies across browsers; the Windows default SAPI voices sound robotic. A user may prefer silence to a bad voice. Ship with a voice-selection control to let the user pick.

---

## Candidate 2 — Top-of-page progress indicator (module-level)

**User need.** Current DCC module pages show progress mid-content. ADHD and low-literacy users benefit from seeing "where am I in this" at-a-glance, persistently, in the same place on every page. The kipi-system "carried forward" / effort-tracked philosophy (from S-027) applies here.

**Implementation sketch.** A thin horizontal dot strip at the top of every module page, below the nav: `● ● ● ○ ○ ○ ○` (filled = completed sections, empty = remaining). One dot per H2 section in the module. Updates via IntersectionObserver as the user scrolls past each section — no click tracking, just presence-detection. Persists in localStorage keyed by module slug.

**Files touched.** New `js/module-progress.js` (~50 lines, no deps). New `css/components.css` rule for `.module-progress-dots` (~25 lines). Per-module HTML edit to add one `<nav class="module-progress-dots" aria-label="Module progress">` after the `<h1>`.

**LOE.** 2-3 hours including per-module injection + accessibility verification.

**Why ship.** Anchors orientation on long module pages. Respects ADHD cognitive style (spatial progress > textual progress).

**Why skip.** Overlaps with the existing progress bar. If the team already likes the existing bar, this is paint-over-paint. Aaron should eyeball one module's current progress UI and decide if the dot strip is additive or replacing.

---

## Candidate 3 — "Still with us?" gentle check-in

**User need.** Long content (DCC modules run 10-20 minutes of reading). Seniors fatigue. Without permission to stop, some push through, dislike it, and don't come back. Evidence: the S-025 kipi comparison's ADHD philosophy section — "No shame. Always 'carried forward.' Never 'you forgot.'"

**Implementation sketch.** After 8 minutes of idle scrolling OR when the user reaches the midpoint of a module, a small non-blocking banner slides in at the bottom: *"Take a break if you need one. This page will be here when you're back — your progress is saved."* Two buttons: "Keep going" (dismiss) and "I'll come back later" (saves progress + flashes the dismiss-scroll-position so the user can pick up where they left off). Settings toggle to disable if it annoys the user.

**Files touched.** New `js/check-in.js` (~100 lines). New `css/components.css` rule for `.check-in-banner` (~30 lines). Per-module injection: one `<div class="check-in-banner" hidden>` element.

**LOE.** 3-4 hours including idle-detection tuning + user-setting toggle + cross-viewport test.

**Why ship.** Signature psychological-safety feature aligned with Warm Hearth kitchen-table tone. Differentiator from every other digital-literacy site (GCF, Age UK, AARP don't do this).

**Why skip.** Risk of annoyance — the wrong tuning (too frequent, too intrusive) flips it from helpful to patronising. Needs a settings opt-out from day one. Consider piloting on ONE module before rolling to all 29.

---

## Candidate 4 — Keyboard-shortcut helper (`?` pop-up)

**User need.** Users who can't use a mouse (arthritis, tremor, preference) navigate DCC purely by keyboard. Today there's no discoverable list of what shortcuts the site supports. Common pattern in apps, rare in content sites.

**Implementation sketch.** Pressing `?` anywhere on the site (except inside an input) opens a modal listing available shortcuts: `Tab` (next focusable), `Shift+Tab` (previous), `Enter` (activate), `Escape` (close dialogs, return to content), `/` (focus search), `A-`/`A+` (text size). Modal is focus-trapped; Escape closes it.

**Files touched.** New `js/keyboard-helper.js` (~60 lines). New `<dialog id="kbd-help">` element injected site-wide via one JS insertion. New `css/components.css` for `.kbd-help` (~40 lines).

**LOE.** 2 hours including the focus-trap + keyboard-detection + modal markup.

**Why ship.** Explicit keyboard support is a WCAG-plus accessibility signal. Low effort, high respect-for-user. Pairs well with the `prefers-reduced-motion` work already shipped.

**Why skip.** The senior demographic has relatively few pure-keyboard users compared to screen-reader / text-enlargement users. May be effort better spent on read-aloud (Candidate 1) for the core audience.

---

## Not proposed (on purpose)

- **Dark mode theme swap UI** — shipped via tokens-dark.css + OS-level `prefers-color-scheme` auto-detect. Exposed in the styleguide as a demo; no user-facing toggle yet, and building one is a design decision that deserves its own proposal.
- **Captions / transcripts for video** — DCC has no video content today. File when video lands.
- **High-contrast manual toggle** — same as dark mode, already available via OS `prefers-contrast: more` + committed `tokens-high-contrast.css`. User-facing toggle is a design call.

---

## Recommended sequencing if you approve 2+

1. **Candidate 1 (Read-Aloud)** first — highest payoff, zero-dep, works everywhere.
2. **Candidate 4 (Keyboard helper)** next — cheapest, shortest LOE, compounds with keyboard navigation that already works.
3. **Candidate 2 (Progress dots)** — worth it only after Aaron eyeballs a current module and confirms it's additive, not duplicative.
4. **Candidate 3 (Still-with-us banner)** — highest emotional-resonance but highest risk of annoyance; pilot on ONE module, gather feedback, then decide.

## Confidence

85%. High on user needs (grounded in S-025 research, Warm Hearth governance, kipi / GCF / Age UK / AARP patterns). Medium on LOE estimates (could shift ±50% depending on how clean the existing module HTML is for injection). 15% uncertainty reserved for: this set reflects MY judgment about what would help DCC users — you may know something about your actual user base (Brenda, library-director conversations) that tips the priority differently.

## Next action

Flip 0-N of these to Ready in Notion — or paste an entirely different component spec. I execute whatever lands Ready next.
