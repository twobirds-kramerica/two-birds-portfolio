# tts-speak.ps1 — Read text aloud via Windows Speech Synthesis
# Usage: .\tts-speak.ps1 "Your text here"
# Or pipe: echo "hello" | .\tts-speak.ps1
# Works immediately, no API key, no install. Fallback until VoiceMode + OpenAI key is live.

param([Parameter(ValueFromPipeline=$true)][string]$Text)

if (-not $Text) {
    $Text = $args -join " "
}
if (-not $Text) { exit 0 }

Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.Rate = 1   # -10 (slowest) to 10 (fastest). 1 = slightly faster than default.
$synth.Volume = 90
$synth.Speak($Text)
