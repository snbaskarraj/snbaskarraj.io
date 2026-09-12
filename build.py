#!/usr/bin/env python3
"""Wrap .artifact-source.html into a standalone index.html for GitHub Pages.

The source file is authored as artifact body content (no doctype/head/body),
so it can be published to claude.ai unchanged. GitHub serves files raw, so the
published copy needs a real document shell - most importantly the viewport meta,
without which the page renders desktop-width on phones.
"""
import pathlib

here = pathlib.Path(__file__).parent
src = (here / '.artifact-source.html').read_text(encoding='utf-8')
i = src.index('</style>') + len('</style>')
head_part, body_part = src[:i], src[i:]

SHELL = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Baskarraj S N - Senior Engineering Manager and Director of Engineering. Data platforms, applied AI and agentic systems. 22+ years in software engineering, 9+ years leading engineers and engineering managers.">
<meta name="author" content="Baskarraj S N">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="https://snbaskarraj.github.io/snbaskarraj.io/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%230B6E63'/%3E%3Ctext x='32' y='44' font-family='Helvetica,Arial,sans-serif' font-size='34' font-weight='700' fill='%23F4F5F1' text-anchor='middle'%3EB%3C/text%3E%3C/svg%3E">
<meta property="og:type" content="profile">
<meta property="og:title" content="Baskarraj S N - Engineering Leader">
<meta property="og:description" content="Data platforms, applied AI and agentic systems. Governed agent layers on MCP, evals as release gates, lakehouse platforms used by 10,000+ engineers.">
<meta property="og:url" content="https://snbaskarraj.github.io/snbaskarraj.io/">
<meta property="og:image" content="https://snbaskarraj.github.io/snbaskarraj.io/portrait.jpg">
<meta name="twitter:card" content="summary">
<style>
  html { color-scheme: light dark; }
  body { margin: 0; }
  img { max-width: 100%; }
  [hidden] { display: none !important; }
</style>
'''

out = SHELL + head_part + '\n</head>\n<body>\n' + body_part.strip() + '\n</body>\n</html>\n'
(here / 'index.html').write_text(out, encoding='utf-8')
print('index.html:', len(out), 'bytes')
