---
title: "Lua:viewport"
archived_url: "https://web.archive.org/web/20100618083137/http://www.openlierox.net:80/wiki/index.php/Lua:viewport"
last_modified: "13:14, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:viewport).

###### Class Viewport

```
===== See also: =====
```

[bindings.wormRender](/wiki/index.php/Lua_global/#bindings.wormrender), [bindings.wormRender](/wiki/index.php/Lua_global/#bindings.wormrender), [bindings.viewportRender](/wiki/index.php/Lua_global/#bindings.viewportrender)

##### bitmap

```
 bitmap()
```

(Known as get_bitmap before 0.9c)

Returns the HUD [bitmap](#bitmap) of this viewport.

##### from_map

(available from version 0.9c)

```
 from_map(x, y)
```

Converts the map coordinates (x, y) to
coordinates relative to the viewport [bitmap](#bitmap) and returns them.
{% endraw %}
