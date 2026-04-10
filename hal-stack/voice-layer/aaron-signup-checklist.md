<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:20 EST (Toronto)
Confidence: MEDIUM — signup processes change, verify URLs before creating accounts
Known gaps: Whether Aaron already has an OpenAI account (he might from ChatGPT usage)
-->

# Voice Layer — Aaron's Signup Checklist

Minimum accounts needed to unshackle voice. Ranked by unshackle-value (how much capability each account unlocks).

## Priority 1: OpenAI Platform Account (if not already exists)

**Why:** Whisper API for STT is the fastest path to voice input. Also unlocks GPT-4o-mini as an L2 intent parser.

**What to do:**
1. Go to platform.openai.com (NOT chatgpt.com — different account system)
2. Create account or log in
3. Add CA$5 in credits (minimum top-up, lasts months at Aaron's usage level)
4. Generate an API key → save to a .env file locally (NEVER commit to git)

**Free tier:** No free tier for Whisper API. But CA$5 covers ~800 minutes of transcription.
**Lock-in risk:** LOW — Whisper model is open-source. The API is just a convenience. L4 fallback is Whisper.cpp local.
**L4 fallback:** Whisper.cpp on desktop. Same model, runs locally.

**Unshackle value:** HIGH — unlocks STT + L2 intent parsing in one signup.

## Priority 2: No Additional Signups Needed

Everything else can be built with what Aaron already has:

- **Claude API:** Aaron has Claude Pro. Haiku API may be available through the existing plan or with minimal additional setup.
- **Windows TTS:** Already installed. Zero signup.
- **Command router:** Local script. Zero signup.
- **Git, Node.js, PowerShell:** Already installed.

## Optional (Not Needed for First Build)

### Deepgram (L2 STT backup)
- Free: 200 min/month
- Sign up at deepgram.com
- **When:** Only if OpenAI Whisper API goes down or Aaron wants a backup
- **Lock-in risk:** LOW

### ElevenLabs (L1 TTS upgrade)
- Free: 10K chars/month
- Sign up at elevenlabs.io
- **When:** Only if Aaron wants natural-sounding voice instead of Windows TTS
- **Lock-in risk:** LOW — L4 fallback is Piper or Windows SAPI

## Summary

| Account | Priority | Cost | Minutes to Create |
|---------|----------|------|-------------------|
| OpenAI Platform | **#1 — Do This First** | CA$5 top-up | 10 minutes |
| Everything else | Not needed yet | Free | 0 minutes |

**Aaron wakes up knowing:** Create ONE account (OpenAI Platform), add CA$5, save the API key. That's it. Everything else is already installed or can be built with local tools.
