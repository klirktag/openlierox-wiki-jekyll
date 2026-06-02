# OpenLieroX wiki — MediaWiki export

The Jekyll articles in `_wiki/` translated back to MediaWiki wikitext, ready
to load into a real MediaWiki install hosted elsewhere.

## What's in here

- `*.wiki` — one wikitext file per article (310 files). Filename = the
  underscored MediaWiki page name (e.g. `Liero_1.0.wiki` for the page
  *Liero 1.0*).
- `openlierox-wiki.xml` — a single MediaWiki 0.11 XML export containing every
  article in one bundle, suitable for **Special:Import** or `importDump.php`.

## Loading into your MediaWiki

### Easy: Special:Import (admin only)

1. Sign in to your MediaWiki as an account with the `import` right (sysop by
   default).
2. Go to `Special:Import`, choose **Upload file**, pick
   `openlierox-wiki.xml`, set the interwiki prefix to blank, and submit.

### CLI: `importDump.php` (server access)

```sh
php maintenance/run.php importDump --conf LocalSettings.php < openlierox-wiki.xml
php maintenance/run.php rebuildrecentchanges --conf LocalSettings.php
php maintenance/run.php initSiteStats --conf LocalSettings.php --update
```

(`maintenance/run.php` replaces direct script execution on MW ≥ 1.40; on
older releases just run `php maintenance/importDump.php`.)

### One article at a time

Each `.wiki` file is plain wikitext: copy/paste it into the page's edit box,
or use the `edit.php` maintenance script:

```sh
php maintenance/run.php edit --conf LocalSettings.php \
  --user 'WaybackImport' --summary 'Imported from Wayback Machine' \
  'Liero 1.0' < Liero_1.0.wiki
```

## Images

Image references use the standard `[[File:Name.png]]` syntax. The image bytes
live under `wiki/images/` in the repository root — upload them to your new
wiki with the **Special:Upload** form or in bulk via `importImages.php`:

```sh
cp -r ../wiki/images/* /tmp/olx-images/
php maintenance/run.php importImages --conf LocalSettings.php /tmp/olx-images
```

(Eight images that pages reference were never captured by the Wayback Machine
and so are missing — those `[[File:...]]` links will show as red until you
re-supply them.)

## Regenerating

```sh
python3 scripts/to_mediawiki.py
```

Reads `_wiki/*.md`, writes everything in this folder.

## What got converted

| Markdown / HTML                  | MediaWiki wikitext              |
|----------------------------------|---------------------------------|
| `## Heading`                     | `== Heading ==`                 |
| `**bold**` / `*italic*`          | `'''bold'''` / `''italic''`     |
| `[text](/wiki/index.php/Foo/)`   | `[[Foo\|text]]` (or `[[Foo]]`)  |
| `[text](https://example.com)`    | `[https://example.com text]`    |
| `![alt](/wiki/images/X/YY/F.png)`| `[[File:F.png\|alt]]`           |
| `* item` / `1. item`             | `* item` / `# item`             |
| ` ```lang … ``` `                | `<syntaxhighlight lang="lang">` |
| `<table>…</table>` (Main Page)   | left as inline HTML             |
| `categories: [Mods, Guides]`     | `[[Category:Mods]]` (appended)  |

The trailing HTML comment in each file records the Wayback Machine snapshot
the content came from.
