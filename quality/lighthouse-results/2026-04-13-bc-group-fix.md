# B/C Group Fix Verification -- 2026-04-13

## Verification Checklist

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Header shows full name or "DCC" at 360px | PASS (code) | Responsive spans: full name >360px, "DCC" at 360px. Never "Digital C". |
| 2 | Hamburger has no gray box in dark mode | PASS (code) | CSS: `border: none; background: none; box-shadow: none;` Dark mode: `color: #FFFFFF`. |
| 3 | Nav panel close button visible in dark mode | PASS (code) | Changed from bare "X" to "Close X" with background, border, and `color: #FFFFFF` in dark mode. |
| 4 | Interactive Tools links correctly | PASS (code) | `interactive/index.html` exists. Gamepad icon replaced with target icon. |
| 5 | "Home" link visible on module pages | PASS (code) | B3 back link added via app.js. 44px tap target. Teal colour. |
| 6 | Help button is bottom-right circle | PASS (code) | 52x52px circle, position fixed, bottom 24px right 20px. Bottom sheet on tap. |
| 7 | Search magnifying glass triggers search | PASS (code) | Microphone removed. Magnifying glass is now a button that triggers search. |
| 8 | Zero 404 internal links on homepage | PASS (code) | Scanned. No real 404s found (template strings and tel: links are not issues). |

## Changes Made

- `css/main.css`: Hamburger button stripped of border/background/box-shadow. Dark mode forced white. Site title responsive with full/short spans. Sidebar close button restyled with contrast.
- `index.html`: Header rebuilt with link-wrapped responsive site title. Sidebar close button changed to "Close X" with bilingual attrs. Gamepad icon replaced with target.
- `js/app.js`: B3 back button history intercept. Visible "Home" link on non-homepage pages. B4 help button (52px circle, bottom-right) with bottom sheet.
- `js/search.js`: Microphone removed. Magnifying glass replaced with clickable search submit button.

## Needs Aaron Verification (Samsung S24)

1. Open DCC in Chrome dark mode
2. Check hamburger: no gray box, white icon
3. Open nav: "Close X" button visible
4. Tap browser back: stays on DCC, goes to homepage
5. Help button: bottom-right circle, bottom sheet appears on tap
