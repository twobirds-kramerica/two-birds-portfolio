# 🔴 EUREKA-002 — The Trigger Word System
Date captured: April 1, 2026
Theme: Workflow
Shareability: 4
Personal flag: 🟡 Adaptable

## The Problem It Solves
When you finish a Claude Code session, you have no easy way to check what happened from another device. Screenshots are fragile, chat histories are long, and copy-pasting summaries is manual work. The trigger word system replaces all of that: Claude writes a plain-text summary to a file on GitHub, and you check it by pasting a single raw URL into any browser or AI tool.

## Why It's A Eureka Moment
The insight is that a raw GitHub URL is a universal, persistent, always-current API endpoint for your own work. You don't need a dashboard, a Slack bot, or a notification system. You just need a file that gets overwritten after every session and a URL you can paste anywhere. One word in your next session — "Retro" or "State" — and Claude reads that file to pick up exactly where you left off.

## The Hook (for social media)
"I replaced screenshots with a single URL. After every Claude Code session, it writes a summary to GitHub. I paste the URL anywhere to see what happened."

## The Verbatim Prompt
```
Finally, overwrite C:\twobirds\two-birds-portfolio\logs\LAST-RUN-SUMMARY.md
with a plain-text summary of what ran, then commit and push it.
```

Added to the end of every autonomous prompt. The file lives at:
`https://raw.githubusercontent.com/twobirds-kramerica/two-birds-portfolio/master/logs/LAST-RUN-SUMMARY.md`

## The Result
A single URL that always shows the most recent session summary. Pasteable into Claude Web, a browser, or any tool that can fetch a URL. No screenshots needed. No context lost. The file is version-controlled, so you can see the history of every session summary via git log.

## How To Adapt It
- Create your own LAST-RUN-SUMMARY.md in any GitHub repo
- Add the overwrite instruction to the end of every autonomous prompt
- Bookmark the raw GitHub URL for quick access
- Use it as input for your next session: "Read this URL and continue from where we left off"
- Works with any CI/CD system or automation tool that can read a URL
