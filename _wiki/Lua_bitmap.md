---
title: "Lua:bitmap"
archived_url: "https://web.archive.org/web/20121214065623/http://www.openlierox.net:80/wiki/index.php/Lua:bitmap"
last_modified: "13:05, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:bitmap).

###### Class Bitmap

```
===== See also: =====
```

[gfx_draw_box](/wiki/index.php/Lua_global/#gfx_draw_box)

##### draw_box

```
 draw_box(bitmap, x1, y1, x2, y2, color)
```

Draws a filled box with the corners (x1, y1) and (x2, y2)
with the color //color// using the currently selected blender.

##### h

```
 h()
```

Returns the width of this bitmap.

##### hline

(available from version 0.9c)

```
 hline(x1, y1, x2, color)
```

Draws a horizontal [line](/wiki/index.php/Lua_bitmap/#line) from (x1, y1) to (x2, y1)
with the color //color// using the currently selected blender.

##### line

(available from version 0.9c)

```
 line(x1, y1, x2, y2, color)
```

Draws a [line](/wiki/index.php/Lua_bitmap/#line) from (x1, y1) to (x2, y2)
with the color //color// using the currently selected blender.

##### linewu

(available from version 0.9c)

```
 linewu(x1, y1, x2, y2, color)
```

Draws a Wu-line from (x1, y1) to (x2, y2)
with the color //colour// using the currently selected blender.

##### putpixel

(available from version 0.9c)

```
 putpixel(x1, y1, color)
```

Draws a pixel at position (x1, y1)
with the color //color// using the currently selected blender.

##### putpixelwu

(available from version 0.9c)

```
 putpixelwu(x1, y1, color)
```

Draws a Wu-pixel at position (x1, y1)
with the color //color// using the currently selected blender.

##### w

```
 w()
```

Returns the width of this bitmap.
{% endraw %}
