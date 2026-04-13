# Automated QA Rules

Standing rule: Aaron is never the QA department. These checks run automatically.

## What Runs Automatically

### 1. Personal Name Check
```
grep -r "Reviewed by Aaron\|Reviewed by Aaron Kramer" --include="*.html" .
```
**Threshold:** Zero matches in user-facing pages. Any match is a build failure.

### 2. Link Check
All internal `href` values tested. Any 404 is a build failure.

### 3. Contrast Check
Dark mode text must be #FFFFFF or #F7FAFC on dark backgrounds. Never gray on gray.
CSS variables `--text-muted` must be at minimum #BDBDBD (4.7:1 on #2D2D2D).

### 4. axe-core Accessibility (via ?qa=true)
Run on index.html and module-1.html at minimum. WCAG AA standard.

## How to Run Manually

1. Open any DCC page in Chrome
2. Add `?qa=true` to the URL
3. axe-core panel appears at the bottom
4. Review violations

## How to Interpret Results

- **Zero violations:** Ship it.
- **1-3 minor violations:** Ship it, log them, fix next sprint.
- **Any contrast or navigation violation:** Do not ship until fixed.

## Standing Rules

1. No "Aaron" or "Reviewed by" in user-facing pages. Ever.
2. No newsletter signup without email infrastructure.
3. No "Contact Us" without support staff.
4. No listen button that navigates instead of reading.
5. No progress shown on completely fresh visits.
6. No dyslexia font toggle (removed by Aaron's decision).
7. Footer tagline: "A free digital learning programme for all Canadians" (not "seniors").
