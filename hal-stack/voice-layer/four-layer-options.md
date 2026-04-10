<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:20 EST (Toronto)
Confidence: MEDIUM — pricing/features based on public docs as of April 2026, may be outdated
Known gaps: Local model performance on EZbook (Celeron, 12GB) untested. Whisper.cpp may be very slow.
-->

# Voice Layer — Four-Layer Options

## STT (Speech-to-Text)

| Layer | Option | Cost | Setup Time | Quality | Decapitation Cost |
|-------|--------|------|-----------|---------|-------------------|
| **L1** | OpenAI Whisper API | ~US$0.006/min | 15 min (API key + script) | Excellent | L1→L2: 10 min |
| **L1 alt** | Google Cloud Speech-to-Text | Free: 60 min/mo, then US$0.006/15s | 30 min (GCP account) | Excellent | — |
| **L2** | Deepgram | Free: 200 min/mo | 20 min | Very good | L1→L2: 15 min |
| **L2 alt** | AssemblyAI | Free tier available | 20 min | Very good | — |
| **L3** | Whisper (open-source) on VPS | VPS cost (~US$5-10/mo) | 2-3 hours | Excellent (same as L1) | L1→L3: 3 hours |
| **L4** | Whisper.cpp on local machine | Free | 1-2 hours | Good (depends on hardware) | L1→L4: 2 hours |

**Recommendation:** Start with L1 (OpenAI Whisper API). Free tier doesn't exist but cost is negligible for Aaron's usage (~CA$0.50/month). Whisper.cpp is the L4 path — same model, runs locally, but will be slow on EZbook's Celeron. Desktop needed for comfortable L4.

## Intent Parser

| Layer | Option | Cost | Setup Time | Quality | Decapitation Cost |
|-------|--------|------|-----------|---------|-------------------|
| **L1** | Claude API (Haiku) | ~US$0.001/request | 10 min | Excellent | L1→L2: 10 min |
| **L1 alt** | OpenAI GPT-4o-mini | ~US$0.001/request | 10 min | Excellent | — |
| **L2** | Google Gemini Flash | Free tier: 15 RPM | 15 min | Very good | L1→L2: 15 min |
| **L3** | Ollama + Llama on VPS | VPS cost | 1-2 hours | Good | L1→L3: 2 hours |
| **L4** | Keyword map (no LLM) | Free | 30 min | Basic but sufficient | L1→L4: 30 min |
| **L4 alt** | Ollama + small local model | Free | 1-2 hours | Moderate | — |

**Recommendation:** Start with L1 (Claude Haiku or GPT-4o-mini — whichever Aaron already has an API key for). But build the L4 keyword map FIRST as the foundation. The LLM is an enhancement, not a requirement. Aaron uses maybe 10-20 commands — a keyword map handles that fine.

## Command Router

| Layer | Option | Cost | Setup Time | Quality | Notes |
|-------|--------|------|-----------|---------|-------|
| **L4** | PowerShell/Bash script | Free | 1-2 hours | Perfect | This component IS L4. No cloud needed. |

**No other layers needed.** The command router is a local script that maps intents to actions. It's the most sovereign component by nature.

## TTS (Text-to-Speech)

| Layer | Option | Cost | Setup Time | Quality | Decapitation Cost |
|-------|--------|------|-----------|---------|-------------------|
| **L1** | OpenAI TTS API | ~US$0.015/1K chars | 15 min | Excellent (natural voice) | L1→L2: 10 min |
| **L1 alt** | Google Cloud TTS | Free: 4M chars/mo | 30 min | Excellent | — |
| **L2** | ElevenLabs | Free: 10K chars/mo | 15 min | Best quality | L1→L2: 15 min |
| **L3** | Piper TTS on VPS | VPS cost | 2-3 hours | Good (neural, natural) | L1→L3: 3 hours |
| **L4** | Windows SAPI (built-in) | Free | 5 min | Robotic but functional | L1→L4: 5 min |
| **L4 alt** | Piper TTS local | Free | 1-2 hours | Good | — |

**Recommendation:** Start with L4 (Windows built-in TTS). It's already installed, requires zero setup, and works offline. Upgrade to L1 or Piper only if the robotic voice bothers Aaron. For "retro complete, three items shipped" type responses, robotic is fine.

## Summary: Fastest Path to Working Voice

| Component | Start With | Cost | Why |
|-----------|-----------|------|-----|
| STT | OpenAI Whisper API (L1) | ~CA$0.50/mo | Best quality, cheapest, simplest |
| Intent | Keyword map (L4) | Free | 10-20 commands, no LLM needed |
| Router | PowerShell script (L4) | Free | Inherently local |
| TTS | Windows built-in (L4) | Free | Already installed |

**Total monthly cost: ~CA$0.50** (just the Whisper API calls)
**Total setup time: ~3 hours** for a working loop
