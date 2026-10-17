# Brand source of truth

The brand skills in `skills/brand-*` read these files. They never invent brand
content. If a file below is still a stub, the skill stops and asks for the
approved text instead of guessing.

| File | Owner | Status |
|------|-------|--------|
| `visual-identity` (in `skills/brand-visual-identity/`) | Brand | Populated from the HCLSW brand kit skill |
| `voice-and-tone.md` | Marketing / Brand | **Stub: needs approved content** |
| `positioning-and-claims.md` | Product Marketing | **Stub: needs approved content** |
| `terminology.md` | Marketing / Legal | **Stub: needs approved content** |
| `briefs/` | Campaign owners | Output folder for `brand-campaign-brief` |

Rule of thumb: confirmed facts go in these files with a source and date;
aspirational statements are labelled `ASPIRATIONAL` and are never used as claims.
