@echo off
:: HAL Stack — One-Shot Claude Code Launcher
:: Double-click this to start everything:
::   1. Kokoro TTS server (voice output)
::   2. Claude Code in two-birds-portfolio
::
:: Works after restart. No admin needed.
:: Cross-PC setup guide: hal-stack/voice-layer/VOICE-SETUP.md
::
:: Model override: launch-claude.bat OPUS  (or HAIKU)
:: To update when new models ship: edit hal-stack\config\models.env — one line.

:: ── Model Tier ─────────────────────────────────────────────────────────────────
set "MODELS_ENV=C:\twobirds\two-birds-portfolio\hal-stack\config\models.env"

if exist "%MODELS_ENV%" (
    for /f "usebackq tokens=1,* delims==" %%a in ("%MODELS_ENV%") do (
        if not "%%a"=="" set "%%a=%%b"
    )
) else (
    set CLAUDE_SONNET=claude-sonnet-4-6
    set CLAUDE_OPUS=claude-opus-4-7
    set CLAUDE_HAIKU=claude-haiku-4-5-20251001
    set CLAUDE_DEFAULT_TIER=SONNET
)

if not "%~1"=="" set CLAUDE_DEFAULT_TIER=%~1
call set "ANTHROPIC_MODEL=%%CLAUDE_%CLAUDE_DEFAULT_TIER%%%"
if "%ANTHROPIC_MODEL%"=="" set ANTHROPIC_MODEL=claude-sonnet-4-6

echo [HAL] Model tier: %CLAUDE_DEFAULT_TIER% -- %ANTHROPIC_MODEL%

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
wt -d C:\twobirds\two-birds-portfolio cmd /k "set ANTHROPIC_MODEL=%ANTHROPIC_MODEL% && claude"
