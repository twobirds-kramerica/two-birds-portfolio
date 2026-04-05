# QA Framework — Two Birds Innovation

**Date:** April 5, 2026
**Standard:** Every product must defend itself to a critical board before being shown to a client.

---

## Section 1 — Accessibility and Compliance Testing

### WCAG 2.1 AA (Minimum) / AAA (Target for DCC)

| Check | AA (Required) | AAA (Target) | How to Test |
|-------|--------------|-------------|-------------|
| Alt text on all images | All images have descriptive alt | Alt describes content + context | axe-core audit |
| Form labels | All fields have associated `<label>` | Labels are descriptive + helpful | axe-core audit |
| Colour contrast | 4.5:1 minimum (text), 3:1 (large text) | 7:1 for all text | axe-core / Chrome DevTools |
| Focus indicators | Visible on all interactive elements | Custom high-visibility focus | Tab through every page |
| No flash content | Nothing flashes >3 times/second | No flashing at all | Manual review |
| Keyboard navigation | All functionality via keyboard alone | Tab order is logical | Tab through every page |
| Reading level | Appropriate for audience | DCC: Grade 6-8 equivalent | Hemingway App (free) |
| Skip navigation | Skip link present on pages with nav | Skip link + landmark roles | axe-core audit |

### AODA (Accessibility for Ontarians with Disabilities Act)

| Requirement | Status | Notes |
|------------|--------|-------|
| WCAG 2.0 Level AA minimum | Required for all Ontario public-facing sites | DCC targets AAA |
| Accessible PDFs (tagged) | Required if PDFs are offered | DCC: no PDFs (HTML only) |
| Video captions | Required | DCC: no video content currently |
| Audio transcripts | Required | DCC: no audio content currently |
| Accessible contact info | Required | Present on all products |

### Bilingual Quality Checks

| Check | Method |
|-------|--------|
| All English has French equivalent | Grep for `data-en` without matching `data-fr` |
| Quebec French (not European) | Manual review of terminology (courriel not e-mail, magasinage not shopping) |
| data-en/data-fr pairs on all elements | `grep -c "data-en" file.html` vs `grep -c "data-fr" file.html` — counts must match |
| Language toggle works and persists | Manual test: switch to FR, navigate to another page, confirm FR persists |
| No English leaking into French view | Manual test: switch to FR, check all visible text |

### Tool: axe-core

**Licence:** MIT (open source, zero cost, no volume cap)
**Integration:** Add to every product as a dev-mode audit panel.

When URL includes `?qa=true`, axe runs automatically:
```html
<script>
if (new URLSearchParams(window.location.search).has('qa')) {
  var s = document.createElement('script');
  s.src = 'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.7.0/axe.min.js';
  s.onload = function() {
    axe.run().then(function(results) {
      console.log('axe-core results:', results);
      var panel = document.createElement('div');
      panel.style.cssText = 'position:fixed;bottom:0;left:0;right:0;max-height:50vh;overflow-y:auto;background:#1a1a2e;color:#e6edf3;font-family:monospace;font-size:13px;padding:16px;z-index:99999;border-top:3px solid #e63946;';
      panel.innerHTML = '<h3 style="margin:0 0 8px;color:#ff9f1c;">axe-core Audit — ' + results.violations.length + ' violations, ' + results.passes.length + ' passes</h3>' +
        results.violations.map(function(v) { return '<div style="margin:4px 0;color:#e63946;">FAIL: ' + v.help + ' (' + v.nodes.length + ' instances)</div>'; }).join('') +
        '<button onclick="this.parentNode.remove()" style="margin-top:8px;padding:6px 12px;background:#2ec4b6;color:#fff;border:none;border-radius:4px;cursor:pointer;">Dismiss</button>';
      document.body.appendChild(panel);
    });
  };
  document.head.appendChild(s);
}
</script>
```

---

## Section 2 — Mobile Layout Baseline Checks

### Breakpoints to Test

| Breakpoint | Device | Priority |
|-----------|--------|----------|
| 375px | iPhone SE (smallest common) | P0 |
| 390px | iPhone 14 | P1 |
| 414px | iPhone Plus | P1 |
| 768px | iPad portrait | P0 (DCC primary audience) |
| 1024px | iPad landscape / small laptop | P1 |
| 1440px | Desktop | P1 |

### Checks Per Breakpoint

- [ ] No horizontal scroll (`document.documentElement.scrollWidth <= window.innerWidth`)
- [ ] No text smaller than 16px
- [ ] No tap targets smaller than 44px
- [ ] No overlapping elements
- [ ] Navigation is usable (hamburger or stacked on mobile)
- [ ] Hero/header section readable
- [ ] CTA button visible without scrolling (above fold)

### Layout Check Script

Create and run in browser console:
```javascript
// Run at any breakpoint — logs failures
(function() {
  var issues = [];
  if (document.documentElement.scrollWidth > window.innerWidth)
    issues.push('OVERFLOW: page wider than viewport by ' + (document.documentElement.scrollWidth - window.innerWidth) + 'px');
  document.querySelectorAll('*').forEach(function(el) {
    var style = getComputedStyle(el);
    var fontSize = parseFloat(style.fontSize);
    if (fontSize > 0 && fontSize < 16 && el.textContent.trim().length > 0 && style.display !== 'none')
      issues.push('SMALL TEXT (' + fontSize + 'px): ' + el.tagName + '.' + el.className.split(' ')[0] + ' — "' + el.textContent.trim().substring(0, 40) + '"');
    var rect = el.getBoundingClientRect();
    if ((el.tagName === 'A' || el.tagName === 'BUTTON' || el.role === 'button') && rect.height > 0 && rect.height < 44)
      issues.push('SMALL TAP (' + Math.round(rect.height) + 'px): ' + el.tagName + ' — "' + el.textContent.trim().substring(0, 30) + '"');
  });
  if (issues.length === 0) console.log('%c✅ Layout check passed at ' + window.innerWidth + 'px', 'color:green;font-weight:bold');
  else { console.log('%c❌ ' + issues.length + ' issues at ' + window.innerWidth + 'px', 'color:red;font-weight:bold'); issues.forEach(function(i) { console.log('  ' + i); }); }
})();
```

---

## Section 3 — P0 Gate (Must Pass Before Client Demo)

No product is shown to a client until all three pass:

| Gate | Check | How |
|------|-------|-----|
| Security | No hardcoded API keys, .env in .gitignore | Security audit script |
| Lighthouse | Performance 90+, Accessibility 90+, SEO 85+ | Chrome DevTools Lighthouse |
| UX Review | Layout check passes at 375px and 768px | Console script above |

Track gate status in PRODUCT-SCORES.md per product.
