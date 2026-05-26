# Claude Code Stop Hook — TTS via Kokoro (or Windows fallback)
# Fires when Claude finishes a turn. Reads last assistant message, speaks it.
# Kokoro must be running: C:\twobirds\tools\Kokoro-FastAPI\start-kokoro.ps1

param()

$logFile = "$env:TEMP\claude-tts-debug.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$input_data = $input | Out-String
"[$timestamp] Hook fired. Raw input length: $($input_data.Length)" | Out-File $logFile -Append

$json = $input_data | ConvertFrom-Json -ErrorAction SilentlyContinue
"[$timestamp] transcript_path: $($json.transcript_path)" | Out-File $logFile -Append

$text = ""

# Try to get text from stop_hook_active transcript
if ($json.transcript_path -and (Test-Path $json.transcript_path)) {
    $lines = Get-Content $json.transcript_path -ErrorAction SilentlyContinue
    "[$timestamp] Transcript lines: $($lines.Count)" | Out-File $logFile -Append
    for ($i = $lines.Count - 1; $i -ge 0; $i--) {
        $msg = $lines[$i] | ConvertFrom-Json -ErrorAction SilentlyContinue
        if ($msg.role -eq "assistant") {
            if ($msg.content -is [string]) {
                $text = $msg.content
            } elseif ($msg.content -is [array]) {
                $text = ($msg.content | Where-Object { $_.type -eq "text" } | Select-Object -Last 1).text
            }
            if ($text) { break }
        }
    }
} elseif (-not $json.transcript_path) {
    "[$timestamp] ERROR: no transcript_path in hook input" | Out-File $logFile -Append
} else {
    "[$timestamp] ERROR: transcript_path not found on disk: $($json.transcript_path)" | Out-File $logFile -Append
}

"[$timestamp] text extracted (first 100 chars): $($text.Substring(0, [Math]::Min(100, $text.Length)))" | Out-File $logFile -Append

if (-not $text) {
    "[$timestamp] No text - exiting without speaking" | Out-File $logFile -Append
    exit 0
}

# Trim to 800 chars max to avoid very long TTS runs
if ($text.Length -gt 800) { $text = $text.Substring(0, 800) + "..." }

# Try Kokoro first (localhost:8880)
$kokoro = $false
try {
    $body = @{ model = "kokoro"; voice = "af_sky"; input = $text } | ConvertTo-Json
    $tmpMp3 = "$env:TEMP\claude_tts_$(Get-Random).mp3"
    Invoke-RestMethod -Uri "http://localhost:8880/v1/audio/speech" `
        -Method POST -Body $body -ContentType "application/json" `
        -OutFile $tmpMp3 -TimeoutSec 10 -ErrorAction Stop
    # Play with ffplay — check PATH-refreshed location or WinGet links
    $ffplayCandidates = @(
        "ffplay",
        "C:\Users\getkr\AppData\Local\Microsoft\WinGet\Links\ffplay.exe",
        "C:\Program Files\ffmpeg\bin\ffplay.exe"
    )
    $ffplay = $null
    foreach ($c in $ffplayCandidates) {
        if (Get-Command $c -ErrorAction SilentlyContinue) { $ffplay = $c; break }
    }
    if (-not $ffplay) {
        $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
        $ffplay = Get-Command ffplay -ErrorAction SilentlyContinue
        $ffplay = if ($ffplay) { $ffplay.Source } else { $null }
    }
    if ($ffplay) {
        Start-Process $ffplay -ArgumentList "-autoexit", "-nodisp", "`"$tmpMp3`"" -Wait -NoNewWindow
        Remove-Item $tmpMp3 -ErrorAction SilentlyContinue
        $kokoro = $true
    }
} catch {}

# Fallback: Windows built-in TTS
if (-not $kokoro) {
    "[$timestamp] Using Windows TTS fallback" | Out-File $logFile -Append
    Add-Type -AssemblyName System.Speech
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $synth.Rate = 2
    $synth.Speak($text)
    "[$timestamp] Windows TTS done" | Out-File $logFile -Append
} else {
    "[$timestamp] Kokoro TTS done" | Out-File $logFile -Append
}
