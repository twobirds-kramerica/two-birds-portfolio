<!--
STATUS: v0.1 — SELF-AUDIT — CLAUDE CODE CHECKING ITS OWN WORK
Created: 2026-04-10 20:55 EST (Toronto)
Confidence: MEDIUM — an author auditing their own work has blind spots
Known gaps: Cannot verify external tool pricing or availability claims
-->

# Overnight Sprint — Self-Audit

Checking every file from commits `63e29fa` through `f82a9de` against six criteria.

## Audit Legend

| Check | What It Means |
|-------|--------------|
| SOV | Does it contradict sovereignty-principles.md? |
| VENDOR | Does it assume a specific vendor where it should be agnostic? |
| CLAUDE | Does it use Claude-specific features that wouldn't work elsewhere? |
| FACT | Is anything stated as fact that is actually a guess? |
| CLEAR | Is anything unclear enough that Aaron might misread it? |
| CONSIST | Are there internal contradictions between files? |

Pass = no issue. Flag = issue found, details in notes.

---

## File-by-File Audit

### architecture/sovereignty-principles.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Flag |

**Notes:** References "Float-Free Architecture documented in `sovereignty/`" but the actual path is `C:\twobirds\two-birds-portfolio\sovereignty\`. The reference works for humans who know the repo but an LLM following the path literally would look inside `hal-stack/sovereignty/` and find nothing. Minor — but should say `../../sovereignty/` or use the full repo-relative path.

### architecture/decapitation-checklist.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Pass | Pass |

**Notes:** States Claude Code L1→L2 swap takes "30 minutes" and Cursor costs "~US$20/mo." Neither is verified. These are reasonable estimates but presented without hedging. The header says "MEDIUM — L2/L3 swap times are estimates, not tested" which partially covers this, but the estimates in the body read like facts.

### architecture/layer-tags.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean. Simple vocabulary definition. No issues.

### architecture/overview.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean. Correctly layer-tags each component.

### architecture/principles.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Flag | Pass |

**Notes:** Principle #8 says "Static Over Dynamic — No Node frameworks." But the HAL Stack itself may use Node.js for voice layer scripts and utilities. The constraint applies to **products** (DCC, Clarity, etc.), not to **internal infrastructure**. This distinction isn't stated and Aaron might read it as "no Node anywhere." Should clarify: "Products ship as static. Internal tools can use whatever works."

### architecture/decisions/0001-folder-structure.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean.

### architecture/decisions/0002-sovereignty-four-layer-model.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Flag |

**Notes:** Same Float-Free path reference issue as sovereignty-principles.md. References "Float-Free Architecture (March 2026)" without linking to the actual document location.

### hal-stack/README.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Flag | Pass |

**Notes:** "Current State" table says Voice Layer status is "Research complete" and Context Bridge is "v0.1 shipped." The word "shipped" is misleading — these are documentation specifications, not deployed running systems. A reader unfamiliar with the project might think these are operational services. Should use "v0.1 documented" or "v0.1 specified."

### context-system/README.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean. Correctly describes layer-by-layer usage.

### context-system/context-export-template.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean template. No issues.

### context-system/context-index.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Flag | Flag |

**Notes:** Two issues.
1. Logo v1.1 entry says "needs rework per Aaron" as its status but the context-index also lists v1.0 as "Superseded by v1.1." If v1.1 needs rework, is v1.0 still superseded? Ambiguous.
2. The "Unrecovered Contexts" section lists "Early DCC module builds (Sessions 1-8)" but SESSION-STATE.md doesn't number sessions before Session 10. Where did sessions 1-8 happen? Were they Claude Web only? Should state that explicitly.

### context-system/context-loader-prompt.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Pass | Pass |

**Notes:** States DCC has "29 modules" in the prompt block. SESSION-STATE.md says "27 numbered modules + Module 2.5 + Visual AI bonus." These are consistent (27 + 1 + 1 = 29) but the loader prompt doesn't explain the count. Also, DCC has grown since — modules 25-27 were added in recent commits. The actual count may now be higher. The loader prompt should probably say "29+ modules" or just "digital literacy programme for Canadian seniors" without a specific count that will go stale.

### context-system/retroactive-catchup-plan.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Honestly flags its own L1 dependency. Clean.

### voice-layer/README.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean.

### voice-layer/component-breakdown.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean. Swap interfaces are properly vendor-agnostic.

### voice-layer/four-layer-options.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Flag | Pass |

**Notes:** Two issues.
1. **Pricing presented as fact:** Whisper API at US$0.006/min, TTS at US$0.015/1K chars, Deepgram at 200 min/mo free, etc. Header says "may be outdated" but tables present numbers without caveats. Someone reading the table alone would assume these are current.
2. **Whisper.cpp performance:** "5-15 seconds per utterance on Celeron" is an estimate from benchmark extrapolation, not a measurement on Aaron's hardware. Presented as a data point in a comparison table where other entries (cloud APIs) are based on published specs. The comparison is apples to oranges.

### voice-layer/aaron-signup-checklist.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Pass | Pass |

**Notes:** States "CA$5 covers ~800 minutes of transcription" — math: CA$5 ÷ US$0.006/min ≈ 833 min at current exchange rates, but only if the price hasn't changed. Also, the CA$ to US$ conversion isn't shown. The claim is approximately right but the precision implies more certainty than exists.

### voice-layer/build-sprint-plan.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Pass | Pass |

**Notes:** Sub-Sprint 1 assumes `node-record-lpcm16` or `sox` work on Windows. Neither has been tested on EZbook. The plan states microphone and speakers are prerequisites and marks them as checked ([x]) — but this was not verified during the overnight sprint. The machine profile doesn't include audio hardware info.

### voice-layer/sovereignty-notes.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Pass | Pass |

**Notes:** Performance comparison table ("L1 Experience" vs "L4 Experience") presents specific latency numbers (0.5s, 5-15s, 30s+) as data points. These are estimates. The header says "MEDIUM confidence" but a table with specific numbers reads as measured data. Should add a row header like "estimated latency" or a footnote.

### machine-profile/README.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean.

### machine-profile/claude-code-identifier.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Flag | Pass | Pass | Pass |

**Notes:** The title says "Claude Code Machine Identification" and the doc focuses on Claude Code session starts. But per sovereignty principles, this should work with any tool. The doc does say "Claude Code (or any tool)" in the body, but the title and filename are Claude-specific. Minor — the filename `claude-code-identifier.md` could be `machine-identifier.md`.

### machine-profile/machines.json
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Flag | Pass |

**Notes:** Two issues.
1. The `"layer"` field on each machine is set to `"L1"` (except desktop at `"L4"`). It's unclear what this means — is it the sovereignty layer the machine operates at, or the layer it's designed for? Machines don't have sovereignty layers; components do. This field needs a definition or should be removed.
2. Multiple fields are "unknown" (Claude Code version, git version on EZbook; hostname on i5 Lenovo; most Pentium specs). These are acknowledged gaps but they mean the machine identification system can't actually identify 2 of 4 machines right now.

### machine-profile/register-machine.ps1
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean. L4-native by design.

### backlog/epics.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Flag | Pass |

**Notes:** Uses "SHIPPED" for items that are documentation specs, not deployed systems. E1, E2, E4 say "v0.1 SHIPPED" but nothing was deployed to users. Recommend "DOCUMENTED" or "SPECIFIED."

### backlog/stories.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Flag | Pass |

**Notes:** All stories show status "Pending" without distinguishing "ready to start," "blocked," and "not yet defined." Stories with blockers show the blocker column, but a reader scanning the status column sees "Pending" everywhere and can't quickly tell what's actionable.

### backlog/evaluation-candidates.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Flag | Pass | Pass |

**Notes:** Aider described as "MIT license" — should verify current license. Tool feature claims (Ollama support, BYOK) are based on knowledge as of the training cutoff and may have changed.

### sessions/2026-04-09-overnight-sprint.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean. Sprint plan only.

### sessions/2026-04-09-overnight-sprint-RESULTS.md
| SOV | VENDOR | CLAUDE | FACT | CLEAR | CONSIST |
|-----|--------|--------|------|-------|---------|
| Pass | Pass | Pass | Pass | Pass | Pass |

**Notes:** Clean. Honestly flags its own uncertainties.

---

## Summary

| Metric | Count |
|--------|-------|
| Files audited | 27 |
| SOV contradictions | 0 |
| Vendor assumptions (should be agnostic) | 0 |
| Claude-specific features | 1 (minor — filename only) |
| Facts that are actually guesses | 7 |
| Clarity issues | 8 |
| Internal contradictions | 3 |
| **Total issues** | **19** |

### Severity Breakdown

| Severity | Count | Description |
|----------|-------|-------------|
| High | 0 | Nothing that would cause harm or waste significant time |
| Medium | 7 | Things that could mislead if not caught |
| Low | 12 | Naming, wording, minor inconsistencies |

---

## Top 5 Things Aaron Should Look at First

1. **"Shipped" terminology (MEDIUM)** — Epics and README say "shipped" for documentation that hasn't been deployed. Could confuse future readers or Aaron himself in 3 months. Quick fix: find-replace "SHIPPED" with "DOCUMENTED." Files: `backlog/epics.md`, `README.md`

2. **Voice layer pricing treated as fact (MEDIUM)** — Six specific prices in `four-layer-options.md` are presented in tables without per-cell caveats. If Aaron budgets based on these, he may be off. Fix: verify at platform.openai.com and deepgram.com before the voice build sprint. File: `voice-layer/four-layer-options.md`

3. **Principles.md "no Node frameworks" ambiguity (MEDIUM)** — Reads as "no Node anywhere" but should say "no Node in products." Internal tools (voice layer, register script) will likely use Node. Fix: add one clarifying sentence. File: `architecture/principles.md`

4. **Logo v1.1 status contradicts across files (MEDIUM)** — Context index says "superseded v1.0" but results say "needs rework." If Aaron reads only the index, he might think v1.1 is final. Fix: update context-index to say "v1.1 under review." File: `context-system/context-index.md`

5. **machines.json `layer` field undefined (LOW)** — Field exists on every machine entry but its meaning isn't documented. Does "L1" mean the machine runs L1 tools? All machines can run L4 tools too. Fix: define the field or remove it. File: `machine-profile/machines.json`

---

## Blind Spots in This Audit

1. I wrote the overnight files and I'm auditing them. I'm likely to miss errors in my own reasoning rather than in my formatting.
2. I cannot verify external claims (pricing, tool availability, hardware benchmarks).
3. I may have normalised my own writing style and missed clarity issues that would confuse Aaron specifically.
4. I don't know what Aaron's mental model looks like — the sovereignty framework may match it perfectly or may feel over-engineered. I can't assess that.
