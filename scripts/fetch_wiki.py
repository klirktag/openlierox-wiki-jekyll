#!/usr/bin/env python3
"""Reconstruct the OpenLieroX MediaWiki from the Internet Archive.

Pipeline:
  1. Query the Wayback Machine CDX API for every archived wiki article.
  2. Download the latest good snapshot of each page (raw, via the `id_`
     modifier so no Wayback toolbar is injected).
  3. Strip the MediaWiki chrome, rewrite internal links/images, and convert
     the article body to Markdown (markdownify), keeping tables and image
     thumbnails as small HTML blocks.
  4. Write Jekyll collection documents into ../_wiki/ and record every
     referenced image into scripts/images.tsv for a later download pass.

The script is resumable: pages already converted are skipped.
"""

import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup, Comment, NavigableString
from markdownify import markdownify as md

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WIKI_DIR = os.path.join(ROOT, "_wiki")
MANIFEST = os.path.join(HERE, "manifest.json")
IMAGES_TSV = os.path.join(HERE, "images.tsv")

UA = {"User-Agent": "Mozilla/5.0 (OpenLieroX wiki archival re-creation)"}

# MediaWiki namespaces we do NOT reproduce (user/talk/maintenance pages).
SKIP_NS = {
    "user", "user_talk", "talk", "special", "image", "file", "template",
    "template_talk", "mediawiki", "category", "moderation",
    "openlierox_wiki_talk", "help_talk",
}


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def get(url, tries=6, raw=True):
    """Fetch a URL with retries; returns bytes or None."""
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=45) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            wait = 3 * (attempt + 1)
            sys.stderr.write(f"  retry {attempt + 1}/{tries} ({exc}) in {wait}s\n")
            time.sleep(wait)
    return None


def wb_raw(timestamp, original_url):
    """Wayback 'identity' URL: the archived resource with no rewriting."""
    return f"https://web.archive.org/web/{timestamp}id_/{original_url}"


def page_basename(name):
    """MediaWiki page title -> safe flat filename / URL segment.

    'Liero 1.0'  -> 'Liero_1.0'      'Lua:Worm' -> 'Lua_Worm'
    'Firefox/2'  -> 'Firefox_2'
    """
    name = urllib.parse.unquote(name)
    name = name.replace(" ", "_")
    name = name.replace(":", "_").replace("/", "_")
    name = re.sub(r"_+", "_", name).strip("_")
    return name


def title_from_name(name):
    """Underscored MediaWiki name -> human title ('Liero_1.0' -> 'Liero 1.0')."""
    return urllib.parse.unquote(name).replace("_", " ").strip()


# --------------------------------------------------------------------------
# Step 1 - build the manifest of pages from the CDX API
# --------------------------------------------------------------------------
def snapshot_rank(ts):
    """Lower is better. The wiki was healthy ~2009-2014; later snapshots
    increasingly captured PHP error pages, so prefer the good era and, within
    a tier, the most recent capture."""
    year = ts[:4]
    if "2009" <= year <= "2014":
        tier = 0
    elif "2015" <= year <= "2017":
        tier = 1
    elif year < "2009":
        tier = 2
    else:
        tier = 3
    # newest-first inside a tier -> negate the timestamp
    return (tier, -int(ts))


def build_manifest():
    if os.path.exists(MANIFEST):
        with open(MANIFEST) as fh:
            return json.load(fh)

    print("Querying Wayback CDX API for the page list ...")
    cdx = (
        "http://web.archive.org/cdx/search/cdx?"
        "url=openlierox.net/wiki/index.php/*&output=json"
        "&filter=statuscode:200&filter=mimetype:text/html&collapse=digest"
    )
    data = get(cdx)
    rows = json.loads(data.decode("utf-8", "replace"))
    rows = rows[1:]  # drop header row

    pages = {}  # basename -> {title, snapshots: [[ts, original], ...]}
    for row in rows:
        _key, ts, original = row[0], row[1], row[2]
        m = re.search(r"/index\.php/(.+)$", original)
        if not m:
            continue
        raw = m.group(1)
        # skip query-string / action / oldid / printable variants
        if any(c in raw for c in ("?", "&", "=")) or "%26" in raw:
            continue
        name = urllib.parse.unquote(raw)
        ns = name.split(":", 1)[0].lower().replace(" ", "_") if ":" in name else ""
        if ns in SKIP_NS:
            continue
        if not name or name.lower() == "index.php":
            continue
        base = page_basename(name)
        if not base:
            continue
        entry = pages.setdefault(
            base,
            {"title": title_from_name(name.replace(" ", "_")), "snapshots": []},
        )
        entry["snapshots"].append([ts, original])

    # order each page's snapshots best-candidate-first
    for entry in pages.values():
        entry["snapshots"].sort(key=lambda s: snapshot_rank(s[0]))

    with open(MANIFEST, "w") as fh:
        json.dump(pages, fh, indent=1, sort_keys=True)
    print(f"  {len(pages)} content pages discovered -> {MANIFEST}")
    return pages


# --------------------------------------------------------------------------
# Step 2/3 - convert one archived HTML page to a Jekyll Markdown document
# --------------------------------------------------------------------------
def rewrite_link(href):
    """Map a MediaWiki <a href> to a link for the static site.

    Returns (new_href_or_None, is_redlink). new_href None -> drop the link.
    """
    if not href:
        return None, False
    href = html.unescape(href)
    # absolute links back into the wiki
    href = re.sub(r"^https?://(www\.)?openlierox\.net", "", href)
    if href.startswith("#"):
        return href, False
    # red links / edit links -> page does not exist on the archived wiki
    if "action=edit" in href or "redlink=1" in href:
        return None, True
    m = re.match(r"^/wiki/index\.php/([^?#]+)(#.+)?$", href)
    if m:
        target = page_basename(m.group(1))
        anchor = (m.group(2) or "").lower().replace(" ", "-")
        return f"/wiki/index.php/{target}/{anchor}", False
    if href.startswith(("http://", "https://", "ftp://", "irc://", "mailto:")):
        return href, False
    if href.startswith("/wiki/"):  # other wiki resource, leave root-relative
        return href, False
    return href, False


def clean_fragment(tag, soup):
    """In-place: strip MediaWiki chrome, rewrite links and image sources."""
    for c in tag.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for el in tag.find_all(["script", "style"]):
        el.decompose()
    for sel in ("#siteSub", "#contentSub", "#jump-to-nav", ".printfooter",
                ".editsection", "#toc", ".toc", ".visualClear", "#catlinks"):
        for el in tag.select(sel):
            el.decompose()
    for a in tag.find_all("a", attrs={"name": True}):
        a.unwrap()

    # images: keep wiki images root-relative, unwrap "click to enlarge" links
    for img in tag.find_all("img"):
        src = img.get("src", "")
        src = re.sub(r"^https?://(www\.)?openlierox\.net", "", src)
        src = re.sub(r"^https?://web\.archive\.org/web/[^/]+/", "", src)
        src = re.sub(r"^https?://(www\.)?openlierox\.net", "", src)
        img["src"] = src
        for attr in ("srcset", "width", "height", "longdesc"):
            img.attrs.pop(attr, None)
        if not img.get("alt"):
            img["alt"] = ""

    for a in tag.find_all("a"):
        if a.get("class") and "image" in a.get("class"):
            a.unwrap()
            continue
        new_href, is_red = rewrite_link(a.get("href", ""))
        if new_href is None:
            a.replace_with(NavigableString(a.get_text()))
        else:
            a["href"] = new_href
            for attr in ("title", "rel", "class"):
                a.attrs.pop(attr, None)


def collect_images(tag):
    imgs = []
    for img in tag.find_all("img"):
        src = img.get("src", "")
        if src.startswith("/wiki/images/"):
            imgs.append(src)
    return imgs


def html_block(el):
    """Render a kept element (table / thumbnail) as a compact HTML string."""
    for attr in ("style",):  # keep styles - they matter for faithful tables
        pass
    return str(el)


BAD_MARKERS = (
    "Parse error", "Fatal error", "T_NAMESPACE", "MWException",
    "Database error", "Notice: Undefined", "Warning: ",
    "There is currently no text in this page",
)


def looks_broken(html_bytes):
    """True if the archived capture is a PHP error / empty / dead page."""
    if not html_bytes or len(html_bytes) < 200:
        return True
    head = html_bytes[:4000].decode("utf-8", "replace")
    soup_probe = head
    return any(mark in soup_probe for mark in BAD_MARKERS[:5])


def convert(html_bytes, fallback_title, timestamp, original):
    """Return (front_matter_dict, markdown_body, image_list).

    Raises ValueError if the capture is unusable (caller falls back).
    """
    soup = BeautifulSoup(html_bytes, "html.parser")

    info = {"title": fallback_title, "timestamp": timestamp,
            "original": original}

    # title from <title>Foo - OpenLieroX Wiki</title>
    title = info["title"]
    if soup.title and soup.title.string:
        t = soup.title.string.strip()
        t = re.sub(r"\s*-\s*OpenLieroX Wiki\s*$", "", t)
        if t:
            title = t

    cm = soup.find(id="content-main")
    if cm is None:
        raise ValueError("no #content-main (not a wiki page capture)")

    if any(mark in cm.get_text() for mark in BAD_MARKERS):
        raise ValueError("capture contains a server error message")

    # redirect detection
    sub = cm.find(id="contentSub")
    redirect_from = sub and "Redirected from" in sub.get_text() if sub else False

    # categories
    cats = []
    catlinks = cm.find(id="catlinks")
    if catlinks:
        for a in catlinks.find_all("a"):
            txt = a.get_text().strip()
            if txt and txt.lower() not in ("categories", "category"):
                cats.append(txt)

    # last-modified date from the footer
    last_mod = None
    lm = soup.find(id="lastmod")
    if lm:
        m = re.search(r"last modified (.+?)\.?\s*$", lm.get_text().strip())
        if m:
            last_mod = m.group(1)

    clean_fragment(cm, soup)

    if redirect_from:
        # The archived page already shows the *destination*; emit a stub that
        # forwards to it so the redirect name keeps working.
        dest = page_basename(title.replace(" ", "_"))
        body = (f'This page redirects to '
                f'**[{title}](/wiki/index.php/{dest}/)**.\n')
        fm = {"title": info["title"], "redirect_target": dest}
        return fm, body, []

    images = collect_images(cm)

    # pull tables and thumbnails out so markdownify leaves them alone
    blocks = []

    def stash(el):
        token = f"XWIKIBLOCK{len(blocks)}X"
        blocks.append(html_block(el))
        placeholder = soup.new_tag("p")
        placeholder.string = token
        el.replace_with(placeholder)

    # only stash the outermost block of each kind (nested tables/thumbs come
    # along inside their parent's serialized HTML)
    outer = [el for el in cm.find_all("div", class_="thumb")
             if not el.find_parent("table")
             and not el.find_parent("div", class_="thumb")]
    outer += [el for el in cm.find_all("table")
              if not el.find_parent("table")
              and not el.find_parent("div", class_="thumb")]
    for el in outer:
        stash(el)

    body_html = "".join(str(c) for c in cm.contents)
    markdown = md(
        body_html,
        heading_style="ATX",
        bullets="*",
        strip=["script", "style"],
        escape_asterisks=False,
        escape_underscores=False,
    )

    # restore stashed HTML blocks
    def unstash(m):
        return "\n\n" + blocks[int(m.group(1))] + "\n\n"

    markdown = re.sub(r"XWIKIBLOCK(\d+)X", unstash, markdown)

    # tidy whitespace
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"

    fm = {
        "title": info["title"],
        "archived_url": (
            f"https://web.archive.org/web/{info['timestamp']}/"
            f"{info['original']}"
        ),
    }
    if last_mod:
        fm["last_modified"] = last_mod
    if cats:
        fm["categories"] = cats
    return fm, markdown, images


def yaml_value(v):
    if isinstance(v, list):
        return "[" + ", ".join(yaml_value(x) for x in v) + "]"
    s = str(v)
    if re.search(r'[:#\[\]{}\'"]|^\s|\s$', s) or s == "":
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def write_page(base, fm, body):
    lines = ["---"]
    for k, v in fm.items():
        lines.append(f"{k}: {yaml_value(v)}")
    lines.append("---")
    # The article body is verbatim wiki content and may contain '{{' / '{%'
    # (MediaWiki template syntax). Wrap it so Liquid leaves it untouched.
    out = ("\n".join(lines) + "\n{% raw %}\n"
           + body.strip() + "\n{% endraw %}\n")
    with open(os.path.join(WIKI_DIR, base + ".md"), "w", encoding="utf-8") as fh:
        fh.write(out)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    os.makedirs(WIKI_DIR, exist_ok=True)
    pages = build_manifest()
    images = set()
    if os.path.exists(IMAGES_TSV):
        with open(IMAGES_TSV) as fh:
            images = {ln.strip() for ln in fh if ln.strip()}

    todo = sorted(pages.items())
    done = skipped = failed = 0
    for i, (base, info) in enumerate(todo, 1):
        out = os.path.join(WIKI_DIR, base + ".md")
        if os.path.exists(out):
            skipped += 1
            continue
        sys.stdout.write(f"[{i}/{len(todo)}] {base} ... ")
        sys.stdout.flush()

        # try snapshots best-candidate-first until one converts cleanly
        result = None
        last_err = "no snapshots"
        for ts, original in info["snapshots"][:6]:
            data = get(wb_raw(ts, original))
            if not data or looks_broken(data):
                last_err = "broken/empty capture"
                continue
            try:
                result = convert(data, info["title"], ts, original)
                break
            except Exception as exc:  # noqa: BLE001
                last_err = str(exc)
            time.sleep(0.3)

        if result is None:
            print(f"FAILED ({last_err})")
            failed += 1
            time.sleep(0.3)
            continue

        fm, body, imgs = result
        write_page(base, fm, body)
        for im in imgs:
            images.add(im)
        done += 1
        print("ok" + (f" (+{len(imgs)} img)" if imgs else ""))
        time.sleep(0.3)

    with open(IMAGES_TSV, "w") as fh:
        for im in sorted(images):
            fh.write(im + "\n")

    print(f"\nDone. converted={done} skipped={skipped} failed={failed} "
          f"images={len(images)}")


if __name__ == "__main__":
    main()
