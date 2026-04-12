# Content Freshness System

Monitors content age across all Two Birds products. Flags stale content before it becomes a problem.

**Layer:** L4-native — pure Node.js, no dependencies

## How to Run

```
node hal-stack/content-freshness/check-freshness.js                           # scans DCC (default)
node hal-stack/content-freshness/check-freshness.js C:\twobirds\clarity       # scans specific repo
node hal-stack/content-freshness/check-freshness.js C:\twobirds\career-coach  # scans Career Coach
```

## How to Read the Report

- **Fresh (green):** No action needed
- **Warning (yellow):** Schedule a content review next sprint
- **Stale (red):** Update urgently — flag in human-backlog as P2

The script exits with code 1 if any stale files are found (useful for CI/automation).

## How to Update Staleness Rules

Edit `staleness-rules.md`. The thresholds are also hardcoded in `check-freshness.js` — update both if changing rules.

## Override

Add `<!-- freshness-override: reason -->` to any HTML file to skip it in the scan.

## Integration with Overnight Build

The overnight build script can run this after Lighthouse to produce a daily freshness report alongside quality scores.
