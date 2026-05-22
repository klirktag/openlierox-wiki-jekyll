---
title: "Lua:spriteset"
archived_url: "https://web.archive.org/web/20100618081912/http://www.openlierox.net:80/wiki/index.php/Lua:spriteset"
last_modified: "17:19, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:spriteset).

###### Class SpriteSet

##### See also:

[sprites_load](/wiki/index.php/Lua_global/#sprites_load)

##### frames

```
 frames()
```

Returns the number of [frames](#frames) in this sprite set.

##### render

```
 render(bitmap, frame, x, y)
```

Draws the frame //frame// of the sprite set on //bitmap// with the pivot at position (x, y).

##### render_skinned_box

```
 render_skinned_box(bitmap, x1, y1, x2, y2, color)
```

Draws the sprite set as a skinned box with the rectangle (x1, y1) - (x2, y2)
and background color //color//.

**Note that in versions before 0.9c, color was specified as three parameters. This has been deprecated.**
{% endraw %}
