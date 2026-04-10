<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:20 EST (Toronto)
Confidence: MEDIUM — assessments based on public benchmarks, not tested on Aaron's hardware
Known gaps: Whisper.cpp performance on Celeron 5205U unknown. Piper TTS quality on Windows untested.
-->

# Voice Layer — Sovereignty Notes

Honest assessment of what's easy and what's hard to make fully sovereign (L4).

## Easy to Make L4

### Command Router
Already L4 by nature. It's a local script that maps commands to actions. No cloud dependency exists or could exist. This is the most sovereign component.

### TTS (Text-to-Speech)
Windows has built-in TTS (`System.Speech.Synthesis`). It's robotic but it works. Zero setup, zero cost, zero internet. If Aaron wants better quality, Piper TTS is open-source and runs locally with good neural voices. Piper needs ~500MB of disk and minimal CPU.

**L4 difficulty: TRIVIAL**

### Intent Parser (for limited commands)
Aaron uses maybe 10-20 voice commands. A keyword map handles this perfectly at L4. No LLM needed. "Next sprint" → sprint action. "Retro" → retro action. A JSON file and `String.includes()`.

For complex natural language ("What was the last thing I changed in the DCC repo last Tuesday?"), an LLM is needed. But that's an enhancement, not a requirement for the core voice loop.

**L4 difficulty: TRIVIAL for commands, HARD for natural language**

## Hard to Make L4

### STT (Speech-to-Text)
This is the sovereignty bottleneck. Here's why:

**Whisper.cpp exists and works.** The model is open-source, MIT-licensed, runs locally. No lock-in risk.

**But it's slow on weak hardware.** Whisper "base" model on a Celeron with no GPU will take 5-15 seconds to transcribe a 5-second utterance. That's awkward for a voice loop. The "tiny" model is faster but less accurate.

**The i5 Lenovo is marginally better.** Still no GPU, but the i5-6200U is ~2x faster than the Celeron for this workload. Expect 3-8 seconds for a short utterance.

**The future desktop fixes this.** A modern CPU (or any GPU) makes Whisper.cpp fast. This is the L4 endgame.

**L4 difficulty: MEDIUM — works but slow on current hardware. Desktop solves it.**

### Natural Language Intent Parsing
If Aaron wants to say "What's the status of the Career Coach?" and have HAL understand that means "read the product score for Career Coach from the QA framework," that requires an LLM.

Local LLMs (Ollama + Llama 3, Phi-3, etc.) work but:
- Need 8-16GB RAM minimum for decent models
- Slow on EZbook's Celeron (30+ seconds per response)
- The i5 is marginally better
- Desktop with 32GB+ RAM makes this comfortable

**L4 difficulty: HARD on current hardware. MEDIUM on desktop.**

## Honest Trade-Offs

| Scenario | L1 Experience | L4 Experience |
|----------|--------------|---------------|
| "Next sprint" | Instant (0.5s STT + 0.1s parse) | 5-15s STT wait, then instant parse |
| "What changed in DCC?" | Instant (0.5s STT + 1s LLM parse) | 5-15s STT + 30s+ local LLM |
| "Read me the retro" | Instant STT, natural TTS | 5-15s STT, robotic TTS |

**Verdict:** L4 is functional but sluggish on current hardware. The recommended path:
1. Start at L1 (Whisper API) — fast, cheap, works now
2. Build the L4 keyword map alongside it — no LLM needed for commands
3. Test Whisper.cpp on desktop when it arrives — if fast enough, drop STT to L4
4. Keep LLM intent parsing at L1 until desktop has enough RAM for local models

**The architecture never changes.** Only the implementation behind each interface swaps. That's the whole point of the sovereignty model.
