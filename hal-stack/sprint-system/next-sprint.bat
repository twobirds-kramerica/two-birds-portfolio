@echo off
REM Two Birds Innovation — Next Sprint Launcher
REM Double-click to open Claude Code and run the next sprint.
REM
REM NOTE: Claude Code CLI may not accept a prompt via command line
REM argument. If this doesn't work, open Claude Code manually and
REM paste the contents of next-sprint-mobile.txt.

cd C:\twobirds\two-birds-portfolio

echo ============================================
echo   Two Birds Innovation — Next Sprint
echo ============================================
echo.
echo Opening Claude Code...
echo Paste this command when Claude Code is ready:
echo.
echo Read C:\twobirds\two-birds-portfolio\hal-stack\sprint-system\sprint-queue.md — find the first sprint with status READY. Execute its prompt exactly as written. When done, change its status to DONE, add today's date, update SESSION-STATE.md with the results, auto-generate context export, commit, and push to master.
echo.
echo ============================================

REM Try launching Claude Code
claude

pause
