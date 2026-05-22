---
title: "Gusanos:game actions"
archived_url: "https://web.archive.org/web/20110721124803/http://www.openlierox.net/wiki/index.php/Gusanos:game_actions"
last_modified: "14:59, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:game_actions).

###### General Actions:

General actions can be used in both objects and explosions.

##### apply_map_effect

```
 apply_map_effect ( <string> map_effect )
```

* <string> //map_effect// - Map effect name (map effect file name without the ".mfx" extension).

It will apply a [map effect](/wiki/index.php/Gusanos_map_effects/) to the map. This is usually used for digging holes on dirt materials and such. See also: [Modding Docs: Map effects](/wiki/index.php/Gusanos_map_effects/)

##### add_angle_speed

```
 add_angle_speed ( <float> amount,
                   <float> amount_var = 0 )
```

```
 * <float> //amount// - Amount of angular speed.
 * <float> //amount_var// - Amount of angular speed variation.
```

Adds a specific amount and amount variation to the angular speed of the object. See also: [Ratio variation](/wiki/index.php/Gusanos_variations/#ratio_variation)

##### add_speed

```
 add_speed ( <float> amount,
             <float> amount_var = 0,
             <float> offset = 0,
             <float> offset_var = 0 )
```

```
 * <float> //amount// - Amount of angular speed.
 * <float> //amount_var// - Amount of angular speed variation.
 * <float> //offset// - Angle offset.
 * <float> //offset_var// - Angle offset variation.
```

Adds a specific amount and amount variation to the angular speed of the object using a different angle offset and offset variation. See also: [Ratio variation](/wiki/index.php/Gusanos_variations/#ratio_variation)

##### create_explosion

```
 create_explosion( <string> explosion )
```

* <string> //explosion// - Explosion name (explosion file name without the ".exp" extension).

Creates an [explosion](/wiki/index.php/Gusanos_explosions/) on the current position of the object.

##### custom_event

```
 custom_event( <int> index )
```

```
 * <int> //index// - custom event number
```

Will trigger the custom event indexed as **index** in the target particle. Note that this action needs to be inside a detection event or an event that interacts with other objects.

##### damage

```
 damage ( <float> amount,
          <float> amount_var,
          <float> max_distance )
```

* <float> //amount// - damage amount
* <float> //amount_var// - damage amount variation to //amount//
* <float> //max_distance// - distance where damage will equal zero. Object will have reduced damage if within range but farther from damage center.

Will damage the object by the **amount** value. Will only work on detection events involving an object with health, specified by the property health = <float>. If the **max_distance** parameter is set to a number > 0 the damage will fade from **amount** to 0 damage when the distance from the damaged object to the damager is equal to max_distance.

Good usage would be if it was used with on detect_range(a,b,[x1,x2,x3]), then it would damage all objects in collision layers and/or worms specified in the [].

##### damp

```
 damp ( <float> factor )
```

```
 * <float> //factor// - speed multiplication factor.
```

It will multiply the detected object speed by this factor. When the **factor**:

```
 * F>1: increases its speed.
 * F is 1: speed stays the same.
 * 0<F<1: reduces its speed.
 * F is 0: object returns to inertia.
 * F<0: speed is inversed.
```

##### push

```
 push ( <float> factor )
```

```
 * <float> //factor// - speed multiplication factor.
```

Adds the speed of the owner object to the object that caused the event to trigger. The **factor** variable will multiply the speed to be added. Note that this action will obviously only work when called in an event that gets triggered by an object, for example, it wont do anything if you use it on a timer trigger.

##### put_particle

```
 put_particle ( <string> type,
                <float> x,
                <float> y,
                <float> xspd = 0,
                <float> yspd = 0,
                <float> angle = 0 )
```

```
 * <float> //type// - particle type.
 * <float> //x// - horizontal position.
 * <float> //y// - vertical position.
 * <float> //xspd// - horizontal speed.
 * <float> //yspd// - vertical speed.
 * <float> //angle// - angle of direction.
```

It will create a single particle of the **type** passed in the position specified on the map. This is normally used not for mods, but for map objects that need to create things on some other position ( Like buttons etc ).

##### remove

```
 remove ()
```

After this action gets called, the owner particle will disappear.

Good usage would be to make SURE all objects you create are removed eventually (unless you specifically don't want to remove them). Unremoved objects may slow down the game severely. For example, in a bazooka you may want to use it like this:

```
 on ground_collision()
  create_explosion(x.exp)
  remove()
 on detect_range(10,0,[worms])
  create_explosion(x.exp)
  remove()
```

##### repel

```
 repel ( <float> max_force,
         <float> max_distance,
         <float> min_force = 0 )
```

```
 * <float> //max_force// - force when object is in distance 0.
 * <float> //max_distance// - maximum distance in which the repelling action will be applied.
 * <float> //min_force// - force when object is in distance //max_distance//.
```

It will push the target object away from the owner object. If the distance between the two objects is 0 the force of repel will be equal to **max_force**, if the distance between both is equal to max_distance the repel force will be equal to **min_force**.

##### run_script

```
 run_script( <string> file_name )
```

```
 * <float> //file_name// - file name of the script, without extention and path.
```

### Description:

It will run the script that matches with **name**. The script will be passed the reference to the object that called it, and if this action was triggered from an event that involves a second object it will also be passed as a second parameter.

##### set_alpha_fade

```
 set_alpha_fade( <int> frames ,
                 <int> dest = 0 )
```

```
 * <float> //frames// - number of frames for the duration of the fade.
 * <float> //dest// - alpha level to fade to.
```

Once this action is called the objects alpha fades to the **dest** alpha in the specified **frames**. Can only be used if the object property //blender// is set to something different than //NONE//.

An example of usage would be:

```
 blender=add
 alpha=100
 on_creation()
  set_alpha_fade(100,0)
 on timer(100)
  remove()
```

This would cause a particle to begin with 100 alpha and gradually fade to 0 over 100 frames and remove itself.

##### shoot_particles

```
 shoot_particles ( <string> type,
                   <int> amount,
                   <float> speed = 0,
                   <float> speed_var = 0,
                   <float> motion_inheritance = 0,
                   <int> amount_var = 0,
                   <float> distribution = 360,
                   <float> angle_offs = 0,
                   <float> distance_offs = 0 )
```

* <string> //type// - filename of the object to shoot ( See [Gusanos:objects](/wiki/index.php/Gusanos_objects/) ).
* <int> //amount// - the amount of objects to shoot.
* <float> //speed// - the speed at which objects will be shot.
* <float> //speed_var// - the [Gusanos:variations#ratio variation](/wiki/index.php/Gusanos_variations/#ratio_variation) of the speed in which objects will be shot.
* <float> //motion_inheritance// - a factor that will decide how much of the speed of the owner particle will be transferred to the shot particles. *For example, motionInheritance = 2 transfers twice the amount of speed of the owner to the shot particles.*\\
* <int> //amount_var// - the [Gusanos:variations#positive variation](/wiki/index.php/Gusanos_variations/#positive_variation) of amount of particles that will be shot.
* <int> //distribution// - a [Gusanos:variations#ratio variation](/wiki/index.php/Gusanos_variations/#ratio_variation) of the angle in which the particles will be shot relative to the current particle angle.
* <int> //angle_offs// - the angular offset in which particles will be shot relative to the angle of the owner.
* <int> //distance_offs// - how far the object will be created from the position of the owner object. *This is a useful feature for making particles not detect the particle that created them.*

Will shoot particles from the position the owner object is placed.

##### uniform_shoot_particles

```
 uniform_shoot_particles ( <string> type,
                           <int> amount,
                           <float> speed = 0,
                           <float> speed_var = 0,
                           <float> motion_inheritance = 0,
                           <int> amount_var = 0,
                           <float> distribution = 360,
                           <float> angle_offs = 0,
                           <float> distance_offs = 0 )
```

Works in the same way as **shoot_particles** except the particles wont be shot at random directions inside the distribution. Instead, the angle in which particles will be shot is distribution / ( total number of particles ).
TODO: Add an image that explains this.

###### Weapon Specific Actions:

##### delay_fire

```
 delay_fire ( <int> time,
              <int> time_var = 0 )
```

```
 * <int> //time// - amount of time for the weapon to fire.
 * <int> //time_var// - amount of time variation for the weapon to fire.
```

Will disable firing of the weapon for **time** + random from 0 to **time_var** ( **time_var** is a [Gusanos:variations#positive variation](/wiki/index.php/Gusanos_variations/#positive_variation). Works only on weapon events.)

delay_fire is used not as reload time, but as the amount of time between each projectile (aka, firing rate). If used in the "on_primary_press" event, delay_fire equates to the amount of time needed before the weapon fires the "on_primary_shoot" event. If used in the "on_primary_shoot" event, delay_fire equates to firing rate.

##### show_firecone

```
 show_firecone ( <string> sprite,
                 <int> frames,
                 <int> draw_distance = 0 )
```

* <string> //sprite// - sprite to show.
* <int> //frames// - amount of frames in which the animation ends.
* <int> //draw_distance// - distance offset from the worm at the worm's own angle in which to draw the center of the animation.

It will show the firecone image passed as **sprite** during the passed number of **frames**. **draw_distance** will offset the image away from the center of the worm.

##### use_ammo (0.9c)

```
 use_ammo ( <int> amount )
```

```
 * <int> //amount// - amount to use by the weapon.
```

It drains an amount of weapon ammo. This is needed whenever a bullet is shot from the weapon. If this is not used, the weapon has unlimited ammunition, even if there is a limit specified (never spends the amount).

###### Sound Actions:

##### play_sound

```
 play_sound ( <string[]|string> sound,
              <float> loudness = 100,
              <float> pitch = 1,
              <float> pitch_var = 0 )
```

* <string[]|string> sound - Sound file without extention and path.
* <float> loudness - Loudness level in percent.
* <float> pitch - Frequency multiplier at which the sound is to be played.
* <float> pitch_var- Frequency multiplier variation at which the sound is to be played.

Will play a 3D sound that will follow the position of the owner object, **soundFile** is the name of the sound to play ( See the list of [supported sound formats](/wiki/index.php/Gusanos_sounds/) ). **loudness** is directly related to how loud it will be heard from the distance. **pitch** is a modifier of the sound play frequency and **pitchVariation** is a [rate variation](/wiki/index.php/Gusanos_variations/#ratio_variation) of it.

* * Tip:** Rather than creating several different sounds for a single object (dropping shells, for example), you can use pitch variation to create differences between each time the sound is played.

##### play_sound_static

```
 play_sound_static ( <string[]|string> sound,
                     <float> loudness = 100,
                     <float> pitch = 1,
                     <float> pitch_var = 0 )
```

Behaves exactly the same as <#play_sound> but the sound will not follow the object. Once the sound is created, it will stay in the same place and not move.

##### play_global_sound

```
 play_global_sound ( <string[]|string> sound,
                     <float> volume,
                     <float> volume_var,
                     <float> pitch = 1,
                     <float> pitch_var = 0 )
```

* <string[]|string> sound - Sound file without extention and path.
* <float> volume - Volume of the sound to be played.
* <float> volume_var - Volume variation of the sound to be played.
* <float> pitch - Frequency multiplier at which the sound is to be played.
* <float> pitch_var- Frequency multiplier variation at which the sound is to be played.

Will play a sound in no particular position. The sound can always be heard no and wont fade with distance. If more than one sound is passed as first param then the sound to play will be chosen at random from that list.
{% endraw %}
