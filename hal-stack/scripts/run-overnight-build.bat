@echo off
REM ============================================
REM Two Birds Innovation — Overnight Build
REM Runs: Daily at 2:00 AM via Windows Task Scheduler
REM Logs: C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
REM Updated: 2026-05-08 — added Notion sync verify, content freshness (Mon), backlog health (Sun)
REM ============================================

set LOG=C:\twobirds\two-birds-portfolio\logs\automated-run-log.md

echo [%date% %time%] Overnight build starting... >> %LOG%

REM --- Detect day of week ---
for /f %%w in ('powershell -command "(Get-Date).DayOfWeek"') do set WEEKDAY=%%w
echo [%date% %time%] Day of week: %WEEKDAY% >> %LOG%

REM --- Pull and push all repos ---
cd C:\twobirds

for /D %%d in (digital-confidence career-coach clarity two-birds-innovation aaron-patzalek kevins-apartment-search two-birds-command-centre quality-dashboard elite-karate-site two-birds-portfolio) do (
    if exist "%%d\.git" (
        echo [%date% %time%] Syncing %%d... >> %LOG%
        cd C:\twobirds\%%d
        git pull --ff-only 2>> %LOG%
        git push origin HEAD 2>> %LOG%
        REM Push to Codeberg if remote exists
        git remote | findstr codeberg >nul 2>&1
        if not errorlevel 1 (
            git push codeberg master 2>> %LOG%
        )
    )
)

REM --- Lighthouse Audits ---
echo [%date% %time%] Running Lighthouse audits... >> %LOG%

for /f "usebackq" %%d in (`powershell -Command "Get-Date -Format yyyy-MM-dd"`) do set LHDATE=%%d
set LHFILE=C:\twobirds\two-birds-portfolio\quality\lighthouse-results\%LHDATE%.md

echo # Lighthouse Audit Results — %LHDATE% > "%LHFILE%"
echo. >> "%LHFILE%"

for %%u in (
    "DCC|https://twobirds-kramerica.github.io/digital-confidence/"
    "Career Coach|https://twobirds-kramerica.github.io/career-coach/"
    "Clarity|https://twobirds-kramerica.github.io/clarity/"
    "Two Birds Innovation|https://twobirds-kramerica.github.io/two-birds-innovation/"
    "Aaron Patzalek|https://twobirds-kramerica.github.io/aaron-patzalek/"
) do (
    for /f "tokens=1,2 delims=|" %%a in (%%u) do (
        echo Auditing %%a...
        echo ## %%a >> "%LHFILE%"
        echo URL: %%b >> "%LHFILE%"
        lighthouse "%%b" --output=json --output-path="%TEMP%\lh-temp.json" --chrome-flags="--headless --no-sandbox" --quiet 2>> %LOG%
        if exist "%TEMP%\lh-temp.json" (
            node -e "const r=JSON.parse(require('fs').readFileSync('%TEMP%/lh-temp.json','utf8'));const c=r.categories;console.log('Performance: '+Math.round(c.performance.score*100));console.log('Accessibility: '+Math.round(c.accessibility.score*100));console.log('Best Practices: '+Math.round(c['best-practices'].score*100));console.log('SEO: '+Math.round(c.seo.score*100))" >> "%LHFILE%"
            echo. >> "%LHFILE%"
        ) else (
            echo Lighthouse failed for %%a — no JSON output >> "%LHFILE%"
            echo. >> "%LHFILE%"
        )
    )
)

REM --- Update RETRO.md ---
cd C:\twobirds\two-birds-portfolio
echo Updating RETRO.md with Lighthouse scores...

if exist "%LHFILE%" (
    echo. >> logs\RETRO.md
    echo ## Lighthouse Scores >> logs\RETRO.md
    type "%LHFILE%" >> logs\RETRO.md
)

REM ============================================================
REM HAL STACK AUTOMATION — added 2026-05-08
REM ============================================================

REM --- Notion sync verify (nightly) ---
echo [%date% %time%] Running Notion sync verify... >> %LOG%
cd C:\twobirds\two-birds-portfolio
python hal-stack/notion-sync/next-sprint.py >> %LOG% 2>&1
echo [%date% %time%] Notion sync verify exit code: %errorlevel% >> %LOG%

REM --- Content freshness check (Mondays only) ---
if "%WEEKDAY%"=="Monday" (
    echo [%date% %time%] Running content freshness check (Monday)... >> %LOG%
    cd C:\twobirds\digital-confidence
    node C:\twobirds\two-birds-portfolio\hal-stack\content-freshness\check-freshness.js >> %LOG% 2>&1
    echo [%date% %time%] Content freshness complete. >> %LOG%
)

REM --- Backlog health check (Sundays only) ---
if "%WEEKDAY%"=="Sunday" (
    echo [%date% %time%] Running backlog health check (Sunday)... >> %LOG%
    cd C:\twobirds\two-birds-portfolio
    python hal-stack/notion-sync/backlog-health.py >> %LOG% 2>&1
    echo [%date% %time%] Backlog health complete. >> %LOG%
)

REM --- Story Dial Chronicle Weekly (Thursdays only) ---
REM Layer 1: pulls git commits, creates Notion stub (Raw Data Ready)
REM Layer 2 (Chronicle session) completes the entry next time Aaron opens Claude Code
if "%WEEKDAY%"=="Thursday" (
    echo [%date% %time%] Running Story Dial chronicle weekly (Thursday)... >> %LOG%
    cd C:\twobirds\two-birds-portfolio
    python hal-stack/story-dial/chronicle-weekly.py >> %LOG% 2>&1
    echo [%date% %time%] Chronicle weekly Layer 1 complete. >> %LOG%
)

REM --- CoS morning briefing (daily) ---
echo [%date% %time%] Generating CoS morning briefing... >> %LOG%
cd C:\twobirds\two-birds-portfolio
python hal-stack/cos/morning-briefing.py >> %LOG% 2>&1
echo [%date% %time%] CoS morning briefing complete. >> %LOG%

REM ============================================================

REM --- Final commit ---
cd C:\twobirds\two-birds-portfolio
git add -A
git commit -m "chore: overnight build complete — Lighthouse + HAL checks [%LHDATE%]"
git push origin master

echo [%date% %time%] Overnight build complete. >> %LOG%

REM --- RETRO Health Check ---
echo Running RETRO health check...
call C:\twobirds\two-birds-portfolio\tools\retro-health-check.bat
