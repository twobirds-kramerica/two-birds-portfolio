# HAL Stack — New Machine Setup
# Run once on any Windows PC to get fully operational.
# After this script: double-click launch-claude.bat on the desktop and you're in.
#
# Prerequisites: git, Python 3.8+, uv, Node/npm (Claude Code install)
# If uv is missing: winget install astral-sh.uv

param(
    [string]$TwoBirdsRoot = "C:\twobirds"
)

Write-Host "=== HAL Stack New Machine Setup ===" -ForegroundColor Cyan
Write-Host "Root: $TwoBirdsRoot"
Write-Host ""

# 1. ffmpeg
Write-Host "[1/5] Installing ffmpeg..." -ForegroundColor Yellow
winget install --id Gyan.FFmpeg --silent --accept-package-agreements --accept-source-agreements 2>$null
if ($LASTEXITCODE -eq 0) { Write-Host "     ffmpeg OK" -ForegroundColor Green }

# 2. pyaudio (portaudio for Python)
Write-Host "[2/5] Installing pyaudio..." -ForegroundColor Yellow
pip install pyaudio --quiet
if ($LASTEXITCODE -eq 0) { Write-Host "     pyaudio OK" -ForegroundColor Green }

# 3. eSpeak NG
Write-Host "[3/5] Installing eSpeak NG..." -ForegroundColor Yellow
if (-not (Test-Path "C:\Program Files\eSpeak NG\libespeak-ng.dll")) {
    $msi = "$env:TEMP\espeak-ng.msi"
    Invoke-WebRequest -Uri "https://github.com/espeak-ng/espeak-ng/releases/download/1.52.0/espeak-ng.msi" -OutFile $msi
    Start-Process msiexec.exe -ArgumentList "/i `"$msi`" /quiet /norestart" -Wait
    Write-Host "     eSpeak NG installed" -ForegroundColor Green
} else {
    Write-Host "     eSpeak NG already installed" -ForegroundColor Green
}

# 4. Kokoro-FastAPI
Write-Host "[4/5] Setting up Kokoro TTS..." -ForegroundColor Yellow
$kokoroDir = "$TwoBirdsRoot\tools\Kokoro-FastAPI"
if (-not (Test-Path $kokoroDir)) {
    git clone https://github.com/remsky/Kokoro-FastAPI.git $kokoroDir
    Write-Host "     Cloned Kokoro-FastAPI" -ForegroundColor Green
} else {
    Write-Host "     Kokoro already cloned" -ForegroundColor Green
}

Set-Location $kokoroDir
if (-not (Test-Path "$kokoroDir\.venv")) {
    uv venv
}
Write-Host "     Installing Python deps (first time: 2-5 min)..." -ForegroundColor Yellow
uv pip install --python .venv\Scripts\python.exe -e ".[cpu]" --quiet
Write-Host "     Kokoro deps OK" -ForegroundColor Green

# 5. Desktop shortcut (Sonnet default)
Write-Host "[5/6] Creating desktop shortcut (Sonnet)..." -ForegroundColor Yellow
$launcherBat = "$TwoBirdsRoot\two-birds-portfolio\hal-stack\scripts\launch-claude.bat"
$desktopLnk  = "$env:USERPROFILE\Desktop\Claude Code.lnk"

if (Test-Path $launcherBat) {
    $shell  = New-Object -ComObject WScript.Shell
    $lnk    = $shell.CreateShortcut($desktopLnk)
    $lnk.TargetPath       = $launcherBat
    $lnk.WorkingDirectory = "$TwoBirdsRoot\two-birds-portfolio"
    $lnk.Description      = "Start Kokoro TTS + Claude Code (Sonnet)"
    $lnk.Save()
    Write-Host "     Shortcut created: $desktopLnk" -ForegroundColor Green
} else {
    Write-Host "     [WARN] launch-claude.bat not found — clone two-birds-portfolio first" -ForegroundColor Red
}

# 6. Desktop shortcut (Opus override)
Write-Host "[6/6] Creating desktop shortcut (Opus)..." -ForegroundColor Yellow
$opusLnk = "$env:USERPROFILE\Desktop\Claude Code (Opus).lnk"
if (Test-Path $launcherBat) {
    $shell2  = New-Object -ComObject WScript.Shell
    $lnk2    = $shell2.CreateShortcut($opusLnk)
    $lnk2.TargetPath       = $launcherBat
    $lnk2.Arguments        = "OPUS"
    $lnk2.WorkingDirectory = "$TwoBirdsRoot\two-birds-portfolio"
    $lnk2.Description      = "Start Kokoro TTS + Claude Code (Opus)"
    $lnk2.Save()
    Write-Host "     Shortcut created: $opusLnk" -ForegroundColor Green
} else {
    Write-Host "     [WARN] launch-claude.bat not found" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== Done ===" -ForegroundColor Cyan
Write-Host "Desktop shortcuts:" -ForegroundColor White
Write-Host "  'Claude Code'        — Sonnet (default, fastest)" -ForegroundColor White
Write-Host "  'Claude Code (Opus)' — Opus (deeper reasoning)" -ForegroundColor White
Write-Host "Model IDs: edit hal-stack\config\models.env to update when new versions ship." -ForegroundColor White
Write-Host "First Kokoro start takes ~30s to load the model. Subsequent starts are faster."
