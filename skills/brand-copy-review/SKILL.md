---
name: brand-copy-review
description: Use when writing, editing or reviewing marketing copy - web pages, emails, social posts, sales content, press text - before it is shared or published
---

# Brand Copy Review

Review and draft copy against approved sources, not taste.

## Inputs (stop if missing)

- `docs/brand/voice-and-tone.md`
- `docs/brand/terminology.md`
- `docs/brand/positioning-and-claims.md`

If any is still a stub, say so, ask for the approved text, and limit the review to the checks below that need no source (marked **no source needed**). Do not infer a voice from existing copy.

## Process

1. Identify the channel, audience and goal of the piece. Ask if unclear.
2. Run the checklist. Record each finding as: location, issue, evidence, suggested fix.
3. Separate **must fix** (claims, terminology, accuracy) from **suggestions** (style).
4. Give the revised copy only after the findings, and keep the author's meaning.

## Checklist

| Check | Source |
|-------|--------|
| Every factual or capability claim appears in `positioning-and-claims.md` as CONFIRMED | claims file |
| No claim is aspirational presented as fact; no promised timelines, pricing or support levels | claims file |
| No unsupported superlatives ("best", "leading", "only", "fastest") or competitor comparisons without evidence | claims file |
| No implied endorsement, partnership or certification unless provided | **no source needed** |
| Product names, capitalisation and trademarks match terminology | terminology |
| Voice and tone match the channel guidance | voice file |
| No customer names, quotes or figures without documented permission | **no source needed** |
| No secrets, internal-only details or PII; placeholders used in examples | **no source needed** |
| Clear, specific, one call to action; no filler | **no source needed** |

## Output format

```
Verdict: ready / needs changes / blocked (missing sources)
Must fix: ...
Suggestions: ...
Needs approval from: <legal/product marketing/...>
Revised copy: ...
```

Run `brand-compliance-guardrails` as well before anything is published.
