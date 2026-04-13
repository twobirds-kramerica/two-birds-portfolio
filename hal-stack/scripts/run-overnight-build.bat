@echo off
REM ============================================
REM Two Birds Innovation — Overnight Build
REM Runs: Daily at 2:00 AM via Windows Task Scheduler
REM Logs: C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
REM ============================================

echo [%date% %time%] Overnight build starting... >> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md

REM --- Pull and push all repos ---
cd C:\twobirds

for /D %%d in (digital-confidence career-coach clarity two-birds-innovation aaron-patzalek kevins-apartment-search two-birds-command-centre quality-dashboard elite-karate-site two-birds-portfolio) do (
    if exist "%%d\.git" (
        echo [%date% %time%] Syncing %%d... >> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
        cd C:\twobirds\%%d
        git pull --ff-only origin 2>> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
        git push origin master 2>> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
        REM Push to Codeberg if remote exists
        git remote | findstr codeberg >nul 2>&1
        if not errorlevel 1 (
            git push codeberg master 2>> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
        )
    )
)

REM --- Lighthouse Audits ---
echo [%date% %time%] Running Lighthouse audits... >> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md

set LHDATE=%date:~10,4%-%date:~4,2%-%date:~7,2%
set LHFILE=C:\twobirds\two-birds-portfolio\quality\lighthouse-results\%LHDATE%.md

echo # Lighthouse Audit Results — %LHDATE% > "%LHFILE%"
echo. >> "%LHFILE%"

REM Audit each product
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
        lighthouse "%%b" --output=json --output-path="%TEMP%\lh-temp.json" --chrome-flags="--headless --no-sandbox" --quiet 2>> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
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

REM Copy Lighthouse results into RETRO if file exists
if exist "%LHFILE%" (
    echo. >> logs\RETRO.md
    echo ## Lighthouse Scores >> logs\RETRO.md
    type "%LHFILE%" >> logs\RETRO.md
)

git add -A
git commit -m "chore: overnight build complete — Lighthouse scores updated"
git push origin master

echo [%date% %time%] Overnight build complete. >> C:\twobirds\two-birds-portfolio\logs\automated-run-log.md

REM --- RETRO Health Check ---
echo Running RETRO health check...
call C:\twobirds\two-birds-portfolio\tools\retro-health-check.bat
