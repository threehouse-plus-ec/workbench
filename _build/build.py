#!/usr/bin/env python3
"""
Workbench build script.

Converts all .md files in topic folders to minimalist HTML pages
following the T(h)reehouse +EC corporate design blueprint.

Pulls assets from threehouse-plus-ec/cd-rules (Model B).

Usage:
    python build.py

Output goes to _site/ for GitHub Pages deployment.
"""

import os
import re
import sys
import json
import hashlib
import shutil
import urllib.request
from pathlib import Path
from datetime import datetime

# --- Configuration ---

CD_REPO_RAW = "https://raw.githubusercontent.com/threehouse-plus-ec/cd-rules/main"
CD_ASSETS = {
    "tokens.css": f"{CD_REPO_RAW}/tokens.css",
    "emblem-32.svg": f"{CD_REPO_RAW}/emblem-32.svg",
    "emblem-64.svg": f"{CD_REPO_RAW}/emblem-64.svg",
    "wordmark-full.svg": f"{CD_REPO_RAW}/wordmark-full.svg",
    "wordmark-silent.svg": f"{CD_REPO_RAW}/wordmark-silent.svg",
}

ROOT = Path(__file__).parent.parent  # repo root (one level above _build/)
SITE_DIR = ROOT / "_site"
ASSETS_DIR = SITE_DIR / "assets"
SKIP_DIRS = {"_templates", "_build", "_site", ".github", "assets", "archive", ".git"}

# --- Asset fetching (Model B) ---

def fetch_assets():
    """Download CD assets and record checksums."""
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    checksums = {}
    for name, url in CD_ASSETS.items():
        dest = ASSETS_DIR / name
        try:
            urllib.request.urlretrieve(url, dest)
            h = hashlib.sha256(dest.read_bytes()).hexdigest()
            checksums[name] = h
            print(f"  ✓ {name} ({h[:12]}…)")
        except Exception as e:
            print(f"  ✗ {name}: {e}")
            # Fall back to local copy if available
            local = ROOT / "assets" / name
            if local.exists():
                shutil.copy2(local, dest)
                h = hashlib.sha256(dest.read_bytes()).hexdigest()
                checksums[name] = h
                print(f"    → used local fallback ({h[:12]}…)")
    # Write SOURCE.md
    source_md = ASSETS_DIR / "SOURCE.md"
    lines = [
        "# Asset Source Record",
        "",
        f"Fetched: {datetime.now(tz=__import__('datetime').timezone.utc).isoformat()}",
        f"Source: {CD_REPO_RAW}",
        "",
        "| File | SHA-256 |",
        "| --- | --- |",
    ]
    for name, h in sorted(checksums.items()):
        lines.append(f"| {name} | `{h}` |")
    source_md.write_text("\n".join(lines) + "\n")


# --- Markdown to HTML ---

def parse_frontmatter(text):
    """Extract YAML frontmatter as a dict."""
    fm = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            block = text[3:end].strip()
            body = text[end + 3:].strip()
            for line in block.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
            return fm, body
    return fm, text


def md_to_html_body(md_text):
    """
    Minimal Markdown to HTML converter.
    Handles: headings, paragraphs, bold, italic, inline code,
    code blocks, links, horizontal rules, blockquotes,
    unordered and ordered lists.
    """
    lines = md_text.split("\n")
    html_parts = []
    in_code_block = False
    code_lang = ""
    code_lines = []
    in_list = False
    list_type = None  # 'ul' or 'ol'
    in_blockquote = False
    bq_lines = []

    def inline(text):
        """Process inline formatting."""
        # Code spans first (protect from other processing)
        parts = []
        i = 0
        while i < len(text):
            tick = text.find("`", i)
            if tick == -1:
                parts.append(text[i:])
                break
            parts.append(text[i:tick])
            end_tick = text.find("`", tick + 1)
            if end_tick == -1:
                parts.append(text[tick:])
                break
            parts.append(f'<code>{escape(text[tick+1:end_tick])}</code>')
            i = end_tick + 1
        text = "".join(parts)
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # Links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        return text

    def escape(text):
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            tag = list_type
            html_parts.append(f"</{tag}>")
            in_list = False
            list_type = None

    def flush_blockquote():
        nonlocal in_blockquote, bq_lines
        if in_blockquote:
            content = " ".join(bq_lines)
            html_parts.append(f'<blockquote><p>{inline(content)}</p></blockquote>')
            in_blockquote = False
            bq_lines = []

    for line in lines:
        stripped = line.strip()

        # Code blocks
        if stripped.startswith("```"):
            if in_code_block:
                html_parts.append(f'<pre><code>{chr(10).join(code_lines)}</code></pre>')
                in_code_block = False
                code_lines = []
            else:
                flush_list()
                flush_blockquote()
                in_code_block = True
                code_lang = stripped[3:].strip()
            continue
        if in_code_block:
            code_lines.append(escape(line))
            continue

        # Horizontal rule
        if re.match(r'^-{3,}$', stripped) or re.match(r'^\*{3,}$', stripped):
            flush_list()
            flush_blockquote()
            html_parts.append('<hr class="section-rule">')
            continue

        # Blockquote
        if stripped.startswith("> "):
            flush_list()
            if not in_blockquote:
                in_blockquote = True
                bq_lines = []
            bq_lines.append(stripped[2:])
            continue
        elif in_blockquote:
            if stripped == "":
                flush_blockquote()
            else:
                flush_blockquote()

        # Headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if heading_match:
            flush_list()
            level = len(heading_match.group(1))
            text = heading_match.group(2)
            slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
            if level == 1:
                html_parts.append(f'<h1 id="{slug}">{inline(text)}</h1>')
            elif level == 2:
                html_parts.append(f'<hr class="section-rule">')
                html_parts.append(f'<h2 id="{slug}">{inline(text)}</h2>')
            else:
                html_parts.append(f'<h{level} id="{slug}">{inline(text)}</h{level}>')
            continue

        # Unordered list
        ul_match = re.match(r'^[-*+]\s+(.+)$', stripped)
        if ul_match:
            flush_blockquote()
            if not in_list or list_type != "ul":
                flush_list()
                html_parts.append("<ul>")
                in_list = True
                list_type = "ul"
            html_parts.append(f"<li>{inline(ul_match.group(1))}</li>")
            continue

        # Ordered list
        ol_match = re.match(r'^\d+\.\s+(.+)$', stripped)
        if ol_match:
            flush_blockquote()
            if not in_list or list_type != "ol":
                flush_list()
                html_parts.append("<ol>")
                in_list = True
                list_type = "ol"
            html_parts.append(f"<li>{inline(ol_match.group(1))}</li>")
            continue

        # Empty line
        if stripped == "":
            flush_list()
            continue

        # Paragraph
        flush_list()
        html_parts.append(f"<p>{inline(stripped)}</p>")

    # Flush remaining
    flush_list()
    flush_blockquote()
    if in_code_block:
        html_parts.append(f'<pre><code>{chr(10).join(code_lines)}</code></pre>')

    return "\n".join(html_parts)


def status_marker(status):
    """Return HTML for a status badge."""
    if status == "draft":
        return '<span class="status-badge status-draft">DRAFT</span>'
    elif status == "frozen":
        return '<span class="status-badge status-frozen">FROZEN</span>'
    return ""


def type_label(doc_type):
    """Return a display label for the document type."""
    labels = {
        "breakwater": "Breakwater · Claim Analysis",
        "reference": "Reference Note",
        "essay": "Essay · Sail",
    }
    return labels.get(doc_type, doc_type.title() if doc_type else "")


def build_page(fm, body_html, rel_path):
    """Wrap body HTML in a full blueprint-compliant page."""
    title = fm.get("title", rel_path)
    status = fm.get("status", "")
    doc_type = fm.get("type", "")
    date = fm.get("date", "")
    topic = fm.get("topic", "")

    badge = status_marker(status)
    label = type_label(doc_type)
    depth = rel_path.count("/")
    asset_prefix = "../" * depth + "assets/"

    date_line = f'<p class="meta-date">{date}</p>' if date else ""
    topic_line = f'<p class="meta-topic">Topic: {topic}</p>' if topic else ""
    label_line = f'<p class="section-heading">{label}</p>' if label else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Workbench</title>
<link rel="icon" href="{asset_prefix}emblem-32.svg" type="image/svg+xml">
<link rel="stylesheet" href="{asset_prefix}tokens.css">
<style>
:root {{ color-scheme: light; }}
* {{ box-sizing: border-box; }}
html, body {{
  margin: 0;
  min-height: 100%;
  background: var(--parchment);
  color: var(--ink);
}}
body {{
  font-family: var(--font-serif);
  font-size: 17px;
  line-height: 1.68;
}}
@media (max-width: 640px) {{
  body {{ font-size: 16px; }}
}}
:focus-visible {{
  outline: var(--focus-ring);
  outline-offset: var(--focus-offset);
}}

/* Shell */
.page-shell {{
  width: min(calc(100% - 3rem), 38rem);
  margin: 0 auto;
  padding: 2rem 0 4rem;
}}
@media (max-width: 640px) {{
  .page-shell {{
    width: min(calc(100% - 2.5rem), 38rem);
  }}
}}

/* Header */
.page-header {{
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 3rem;
  text-decoration: none;
  color: inherit;
}}
.page-header img:first-child {{
  width: 32px; height: 32px; flex: none;
}}
.page-header img:last-child {{
  width: 7.05rem; height: auto; flex: none;
}}

/* Meta */
.section-heading {{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  color: var(--sea);
  margin: 0 0 0.3rem;
}}
.meta-date, .meta-topic {{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  color: var(--stone);
  margin: 0.2rem 0;
}}

/* Status badges */
.status-badge {{
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  padding: 0.15em 0.5em;
  border: 1px solid;
  margin-left: 0.5rem;
  vertical-align: middle;
}}
.status-draft {{
  color: var(--sea);
  border-color: var(--sea);
}}
.status-frozen {{
  color: var(--signal);
  border-color: var(--signal);
}}

/* Content */
h1 {{
  font-family: var(--font-serif);
  font-size: 1.9rem;
  line-height: 1.08;
  font-weight: 400;
  margin: 0.5rem 0 1.5rem;
}}
h2 {{
  font-family: var(--font-serif);
  font-size: 1.35rem;
  line-height: 1.2;
  font-weight: 400;
  margin: 2rem 0 0.8rem;
}}
h3 {{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  font-weight: 500;
  color: var(--sea);
  margin: 1.5rem 0 0.5rem;
}}
h4, h5, h6 {{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  font-weight: 500;
  color: var(--ink);
  margin: 1.2rem 0 0.4rem;
}}
p {{
  max-width: var(--measure);
  margin: 0 0 0.85rem;
}}
a {{
  color: var(--sea);
}}
strong {{
  font-weight: 600;
}}
blockquote {{
  margin: 1rem 0;
  padding: 1rem 1.25rem;
  background: var(--warm-white);
  border-left: 3px solid var(--sea);
  font-style: italic;
}}
blockquote p {{
  margin: 0;
}}
pre {{
  background: var(--warm-white);
  border: 1px solid var(--grid);
  padding: 1rem;
  overflow-x: auto;
  font-family: var(--font-mono);
  font-size: 0.82rem;
  line-height: 1.5;
}}
code {{
  font-family: var(--font-mono);
  font-size: 0.88em;
  background: var(--warm-white);
  padding: 0.1em 0.3em;
  border: 1px solid var(--grid);
}}
pre code {{
  background: none;
  border: none;
  padding: 0;
  font-size: inherit;
}}
ul, ol {{
  padding-left: 1.2rem;
  margin: 0.5rem 0 1rem;
}}
li {{
  margin-bottom: 0.3rem;
}}
hr.section-rule {{
  width: 1.5rem;
  height: 1px;
  margin: 2.5rem 0 1.2rem;
  border: 0;
  background: var(--grid);
}}

/* Classification badges for Breakwater */
.classification {{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 500;
  padding: 0.2em 0.6em;
  display: inline-block;
}}

/* Footer */
.page-footer {{
  margin-top: 4rem;
  padding-top: 1rem;
  border-top: 1px solid var(--grid);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--stone);
}}
.page-footer a {{
  color: var(--stone);
}}
</style>
</head>
<body>
<div class="page-shell">
  <a class="page-header" href="{asset_prefix}../index.html" aria-label="Back to workbench index">
    <img src="{asset_prefix}emblem-32.svg" alt="">
    <img src="{asset_prefix}wordmark-silent.svg" alt="T[h]ree">
  </a>
  <main>
    {label_line}
    {date_line}
    {topic_line}
    {body_html}
  </main>
  <footer class="page-footer">
    <p><a href="{asset_prefix}../index.html">← Workbench index</a></p>
    <p>T(h)reehouse +EC · Local candidate framework</p>
  </footer>
</div>
</body>
</html>"""


def build_index(pages):
    """Build the index page grouping entries by topic."""
    # Group by topic
    topics = {}
    for p in pages:
        topic = p["topic"] or "ungrouped"
        topics.setdefault(topic, []).append(p)

    sections_html = []
    for topic in sorted(topics.keys()):
        entries = topics[topic]
        sections_html.append(f'<hr class="section-rule">')
        sections_html.append(f'<h2>{topic}</h2>')

        # Group by type within topic
        by_type = {}
        for e in entries:
            t = e.get("type", "other")
            by_type.setdefault(t, []).append(e)

        for doc_type in ["breakwater", "reference", "essay", "other"]:
            if doc_type not in by_type:
                continue
            label = type_label(doc_type) or doc_type.title()
            sections_html.append(f'<h3>{label}</h3>')
            sections_html.append('<ul>')
            for e in sorted(by_type[doc_type], key=lambda x: x.get("date", "")):
                status = e.get("status", "")
                badge = status_marker(status) if status in ("draft", "frozen") else ""
                title = e.get("title", e["path"])
                sections_html.append(
                    f'<li><a href="{e["path"]}">{title}</a>{badge}</li>'
                )
            sections_html.append('</ul>')

    body = "\n".join(sections_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Workbench — T(h)reehouse +EC</title>
<link rel="icon" href="assets/emblem-32.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/tokens.css">
<style>
:root {{ color-scheme: light; }}
* {{ box-sizing: border-box; }}
html, body {{
  margin: 0;
  min-height: 100%;
  background: var(--parchment);
  color: var(--ink);
}}
body {{
  font-family: var(--font-serif);
  font-size: 17px;
  line-height: 1.68;
}}
@media (max-width: 640px) {{
  body {{ font-size: 16px; }}
}}
:focus-visible {{
  outline: var(--focus-ring);
  outline-offset: var(--focus-offset);
}}
.page-shell {{
  width: min(calc(100% - 3rem), 38rem);
  margin: 0 auto;
  padding: 2rem 0 4rem;
}}
@media (max-width: 640px) {{
  .page-shell {{
    width: min(calc(100% - 2.5rem), 38rem);
  }}
}}
.page-header {{
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 2rem;
  text-decoration: none;
  color: inherit;
}}
.page-header img:first-child {{
  width: 32px; height: 32px; flex: none;
}}
.page-header img:last-child {{
  width: 7.05rem; height: auto; flex: none;
}}
h1 {{
  font-family: var(--font-serif);
  font-size: 1.9rem;
  line-height: 1.08;
  font-weight: 400;
  margin: 0 0 0.5rem;
}}
.intro {{
  font-size: 1.15rem;
  line-height: 1.55;
  margin: 0 0 1rem;
  max-width: var(--measure);
}}
h2 {{
  font-family: var(--font-serif);
  font-size: 1.35rem;
  line-height: 1.2;
  font-weight: 400;
  margin: 1.5rem 0 0.5rem;
}}
h3 {{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  font-weight: 500;
  color: var(--sea);
  margin: 1rem 0 0.4rem;
}}
hr.section-rule {{
  width: 1.5rem;
  height: 1px;
  margin: 2.5rem 0 1.2rem;
  border: 0;
  background: var(--grid);
}}
ul {{
  padding-left: 1.2rem;
  margin: 0.3rem 0 1rem;
}}
li {{
  margin-bottom: 0.3rem;
}}
a {{
  color: var(--sea);
}}
.section-heading {{
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  color: var(--sea);
}}
.status-badge {{
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.3;
  padding: 0.15em 0.5em;
  border: 1px solid;
  margin-left: 0.5rem;
  vertical-align: middle;
}}
.status-draft {{
  color: var(--sea);
  border-color: var(--sea);
}}
.status-frozen {{
  color: var(--signal);
  border-color: var(--signal);
}}
.page-footer {{
  margin-top: 4rem;
  padding-top: 1rem;
  border-top: 1px solid var(--grid);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--stone);
}}
.page-footer a {{
  color: var(--stone);
}}
</style>
</head>
<body>
<div class="page-shell">
  <div class="page-header">
    <img src="assets/emblem-32.svg" alt="">
    <img src="assets/wordmark-full.svg" alt="T[h]ree +EC">
  </div>
  <main>
    <p class="section-heading">Workbench</p>
    <h1>Essay and Breakwater workspace</h1>
    <p class="intro">
      Topics are organised as self-contained folders, each with Breakwater analysis,
      reference notes, and essay drafts. Select a document below.
    </p>
    <p><a href="BLUEPRINT.html">→ Methodology blueprint</a></p>
    {body}
  </main>
  <footer class="page-footer">
    <p>T(h)reehouse +EC · Local candidate framework</p>
    <p>The emblem is the seed; the network is its recursive unfolding.</p>
  </footer>
</div>
</body>
</html>"""


# --- Main ---

def main():
    print("Workbench build")
    print("=" * 40)

    # Clean
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)

    # Fetch assets
    print("\nFetching CD assets...")
    fetch_assets()

    # Find all .md files in topic folders
    print("\nScanning for .md files...")
    pages = []

    # Also build BLUEPRINT.md at root level
    blueprint_path = ROOT / "BLUEPRINT.md"
    if blueprint_path.exists():
        text = blueprint_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        body_html = md_to_html_body(body)
        page_html = build_page(
            {**fm, "title": fm.get("title", "Workbench Blueprint")},
            body_html,
            "BLUEPRINT.html"
        )
        out_path = SITE_DIR / "BLUEPRINT.html"
        out_path.write_text(page_html, encoding="utf-8")
        print(f"  ✓ BLUEPRINT.html")

    for entry in sorted(ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in SKIP_DIRS or entry.name.startswith("."):
            continue

        # This is a topic folder
        topic_name = entry.name
        for md_file in sorted(entry.rglob("*.md")):
            rel = md_file.relative_to(ROOT)
            rel_html = rel.with_suffix(".html")

            text = md_file.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(text)

            # Auto-detect type from folder
            if not fm.get("type"):
                parent = md_file.parent.name
                if parent in ("breakwater", "references", "essay"):
                    fm["type"] = parent.rstrip("s")  # references -> reference

            if not fm.get("topic"):
                fm["topic"] = topic_name

            body_html = md_to_html_body(body)
            page_html = build_page(fm, body_html, str(rel_html))

            out_path = SITE_DIR / rel_html
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(page_html, encoding="utf-8")

            pages.append({
                "path": str(rel_html),
                "title": fm.get("title", md_file.stem),
                "date": fm.get("date", ""),
                "status": fm.get("status", ""),
                "type": fm.get("type", ""),
                "topic": fm.get("topic", topic_name),
            })
            print(f"  ✓ {rel_html}")

    # Build index
    print("\nBuilding index...")
    index_html = build_index(pages)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print("  ✓ index.html")

    # .nojekyll for GitHub Pages
    (SITE_DIR / ".nojekyll").write_text("")

    print(f"\nDone. {len(pages)} pages built in _site/")


if __name__ == "__main__":
    main()
