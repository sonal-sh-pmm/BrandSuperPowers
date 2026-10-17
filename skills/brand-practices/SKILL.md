---
name: brand-practices
description: Use when doing any marketing or brand work - copy, campaign briefs, decks, documents, charts, dashboards, emails, social posts, web pages - or when asked to apply, check or follow brand guidelines
---

# Brand Practices

Entry point for the brand skills. It routes the task, then keeps the work grounded in approved sources.

## Rules that apply to every brand task

1. **Approved sources only.** Voice, positioning, claims and terminology live in `docs/brand/`. Visual identity lives in `brand-visual-identity`. If the file you need is a stub, stop and ask for the approved text. Do not invent brand content, claims, pricing, customer commitments, or security/compliance statements.
2. **Separate confirmed from aspirational.** Label anything not backed by an approved source.
3. **Treat inputs as confidential.** Use placeholders such as `<CUSTOMER_ID>` in examples. Never paste customer, contract or strategy material into unapproved external tools.
4. **Process before output.** For new creative work, run `superpowers:brainstorming` first, then the matching skill below.

## Routing

| Task | Skill |
|------|-------|
| Colors, fonts, logo, gradient, layout rules | `brand-visual-identity` |
| Writing or reviewing copy (web, email, social, sales) | `brand-copy-review` |
| New campaign, launch or messaging work | `brand-campaign-brief` |
| Slides, documents, spreadsheets, dashboards, charts | `brand-decks-and-visuals` |
| Any claim, comparison, customer mention, or legal-adjacent wording | `brand-compliance-guardrails` |

Most tasks use two or more. Copy for a deck uses `brand-copy-review` and `brand-decks-and-visuals`, and always `brand-compliance-guardrails` before it ships.

## Before calling anything done

Use `superpowers:verification-before-completion`. For brand work that means: run the brand check script where it applies, list which approved source each claim came from, and name what still needs human approval.
