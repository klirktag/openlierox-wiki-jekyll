---
title: "Gusanos:weapons"
archived_url: "https://web.archive.org/web/20110721122959/http://www.openlierox.net/wiki/index.php/Gusanos:weapons"
last_modified: "12:23, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:weapons).

###### General:

Weapon files should be named .wpn and placed under the *gusanos/mod/weapons/* directory.

###### Properties:

Weapon properties must be added to the .wpn file before events. These properties may only be used in .wpn files.

##### ammo

```
 ammo = <int>
```

Determines how much ammo the weapon holds.

* * Default value:** 1

Also use **use_ammo** to drain ammo from weapons from now on.

##### laser_sight_alpha

```
 laser_sight_alpha = <int> ( from 0 to 255 )
```

Determines the translucency of the lasersight. It only works if **laser_sight_blender** is not equal to "none".

* * Default value:** 255

##### laser_sight_blender

```
 laser_sight_blender = { add, alpha, none }
```

Determines the blender with which the laser sight will be drawn.

* * Default value:** none

##### laser_sight_color / laser_sight_colour

```
 laser_sight_colour = [ <int> r, <int> g, <int> b ] ( All ranging from 0 to 255 )
```

```
 e.g.
 laser_sight_colour = [ 255, 128, 0] # Makes an orange laser sight
```

Determines the colour ( in RGB format ) with which the laser sight will be drawn.

* * Default value:** [ 255, 0, 0 ]

##### laser_sight_intensity

```
 laser_sight_intensity = <float> ( from 0 to 1 )
```

Its the intensity of the laser sight of the weapon. 1 is full intensity, 0.5 half, 0 no laser sight.

* * Default value:** 0

##### laser_sight_range

```
 laser_sight_range = <float>
```

Is the distance in which the lasersight will fade completely from the given laser_sight_intensity to 0 intensity. -1 will make it not fade.

* * Default value:** -1

##### name

```
 name = <string>
```

The name of the weapon.

* * Default value:** ""

##### reload_time

```
 reload_time = <int>
```

Determines the time in frames that will take for the weapon to reload.

* * Default value:** 0

##### skin

```
 skin = <string>
```

The image that will be displayed on top of the worm.

* * Default value:** null

##### sync_reload

```
 sync_reload = <bool>
```

###### Events:

##### active_timer

```
 on active_timer( <int> delay, <int> delay_var = 0, <int> max_trigger = 0 , <int> start_delay = 0 )
```

It behaves the same as a normal timer except that it will only count time when the weapon is selected and it gets reset when the player changes to another weapon. **start_delay** is how much time it should wait to start counting time, if set to -1 the time will be equal to the delay + variation.

* * Example:**

```
 on active_timer( 0, max_trigger = 1 )
 play_sound( sword_chosen.wav )
```

This would play the sound sword_chosen.wav every time the player changes to the sword (this) weapon.

##### primary_shoot

```
 on primary_shoot()
```

It will trigger while the gun is shooting.

##### primary_press

```
 on primary_press()
```

It will trigger **once** when the player presses the fire button.

##### primary_release

```
 on primary_release()
```

It will trigger **once** when the player releases the fire button.

##### out_of_ammo

```
 on out_of_ammo()
```

It will trigger **once** when the weapon gets out of ammo.

##### reload_end

```
 on reload_end()
```

It will trigger **once** when the weapon reloading ends.

##### timer

```
 on timer ( <int> delay, <int> delay_var = 0, <int> trigger_times = 0 )
```

The timer will get triggered every **delay** frames plus the **delay_var**. If the **trigger_times** param is bigger than 0 then the timer will only be triggered that amount of times.
{% endraw %}
