# Rework Log -- Two Birds Innovation
Chief Rework Officer (CRO) -- permanent record.
Purpose: Aaron never repeats a bug report twice.

## How to use
Every rework item logged with:
- Date first reported
- Date fix attempted
- Date verified on device (or NOT VERIFIED)
- Root cause
- Test added to suite: yes/no

## April 12-13, 2026 -- DCC 27-item session
Items: contrast failures, listen button navigation, admin stamps in user view, truncated site name, hamburger gray box, help button overlap, search icon not removed site-wide, accordion invisible dark mode, resume banner contrast failure, "Reviewed by Aaron" visible.
Root cause: fixes applied to individual pages not shared CSS/JS.
Commits: 3c2466c, e850e91, 3825ca4
Device verification: PENDING -- Aaron verifies on S24.

## Standing rules
- All CSS/JS fixes in shared files only, never per-page
- Aaron is never the QA department
- Repeat bug = test suite gap, not a new task
