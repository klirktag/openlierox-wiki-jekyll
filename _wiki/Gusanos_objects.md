---
title: "Gusanos:objects"
archived_url: "https://web.archive.org/web/20100528073736/http://www.openlierox.net:80/wiki/index.php/Gusanos:objects"
last_modified: "13:59, 21 March 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:objects).

###### Properties:

Object properties must be added to the .obj file before events. These properties may only be used in .obj files.

##### acceleration

```
 acceleration = <float>
```

Determines the speed value that will be added to the object each frame. The speed will be added in the direction of the object angle. *Note that this speed can be capped using the **max_speed** property.*

* * Default value:** 0

##### alpha

```
 alpha = <int> ( from 0 to 255 )
```

Alpha is the value of transparency used by the blender. This cannot be used without specifying the blender.

* * Default value:** 255

##### angular_friction

```
 angular_friction = <float>
```

Each frame the angular speed will be decremented by this value.
>> This may change to work like a factor instead of this silly friction method.

* * Default value:** 0

##### anim_duration

```
 anim_duration = <int>
```

Determines how much time ( in frames ) will pass until 1 cycle of the sprite animation ends.

* * Default value:** 100

##### anim_on_ground

```
 anim_on_ground = <bool>
```

If true, the animation will not stop while the object is on the ground.

* * Default value:** false

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

Blender is the the blender used for manipulating the alpha of an object. There are two blenders, **Alpha** and **Add**. (possibly more later) Alpha will make the object translucent depending on the alpha value and add will make the object light up the background.

* * Default value:** none

##### bounce_factor

```
 bounce_factor = <float>
```

When the particle collides against a wall one of the speed will be multiplied by this factor. So values between 0 and 1 will make the object lose speed after a collision. *Note that only one axis of the speed will be affected which depends in if the wall was an horizontal or vertical one.*

* * Default value:** 1

##### color/colour

```
 color/colour = [r, g, b]
```

Determines the colour in which the object will be drawn.

* * Default value:** 255,255,255

##### col_layer

```
 col_layer = <int> ( from 0 to 7 )
```

Determines in which collision layer the object will be placed.

* * Default value:** 0

##### damping

```
 damping = <float>
```

Each frame the object speed will be multiplied by this value. Its normally used to simulate air friction, but it can also be used to make an object accelerate if the value is bigger than 1.

* * Default value:** 1

##### distortion

```
 distortion = <distortFunction>(radius)
```

If this is set to a distortion function then the object will apply a distortion to the screen after it draws itself.
The possible distortion functions are lens, swirl, spin, ripple and random.

###### Example:

```
 distortion = lens(30)
```

##### distort_magnitude

```
 distort_magnitude = <float>
```

* * distort_magnitude** will multiply the effect of the **distortion**.

* * Default value:** 0.8

##### distort_gen (buggy)

##### distort_size (buggy)

##### gravity

```
 gravity = <float>
```

Each frame the object vertical speed will increase by the number passed.

* * Default value:** 0

##### ground_friction

```
 ground_friction = <float>
```

When an object collides against a wall the speed of the object in the direction of the wall will be multiplied by this value.

* * Default value:** 1

##### health

```
 health = <float> ( > 0 )
```

Determines the initial health of the object.

* * Default value:** 100

##### invisible

```
 invisible = <int>
```

If its not equal 0 then the particle will not be displayed.

* * Default value:** 0

##### light_radius

```
 light_radius = <int>
```

It will render a light of radius **light_radius** centered on the particle. Works only on darkmode.

* * Default value:** 0

##### light_gen

```
 light_gen = <pie>
```

Description.

* * Default value:** zomg

##### light_size

```
 light_size = [<int>, <int>]
```

The height and width to generate the light within.

* * Default value:** Unknown.

##### line_to_origin

```
 line_to_origin = <bool>
```

If true a line will be rendered from where the object was created to the position of the object.

* * Default value:** false

##### max_speed

```
 max_speed = <float>
```

This value will cap the **acceleration** of the object, Once the speed is greater than this value the object will stop accelerating. Negative values will make it have no limit to the speed.

* * Default value:** -1

##### network_init (->sync_reload)

```
 network_init = <string>
```

Syncronizes whenever the screen is reloaded when the string is different than "".

* * Default value:** ""

##### occluded

```
 occluded = <int>
```

If its not equal to 0 and the particle has a sprite then the particle will be rendered as an occluded light.

* * Default value:** 0

##### radius (not useful/buggy)

```
 radius = <int>
```

This sets the radius of the particle when trying to hit scenary. It's not fully syncronized for network play. Also, the particle might hit the scenary if it is fast enough, or it finds it in certain angles. If the radius is greater than the hit radius, it will bounce infinitely...

* * Default value:** 0

##### render_layer

```
 render_layer = <int> ( from 0 to 8 )
```

When the objects are rendered they are rendered in order of its layers, objects with **render_layer** = 0 will be rendered before objects with greater values. Worms are rendered in layer 5. *Note that Objects in the same layer will be rendered in order of appearance.*

* * Default value:** 5

##### repeat

```
 repeat = <int> ( >= 1 )
```

Determines the amount of times an object will repeat its logic per game frame. Its usually used to make fast objects without skipping collisions. *Note that all properties, events or actions that depend on the object frames will be affected since the frames will pass repeat times faster.*

* * Default value:** 1

##### sprite

```
 sprite = <string>
```

The string passed as parameter has to be the name of a sprite inside the sprites folder of the mod or default.
If the file exists the object will be displayed with that image instead of a pixel.

##### sync_pos (->sync_reload)

##### sync_reload

```
 sync_reload = <bool>
```

Syncronizes whenever the next game cycle is reloaded.

* * Default value:** false

##### sync_shot (->sync_reload)

##### wu_pixels

```
 wu_pixels = <bool>
```

If true and the object would be rendered as a pixel, it will be rendered as a wu pixel instead.

* * Default value:** false

###### Events:

##### creation

```
 on creation ()
```

Gets triggered once when the object was just created.

##### custom_event

```
 on custom_event ( <int> index )
```

Will get triggered when some other object uses the custom_event action with the specified **index** on this particle.

##### death

```
 on death ()
```

Gets triggered when the object health is <= 0.

##### detect_range

```
 on detect_range ( <float> range,  <bool> detect_owner = true, <[layer]> layers = [worms] )
```

Gets triggered if there is an object with distance < than **range**. Only the objects that are in the specified collision layer will be detected, there is a special layer called "worms" that has to be used to be able to detect worms. If **detect_owner** is false then the event wont trigger for object that have the same owner than the particle.

##### ground_collision

```
 on ground_collision ()
```

Gets triggered when the object collides with ground.

##### timer

```
 on timer ( <int> delay, <int> delay_var = 0, <int> trigger_times = 0 )
```

The timer will get triggered every **delay** frames plus the **delay_var**. If the **trigger_times** param is bigger than 0 then the timer will only be triggered that amount of times.
{% endraw %}
