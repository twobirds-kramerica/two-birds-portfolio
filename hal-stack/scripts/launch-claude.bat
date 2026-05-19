@echo off
:: HAL Stack — One-Shot Claude Code Launcher
:: Double-click this to start everything:
::   1. Kokoro TTS server (voice output)
::   2. Claude Code in two-birds-portfolio
::
:: Works after restart. No admin needed.
:: Cross-PC setup guide: hal-stack/voice-layer/VOICE-SETUP.md

:: ── Kokoro TTS ────────────────────────────────────────────────────────────────
:: Start in minimized window. Stays running in background while you work.
:: Model load takes ~30s — Claude Code opens immediately, voice ready shortly after.
if exist "C:\twobirds\tools\Kokoro-FastAPI\start-kokoro.ps1" (
    start "Kokoro TTS" /min powershell.exe -ExecutionPolicy Bypass -WindowStyle Minimized -File "C:\twobirds\tools\Kokoro-FastAPI\start-kokoro.ps1"
) else (
    echo [WARN] Kokoro not installed at C:\twobirds\tools\Kokoro-FastAPI
    echo [WARN] Voice will fall back to Windows TTS.
    echo [WARN] To install: see hal-stack/voice-layer/VOICE-SETUP.md
)

:: ── Claude Code ───────────────────────────────────────────────────────────────
:: Opens Windows Terminal in the portfolio repo and starts claude
:: Change the -d path below if you want a different default repo
wt -d C:\twobirds\two-birds-portfolio cmd /k "claude"
