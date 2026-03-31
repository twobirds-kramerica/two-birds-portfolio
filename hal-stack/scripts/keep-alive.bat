@echo off
:: HAL Stack Keep-Alive Script
:: Runs Claude Code in a loop — if it crashes, restarts after 30 seconds
:loop
wt -d C:\twobirds\digital-confidence cmd /k "claude"
timeout /t 30 /nobreak
goto loop
