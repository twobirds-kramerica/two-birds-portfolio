# Lighthouse Results

Run Lighthouse audits from Chrome DevTools on each product URL.
Export results as JSON or note scores manually.
Save each audit as `YYYY-MM-DD-[product].md`.

## Target Scores

| Category | Minimum | Target |
|----------|---------|--------|
| Performance | 80 | 90+ |
| Accessibility | **90** | 95+ |
| Best Practices | 80 | 90+ |
| SEO | 80 | 90+ |

**P0 gate:** No product ships to a client until mobile accessibility score is 90+.

## Products to Audit

| Product | URL |
|---------|-----|
| DCC | https://twobirds-kramerica.github.io/digital-confidence/ |
| Career Coach | https://twobirds-kramerica.github.io/career-coach/ |
| Clarity | https://twobirds-kramerica.github.io/clarity/ |
| Two Birds Innovation | https://twobirds-kramerica.github.io/two-birds-innovation/ |
| Aaron Patzalek | https://twobirds-kramerica.github.io/aaron-patzalek/ |

## How to Run

See `quality/LIGHTHOUSE-MANUAL.md` for step-by-step instructions using Chrome DevTools.

If Lighthouse CLI is installed (`lighthouse --version`):
```
lighthouse [URL] --output=json --chrome-flags="--headless" --output-path=./quality/lighthouse-results/YYYY-MM-DD-[product].json
```

The overnight build script (`run-overnight-build.bat`) runs Lighthouse automatically on all products.
