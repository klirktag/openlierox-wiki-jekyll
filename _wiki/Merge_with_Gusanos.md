---
title: Merge with Gusanos
archived_url: "https://web.archive.org/web/20120321054530/http://www.openlierox.net/wiki/index.php/Merge_with_Gusanos"
last_modified: "14:16, 30 January 2010"
---
{% raw %}
In [OpenLieroX](/wiki/index.php/OpenLieroX/) 0.59, we started to merge [Gusanos](/wiki/index.php/Gusanos/) into OpenLieroX. This is some rough overview what this means.

# Effects for the player

* You can play Gusanos maps and Gusanos mods.
* You can play Gusanos maps and LieroX mods.
* LieroX maps and Gusanos mods.
* (Of course also LieroX maps and LieroX mods.)
* You have 3D sounds.
* Special Gusanos gamemodes will be ignored (they are implemented in the mods, not in Gusanos and we don't want that), you can play all OLX gamemodes (CTF, Hide&seek, and so on) in Gusanos mods/maps.
* OLX will do the game logic handling (check things like killlimit, lifelimit, and so on).
* We have [Lua](/wiki/index.php/Lua/) scripting possibilities now for both maps and mods (i.e. weapons).
* There are much more terrain types for maps, not just rock, dirt, background.
* You have dynamic elements in maps.

You can also write your own scripted and dynamic maps / mods now. Read the [Gusanos Modding](/wiki/index.php/Gusanos_Modding/) page.

# Technically

## Code base

I have used the Vermes code base to start with. Vermes was a fork of Gusanos which had prepared to clean up the Gusanos code base and to replace the commercial libraries in Gusanos by open ones. The problematic libraries used in Gusanos are fmod and Zoidcom. Those are commercial and restricted to a very limited set of systems. Most importantly, they are incompatible to [GPL](/wiki/index.php/GPL/). In Vermes, fmod was already replaced by OpenAL.

## Network

The further work I did was to reimplement Zoidcom (I don't know of any Open Source, GPL compatible replacement) - or at least those functions which were used in the Gusanos code. First, I refactured all the code in Gusanos to not use the ZCom_ (or similar) prefixed functions and classes but to have it prefixed with Net_ or NetStream_ (or similar). Then, I collected all used functions/classes from the Gusanos code and wrote a new header (gusanos/netstream.h) including exactly those functions/classes (I never had ZoidCom on my disk at all). Then, I started to implement this (gusanos/netstream.cpp). It uses our OLX CChannel network reliable channel implementation as a backend (whereby it could easily be used also with other backends in other projects, I guess).

This works good, except that it is not very optimised yet for bandwidth. At the moment, Gusanos gameplay takes more network than OLX gameplay (I think - I never actually messured it).

When we finished the work on the New network engine, this whole thing may become obsolete anyway. On the other side, it is more elegant and robust than the old LX network engine.

## Graphics

This may change in the future, so I keep myself short here about how it is right now (at the time of writing): Gusanos draws everything with 320x240 resolution. The OLX window/fullscreen uses 640x480 pixels. In LX, it is a bit mixed (map in 320x240, worm skins in 640x480, etc.) and the LX draw functions of all objects (map, worms, projectiles) directly draw for 640x480. Because the whole Gusanos drawing is for 320x240, we draw this to some buffer surface and then scale it up to 640x480 to the screen surface (see CClient_Draw.cpp).

## Sounds

OpenAL is the new base for everything, also for the OLX sounds.

## Loading of map/mod

This may also change (and it should, because it is hacky):

CMap and CGameScript are still the base classes which are used for the mod / map. They were just extended to handle also Gusanos.

### CGameScript

Actually, CGameScript just have a single flag: gusEngineUsed(). It doesn't do any loading at all. In Gusanos, the loading of the mod is always done at the time where we load a new map. So we handle it there. In case, you play a game with a LX map & Gus mod, there is some special code which loads the Gus mod without a Gus map in game/Game.cpp. In any case, for a Gusanos mod, the CGameScript::Load() function just sets the Gusanos mod and remembers it to be loaded the next time when we start a game or load a Gusanos map.

It works like this because for debugging reasons, I tried to make it behave exactly as Gusanos behaved when loading the mod/map. It does that quite well now.

Because of this situation, in CServer/CClient, when we load the mod/map, we always first must load the mod and then the map!

### CMap

This also has a flag, if this is a Gusanos map. Right now, Gusanos have a seperated array for pixel flags (because they differ a lot, there are much more different types, actually up to 255 types). Gusanos has also its own surfaces, three types of them. As with CGameScript, CMap::Load() handles all possible cases for all map types (the whole map loading code is in MapLoader.cpp).

No matter what map type you load (we currently support three main types: LX, Commander Keen, Gusanos), it will always setup both LX pixelflags and Gusanos pixel flags. And all maps will also setup the LX drawing surfaces (bmpBackImage and bmpImage). This works also fine for Gusanos because LX maps anyway have only 320x240 resolution, as the Gusanos maps. In fact, bmpImage uses even the same SDL_Surface as the internal surface of the Gusanos allegro surface.

## Gusanos objects

Gusanos has these kind of objects:

* map: CMap
* worm: CWorm
* player: CWormInputHandler
* particles: own class - similar to LX projectiles
* weapons

## Lua

Lua is kept totally seperated. It is initiallised when you load a Gusanos mod (I really mean the Gusanos loading functions of a mod here, not CGameScript::Load() which does nothing for a Gusanos mod). And it is reset for each game. It has bindings for all types of Gusanos objects and can basically do anything with them. There are also a bunch of callbacks for different kind of actions (like a new worm initialised - or just some player update frame callback).

Every mod and map can have scripts attached.

## OmfgScript

This is more a description language than a scripting language. All particles and weapons are described in this language. You setup the basic attributes and also any type of events here. You can setup as much events as you want and you have many different possibilities here. For each event, there are several different fixed types of actions you can use. One action is also to call a Lua script function. This is the way how you use Lua together with your particles / weapons.
{% endraw %}
