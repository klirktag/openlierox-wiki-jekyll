---
title: "Lua:weapon"
archived_url: "https://web.archive.org/web/20100618082321/http://www.openlierox.net:80/wiki/index.php/Lua:weapon"
last_modified: "15:11, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:weapon).

###### Class Weapon

##### ammo

```
 ammo()
```

Returns the amount of [ammo](#ammo) left in this weapon.

##### is_reloading

```
 is_reloading()
```

Returns true if this weapon is reloading.

##### reload_time

```
 reload_time()
```

Returns the reload time left on this weapon.
Does only make sense if is_reloading() is true.

##### type

```
 type()
```

Returns the weapon [type](#type) in the form of a [WeaponType](/wiki/index.php/Lua_weapontype/) object.
{% endraw %}
