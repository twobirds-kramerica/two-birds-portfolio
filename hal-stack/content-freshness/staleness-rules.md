# Content Freshness — Staleness Rules

Defines when content is "fresh," "warning," or "stale" for each content type.

## Rules

| Content Type | Fresh | Warning | Stale | Check Against |
|-------------|-------|---------|-------|---------------|
| DCC modules | < 60 days | 60-90 days | > 90 days | lastmod meta tag or sitemap |
| DCC resources page | < 45 days | 45-60 days | > 60 days | lastmod meta tag |
| Company sites (TBI, Aaron P) | < 120 days | 120-180 days | > 180 days | lastmod or git commit date |
| Backlog / session state | < 7 days | 7-14 days | > 14 days | file modification date |
| LinkedIn content | < 3 days since last post | 3-7 days | > 7 days | posting schedule |
| Career Coach | < 90 days | 90-180 days | > 180 days | lastmod or git commit |
| Clarity | < 90 days | 90-180 days | > 180 days | lastmod or git commit |

## Thresholds

- **Fresh (green):** Content has been updated recently. No action needed.
- **Warning (yellow):** Content is aging. Schedule a review in the next sprint.
- **Stale (red):** Content is overdue for update. Flag as P2 in human-backlog.

## Why These Numbers

- DCC modules: seniors content must stay current — outdated security advice is dangerous
- Resources: links go dead fast, check frequently
- Company sites: brand sites can age longer but 6 months without an update looks abandoned
- Backlog: if nobody's updated in 2 weeks, the project looks dormant
- LinkedIn: 3x/week schedule means more than 7 days gap breaks momentum

## Override

Aaron can override any rule by adding a comment to the file: `<!-- freshness-override: reason -->`. The script will skip files with this comment.
