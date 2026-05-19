# Claude Code Stop Hook — TTS via Kokoro (or Windows fallback)
# Fires when Claude finishes a turn. Reads last assistant message, speaks it.
# Kokoro must be running: C:\twobirds\tools\Kokoro-FastAPI\start-kokoro.ps1

param()

$input_data = $input | Out-String
$json = $input_data | ConvertFrom-Json -ErrorAction SilentlyContinue

$text = ""

# Try to get text from stop_hook_active transcript
if ($json.transcript_path -and (Test-Path $json.transcript_path)) {
    $lines = Get-Content $json.transcript_path -ErrorAction SilentlyContinue
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
}

if (-not $text) { exit 0 }

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
    # Play with ffplay (installed with ffmpeg)
    $ffplay = (Get-Command ffplay -ErrorAction SilentlyContinue)?.Source
    if ($ffplay) {
        Start-Process $ffplay -ArgumentList "-autoexit", "-nodisp", "`"$tmpMp3`"" -Wait -NoNewWindow
        Remove-Item $tmpMp3 -ErrorAction SilentlyContinue
        $kokoro = $true
    }
} catch {}

# Fallback: Windows built-in TTS
if (-not $kokoro) {
    Add-Type -AssemblyName System.Speech
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $synth.Rate = 2
    $synth.Speak($text)
}
