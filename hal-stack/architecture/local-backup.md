<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 02:25 EST (Toronto)
Confidence: HIGH — simple git operations, well-understood
Known gaps: Pentium Silver's current state (OS, git version, drive space) not verified
-->

# Local Git Backup — L4 Insurance

A local git mirror on the Pentium Silver (or any spare machine) that auto-syncs from GitHub. Zero maintenance from Aaron. If GitHub dies, Aaron has every repo on a machine in his house.

## What This Is

A dumb mirror. It pulls from GitHub every few hours. It never pushes. It never modifies files. It just maintains a complete, current copy of every repo.

## Why This Exists

GitHub is L1. If Microsoft acquires GitHub (done), changes pricing (possible), goes hostile (unlikely but non-zero), or just has a multi-day outage (has happened), Aaron needs his repos accessible locally. Since every machine already has clones, the worst case is "clones are a few hours stale." The Pentium Silver closes that gap.

## Setup — Step by Step

### 1. Create the sync script

Save as `C:\twobirds\sync-from-github.bat` on the Pentium Silver:

```batch
@echo off
echo [%date% %time%] Starting GitHub sync... >> C:\twobirds\sync-log.txt

cd C:\twobirds

for /D %%d in (*) do (
    if exist "%%d\.git" (
        echo Pulling %%d... >> C:\twobirds\sync-log.txt
        cd %%d
        git pull --ff-only origin 2>> C:\twobirds\sync-log.txt
        cd ..
    )
)

echo [%date% %time%] Sync complete. >> C:\twobirds\sync-log.txt
```

### 2. Clone all repos (one-time)

On the Pentium Silver, clone every repo:

```batch
cd C:\twobirds
git clone https://github.com/twobirds-kramerica/digital-confidence
git clone https://github.com/twobirds-kramerica/two-birds-portfolio
git clone https://github.com/twobirds-kramerica/career-coach
git clone https://github.com/twobirds-kramerica/clarity
git clone https://github.com/twobirds-kramerica/aaron-patzalek
git clone https://github.com/twobirds-kramerica/two-birds-innovation
git clone https://github.com/twobirds-kramerica/quality-dashboard
git clone https://github.com/twobirds-kramerica/two-birds-command-centre
git clone https://github.com/twobirds-kramerica/kevins-apartment-search
git clone https://github.com/twobirds-kramerica/elite-karate-site
```

### 3. Schedule the sync

Using Windows Task Scheduler on the Pentium Silver:
- Task name: `GitHub Mirror Sync`
- Trigger: Every 4 hours (or every 6 hours if the machine is slow)
- Action: Run `C:\twobirds\sync-from-github.bat`
- Conditions: Start only if network is available
- Settings: Stop task if it runs longer than 30 minutes

### 4. Verify

Check `C:\twobirds\sync-log.txt` after the first scheduled run. Every repo should show "Already up to date" or a list of pulled changes.

## What Happens If GitHub Dies

1. **Aaron notices GitHub is down** (or reads the news)
2. **All repos are on the Pentium Silver** (and on EZbook and i5, but potentially stale)
3. **Switch remotes:** On working machines, add the Pentium Silver as a local remote:
   ```
   git remote add local \\PENTIUM-HOSTNAME\twobirds\repo-name
   ```
   Or copy repos via USB if network sharing isn't set up.
4. **Continue working** — push to local remote until GitHub recovers
5. **When GitHub returns** — push everything back, remove local remote

## What Happens If GitHub AND the Pentium Silver Die

Every machine that has ever cloned a repo has a full copy. Aaron has at least 3 machines with clones (EZbook, i5, Pentium). Losing all three simultaneously would require a physical disaster affecting his entire house. At that point, git repos are not the main concern.

## Hardware Requirements

Basically nothing. The Pentium Silver is fine:
- Git installed (any version)
- Network connection (Wi-Fi or ethernet)
- Enough disk space for all repos (~500MB total currently)
- Runs 24/7 or at least daily

## What This Is NOT

- Not a backup of Aaron's personal data (that's the L4 personal machine — separate)
- Not a CI/CD system (no builds run here)
- Not a push target (one-way pull only)
- Not a replacement for GitHub (just insurance)
