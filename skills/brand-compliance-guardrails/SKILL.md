---
name: brand-compliance-guardrails
description: Use before publishing or sharing any marketing material that contains claims, comparisons, customer references, pricing, security or compliance statements, or legal-adjacent wording
---

# Compliance Guardrails

A pre-publish gate. It does not give legal advice; it finds what needs a human owner's approval.

## Gate checks

| # | Check | If it fails |
|---|-------|-------------|
| 1 | Each claim maps to a CONFIRMED entry in `docs/brand/positioning-and-claims.md` | Remove, soften, or mark UNAPPROVED and route to product marketing |
| 2 | No commitments, warranties, indemnities, SLAs, pricing, security or compliance claims from outside approved sources | Remove and route to legal/security owner |
| 3 | No unsupported superlatives or competitive claims | Remove or supply evidence |
| 4 | Customer names, logos, quotes and numbers have documented permission; none from another customer's confidential material | Remove |
| 5 | No implied endorsement, partnership or certification unless provided | Remove |
| 6 | Aspirational items are labelled as such; no promised dates or support levels | Reword as roadmap-with-caveat only if approved, otherwise remove |
| 7 | No secrets, credentials, internal hostnames, or personal data; examples use placeholders | Remove, and rotate any real secret that was shared |
| 8 | Regulated data is not moved across regions in the workflow (e.g. a data export or tool upload) | Flag to the data owner |
| 9 | Content was not pasted into an unapproved external tool | Stop and escalate |

## Report format

```
Gate result: pass / pass with approvals / blocked
Findings: <#, location, issue>
Approvals needed: <who, for what>
Assumptions and uncertainty: <what you could not verify>
```

Say "pass" only when every check was actually performed against a source. If a source file is a stub, the result is **blocked** or **pass with approvals**, never a clean pass.
