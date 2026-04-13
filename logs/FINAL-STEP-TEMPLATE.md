# FINAL STEP TEMPLATE
Copy this exactly into every Claude Code prompt.
Never modify. Never skip.

---

```
FINAL STEP -- MANDATORY -- DO NOT SKIP

Switch to: C:\twobirds\two-birds-portfolio
Read SESSION-STATE.md first.

1. Overwrite logs/RETRO.md with sprint summary
2. Update SESSION-STATE.md with session entry
3. Overwrite logs/RETRO-LAST-RUN.md with:
   LAST_SPRINT_DATE: [date]
   LAST_SPRINT_TIME: [time] EST
   LAST_SPRINT_NAME: [session name]
   RETRO_STATUS: SYNCED

4. git add logs/RETRO.md logs/SESSION-STATE.md logs/RETRO-LAST-RUN.md
5. git commit -m "chore: RETRO [session name]"
6. git push origin master

If push fails:
   echo "PUSH FAILED [date] [time]" >> logs/ERRORS.md
   git add logs/ERRORS.md
   git commit -m "chore: log push failure"
   Try push again.

7. echo "SPRINT COMPLETE."
```

---

## Why This Exists

On April 13, 2026 at 02:41 AM, an Anthropic API Error 500
caused the RETRO sync to fail silently. Aaron had to detect
the failure manually. This template prevents that by:
- Always switching to the portfolio repo explicitly
- Always writing the staleness detection file
- Logging errors instead of failing silently
- The health check bat runs at end of overnight builds
