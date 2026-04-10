<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:20 EST (Toronto)
Confidence: MEDIUM — plan is sound, time estimates are optimistic
Known gaps: Node.js audio input library compatibility on Windows untested
-->

# Voice Layer — First Build Sprint

After Aaron creates the OpenAI Platform account and has an API key, this is the build plan. Each sub-sprint produces something testable.

## Pre-requisites

- [x] Node.js installed (v24.14.1 on EZbook)
- [x] Git installed
- [ ] OpenAI API key in `.env` file (BLOCKER: Aaron)
- [x] Microphone on EZbook (built-in)
- [x] Speakers on EZbook (built-in)

## Sub-Sprint 1: Working STT Loop (45 min)

**Goal:** Speak into microphone → see text on screen.

1. Create `hal-stack/voice-layer/src/` directory
2. Write a Node.js script that:
   - Records audio from microphone (use `node-record-lpcm16` or `sox`)
   - Sends to OpenAI Whisper API
   - Prints transcribed text to console
3. Test: say "Hello, this is Aaron" → see text appear
4. **Done when:** Aaron can speak and see his words as text

**Sovereignty note:** This sub-sprint is L1 (Whisper API). The recording part is L4-native (local mic). The API call is the only L1 dependency.

## Sub-Sprint 2: Keyword Command Map (30 min)

**Goal:** Speak a command → see it recognised.

1. Write a keyword map in plain JSON:
   ```json
   {
     "next sprint": { "action": "sprint", "args": ["next"] },
     "retro": { "action": "retro" },
     "state": { "action": "state" },
     "dashboard": { "action": "dashboard" }
   }
   ```
2. Match STT output against keywords (fuzzy match — "run next sprint" contains "next sprint")
3. Print matched command to console
4. **Done when:** Saying "next sprint" prints `{ action: "sprint", args: ["next"] }`

**Sovereignty note:** This sub-sprint is L4-native. No cloud dependency. Just a JSON file and string matching.

## Sub-Sprint 3: Command Router + TTS Response (45 min)

**Goal:** Speak a command → hear a response.

1. Wire command map to actual actions:
   - `retro` → read `logs/RETRO.md`, extract summary
   - `state` → read `SESSION-STATE.md`, extract top 3 actions
   - `sprint` → read `NEXT-SPRINT-QUEUE.md`, extract top 3 items
2. Pipe result text to Windows TTS:
   ```powershell
   Add-Type -AssemblyName System.Speech
   $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
   $synth.Speak("Sprint complete. Three items shipped.")
   ```
3. **Done when:** Saying "retro" causes HAL to read back the retro summary aloud

**Sovereignty note:** TTS is L4-native (Windows built-in). Command routing is L4-native. Only STT remains L1.

## Sub-Sprint 4: Continuous Listen Loop (30 min)

**Goal:** HAL listens continuously, responds to wake word or push-to-talk.

1. Implement push-to-talk (hold spacebar to record, release to process)
2. Or: continuous listen with keyword detection ("Hey HAL" or just detect silence gaps)
3. Wire everything together: listen → STT → parse → route → TTS → listen again
4. **Done when:** Aaron can have a back-and-forth with HAL without touching the keyboard

## Total: ~2.5 hours for a working voice loop

That's aggressive but achievable if pre-requisites are met. Each sub-sprint is independently testable — if time runs out, whatever was completed last is a working checkpoint.
