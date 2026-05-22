---
title: Port OpenLieroX to another system
archived_url: "https://web.archive.org/web/20120425164359/http://www.openlierox.net:80/wiki/index.php/Port_OpenLieroX_to_another_system"
last_modified: "21:32, 9 May 2010"
---
{% raw %}
**Porting OpenLieroX to another system** means to add support in the [OpenLieroX](/wiki/index.php/OpenLieroX/) [source code](/wiki/index.php/OpenLieroX_source_code/) so that it works on some other system. This can be a [mobile phone](http://en.wikipedia.org/wiki/Mobile_phone) (or [Smartphone](http://en.wikipedia.org/wiki/Smartphone)), a [gaming console](http://en.wikipedia.org/wiki/Gaming_console) or also another [operating system](http://en.wikipedia.org/wiki/Operating_system) (right now, [Windows](http://en.wikipedia.org/wiki/Windows), [Linux](http://en.wikipedia.org/wiki/Linux), [MacOSX](http://en.wikipedia.org/wiki/MacOSX), [FreeBSD](http://en.wikipedia.org/wiki/FreeBSD) as well as any [POSIX](http://en.wikipedia.org/wiki/POSIX)-compatible system are supported).

# Information for specific ports

* [OLX on PS2](http://lxalliance.net/forum/index.php/topic,11522.0.html)
* [OLX on Wii](http://lxalliance.net/forum/index.php/topic,11505.0.html)
* [OLX on Nokia N800/N810](http://lxalliance.net/forum/index.php/topic,10802.0.html) (working version reported)
* [OLX on Motorola Z6](http://lxalliance.net/forum/index.php/topic,11167.0.html)
* [OLX on LG enV2](http://lxalliance.net/forum/index.php/topic,10917.0.html)
* [OLX on Xbox](http://lxalliance.net/forum/index.php/topic,10760.0.html) (very unprobable to come)
* [OLX on PSP](http://lxalliance.net/forum/index.php/topic,10313.0.html)

In case you want to start a new port, please add it to this list and post some information in the [forum](/wiki/index.php/LXA/) or here in the Wiki.

# Basic requirements

## C++

The most important requirement is that you can compile [C++](/wiki/index.php/C++/) code for that system.

## SDL

[SDL](http://www.libsdl.org/) is currently used for:

* the input system (keyboard, mouse, gamepads)
* creating the window / screen drawing area
* handling system events (closing the game, etc.)
* drawing on the screen/window

SDL is ported to a lot of systems already. Search on Google for an SDL port for your favourite system (because not all are noted on the official homepage). In many cases, having this will make the porting a lot easier. It also means that the system probably has all the requirements in principle to support OLX.

In case there is no SDL port for the system, you might also port SDL yourself. The SDL code is very portable and you will probably get help from many other people who are interested in it.

Getting rid of the SDL dependency in OLX would be a lot of work (maybe even more work than just porting SDL yourself). Though, it is not impossible and it has been made already much easier than it was earlier. The heaviest part is the graphics code and image manipulations. Though, this is also the part which is most likely replaced by [OpenGL](http://en.wikipedia.org/wiki/OpenGL) code at some time.

## OpenAL

Since OLX 0.59, we are using [OpenAL](http://en.wikipedia.org/wiki/OpenAL) for the audio code. (Earlier we used SDL for this. SDL is much more low level though and doesn't have 3D sound support.)

OpenLieroX should work with any OpenAL implementation. There is the [OpenAL Soft](http://kcat.strangesoft.net/openal.html) implementation which should work pretty much on every system (or which should be easy to port).

## Boost

OpenLieroX uses some parts of [Boost](http://en.wikipedia.org/wiki/Boost_C%2B%2B_Libraries). Right now, that are:

* Boost signals
* Boost process
* Boost shared_ptr

## Some other libraries

Like [zlib](http://en.wikipedia.org/wiki/Zlib), [xml2](http://en.wikipedia.org/wiki/Libxml2) and others. I won't list them all here. But most of them are very basic and also pretty much cross platform themself. So even if your system doesn't provide this, the libraries are all [Open Source](http://en.wikipedia.org/wiki/Open_source) and will most likely be compileable on your system (if the rest of OLX compiles).

Take a look at the file *DEPS* in your OpenLieroX archive. That file contains a full list of all dependencies.
{% endraw %}
