<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:20 EST (Toronto)
Confidence: MEDIUM — architecture is sound, specific API details may be outdated
Known gaps: Haven't tested any of these on Aaron's hardware
-->

# Voice Layer — Component Breakdown

## Component 1: STT (Speech-to-Text)

**What it does:** Takes audio input from a microphone and produces a text string.

**Input:** Audio stream (microphone or WAV file)
**Output:** Plain text string

**"Headless" means:** The rest of the system doesn't know or care whether Whisper, Google, or a human transcriptionist produced the text. It's just a string.

**Swap interface:**
```
function transcribe(audioBuffer) → Promise<string>
```

Any STT engine that implements this interface works. No vendor-specific metadata required.

## Component 2: Intent Parser

**What it does:** Takes a plain text string and extracts the user's intent + parameters.

**Input:** Plain text string (e.g., "run next sprint on the DCC repo")
**Output:** Structured intent object:
```json
{ "action": "sprint", "target": "next", "repo": "digital-confidence" }
```

**"Headless" means:** This could be an LLM (Claude, GPT, Llama), a regex-based parser, or a keyword matcher. The command router doesn't care how the intent was parsed.

**Swap interface:**
```
function parseIntent(text) → { action: string, args: object }
```

**L4 simplest version:** A keyword map. "next sprint" → sprint action. "retro" → retro action. No LLM needed for the 10-20 commands Aaron actually uses.

## Component 3: Command Router

**What it does:** Takes a structured intent and executes the corresponding action.

**Input:** Intent object
**Output:** Result text string (for TTS to speak back)

**"Headless" means:** The router is a lookup table. Intent → function call. It doesn't know about LLMs, voice, or any specific tool. It just runs commands.

**Swap interface:**
```
function routeCommand(intent) → Promise<string>
```

**This component is inherently L4-native.** It's just a switch statement or lookup table. No cloud dependency possible or needed.

## Component 4: TTS (Text-to-Speech)

**What it does:** Takes a text string and speaks it aloud.

**Input:** Plain text string
**Output:** Audio playback (speaker)

**"Headless" means:** The rest of the system produces text. Whether that text is spoken by the OS built-in TTS, a cloud service, or a local neural TTS model is irrelevant to the pipeline.

**Swap interface:**
```
function speak(text) → void
```

**L4 simplest version:** Windows built-in `System.Speech.Synthesis` (PowerShell) or `espeak`. Free, local, no internet. Quality is robotic but functional.
