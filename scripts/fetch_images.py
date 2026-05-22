#!/usr/bin/env python3
"""Download the wiki images referenced by the converted pages.

Reads scripts/images.tsv (written by fetch_wiki.py), finds an archived copy
of every /wiki/images/... file in the Wayback Machine and saves it into the
repository under wiki/images/... so Jekyll serves it at the same path the
original MediaWiki used.
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMAGES_TSV = os.path.join(HERE, "images.tsv")

UA = {"User-Agent": "Mozilla/5.0 (OpenLieroX wiki archival re-creation)"}


def get(url, tries=6):
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


def cdx_lookup(paths):
    """Return {path: (timestamp, original_url)} for the archived images."""
    found = {}
    cdx = (
        "http://web.archive.org/cdx/search/cdx?"
        "url=openlierox.net/wiki/images/*&output=json"
        "&filter=statuscode:200&collapse=urlkey"
    )
    data = get(cdx)
    if not data:
        return found
    rows = json.loads(data.decode("utf-8", "replace"))[1:]
    by_lower = {}
    for row in rows:
        ts, original = row[1], row[2]
        m = original.split("/wiki/images/", 1)
        if len(m) != 2:
            continue
        key = "/wiki/images/" + urllib.parse.unquote(m[1])
        by_lower[key.lower()] = (ts, original)
    for p in paths:
        hit = by_lower.get(p.lower())
        if hit:
            found[p] = hit
    return found


def main():
    if not os.path.exists(IMAGES_TSV):
        print("no images.tsv - run fetch_wiki.py first")
        return
    with open(IMAGES_TSV) as fh:
        paths = sorted({ln.strip() for ln in fh if ln.strip().startswith("/wiki/images/")})
    print(f"{len(paths)} image(s) referenced")

    located = cdx_lookup(paths)
    print(f"{len(located)} located in the Wayback Machine")

    done = failed = skipped = 0
    for p in paths:
        out = os.path.join(ROOT, p.lstrip("/"))
        if os.path.exists(out) and os.path.getsize(out) > 0:
            skipped += 1
            continue
        if p not in located:
            print(f"  MISS  {p}")
            failed += 1
            continue
        ts, original = located[p]
        data = get(f"https://web.archive.org/web/{ts}id_/{original}")
        if not data or len(data) < 30:
            print(f"  FAIL  {p}")
            failed += 1
            continue
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as fh:
            fh.write(data)
        print(f"  ok    {p} ({len(data)} B)")
        done += 1
        time.sleep(0.3)

    print(f"\nDone. downloaded={done} skipped={skipped} missing/failed={failed}")


if __name__ == "__main__":
    main()
