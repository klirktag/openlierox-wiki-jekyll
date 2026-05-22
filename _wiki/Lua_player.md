---
title: "Lua:player"
archived_url: "https://web.archive.org/web/20100618083928/http://www.openlierox.net:80/wiki/index.php/Lua:player"
last_modified: "15:11, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:player).

###### Class Player

##### See also:

[bindings.wormRender](/wiki/index.php/Lua_global/#bindings.wormrender), [bindings.viewportRender](/wiki/index.php/Lua_global/#bindings.viewportrender), [bindings.playerUpdate](/wiki/index.php/Lua_global/#bindings.playerupdate), [bindings.playerInit](/wiki/index.php/Lua_global/#bindings.playerinit), [bindings.playerRemoved](/wiki/index.php/Lua_global/#bindings.playerremoved), [NetworkPlayerEvent:send](/wiki/index.php/Lua_networkplayerevent/#send), [network_player_event](/wiki/index.php/Lua_global/#network_player_event), [Object:player](/wiki/index.php/Lua_object/#player), [console_register_control](/wiki/index.php/Lua_global/#console_register_control), [game_players](/wiki/index.php/Lua_global/#game_players), [game_local_player](/wiki/index.php/Lua_global/#game_local_player)

##### data

```
 data()
```

Returns a lua table associated with this player.

##### deaths

```
 deaths()
```

Returns the number of [deaths](#deaths) a player has suffered.

##### is_local

```
 is_local()
```

Returns true if this player is a local player, otherwise false.

##### kills

```
 kills()
```

Returns the number of [kills](#kills) a player has made.

##### name

```
 name()
```

Returns the [name](#name) of the player.

##### say

```
 say(text)
```

Makes the player send 'text' as a chat message.

##### select_weapons

```
 select_weapons(weapons)
```

Tries to change the player's weapons to the [WeaponType](/wiki/index.php/Lua_weapontype/) objects
in the array //weapons//.

##### stats

```
 stats()
```

Returns a lua table associated with the [stats](#stats) of this player.

##### team

```
 team()
```

Returns the [team](#team) number of the player.

##### worm

```
 worm()
```

Returns the [worm](#worm) of the player.
{% endraw %}
