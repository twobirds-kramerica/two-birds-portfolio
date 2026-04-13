# Retro
Date: April 13, 2026
Session: DCC rework -- module page dark mode fixes

Root cause: previous fixes applied to index.html or JS functions that only ran on homepage. Module pages were not covered. This sprint fixed the root by putting all changes in shared CSS (main.css) and shared JS (app.js, search.js, accessibility.js, speech-config.js).

Fixed (141 files, 6 issues):
1. Search icon + Home link: removed from header site-wide. buildMobileSearch() disabled in search.js. initTopBarHome() disabled in accessibility.js. Header is now hamburger + title + lang only on ALL pages.
2. Read Aloud button: compact single-line styling in main.css. 14px font, max-width 220px, inline-flex. Speed controls nowrap.
3. Help button overlap: padding-bottom 80px on all content areas via main.css.
4. Speed control: no longer hidden behind help button (covered by padding fix).
5. Resume banner: dark mode contrast override in main.css. White text on dark teal background.
6. Accordion/summary: dark mode contrast override in main.css. White text, teal border.

Sidebar close button: updated from bare X to "Close X" on all 155 pages with bilingual data attrs.

Standing rule enforced: all CSS/JS fixes go in shared files only. Never patch individual HTML pages.

Aaron verifies on S24: open digital-literacy-101.html in dark mode. All 6 items should be clean.

Last updated: 2026-04-13 at 02:22 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.
