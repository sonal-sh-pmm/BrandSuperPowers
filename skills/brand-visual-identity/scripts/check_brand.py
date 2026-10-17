#!/usr/bin/env python3
"""Lint text files (HTML/CSS/SVG/JS/JSX/MD) against the HCLSW visual identity.

Flags:
  - hex colors outside the brand palette
  - font-family declarations without Arial
  - <img> tags with both width and height whose ratio is not 8:1 (logo files only)

Exit code 1 if any finding, else 0. Zero dependencies.
"""
import re
import sys
from pathlib import Path

PALETTE = {
    "17707f", "2ec0cb", "36d6d9", "aaffff", "0f5fdc", "3c91ff", "8ac6f8",
    "dce6f0", "000032", "ecf3f8", "000000", "14142b", "ffffff", "f7f7fc",
    "f4f4f4", "0b1d3a",
    # semantic data colors, allowed sparingly
    "00c3cd", "f5a623", "dc3545",
}
EXTS = {".html", ".htm", ".css", ".svg", ".js", ".jsx", ".ts", ".tsx", ".md"}
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
FONT = re.compile(r"font-family\s*:\s*([^;}\n]+)", re.IGNORECASE)
IMG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
ATTR = {n: re.compile(n + r'\s*=\s*["\']?(\d+(?:\.\d+)?)', re.IGNORECASE) for n in ("width", "height")}


def expand(h):
    h = h.lower()
    return "".join(c * 2 for c in h) if len(h) == 3 else h


def check(path):
    findings = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for i, line in enumerate(text.splitlines(), 1):
        for m in HEX.finditer(line):
            if expand(m.group(1)) not in PALETTE:
                findings.append((i, f"off-palette color #{m.group(1)}"))
        for m in FONT.finditer(line):
            if "arial" not in m.group(1).lower():
                findings.append((i, f"font-family without Arial: {m.group(1).strip()}"))
    for m in IMG.finditer(text):
        tag = m.group(0)
        if "logo" not in tag.lower():
            continue
        w, h = (ATTR[n].search(tag) for n in ("width", "height"))
        if w and h and float(h.group(1)) > 0:
            ratio = float(w.group(1)) / float(h.group(1))
            if abs(ratio - 8) > 0.1:
                line = text.count("\n", 0, m.start()) + 1
                findings.append((line, f"logo aspect ratio {ratio:.2f}:1, expected 8:1"))
    return findings


def main(args):
    if not args:
        print(__doc__)
        return 2
    files = []
    for a in args:
        p = Path(a)
        if p.is_dir():
            files += [f for f in p.rglob("*") if f.suffix.lower() in EXTS and ".git" not in f.parts]
        elif p.is_file():
            files.append(p)
        else:
            print(f"not found: {a}", file=sys.stderr)
            return 2
    total = 0
    for f in sorted(files):
        for line, msg in check(f):
            print(f"{f}:{line}: {msg}")
            total += 1
    print(f"{total} finding(s) in {len(files)} file(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
