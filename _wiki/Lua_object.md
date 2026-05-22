---
title: "Lua:object"
archived_url: "https://web.archive.org/web/20100618091104/http://www.openlierox.net:80/wiki/index.php/Lua:object"
last_modified: "13:09, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:object).

###### Class Object

```
===== angle =====
```

```
 angle()
```

(Known as get_angle before 0.9c)
Returns the current [angle](#angle) of the object.

##### closest_worm

```
 closest_worm()
```

(Known as get_closest_worm before 0.9c)

Returns the closest worm that fulfills these requirements:

```
 * It is not the owner of the object.
 * It is visible and active.
 * The straight path to it from the object is not, for particles, blocked.
```

##### damage

(available from version 0.9c)

```
 damage(amount[, player])
```

Causes [damage](#damage) to the object. //player// is the [player](#player) inflicting the damage.
If //player// isn't specified or nil, the [damage](#damage) is anonymous.

##### data

```
 data()
```

Returns a table associated with this object that can
be used by Lua scripts to store values.

##### player

```
 player()
```

(Known as get_player before 0.9c)

Returns a [Player](/wiki/index.php/Lua_player/) object of the [player](#player) that owns this object.

##### pos

```
 pos()
```

Returns the position of this object as a tuple.
i.e.:
`local x, y = object:pos()`

##### push

```
 push(x, y)
```

Accelerates the object in the direction (x, y)
e.g.:
`object:push(0, 10) -- Accelerates the object downwards`

##### remove

```
 remove()
```

Removes the object in the next frame.

##### set_pos

```
 set_pos(x, y)
```

Moves the object to the location (x, y)
e.g.:
`object:set_spd(0, 0) -- Moves the object to the upper-left corner`

##### set_spd

(available from version 0.9c)

```
 set_spd(x, y)
```

Changes the speed of this object to (x, y)
e.g.:
`object:set_spd(10, 0) -- Makes the object move to the right`

##### shoot

```
 shoot(type, amount, speed, speedVariation, motionInheritance, amountVariation, distribution, angleOffset, distanceOffset)
```

Shoots an object of ParticleType 'type'. All parameters except 'type' are optional.

##### spd

```
 spd()
```

Returns the speed of this object as a tuple.
e.g.:
`local vx, vy = object:spd()`
{% endraw %}
