# HAL Stack Scripts

## launch-claude.bat
Double-click to open Windows Terminal pointed at the DCC repo with Claude Code running.
Copy to Desktop. Right-click → Run as administrator for full permissions.

## keep-alive.bat
Restart loop — if Claude Code exits, waits 30 seconds and relaunches.
Use via Task Scheduler at startup for always-on operation.

## Usage
1. Copy launch-claude.bat to Desktop
2. Right-click → Properties → Advanced → Run as administrator → OK
3. Double-click to launch
4. For always-on: open Task Scheduler → import keep-alive.bat as a startup task
