---
title: OpenLieroX source code
archived_url: "https://web.archive.org/web/20130212053654/http://www.openlierox.net:80/wiki/index.php/OpenLieroX_source_code"
last_modified: "04:48, 1 July 2011"
---
{% raw %}
This is about the **source code** of [OpenLieroX](/wiki/index.php/OpenLieroX/). The source code is the code behind OpenLieroX which describes exactly what OLX is doing. The game was mostly written in [C++](/wiki/index.php/C++/). Read here [how to get the source](/wiki/index.php/Obtaining_OpenLieroX_source/).

This text was taken from the file doc/Development. Not sure what I will keep more up-to-date, so maybe also take a look there. But I guess this Wiki page is more reliable. :)

# Basic information

If you want to work with the code, read here: [Working with the code](/wiki/index.php/Working_with_the_code/)

# Style guidelines

This is about the code itself. About the organisation in Git, please [read here](/wiki/index.php/Git/#working_on_the_code).

We don't have really strict rules. Some basic rules:

* **Write clean code!** This is probably the most important of all rules.
* Use standard C++. Not MS C++!!

For example:

```
 for(int i = 0;;) {}
 for(i = 0;;) {}
```

is *not* correct C++ code! But this is:

```
 for(int i = 0;;) {}
 for(int i = 0;;) {}
```

* Don't make any really crazy optimizations. Produce clear, simple and short code.
* Make small functions! If your function is too big, cut it into pieces.
* Don't use too much local variables in a function.
  * It is slow.
  * You made something wrong. Generally, you don't need this. Maybe you should split your function up into several function. Or make a small helper class/struct.
  * It looks terrible!
* Don't ever use C-technics. That includes for example all strcpy and related functions and of course in general C-strings. Also don't use int if you mean bool. Things like these...
* Use the STL and STL-like technics (for example, use std::string, std::list, ...).

:   :   Some good links:
    :   * <http://www.cppreference.com/index.html>
    :   * <http://www.sgi.com/tech/stl/table_of_contents.html>

* Produce abstract and general code!

:   (This is realy important because we soon want to change the base code and all code, which is not general enough has to be redone. Keep this in mind...)

* Don't hack around!

:   It's not good if you add some new features only with some small hacks to the code. The code becomes even more terrible by this. Also, almost every hacked-in feature isn't general enough to allow a simple reuse of it in a new codebase. If you want to add kind of a hack for some backward-compatibility, think first about if you realy want this. Perhaps it's just better for this new feature to allow it only for new versions. Because you should not only think of the backward-compatibility. Also think of the forward-compatibility. Also, if you realy want to implement a hack, leave at least the code clean!

* Format and indent the code correct! (Use tabs for indenting!)
* Place spaces between each element which should be read seperated!

:   For example, this looks terrible:

```
 CVec* v=somewhat;for(v->x=0,v->y=10;(v->x<10&&v->y>=0);v->x++,v->y--)cout<<v->x<<v->y<<endl;
```

:   This looks much better:

```
 CVec* v = somewhat;
 for(v->x = 0, v->y = 10; v->x < 10 && v->y >= 0; v->x++, v->y--)
    cout << v->x << v->y << endl;
```

* Mark incomplete or temporary code with a TODO!
* Comment your code where you made some strange, not selfexplaining stuff.
* Don't upload any temporary testing-code into the code which produces for example some debug-files for you which is useless for the others.
* Don't add options for every single change you made in the code. If you are unsure if users will like it, discuss the problem with othrer devs or community first. Too many weird options will only confuse the user. If there is a best option for every user, this is more a question of automatically getting that best option.
* Make sure that the code compiles before uploading!
* TEST your code before uploading (the deeper the better)
  * Mark unstable parts with TODO

...

# Overview of the code

[TODO: This has to be extended a bit. But don't extend it to much, it should only be an overview here that allows you withing an hour to get some basic ideas and impressions of the code. :) Also, don't explain every single code file here; if you want to know what each single code-file is for, look into them; they (should) contain this information themself. Or you could also just link it to a seperate Wiki page.]

So, you are new to the code, so this will perhaps help you a bit:

## Files

* src/main.cpp - includes the main-entry point and the gameloop
* src/client/* - mainly the menu and all client-related stuff
* src/common/* - all more generaly stuff and also the main-structures (like worm, map, ..)
* src/server/* - server-related stuff, also for example the game itself
* src/game/* - all game logic related stuff and the main game handling
* src/sound/* - sound low level backend functions (bindings to OpenAL and such)
* src/gusanos/* - [Gusanos](/wiki/index.php/Gusanos/) related stuff, i.e. also all the [Lua](/wiki/index.php/Lua/) bindings and so on
* src/breakpad/* - [Breakpad](/wiki/index.php/Breakpad/) related stuff (you should not care about that at the beginning)
* include/* - header-files for all sources (*this is depcrecated*)

And there may be more directories in src/, which are probably not that important for now. But it should be self-explanatory from the name. Since 0.59, we are cleaning up the code structure a bit. Earlier, all headers were seperated from the cpp files. For OLX, there is no good reason to seperate them. Also, we may have more deeper directory structures to keep things cleaner.

## Most important code

* main() and most stuff in main.cpp
* game/Game
* CMap
* CWorm
* CServer
* CClient
* CGameScript
* LieroX

## Game-logic

* game/Game
* CServer
* CClient
* CGameScript

## Important for physics

* Physics*
* CMap, CWorm, CProjectile, Entity, CNinjaRope

## Other important things

* File-IO, also (mainly) searchpath-handling: [FindFile](/wiki/index.php/FindFile/)
* Caching system for graphics and sounds: Cache
* Network-related things: [Networking](/wiki/index.php/Networking/), CBytestream, CChannel
* Sound-related: Sounds
* Graphic-related: Graphics, GfxPrimitives
* Gusanos: [Read here about technical details of the merge.](/wiki/index.php/Merge_with_Gusanos/)
{% endraw %}
