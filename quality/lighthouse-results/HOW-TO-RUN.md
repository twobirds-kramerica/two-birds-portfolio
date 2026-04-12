# How to Run a Lighthouse Audit

## From Chrome DevTools (any machine, no install needed)

1. Open **Chrome** browser
2. Navigate to the product URL (e.g., `https://twobirds-kramerica.github.io/digital-confidence/`)
3. Press **F12** (or right-click → Inspect → open DevTools)
4. Click the **Lighthouse** tab (may say "Audits" on older Chrome versions)
5. Select **Mobile** as the device
6. Check all categories: Performance, Accessibility, Best Practices, SEO
7. Click **Analyse page load**
8. Wait 30-60 seconds for the audit to complete
9. Record the four scores:
   - Performance: ___
   - Accessibility: ___
   - Best Practices: ___
   - SEO: ___
10. Save results here as `YYYY-MM-DD-[product].md`

## Result File Format

```markdown
# Lighthouse — [Product Name] — YYYY-MM-DD

URL: [url]
Device: Mobile

| Category | Score |
|----------|-------|
| Performance | XX |
| Accessibility | XX |
| Best Practices | XX |
| SEO | XX |

Notes: [any issues flagged]
```

## From CLI (if Lighthouse is installed)

```
lighthouse https://twobirds-kramerica.github.io/digital-confidence/ --output=html --output-path=./2026-04-12-dcc.html --chrome-flags="--headless --no-sandbox"
```

Check if installed: `lighthouse --version`

## Frequency

- **Automated:** Nightly via `run-overnight-build.bat` (results saved here)
- **Manual:** After any major UX change, before client demos
