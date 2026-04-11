<!--
STATUS: v0.1 — REVIEW AID — NOT A DELIVERABLE
Created: 2026-04-10 20:49 EST (Toronto)
Purpose: Help Aaron review the overnight sprint output faster
-->

# Overnight Sprint Review Guide

Read this on your phone while walking. Five sentences per phase, plain English.

**NO CRITICAL ISSUES FOUND** — nothing that would waste your time or break things if you read it tomorrow instead of today. The overnight output is conservative documentation, not deployed code. Nothing runs, nothing is live, nothing will bite you.

---

## Phase 0 — Sovereignty Framework (3 files)

This phase created the "four-layer model" — a rule that says every tool you use (Claude, GitHub, Formspree, everything) must have a documented escape plan. Layer 1 is the commercial tool you use today. Layer 4 is a version that runs on your own hardware with no internet. The key file is `sovereignty-principles.md` — it defines "Headless Claude," which means treating Claude as a replaceable part, not a permanent dependency. It also includes a "decapitation checklist" template with Claude Code itself as the worked example (verdict: low lock-in risk because all your work lives in git). **You need to decide:** Does this four-layer model match how you think about vendor risk, or is it over-engineered for where you are right now?

## Phase 1 — HAL Scaffolding (6 files)

This phase reorganised the `hal-stack/` folder and wrote foundational docs: an architecture overview, eight design principles, and two Architecture Decision Records (formal "here's what we decided and why" documents). The principles are pulled from things you've said across sessions — sovereignty, low-cost, voice-first, Canadian data residency, static HTML only, plain language. The README was rewritten to reflect the new structure. **You need to decide:** Are these eight principles correct and in the right priority order? The current order says sovereignty beats everything, then cost, then automation.

## Phase 2 — Context Bridge System (5 files)

This phase built a system so your next Claude session (or GPT, or Gemini, or a local AI, or just you reading files) can pick up where the last one left off. It's all markdown files — no code, no database. There's a master index of past sessions, a template you fill out after each session, and a "loader prompt" you can paste into any AI chat to orient it. There's also a plan for recovering context from your old Claude.ai web sessions (this requires you to check if Claude.ai offers a data export — it might not). **You need to decide:** Do you want to add "fill out context export template" to your post-session workflow, or is that too much overhead?

## Phase 3 — Voice Layer Audit (6 files)

This phase researched how to give you a voice interface — speak commands, hear responses — but did NOT build anything. It breaks the voice system into four swappable parts (speech-to-text, intent parsing, command routing, text-to-speech) and evaluates options at all four sovereignty layers. The main recommendation is: create one OpenAI account (CA$5), use their speech-to-text API, and use Windows' built-in robot voice for responses — total cost about CA$0.50 per month. The keyword command map (understanding "next sprint" or "retro") needs no AI at all — it's just string matching. **You need to decide:** Is voice a priority right now, or should this stay parked? The research is done either way.

## Phase 4 — Machine Profile System (4 files)

This phase created a registry of your four machines (EZbook, i5 Lenovo, Pentium Silver, future desktop) as a JSON file. EZbook's specs were auto-detected: Celeron 5205U, 12GB RAM, 512GB SSD. There's a PowerShell script to register new machines automatically. The idea is that any Claude Code session can check which machine it's running on by matching the hostname. **You need to decide:** The Pentium Silver and i5 Lenovo have incomplete entries (missing hostnames and some specs) — worth filling in next time you're on those machines, but not urgent.

## Phase 5 — Backlog Consolidation (3 files)

This phase organised all your pending work into nine epics (big themes) and 22 stories (specific tasks), each tagged with sovereignty layer and priority. It also evaluated six tools you'd flagged for possible use (notebooklm-py, Aider, Ollama, Remotion, etc.). The most useful finding: Aider (open-source AI coding tool) is the highest-value evaluation candidate because it's your best fallback if Claude Code ever becomes unavailable. Logo v1.1 is flagged as "needs rework" — do not upload to LinkedIn until you've reviewed it. **You need to decide:** Are the priorities right? Currently it's sovereignty framework > voice > branding > content freshness > quota optimisation.

## Phase 6 — Session Wrap (2 files)

This phase created the sprint results summary and your morning briefing (which you're reading now, essentially). The top three morning actions were: create OpenAI account, review logo v1.1, and skim the sovereignty principles doc. Nothing was skipped — all seven phases completed. **You need to decide:** Nothing from this phase. It's just the receipt.
