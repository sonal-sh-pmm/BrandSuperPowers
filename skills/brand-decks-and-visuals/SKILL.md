---
name: brand-decks-and-visuals
description: Use when creating or reviewing slides, Word documents, PDFs, spreadsheets, dashboards, charts, or web and HTML pages that need to follow HCL Software branding
---

# Decks and Visuals

Apply `brand-visual-identity` to a specific output type. Read it first for colors, fonts and logo rules.

## By output type

| Output | Rules |
|--------|-------|
| **Slides** | Title slide: brand gradient, white logo, white text. Content slides: white background, black text, teal headings (`#17707F` or `#2EC0CB`). Arial throughout. Footer with date and classification (e.g. "Confidential") when needed. Official template file `HCLSW_TEMPLATE.pptx` is not in this repo; get it from the brand kit. |
| **Word / PDF** | Headings Arial bold in `#17707F`. Body Arial 11pt, `#000000` or `#14142B`. Accent lines `#2EC0CB` at 1-2pt. Table header `#17707F` with white text; rows alternate white / `#F7F7FC`. Cover: gradient with white logo. Logo top-left in header, page numbers bottom-right. |
| **Spreadsheets** | Header row `#17707F` fill, white bold Arial 11pt. Sub-headers `#ECF3F8`. Alternating rows white / `#F7F7FC`. Total rows `#2EC0CB` with white text. Thin `#DCE6F0` borders. |
| **Web / dashboards** | Use `skills/brand-visual-identity/references/brand-tokens.css`. Gradient for headers and hero banners. Cards: white, `1px solid #DCE6F0`, `border-radius: 8px`. Table header `#0F5FDC` with white text or `#DCE6F0` with dark text. |
| **Charts** | Series order from `brand-visual-identity`. Label axes and units, state the sample size and date range, and note caveats. Do not imply causation from correlation. If `dataviz` is available, use it for layout and accessibility. |

## Data and numbers

- Never fabricate figures. If you cannot run the query or open the source, label the chart or table **illustrative**.
- Cite the data source, version or date, and any parameters or seed used so the visual can be reproduced.
- Keep customer-identifiable data out of shared visuals; use `<CUSTOMER_ID>` style placeholders.

## Verify before finishing

1. For HTML/CSS/SVG output run `python3 skills/brand-visual-identity/scripts/check_brand.py <path>`.
2. Check by eye: contrast of text on teal/gradient, logo ratio 8:1, Arial only, no heavy shadows or 3D.
3. Run `brand-compliance-guardrails` on any claim text in the output.
