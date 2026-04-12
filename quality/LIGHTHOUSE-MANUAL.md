# Lighthouse Manual Audit Guide

If the automated Lighthouse CLI fails or isn't installed, use Chrome DevTools.

## From Chrome DevTools (any machine, no install needed)

1. Open Chrome
2. Navigate to the product URL
3. Press **F12** (or right-click → Inspect)
4. Click the **Lighthouse** tab (may say "Audits" on older Chrome)
5. Check all categories: Performance, Accessibility, Best Practices, SEO
6. Select **Mobile** device
7. Click **Analyze page load**
8. Wait 30-60 seconds
9. Screenshot or copy the scores

## Products to Audit

| Product | URL |
|---------|-----|
| DCC | https://twobirds-kramerica.github.io/digital-confidence/ |
| Career Coach | https://twobirds-kramerica.github.io/career-coach/ |
| Clarity | https://twobirds-kramerica.github.io/clarity/ |
| Two Birds Innovation | https://twobirds-kramerica.github.io/two-birds-innovation/ |
| Aaron Patzalek | https://twobirds-kramerica.github.io/aaron-patzalek/ |

## Target Scores

| Category | Minimum | Target |
|----------|---------|--------|
| Performance | 80 | 90+ |
| Accessibility | **90** | 95+ |
| Best Practices | 80 | 90+ |
| SEO | 80 | 90+ |

**Flag anything below 90 on Accessibility** — this is a P0 gate for DCC (seniors audience).

## Where to Log Results

Save to: `quality/lighthouse-results/YYYY-MM-DD.md`

Format:
```
## [Product Name]
URL: [url]
Performance: [score]
Accessibility: [score]
Best Practices: [score]
SEO: [score]
```

## CLI Alternative (if installed)

```
lighthouse https://twobirds-kramerica.github.io/digital-confidence/ --output=json --chrome-flags="--headless"
```
