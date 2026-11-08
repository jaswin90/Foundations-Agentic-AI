#!/usr/bin/env python3
"""Build a redirect-only site for the book's old address.

The book is now published inside the library at
https://jaswin90.github.io/library/AI_Engineering/Foundations-Agentic-AI/ (synced from docs/ by the
jaswin90.github.io repository). The old project address https://jaswin90.github.io/Foundations-Agentic-AI/
keeps working: every page there redirects to the same page in the library, keeping #anchors.

Usage: python3 tools/build_redirects.py OUT_DIR
"""
import html, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NEW = '/library/AI_Engineering/Foundations-Agentic-AI/'
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
(out / '.nojekyll').write_text('')
n = 0
for p in (ROOT / 'docs').rglob('*.html'):
    rel = p.relative_to(ROOT / 'docs').as_posix()
    target = NEW + ('' if rel == 'index.html' else rel)
    t = html.escape(target)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Moved to the library</title>
<link rel="canonical" href="https://jaswin90.github.io{t}">
<meta http-equiv="refresh" content="0; url={t}">
<script>location.replace({target!r} + location.search + location.hash);</script>
</head><body><p>This book has moved to <a href="{t}">the library</a>.</p></body></html>
'''
    d = out / rel; d.parent.mkdir(parents=True, exist_ok=True); d.write_text(page); n += 1
print('redirect pages:', n)
