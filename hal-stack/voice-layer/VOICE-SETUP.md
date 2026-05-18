# Two-Way Voice Setup — HAL Stack
**Built:** 2026-05-17 | **Sprint:** S-VOICE-TWO-WAY

## Current state (what works right now)

### Voice IN → Claude Code
Type `/voice` in Claude Code CLI. Hold spacebar while speaking. Release to transcribe.
This is Boris Cherny's method — built into Claude Code, no extra install.

**For reliable dictation everywhere (replacing Wispr Flow):**
See the Whispering / Speaches section below. Local Whisper, no subscription, no limits.

### Voice OUT ← Claude Code (fallback, works now)
PowerShell TTS — no API key, no install, available on every Windows machine:
```powershell
# Read any text aloud
.\hal-stack\voice-layer\tts-speak.ps1 "Claude says this"

# Or pipe a SESSION-STATE section aloud
Get-Content SESSION-STATE.md | Select-Object -First 20 | .\hal-stack\voice-layer\tts-speak.ps1
```
Quality: passable. Not Jarvis. Gets the job done while VoiceMode full setup is pending.

---

## Full two-way: VoiceMode MCP (installed, needs OpenAI key to activate)

VoiceMode MCP is installed at user scope. When Aaron's OpenAI API key is set,
full two-way voice activates automatically — local Whisper STT + OpenAI TTS.

**To activate:**
```powershell
# Set once in PowerShell profile or system env
$env:OPENAI_API_KEY = "sk-..."
# Then in Claude Code: just talk. VoiceMode handles both directions.
```

**Without OpenAI key (fully local path — more setup):**
VoiceMode supports local Kokoro TTS + Speaches/faster-whisper STT.
See: https://github.com/mbailey/voicemode/blob/master/docs/tutorials/getting-started.md

---

## Replacing Wispr Flow — open source, free, sovereign

Wispr Flow free tier has a weekly limit. Local alternatives:

| Tool | Platform | STT Engine | Cost | Notes |
|------|----------|-----------|------|-------|
| **Whispering** | Win/Mac/Linux | Whisper.cpp local | Free forever | Best Wispr Flow replacement. System-wide. Open source. |
| **OpenWhispr** | Win/Mac/Linux | Whisper + Parakeet | Free | System tray app, no GPU needed |
| **TypeWhisper** | Win/Mac | whisper.cpp models | Free | Windows-native feel |
| **Speaches** | Win/Mac/Linux | faster-whisper | Free | Server mode — feeds VoiceMode too |

**Recommended:** [Whispering](https://github.com/braden-w/whispering) — closest to Wispr Flow UX,
open source (MIT), runs local Whisper models, system-wide hotkey, no account, no limits.

Install: Download release from GitHub → runs immediately, no Python/GPU needed.

---

## Mobile path (Aaron install required)

Claude Code Remote Control (official) doesn't support voice over SSH.
**Happy Coder** fills the gap — open source companion app that adds voice to remote sessions.

- iOS/Android app
- Connects to Claude Code Remote session
- Adds voice input on top
- GitHub: search "Happy Coder Claude Code" or via the Claude Code mobile docs

Filed as Aaron P1 action in Notion.

---

## Architecture summary

```
Voice IN (desktop):    /voice in Claude Code CLI  →  transcribed text → Claude
Voice IN (system-wide): Whispering (local Whisper) → any app including Claude Code
Voice OUT (now):       tts-speak.ps1              ← Claude response
Voice OUT (full):      VoiceMode MCP              ← Claude (needs OPENAI_API_KEY)
Mobile:               Happy Coder app             ↔ Claude Code Remote
```

## What unlocks what

| Action | Unlocks |
|--------|---------|
| Set OPENAI_API_KEY env var | Full VoiceMode two-way (best quality) |
| Install Whispering | Sovereign STT, replaces Wispr Flow, no limits |
| Install Happy Coder on phone | Mobile voice → Claude Code |
