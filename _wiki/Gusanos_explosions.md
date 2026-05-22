---
title: "Gusanos:explosions"
archived_url: "https://web.archive.org/web/20110721124752/http://www.openlierox.net/wiki/index.php/Gusanos:explosions"
last_modified: "15:00, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:explosions).

###### Properties:

These properties may only be used in explosions; .exp files.

##### alpha

```
 alpha = <int> ( from 0 to 255 )
```

Alpha is the value of transparency used by the blender. This cannot be used without specifying the blender.

* * Default value:** 255

##### anim_type

```
 anim_type = { ping_pong / loop_right / right_once }
```

Determines the behaviour of the sprite animation.

* * Default value:** loop_right

##### blender

```
 blender = <alpha/add/alphach/none>
```

Blender is the the blender used for manipulating the alpha of an object. There are two blenders, **Alpha** and **Add**. (possibly more later) Alpha will make the object translucent depending on the alpha value and add will make the object lit the background.

* * Default value:** none

##### colour

```
 color = r, g, b
```

Determines the colour in which the explosion will be drawn.

* * Default value:** 255,255,255

##### dest_alpha

```
 dest_alpha = <int> ( <= 255 )
```

If the value is from 0 to 255 the explosion will interpolate its alpha value from the initial **alpha** to dest_alpha. The speed of the interpolation depends on the **timeout** value.

* * Default value:** -1

##### invisible

```
 invisible = <int>
```

If its not equal 0 then the explosion will not be displayed.

* * Default value:** 0

##### occluded

```
 occluded = <int>
```

If its not equal to 0 and the explosion has a sprite then the it will be rendered as an occluded light.

* * Default value:** 0

##### render_layer

```
 render_layer = <int> ( from 0 to 8 )
```

When the objects are rendered they are rendered in order of its layers, objects with **render_layer** = 0 will be rendered first than objects with greater values. Worms are rendered in layer 5. *Note that Objects in the same layer will be rendered in order of appearance.*

* * Default value:** 5

##### sprite

```
 sprite = <string>
```

The string passed as parameter has to be the name of a sprite inside the sprites folder of the mod or default.
If the file exists the explosion will be displayed with that image instead of a pixel.

##### timeout

```
 timeout = <int> ( >= 0 )
```

Determines the time until the explosion will be removed. If the explosion has a sprite the duration of the animation will depend on this value.

* * Default value:** 0

##### timeout_variation

```
 timeout_variation = <int> ( >= 0 )
```

Adds a variation to the timeout of the explosion.

* * Default value:** 0

###### Events:

##### creation

```
 on creation ()
```

Gets triggered once when the explosion is just created.

##### detect_range

```
 on detect_range ( <float> range,  <bool> detect_owner = true, <[layer]> layers = [worms] )
```

Gets triggered if there is an object with distance < than range. Only the objects that are in the specified collision layer will be detected, there is a special layer called “worms” that has to be used to be able to detect worms. If detect_owner is false then the event wont trigger for object that have the same owner than the explosion.
{% endraw %}
