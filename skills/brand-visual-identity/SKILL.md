---
name: brand-visual-identity
description: Use when creating or reviewing anything visual for HCL Software - colors, typography, logo placement, gradients, chart palettes, or styling for documents, slides, spreadsheets, web pages and dashboards
---

# HCL Software Visual Identity

Source: the HCLSW corporate brand kit as captured in the `hclsw-brand` skill. This skill does not add to it. Machine-readable tokens are in `references/brand-tokens.css`.

## Colors

| Role | Name | Hex |
|------|------|-----|
| Primary | Dark Teal | `#17707F` |
| Primary accent | Software Teal | `#2EC0CB` |
| Accent | Mid Teal | `#36D6D9` |
| Subtle highlight | Light Teal | `#AAFFFF` |
| Supporting blue | Dark Blue | `#0F5FDC` |
| Supporting blue | Tech Blue | `#3C91FF` |
| Soft blue | Mid Blue | `#8AC6F8` |
| Neutral fill | Ice Blue | `#DCE6F0` |
| Deep contrast | Software Blue | `#000032` |
| Subtle fill | Tech Grey | `#ECF3F8` |

Neutrals: black `#000000`, dark text `#14142B`, white `#FFFFFF`, page background `#F7F7FC`, alternating rows `#F4F4F4`.

**Gradient** (title slides, hero sections, covers; always with the white logo and white text):

```css
background: linear-gradient(135deg, #0B1D3A 0%, #17707F 45%, #2EC0CB 85%, #36D6D9 100%);
```

**Semantic data colors**, sparingly and not brand colors: success `#00C3CD`, warning `#F5A623`, error `#DC3545`, info `#3C91FF`.

## Typography

Arial everywhere. Fallbacks: `Arial, "Helvetica Neue", Helvetica, sans-serif`.

| Element | Weight | Slides | Docs | Web |
|---------|--------|--------|------|-----|
| H1 | Bold | 36pt | 28pt | 2.25rem |
| H2 | Bold | 25pt | 22pt | 1.75rem |
| Subheading | Semi-bold | 18pt | 16pt | 1.25rem |
| Body | Regular | 14pt | 11pt | 1rem |
| Caption | Regular | 9pt | 9pt | 0.875rem |

## Logo

- Light backgrounds: horizontal black. Dark or gradient backgrounds: horizontal white. Narrow spaces: vertical variant.
- Place top-left or bottom-left. Clear space equals the height of the "H" in "HCL".
- **Keep the 8:1 aspect ratio** (native 3134x392). Set width and height together: height = width / 8 (200px wide is 25px high).
- Never stretch, rotate, recolor, or add effects.
- Logo files are **not in this repo**. Take them from the official brand kit; do not recreate them.

## Chart series order

`#17707F`, `#2EC0CB`, `#36D6D9`, `#AAFFFF`, `#0F5FDC`, `#3C91FF`, `#8AC6F8`, `#DCE6F0`. Use `#000032` for contrast if needed. Use 2-3 palette colors per section.

## Do and don't

- Do: keep generous white space, a flat modern look, teal-blue as the core identity.
- Don't: use off-brand primary colors, heavy shadows or 3D, fonts other than Arial, or many accents in one view.

Per-output rules (tables, cards, covers, spreadsheets) are in `brand-decks-and-visuals`.

## Checking your work

```bash
python3 skills/brand-visual-identity/scripts/check_brand.py <file-or-dir> [...]
```

It flags off-palette hex colors, non-Arial `font-family` declarations, and `<img>` logo tags whose width/height are not 8:1. It is a lint for HTML/CSS/SVG text files, not proof of brand compliance; review the visual result too.
