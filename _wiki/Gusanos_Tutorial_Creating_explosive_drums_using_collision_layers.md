---
title: "Gusanos Tutorial: Creating explosive drums using collision layers"
archived_url: "https://web.archive.org/web/20100628145928/http://www.openlierox.net:80/wiki/index.php/Gusanos_Tutorial:_Creating_explosive_drums_using_collision_layers"
last_modified: "14:38, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:tutorials:creating_explosive_drums_using_collision_layers).

###### Creating an Explosive Drum with Collision Layers

This tutorial can of course be modified for other objects as well. However, the "explosive drum" idea is one that we surely all recognize from FPS's. This tutorial will deal with several concepts: **collision layers**, **detection**, and **object death**. For this tutorial, we will make two objects: the explosive drum and a bullet that will trigger it.

##### Creating drum.obj

This will be the object that serves as the explosive drum.

```
 sprite=drum.bmp
 gravity=0.02
 col_layer=1
 health=100
 on death()
  create_explosion(explosion1.exp)
  remove()
```

Note that we set the **collision layer** to 1. This means that if you specify another object to detect collision layer 1, then the drum will be affected. The **on death()** event specifies what will happen once the drum loses all its health.

##### Creating bullet.obj

This bullet will trigger the explosion.

```
 gravity = 0.0009
 repeat = 4
 on detect_range(5,0,[1])
  damage(10)
  remove()
 on detect_range(5,0,[worms,2])
  damage(15)
  remove()
```

Notice that we have two **on detect_range** events. The first is to specify what will happen once the bullet collides with collision layer 1; that is, the explosive drum. In this case, it will deal 10 damage to the drum. The second event is to specify what will happen if it collides with a worm or something in collision layer 2.

##### Making undetected objects

What if you don't want an object to be detected by a "detect all layers" event? Simple: set col_layer = -1.
At this point, there are only 8 collision layers (0-7) and a worms layer.

##### Alternatives

Rather than using collision layers, you can use Custom Events.
{% endraw %}
