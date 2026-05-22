---
title: Gusanos Modding
archived_url: "https://web.archive.org/web/20110721114541/http://www.openlierox.net/wiki/index.php/Gusanos_Modding"
last_modified: "22:24, 25 March 2010"
---
{% raw %}
The original Gusanos documentation can be found [here](http://sliekas.org/basara/gusdocs/doku.php).

## Directory structure

The directory structure of Gusanos mods is:

* mod.cfg : mod [configuration](/wiki/index.php/Gusanos_cfg/)
* objects/ : directory of objects
  * *.obj : all kind of [objects](/wiki/index.php/Gusanos_objects/)
  * ninjarope.obj
  * death.obj
  * wormdig.obj
  * *.exp : [explosions](/wiki/index.php/Gusanos_explosions/)
* weapons/
  * *.wpn : [weapons](/wiki/index.php/Gusanos_weapons/)
* sounds/
  * chat.ogg
  * *.wav or *.ogg
* sprites/
  * *.png
* fonts/
  * minifont
* mapeffects/
  * *.mfx: [map effects](/wiki/index.php/Gusanos_map_effects/)
* scripts/ : [Lua](/wiki/index.php/Lua/) scripts
  * <modname>.lua : init-function
  * common.lua : init-function fallback, if <modname>.lua was not found
  * *.lua

## Gusanos Scripting

### Configurations

* [cfg files](/wiki/index.php/Gusanos_cfg/)

### Script

* [game actions](/wiki/index.php/Gusanos_game_actions/)
* [explosions](/wiki/index.php/Gusanos_explosions/)
* [map effects](/wiki/index.php/Gusanos_map_effects/)
* [objects](/wiki/index.php/Gusanos_objects/)
* [weapons](/wiki/index.php/Gusanos_weapons/)

### Lua scripting

* [Lua classes](/wiki/index.php/Lua_classes/)

## General

* [Fonts](/wiki/index.php/Gusanos_fonts/)
* [Sprites](/wiki/index.php/Gusanos_sprites/)
* [Sounds](/wiki/index.php/Gusanos_sounds/)

## Examples

* [Creating explosive drums using collision layers](/wiki/index.php/Gusanos_Tutorial_Creating_explosive_drums_using_collision_layers/)
* Check out the existing mods (there are some very famous already included in OLX). You'll find many more examples [here](/forum/index.php/topic,12842.0.html).
* [The Gusanos forums provide more help about modding.](http://comser.robal.org/forum/index.php/board,15.0.html)

## Changes of Gusanos in OpenLieroX

### Gusanos Console system

The Gusanos console is only used internally for Gusanos; OpenLieroX uses an own console system. And many commands/variables of the Gusanos console system are ignored and don't work in OpenLieroX. That are mostly all the game logic related stuff (maxkills etc.; this is all handled by OLX itself) and also system parameters (gfx settings etc.).

### Gusanos menu system

Is completly ignored in OLX. It is not rendered at all.
{% endraw %}
