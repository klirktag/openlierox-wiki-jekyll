#!/usr/bin/env python3
"""Convert the Jekyll wiki articles to MediaWiki wikitext.

Reads every page in _wiki/*.md and writes:
  - mediawiki/<Page_Name>.wiki         one wikitext file per article
  - mediawiki/openlierox-wiki.xml      bulk Special:Import dump

The original wiki ran MediaWiki, so this round-trips the content back to
its native syntax. Internal links, images, headings, bold/italic, lists
and fenced code blocks all get converted; embedded HTML (tables, image
thumbnails) is preserved because MediaWiki accepts inline HTML.
"""

import glob
import html
import os
import re
import sys
from xml.sax.saxutils import escape as xml_escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "_wiki")
OUT = os.path.join(ROOT, "mediawiki")


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------
def parse_front_matter(text):
    """Return (front_matter_dict, body) for a Jekyll markdown file."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    fm_text, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_text.split("\n"):
        if not line.strip() or ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip()
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
        elif (v.startswith('"') and v.endswith('"')) or (
            v.startswith("'") and v.endswith("'")
        ):
            v = v[1:-1]
        fm[k] = v
    return fm, body


def strip_raw_wrapper(body):
    body = body.strip()
    if body.startswith("{% raw %}"):
        body = body[len("{% raw %}"):].lstrip("\n")
    if body.endswith("{% endraw %}"):
        body = body[:-len("{% endraw %}")].rstrip()
    return body


# --------------------------------------------------------------------------
# Helpers to build wikitext links / file refs
# --------------------------------------------------------------------------
def wiki_link_from_url(url, text):
    """Turn an href into a MediaWiki link. None if it doesn't look like one."""
    url = html.unescape(url or "")
    # /wiki/index.php/Page/  or  /wiki/index.php/Page/#anchor
    m = re.match(r"^/wiki/index\.php/([^/?#]+)/?(#.+)?$", url)
    if m:
        target = m.group(1).replace("_", " ").rstrip()
        anchor = (m.group(2) or "")
        target_with_anchor = target + anchor
        if text in (target, m.group(1), target_with_anchor):
            return f"[[{target_with_anchor}]]"
        return f"[[{target_with_anchor}|{text}]]"
    if url.startswith("#"):
        if text == url[1:]:
            return f"[[{url}]]"
        return f"[[{url}|{text}]]"
    if url.startswith(("http://", "https://", "ftp://", "mailto:", "irc://")):
        if text == url:
            return url
        return f"[{url} {text}]"
    return None


def wiki_file_from_url(url, alt=""):
    """Turn an /wiki/images/... src into [[File:Name|alt]] (None otherwise)."""
    url = html.unescape(url or "")
    m = re.match(
        r"^/wiki/images/(?:thumb/)?[a-f0-9]/[a-f0-9]{1,2}/(?:[^/]+/)?([^/?#]+)$",
        url,
    )
    if not m:
        return None
    name = re.sub(r"^\d+px-", "", m.group(1))
    # Strip MediaWiki's auto-generated "Image:<filename>" alt text -- it is
    # redundant for the new wiki and clutters the wikitext.
    if alt and re.match(r"^(Image|File):", alt, re.I):
        alt = ""
    if alt:
        return f"[[File:{name}|{alt}]]"
    return f"[[File:{name}]]"


# --------------------------------------------------------------------------
# Markdown body -> wikitext
# --------------------------------------------------------------------------
HTML_LINK_RE = re.compile(
    r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.I | re.S
)
HTML_IMG_RE = re.compile(r"<img\s+[^>]*?>", re.I)
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')


def rewrite_html_anchors(body):
    """Replace <a href="/wiki/index.php/X/">T</a> with wikitext links where
    possible. HTML anchors with mediawiki-style hrefs are converted; external
    links and other anchors are left alone (they remain valid HTML inside
    MediaWiki wikitext).
    """
    def repl(m):
        href, inner = m.group(1), m.group(2)
        # only rewrite if inner is plain text (no nested tags)
        if "<" in inner:
            return m.group(0)
        text = re.sub(r"\s+", " ", inner).strip()
        wl = wiki_link_from_url(href, text)
        if wl is None or wl == text:
            return m.group(0)
        return wl
    return HTML_LINK_RE.sub(repl, body)


def rewrite_html_images(body):
    """Replace <img src="/wiki/images/..."> with [[File:Name|alt]]."""
    def repl(m):
        tag = m.group(0)
        attrs = dict(ATTR_RE.findall(tag))
        src = attrs.get("src", "")
        alt = attrs.get("alt", "").strip()
        wf = wiki_file_from_url(src, alt)
        return wf if wf else tag
    return HTML_IMG_RE.sub(repl, body)


def convert_fenced_code(md):
    """``` ... ``` -> <syntaxhighlight> / <pre>."""
    out, in_code, lang, buf = [], False, "", []
    for line in md.split("\n"):
        if not in_code:
            m = re.match(r"^```(\w*)\s*$", line)
            if m:
                in_code = True
                lang = m.group(1)
                buf = []
                continue
            out.append(line)
        else:
            if line.strip() == "```":
                if lang:
                    out.append(f'<syntaxhighlight lang="{lang}">')
                else:
                    out.append("<pre>")
                out.extend(buf)
                out.append("</syntaxhighlight>" if lang else "</pre>")
                in_code = False
                continue
            buf.append(line)
    if in_code:
        out.append("<pre>")
        out.extend(buf)
        out.append("</pre>")
    return "\n".join(out)


def md_to_wikitext(md):
    md = convert_fenced_code(md)

    # Rewrite embedded HTML <a> and <img> first so the rest works uniformly.
    md = rewrite_html_anchors(md)
    md = rewrite_html_images(md)

    # Markdown images: ![alt](src)
    def image(m):
        alt, src = m.group(1), m.group(2)
        wf = wiki_file_from_url(src, alt)
        return wf if wf else f"[{src} {alt or src}]"
    md = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image, md)

    # Markdown links: [text](url)
    def link(m):
        text, url = m.group(1), m.group(2)
        wl = wiki_link_from_url(url, text)
        return wl if wl is not None else f"[{url} {text}]"
    md = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", link, md)

    # Headings: ## -> ==, ### -> ===, ...
    def heading(m):
        eq = "=" * len(m.group(1))
        return f"{eq} {m.group(2).strip()} {eq}"
    md = re.sub(r"^(#{1,6})\s+(.+?)\s*#*\s*$", heading, md, flags=re.M)

    # Bold then italic
    md = re.sub(r"\*\*([^*\n]+)\*\*", r"'''\1'''", md)
    md = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"''\1''", md)

    # Inline code
    md = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", md)

    # Lists: keep nesting depth by counting leading spaces (2-per-level)
    new = []
    for line in md.split("\n"):
        m = re.match(r"^(\s*)\*\s+(.*)$", line)
        if m:
            depth = len(m.group(1)) // 2 + 1
            new.append("*" * depth + " " + m.group(2))
            continue
        m = re.match(r"^(\s*)\d+\.\s+(.*)$", line)
        if m:
            depth = len(m.group(1)) // 2 + 1
            new.append("#" * depth + " " + m.group(2))
            continue
        new.append(line)
    md = "\n".join(new)

    # Horizontal rule
    md = re.sub(r"^-{3,}\s*$", "----", md, flags=re.M)

    # Fix literal brackets surrounding an external link: in the source the
    # author wrote "[link]"; after conversion we'd get [[https://... text]],
    # which MediaWiki would interpret as an internal link. Restore the
    # author's intent by spacing the brackets out.
    md = re.sub(
        r"\[\[(https?://[^\s\]]+)\s+([^\]]+?)\]\]",
        r"[ [\1 \2] ]",
        md,
    )

    return md.strip() + "\n"


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def convert_file(path):
    text = open(path, encoding="utf-8").read()
    fm, body = parse_front_matter(text)
    body = strip_raw_wrapper(body)
    wikitext = md_to_wikitext(body)

    cats = fm.get("categories") or []
    if isinstance(cats, str):
        cats = [cats]
    if cats:
        wikitext = wikitext.rstrip() + "\n\n"
        for cat in cats:
            wikitext += f"[[Category:{cat}]]\n"

    archived = fm.get("archived_url")
    if archived:
        # tiny provenance footer so MediaWiki admins can trace the source
        wikitext = (wikitext.rstrip()
                    + "\n\n<!-- imported from Wayback Machine: "
                    + archived + " -->\n")

    title = fm.get("title") or os.path.basename(path)[:-3].replace("_", " ")
    return title, wikitext


def write_xml_dump(pages, xml_path):
    with open(xml_path, "w", encoding="utf-8") as fh:
        fh.write('<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/" '
                 'version="0.11" xml:lang="en">\n')
        fh.write("  <siteinfo>\n")
        fh.write("    <sitename>OpenLieroX Wiki</sitename>\n")
        fh.write("    <dbname>openlierox</dbname>\n")
        fh.write("    <base>https://www.openlierox.net/wiki/index.php/Main_Page</base>\n")
        fh.write("    <generator>openlierox-wiki-jekyll re-creation</generator>\n")
        fh.write("    <case>first-letter</case>\n")
        fh.write("    <namespaces>\n")
        fh.write('      <namespace key="0" case="first-letter" />\n')
        fh.write('      <namespace key="14" case="first-letter">Category</namespace>\n')
        fh.write('      <namespace key="6" case="first-letter">File</namespace>\n')
        fh.write("    </namespaces>\n")
        fh.write("  </siteinfo>\n")
        for i, (title, wikitext) in enumerate(pages, 1):
            ns = "14" if title.startswith("Category:") else "0"
            fh.write("  <page>\n")
            fh.write(f"    <title>{xml_escape(title)}</title>\n")
            fh.write(f"    <ns>{ns}</ns>\n")
            fh.write(f"    <id>{i}</id>\n")
            fh.write("    <revision>\n")
            fh.write(f"      <id>{i}</id>\n")
            fh.write("      <timestamp>2014-01-01T00:00:00Z</timestamp>\n")
            fh.write("      <contributor>\n")
            fh.write("        <username>WaybackImport</username>\n")
            fh.write("        <id>1</id>\n")
            fh.write("      </contributor>\n")
            fh.write("      <comment>Imported from Internet Archive Wayback Machine</comment>\n")
            fh.write("      <model>wikitext</model>\n")
            fh.write("      <format>text/x-wiki</format>\n")
            n = len(wikitext.encode("utf-8"))
            fh.write(f'      <text xml:space="preserve" bytes="{n}">'
                     f"{xml_escape(wikitext)}</text>\n")
            fh.write("      <sha1></sha1>\n")
            fh.write("    </revision>\n")
            fh.write("  </page>\n")
        fh.write("</mediawiki>\n")


def main():
    os.makedirs(OUT, exist_ok=True)
    pages = []
    for path in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        title, wikitext = convert_file(path)
        fname = os.path.basename(path)[:-3] + ".wiki"
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as fh:
            fh.write(wikitext)
        pages.append((title, wikitext))
    write_xml_dump(pages, os.path.join(OUT, "openlierox-wiki.xml"))
    print(f"wrote {len(pages)} .wiki files and openlierox-wiki.xml")


if __name__ == "__main__":
    main()
