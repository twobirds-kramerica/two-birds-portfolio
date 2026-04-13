@echo off
REM HAL RETRO HEALTH CHECK
REM Run this after every sprint to verify RETRO was updated

echo Checking RETRO health...
cd /d C:\twobirds\two-birds-portfolio

REM Always stage and push RETRO files
git add logs\RETRO.md
git add logs\SESSION-STATE.md
git add logs\RETRO-LAST-RUN.md
git add logs\ERRORS.md

git diff --cached --quiet
if errorlevel 1 (
  git commit -m "chore: RETRO health check sync %date% %time%"
  git push origin master
  echo RETRO synced and pushed.
) else (
  echo No RETRO changes to push.
)

echo Health check complete.
