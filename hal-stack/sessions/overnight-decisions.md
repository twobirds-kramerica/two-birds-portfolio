<!--
STATUS: v0.1 — DECISION LOG — NEEDS AARON RATIFICATION
Created: 2026-04-10 20:58 EST (Toronto)
Purpose: Every autonomous judgment call from the overnight sprint in one place
-->

# Overnight Sprint — Autonomous Decision Log

Every judgment call made without Aaron's input. Numbered for easy reference.

---

1. **Named the sovereignty model "four layers" (L1-L4) instead of three**
   - Why: The existing Float-Free architecture had three backup layers. Added a fourth (L4 = fully local) because Aaron's stated goal of running on his own hardware is qualitatively different from hosting on someone else's VPS.
   - Alternative: Keep three layers (merge L3 and L4 into "open source").
   - Confidence: HIGH — the distinction between "open source on rented infra" and "open source on your own box" is meaningful.
   - Aaron should: **Ratify.** If three layers feel cleaner, say so.

2. **Defined "Headless Claude" as a named concept**
   - Why: Aaron has said versions of "Claude is replaceable" in multiple sessions. Giving it a name makes it referenceable.
   - Alternative: Don't name it, just state the principle each time.
   - Confidence: HIGH — naming concepts makes them stick.
   - Aaron should: **Ratify.** Check if the name resonates or feels forced.

3. **Used Architecture Decision Records (ADRs) format**
   - Why: ADRs are a lightweight industry standard for recording architectural decisions with context. Keeps "why we decided this" alongside "what we decided."
   - Alternative: Just put decisions in a flat list or in the README.
   - Confidence: HIGH — ADRs are well-suited to Aaron's need to revisit decisions months later.
   - Aaron should: **Ignore** — low-stakes format choice.

4. **Prioritised design principles in a specific order (sovereignty > cost > automation > voice > ...)**
   - Why: When two principles conflict, you need a tiebreaker. Sovereignty was placed first because Aaron has repeatedly stated it matters more than convenience.
   - Alternative: Alphabetical, equal weighting, or a different ordering.
   - Confidence: MEDIUM — the order reflects my reading of Aaron's priorities, but he hasn't explicitly ranked them.
   - Aaron should: **Challenge** if the order feels wrong. Especially: is voice-first really #4?

5. **Recommended OpenAI Whisper API as the L1 starting point for speech-to-text**
   - Why: Best quality, lowest cost per minute, simplest setup among cloud STT options. And the underlying model (Whisper) is open-source, so the L4 path is the same model running locally.
   - Alternative: Google Cloud Speech-to-Text (has a free tier but more complex setup), Deepgram (free tier available).
   - Confidence: MEDIUM — recommendation is sound but pricing was not verified live.
   - Aaron should: **Ratify** after checking current pricing at platform.openai.com/pricing.

6. **Recommended starting TTS with Windows built-in (robotic voice) instead of a cloud service**
   - Why: Zero setup, zero cost, zero internet dependency. For "sprint complete, three items shipped" type responses, natural voice quality doesn't matter.
   - Alternative: Start with OpenAI TTS or ElevenLabs for natural voice from day one.
   - Confidence: HIGH — the robotic voice is functional and sovereign (L4-native). Upgrade later if it annoys Aaron.
   - Aaron should: **Ratify** or override if the robotic voice would prevent him from using the system.

7. **Recommended building the L4 keyword map BEFORE any LLM-based intent parsing**
   - Why: Aaron uses maybe 10-20 commands. A JSON file with string matching handles that perfectly. Adding an LLM for intent parsing is over-engineering until the command set grows.
   - Alternative: Start with LLM parsing from day one (more flexible, handles natural phrasing).
   - Confidence: HIGH — simplicity wins for a prototype.
   - Aaron should: **Ignore** — this is a sequencing choice that can be revised during the build sprint.

8. **Set the voice build sprint at 2.5 hours across 4 sub-sprints**
   - Why: Each sub-sprint produces a testable checkpoint. If time runs out, whatever's done is usable.
   - Alternative: One big build session, or a more conservative multi-session plan.
   - Confidence: MEDIUM — 2.5 hours is optimistic. Assumes no Node.js library compatibility issues on Windows, which wasn't tested.
   - Aaron should: **Ignore** — the plan will adapt to reality during execution.

9. **Auto-detected EZbook specs and wrote them to machines.json without Aaron's confirmation**
   - Why: PowerShell system calls return factual hardware data. No judgment involved.
   - Alternative: Wait for Aaron to verify specs manually.
   - Confidence: HIGH for detected specs. LOW for the fields marked "unknown" (Claude Code version, git version).
   - Aaron should: **Ignore** — verify the unknowns when convenient.

10. **Flagged logo v1.1 as "NEEDS REWORK" based on Aaron's earlier comment**
    - Why: Aaron said it's "not quite the spec" in a prior exchange this session. Marking it as a blocker for LinkedIn upload is the conservative choice.
    - Alternative: Ship v1.1 as-is and iterate later.
    - Confidence: HIGH — Aaron's own words.
    - Aaron should: **Ratify** by reviewing the render and providing specific feedback.

11. **Added Aider and Ollama to evaluation candidates and rated Aider as HIGH priority**
    - Why: Aider is the strongest L2/L4 fallback for Claude Code. If Claude becomes unavailable or unaffordable, Aider + Ollama is the best-documented local alternative for AI-assisted coding.
    - Alternative: Don't evaluate fallbacks until there's an actual problem.
    - Confidence: MEDIUM — Aider's quality is good but I haven't verified its current Windows support or Ollama integration.
    - Aaron should: **Challenge** if evaluating fallbacks feels premature. The sovereignty model says document L4 paths but doesn't require testing them immediately.

12. **Listed nine epics and chose their priorities (P1/P2/P3)**
    - Why: Grouping work into epics makes it scannable. Priorities based on: P1 = enables other work, P2 = important but not blocking, P3 = nice to have.
    - Alternative: Flat task list, or different priority groupings.
    - Confidence: MEDIUM — priority ranking is my judgment based on session history.
    - Aaron should: **Challenge** if priorities feel wrong. Key question: should voice (P2) be higher or lower than branding (P2)?

13. **Created the context-loader-prompt as a vendor-agnostic prompt block**
    - Why: Aaron might use GPT, Gemini, or a local model for research. The prompt orients any LLM without Claude-specific features.
    - Alternative: Write Claude-specific prompt with system prompts and tool_use. Faster for Claude, useless elsewhere.
    - Confidence: HIGH — vendor-agnostic is the right call per sovereignty principles.
    - Aaron should: **Ignore** — this directly follows from the sovereignty framework.

14. **Estimated that CA$5 top-up covers ~800 minutes of Whisper transcription**
    - Why: Quick math: US$0.006/min × 800 min = US$4.80. At current exchange rates, CA$5 ≈ US$3.60-3.70, which is actually closer to ~600 minutes. The estimate is generous.
    - Alternative: State "several hundred minutes" without a specific number.
    - Confidence: LOW — exchange rate assumed, pricing unverified. The number is wrong. Should be ~600 min, not 800.
    - Aaron should: **Note** that this estimate is optimistic. Check actual pricing before relying on it.
