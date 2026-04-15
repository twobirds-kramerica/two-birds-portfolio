# Shared Component Library

Reusable HTML partials for all Two Birds Innovation sites. Each component is a standalone HTML snippet that references `tokens.css` for styling values.

## Usage

1. Include `standards/tokens.css` in your page `<head>`
2. Copy the component HTML into your page
3. Adapt content (text, links, colours) — structure stays the same
4. Components use CSS custom properties from tokens.css — override by setting variables on the parent element

## Tailwind Compatibility

Components include Tailwind utility class equivalents in comments. If using Tailwind CDN, you can swap the custom CSS for utility classes. Both approaches reference the same token values.

## Components

| Component | File | Description |
|-----------|------|-------------|
| Nav | `nav.html` | Top navigation bar with logo, links, CTA button |
| Hero | `hero.html` | Landing hero with headline, subtitle, dual CTAs |
| Card | `card.html` | Content card with optional icon, title, description |
| Button | `button.html` | Primary, secondary, and ghost button variants |
| Footer | `footer.html` | Site footer with links, copyright, brand border |
| Form Input | `form-input.html` | Accessible labelled input with help text |
| Section Wrapper | `section-wrapper.html` | Consistent section with max-width, padding, optional heading |
