---
title: "Lua:global"
archived_url: "https://web.archive.org/web/20100618080807/http://www.openlierox.net:80/wiki/index.php/Lua:global"
last_modified: "17:17, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:global).

## Global functions

##### abs

```
 abs(n)
```

Returns the absolute value of n.

##### angle_clamp

```
 angle_clamp(angle)
```

Returns //angle// normalized to [0, 360).

##### angle_diff

```
 angle_diff(a, b)
```

Returns the relative angle in (-180, 180) between
angle //a// and //b// such that (a + angle_diff(a, b)) = b (mod 360)

##### angle_vector

```
 angle_vector(angle[, length = 1])
```

Returns a tuple representing the angle
with length //length//.

##### bindings.afterRender

```
 bindings.afterRender()
```

This is called after a rendering cycle is complete

##### bindings.afterUpdate

```
 bindings.afterUpdate()
```

This is called after every logic cycle is complete.

##### bindings.gameEnded

(available from version 0.9c)

```
 bindings.gameEnded(reason)
```

This is called when the game ended and no new game is pending.

//reason// can be one of the following:
EndReason.ServerQuit : the server disconnected.
EndReason.Kicked : you were kicked from the server.
EndReason.IncompatibleProtocol : you are running a protocol incompatible with the server's.
EndReason.IncompatibleData : your data does not match the server's.

##### bindings.gameNetworkInit

(available from version 0.9c)

```
 bindings.gameNetworkInit(connID)
```

This is called when a new client joins the game. //connID// is the connection ID of the new client.

The connection ID can be passed to the send() method of a [NetworkGameEvent](/wiki/index.php/Lua_networkgameevent/) to send events only
to the new client.

##### bindings.playerInit

```
 bindings.playerInit(player)
```

This is called when a new player is added to the game. //player// is the [Player](/wiki/index.php/Lua_player/) object that was added.

##### bindings.playerNetworkInit

```
 bindings.playerNetworkInit(player, connID)
```

This is called when a player is replicated to a new client. //player// is the player replicated.
//connID// is the connection ID of the new client.

The connection ID can be passed to the send() method of a [NetworkPlayerEvent](/wiki/index.php/Lua_networkplayerevent/) to send events only
to the player on the new client.

##### bindings.playerRemoved

(available from version 0.9c)

```
 bindings.playerRemoved(player)
```

This is called when a player is removed from the game. //player// is the [Player](/wiki/index.php/Lua_player/) object that will be removed.

##### bindings.playerUpdate

```
 bindings.playerUpdate(player)
```

This is called in every logic cycle for every player. //player// is the relevant [Player](/wiki/index.php/Lua_player/) object.

##### bindings.viewportRender

```
 bindings.viewportRender(viewport, worm)
```

This is called for every viewport when it's time to render the viewport HUD.

//viewport// is the [Viewport](/wiki/index.php/Lua_viewport/) object it should be rendered to and //worm// is the
[Worm](/wiki/index.php/Lua_worm/) object of the [Player](/wiki/index.php/Lua_player/) object that owns //viewport//.

##### bindings.wormDeath

```
 bindings.wormDeath(worm)
```

This is called when a worm dies. //worm// is the [Worm](/wiki/index.php/Lua_worm/) object that died.

##### bindings.wormRemoved

```
 bindings.wormRemoved(worm)
```

This is called when a worm is removed from the game. //worm// is the [Worm](/wiki/index.php/Lua_worm/) object that will be removed.

##### bindings.wormRender

```
 bindings.wormRender(x, y, worm, viewport, ownerPlayer)
```

This is called for every worm and viewport combination when it's time to render
the worm HUD.

(x, y) is the position of the worm in viewport coordinates.

//worm// is the [Worm](/wiki/index.php/Lua_worm/) object for which HUD should be rendered and //viewport// is
the [Viewport](/wiki/index.php/Lua_viewport/) object it should be rendered to. Use the bitmap() method of [Viewport](/wiki/index.php/Lua_viewport/)
to retrieve the relevant bitmap to draw on.

//ownerPlayer// is the [Player](/wiki/index.php/Lua_player/) object that owns //viewport//.

##### color

(available from version 0.9c)

```
 color(r, g, b)
```

Returns a [color](#color)

##### connect

```
 connect(address)
```

Connects to the address passed.

##### console_register_command

```
 console_register_command(name, function)
```

Registers the function //function// as a command in the Gusanos console.
When it is called, it will be passed each console parameter as a seperate parameter to the function.
The command will be removed automatically when a new [map](#map) is loaded.

##### console_register_control

(available from version 0.9c)

```
 console_register_control(name, function)
```

Registers a number of console commands that work like player controls.

//function// is a function that is called when the control is activated or
deactivated. It is of the form:

```
 function(player, state)
 end
```

Where //player// is the [Player](/wiki/index.php/Lua_player/) object the control applies to, and //state// is either true
or false depending on if the control is activated or deactivated.

The control can be bound to keys like built-in controls such as FIRE and JUMP
by binding to the command +P//x//_//name// where //x// is the local player number
and //name// is the name passed to this function.

##### fetch_server_list

```
 fetch_server_list(handler)
```

Fetches the server list from the master server and calls
//handler// with one parameter containing an array of
the servers.

##### floor

```
 floor(n)
```

Returns the number n rounded down towards infinity.

##### font_load

```
 font_load(name)
```

Loads and returns a [Font](/wiki/index.php/Lua_font/) object of the font with the passed name.

If the font couldn't be loaded, nil is returned.

##### game_local_player

```
 game_local_player(i)
```

Returns a [Player](/wiki/index.php/Lua_player/) object of the local player with index i.
If the index is invalid, nil is returned.

##### game_players

```
 game_players()
```

Returns an iterator object that returns a [Player](/wiki/index.php/Lua_player/) object
for every player in the game.

Intended to be use together
with a for loop, like this:

```
 for p in game_players() do
   -- Do something with p here
 end
```

##### gfx_draw_box

```
 gfx_draw_box(bitmap, x1, y1, x2, y2, r, g, b)
```

//This function is deprecated in 0.9c and later. Use the draw_box method of [Bitmap](/wiki/index.php/Lua_bitmap/) instead//.

##### gfx_reset_blending

```
 gfx_reset_blending()
```

Deactivates any blender that was active.
Everything drawn after this is called will be drawn solid.

##### gfx_set_add

```
 gfx_set_add(alpha)
```

Activates the add blender.
//alpha// is a value in [0, 255] that specifies the scaling factor
of things drawn after this is called.

##### gfx_set_alpha

```
 gfx_set_alpha(alpha)
```

Activates the alpha blender.
//alpha// is a value in [0, 255] that specifies the opacity
of things drawn after this is called.

##### gfx_set_alphach

(available from version 0.9c)

```
 gfx_set_alphach(alpha)
```

Activates the alphach blender.
//alpha// is a value in [0, 255] that specifies the opacity
of things drawn after this is called.

##### host

```
 host(map)
```

Hosts a networked game with the current mod and [map](#map) //map//.

##### load_particle

```
 load_particle(name)
```

Loads a particle type with the name //name// and returns it as a
ParticleType object.

##### map

```
 map(map)
```

Loads the [map](#map) //map// with the current mod.

##### map_is_blocked

```
 map_is_blocked(x1, y1, x2, y2)
```

Returns true if the line between (x1, y1) and (x2, y2) on the [map](#map) is blocked for particles.
Otherwise false.

##### map_is_loaded

```
 map_is_loaded()
```

Returns true if a [map](#map) is loaded, otherwise false.

##### map_is_particle_pass

```
 map_is_particle_pass(x1, y1)
```

Returns true if the point (x1, y1) on the [map](#map) is passable by particles.

##### maps

```
 maps()
```

Returns an iterator that iterates through all maps.

##### network_game_event

```
 network_game_event(name, handler)
```

Creates and returns a [NetworkGameEvent](/wiki/index.php/Lua_networkgameevent/) object.
//name// is any string that is unique to this NetworkGameEvent.
//handler// is a function that is called when this event is recieved on this client/server.
It has the the form:

```
 function(event, data)
```

Where //event// is the [NetworkGameEvent](/wiki/index.php/Lua_networkgameevent/) returned by //network_game_event// and //data//
is a bitstream with data sent with the event.

##### network_particle_event

```
 network_particle_event(name, handler)
```

Creates and returns a [NetworkParticleEvent](/wiki/index.php/Lua_networkparticleevent/) object.
//name// is any string that is unique to this NetworkParticleEvent.
//handler// is a function that is called when this event is recieved on this client/server.
It has the the form:

```
 function(event, particle, data)
```

Where //event// is the [NetworkParticleEvent](/wiki/index.php/Lua_networkparticleevent/) returned by //network_particle_event//, //particle//
is the [Particle](/wiki/index.php/Lua_particle/) object the event was sent on, and //data// is a bitstream with data sent
with the event.

##### network_player_event

```
 network_player_event(name, handler)
```

Creates and returns a [NetworkPlayerEvent](/wiki/index.php/Lua_networkplayerevent/) object.
//name// is any string that is unique to this NetworkPlayerEvent.
//handler// is a function that is called when this event is recieved on this client/server.
It has the the form:

```
 function(event, player, data)
```

Where //event// is the [NetworkPlayerEvent](/wiki/index.php/Lua_networkplayerevent/) returned by //network_player_event//, //player//
is the [Player](/wiki/index.php/Lua_player/) object the event was sent on, and //data// is a bitstream with data sent
with the event.

##### network_worm_event

```
 network_worm_event(name, handler)
```

Creates and returns a [NetworkWormEvent](/wiki/index.php/Lua_networkwormevent/) object.
//name// is any string that is unique to this NetworkWormEvent.
//handler// is a function that is called when this event is recieved on this client/server.
It has the the form:
`function(event, worm, data)`
Where //event// is the [NetworkWormEvent](/wiki/index.php/Lua_networkwormevent/) returned by //network_worm_event//, //worm//
is the [Worm](/wiki/index.php/Lua_worm/) object the event was sent on, and //data// is a bitstream with data sent
with the event.

##### new_bitstream

```
 new_bitstream()
```

Returns a new [Bitstream](/wiki/index.php/Lua_bitstream/) object.

##### randomfloat

```
 randomfloat(l, u)
```

Returns a random floating point number in the interval [l, u].

##### randomint

```
 randomint(l, u)
```

Returns a random integer in the interval [l, u].

##### sounds

(available from version 0.9c)

```
 sounds
```

This table returns [Sound](/wiki/index.php/Lua_sound/) objects when indexed with a valid sound name, and
nil otherwise.

Example:
`local mySound = sounds["bazooka.wav"]
mySound:play(10, 10)`

##### sprites_load

```
 sprites_load(name)
```

Loads and returns a [SpriteSet](/wiki/index.php/Lua_spriteset/) object of the sprite set with the passed name.

If the sprite set couldn't be loaded, nil is returned.

##### sqrt

```
 sqrt(n)
```

Returns the squareroot of n.

##### to_time_string

```
 to_time_string(v)
```

Converts a frame count //v// to a string showing hours, minutes and seconds as HH:MM:SS.

##### vector_add

```
 vector_add(x1, y1, x2, y2)
```

Returns a tuple equal to (x1 + x2, y1 + y2)

##### vector_diff

```
 vector_diff(x1, y1, x2, y2)
```

Returns a tuple equal to (x2 - x1, y2 - y1)

##### vector_direction

```
 vector_direction(x1, y1, x2, y2)
```

Returns the angle between (x1, y1) and (x2, y2)
in degrees.

##### vector_distance

```
 vector_distance(x1, y1, x2, y2)
```

Returns the distance from (x1, y1) to (x2, y2)

##### weapon_count

```
 weapon_count()
```

Returns the total number of weapons.

##### weapon_random

```
 weapon_random()
```

Returns a random [WeaponType](/wiki/index.php/Lua_weapontype/) object.
{% endraw %}
