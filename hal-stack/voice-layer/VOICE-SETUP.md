# Two-Way Voice Setup — HAL Stack
**Built:** 2026-05-17 | **Updated:** 2026-05-18 | **Sprint:** S-VOICE-TWO-WAY + S-VOICE-KOKORO

## Current Architecture (as of 2026-05-18)

```
Voice IN:   /voice in Claude Code CLI (hold spacebar) → transcribed text → Claude
Voice OUT:  Claude Stop hook → stop-hook-tts.ps1 → Kokoro (local) → spoken audio
                                                  ↓ fallback if Kokoro not running
                                              Windows built-in TTS
Mobile IN:  Happy Coder app → Claude Code Remote (Aaron action — install on phone)
Mobile OUT: Not yet wired (Track 2 sprint)
```

**VoiceMode MCP note:** VoiceMode's `converse` tool does not work on Windows (requires Unix `fcntl` module). Removed from active architecture. Stop hook approach is the Windows-native replacement.

---

## Desktop Voice OUT — How to use

### Step 1: Start Kokoro TTS server (before Claude Code)
```powershell
C:\twobirds\tools\Kokoro-FastAPI\start-kokoro.ps1
```
Leave this terminal open. Server runs on http://localhost:8880. First start takes ~30s to load model.

### Step 2: Open Claude Code normally
The Stop hook fires automatically. When Claude finishes a response, it speaks.

**If Kokoro isn't running:** Hook falls back to Windows built-in TTS automatically. No crash.

---

## Fresh Machine Setup (cross-PC guide)

Run these once on any new Windows machine:

```powershell
# 1. Install ffmpeg
winget install --id Gyan.FFmpeg --silent --accept-package-agreements --accept-source-agreements

# 2. Install pyaudio (portaudio)
pip install pyaudio

# 3. Install eSpeak NG (phonemizer for Kokoro)
# Download: https://github.com/espeak-ng/espeak-ng/releases/download/1.52.0/espeak-ng.msi
# Then: Start-Process msiexec.exe -ArgumentList "/i espeak-ng.msi /quiet /norestart" -Wait

# 4. Clone Kokoro-FastAPI
git clone https://github.com/remsky/Kokoro-FastAPI.git C:\twobirds\tools\Kokoro-FastAPI

# 5. Set up Kokoro (model already in repo after first run — or re-download)
Set-Location C:\twobirds\tools\Kokoro-FastAPI
uv venv
uv pip install -e ".[cpu]"
# Model downloads automatically on first start (~327MB, one time)

# 6. The Stop hook is in two-birds-portfolio git — already committed.
# Just ensure settings.json has the hook (see below).
```

### Claude Code settings.json hook (C:\Users\<you>\.claude\settings.json)
The Stop hook must be present. Copy this block into settings.json:
```json
"hooks": {
  "Stop": [
    {
      "matcher": "",
      "hooks": [
        {
          "type": "command",
          "command": "powershell.exe -NonInteractive -File \"C:\\twobirds\\two-birds-portfolio\\hal-stack\\voice-layer\\stop-hook-tts.ps1\""
        }
      ]
    }
  ]
}
```

---

## Voice IN — Desktop

### Option A: Claude Code native (built-in, no install)
Type `/voice` in Claude Code CLI. Hold spacebar while speaking. Release to transcribe.
Quality: acceptable for most use. Dictation is slow — speak at 60-70% normal pace.

### Option B: Whispering (recommended — replaces Wispr Flow)
Open source, local Whisper models, system-wide hotkey, no account, no limits.
Install: https://github.com/braden-w/whispering — download release, runs immediately.

---

## Mobile

**Voice IN (mobile → Claude Code):** Happy Coder app — filed as P1 Aaron action in Notion.
**Voice OUT (Claude → mobile speaker):** Track 2 sprint — S-VOICE-CLOUD. Not yet built.

Track 2 design: VoiceMode Connect (`uvx voice-mode serve`) + Tailscale (free) for
remote access. Kokoro runs on desktop, audio streams to mobile. No cloud cost.

---

## Kokoro voices
Default voice: `af_sky` (female, clear, natural).
Other options: `af_bella`, `af_nova`, `am_adam` (male). Change in stop-hook-tts.ps1 line ~26.

## TTS character limit
Hook trims responses to 800 chars to avoid reading out long code blocks.
Adjust the limit in stop-hook-tts.ps1 line ~41.

---

## What was tried and why it failed

| Approach | Result | Reason |
|----------|--------|--------|
| VoiceMode MCP `converse` | Does not work on Windows | Requires Unix `fcntl` module |
| `uvx kokoro-fastapi[cpu]` | Package not found | Not published as uvx tool |
| VoiceMode `service install kokoro` | Fails on Windows | Service manager (systemd/launchd) not supported |
| Kokoro-FastAPI download_model.py | Partial failure | Verification bug in script, model actually downloaded |

---

## Files
| File | Purpose |
|------|---------|
| `hal-stack/voice-layer/stop-hook-tts.ps1` | Claude Code Stop hook — speaks responses via Kokoro or Windows TTS |
| `hal-stack/voice-layer/tts-speak.ps1` | Manual TTS — pipe any text to speak it |
| `C:\twobirds\tools\Kokoro-FastAPI\start-kokoro.ps1` | Start Kokoro server before Claude Code |
