# 🔴 EUREKA-005 — The MBA Intern Friction Pattern Observer
Date captured: April 1, 2026
Theme: Business
Shareability: 4
Personal flag: 🟡 Adaptable

## The Problem It Solves
When you're building fast, you don't notice your own inefficiencies. You work around broken things, repeat manual steps, and tolerate friction because fixing it feels slower than enduring it. The friction pattern observer turns Claude into an MBA intern sitting behind you — watching everything you do, noting every point where the workflow breaks or slows down, and logging each one with a severity score.

## Why It's A Eureka Moment
Most people use AI to do work. This prompt uses AI to watch you work. The output isn't code or content — it's a prioritised list of your own inefficiencies. Every friction point is a potential product improvement, process fix, or automation opportunity. The insight: your daily frustrations are data, and the pattern in that data is where the leverage lives.

## The Hook (for social media)
"I told Claude to watch me work like an MBA intern — note every friction point, score it 1-10, and log it. The list it produced was more valuable than the code."

## The Verbatim Prompt
```
While working on this session, observe my workflow for friction points.
A friction point is any moment where:
- I repeat a manual step that could be automated
- I hit an error that wastes time
- I work around something broken instead of fixing it
- I context-switch unnecessarily
- A tool fails and I have to retry

Log each friction point as:
FP-[number]: [description] | Score: [1-10] | Status: LOGGED

At the end of the session, write all friction points to a
FRICTION-LOG.md file. Sort by score descending.
For anything scored 7+, add a "Suggested fix" line.
```

## The Result
Seven friction points logged in a single day of building. FP-001 (context rot between sessions, score 9) led directly to the SESSION-STATE.md system. FP-003 (GitHub Actions flooding, score 8) was fixed immediately. FP-006 (Pentium Silver too slow, score 7) confirmed the need for a new machine. The friction log became a living document on the Language Bank page of the Command Centre.

## How To Adapt It
- Add this instruction to the top of any extended work session
- Adjust the friction criteria to match your workflow
- The score threshold (7+) controls how much follow-up action is suggested
- Review the log weekly — patterns across sessions reveal systemic issues
- Share friction logs with your team — they normalise talking about inefficiency
- The key insight: you can't improve what you don't measure, and friction is measurable
