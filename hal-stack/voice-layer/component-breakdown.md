<!--
STATUS: v0.2 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:20 EST (Toronto)
Updated: 2026-04-11 01:50 EST (Toronto)
Confidence: MEDIUM — architecture is sound, specific API details may be outdated
Known gaps: Haven't tested any of these on Aaron's hardware. Thinking Layer is conceptual.
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

## Component 2: Thinking Layer (NEW — Session 14)

**What it does:** Sits between STT and Command Routing. This is NOT just intent parsing — it's a conversational shepherd that helps Aaron refine his thoughts before routing to execution.

**Input:** Raw transcription text (e.g., "I'm thinking maybe we should... uh, what if we did something with the DCC feedback system, like, make it better for Brenda?")
**Output:** Either a clarified intent for the command router, OR a clarifying question back to Aaron via TTS.

**What makes it different from a simple intent parser:**
- It can **ask questions back.** "When you say 'make it better for Brenda,' do you mean the onboarding flow or the feedback form?"
- It can **refuse.** "That sounds like scope creep. The backlog says the next priority is X. Want to override?"
- It can **suggest.** "Based on the backlog, the most impactful thing right now is Y. Want to do that instead?"
- It can **hold context** across a conversation. Aaron says three fragmented thoughts; the Thinking Layer synthesises them into one coherent prompt.

**"Headless" means:** Any LLM that can hold a short conversation. Claude, GPT, Gemini, or a capable local model. The key requirement is conversational ability, not just classification.

**Swap interface:**
```
function think(rawText, conversationHistory) → {
  type: "command" | "question" | "suggestion" | "refusal",
  payload: string | { action: string, args: object }
}
```

**L1:** Claude Haiku or GPT-4o-mini — fast, cheap, conversational.
**L4:** Ollama + Llama 3 or Phi-3 — needs 8GB+ RAM for decent quality. Will be slower but functional for short conversations.

**Pipeline with Thinking Layer:**
```
[Mic] → STT → raw text
              ↓
         Thinking Layer ←→ Aaron (back-and-forth via TTS)
              ↓
         Clarified intent
              ↓
         Command Router → execute → TTS response
```

**Why this exists:** Aaron's raw speech is often fragmented, exploratory, and thinking-out-loud. A simple keyword matcher would miss the intent. The Thinking Layer is a thought partner, not a transcription tool.

## Component 3: Intent Parser (Simple — L4 Fallback)

**What it does:** Takes a plain text string and extracts the user's intent + parameters. This is the L4 fallback for when no Thinking Layer LLM is available.

**Input:** Plain text string (e.g., "run next sprint on the DCC repo")
**Output:** Structured intent object:
```json
{ "action": "sprint", "target": "next", "repo": "digital-confidence" }
```

**"Headless" means:** This could be a keyword matcher or regex-based parser. No LLM needed.

**Swap interface:**
```
function parseIntent(text) → { action: string, args: object }
```

**L4 simplest version:** A keyword map. "next sprint" → sprint action. "retro" → retro action. No LLM needed for the 10-20 commands Aaron actually uses.

**Relationship to Thinking Layer:** The Intent Parser is the fallback when the Thinking Layer is unavailable. If Aaron's speech is clear and matches a known command, it routes directly. If not, it says "I didn't understand that" via TTS.

## Component 4: Command Router

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
