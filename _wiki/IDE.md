---
title: IDE
archived_url: "https://web.archive.org/web/20110721112400/http://www.openlierox.net/wiki/index.php/IDE"
last_modified: "18:45, 29 January 2010"
---
{% raw %}
IDE stands for *Integrated Development Environment*. [Wikipedia about IDE](http://en.wikipedia.org/wiki/Integrated_development_environment).

If you want to work on the [OpenLieroX](/wiki/index.php/OpenLieroX/) [source code](/wiki/index.php/OpenLieroX_source_code/), an IDE will help you a lot.

There are thousands of different IDEs. Some are much more powerfull than others. Some only have some advanced syntax hightlighting for C++ code (or other source code), some others have much more advanced technices like automatic code checking and automatic code completion and such fancy stuff.

# Windows

## MSVC

In case of MSVC on Windows, the IDE and the compiler are kind of tied together. So setting up MSVC for OpenLieroX means the same as setting up the compiling. Thus, [to setup MSVC is described here](/wiki/index.php/Compiling_OpenLieroX_on_Windows/).

# Linux/Unix

There are so much different IDEs in Linux that I really don't want to go into this topic that much.

## KDevelop

KDevelop is one of the most powerfull native IDEs for Linux for C++ (afaik). It's the one I am using. Setting it up is pretty trivial: First, [setup OLX to compile](/wiki/index.php/Compiling_OpenLieroX_on_Linux/). Then in KDevelop in the menu, there is an option "import existing project". Select the OLX dir. You will be asked about the build system. Either select Custom make based system or select CMake. You can leave all other questions at their default.

# Mac OS X

There is one main IDE on Mac OS X, which is free and can be downloaded from Apple (or may be even preinstalled on your system - or should also be on the MacOSX DVD). That is Xcode.

## Xcode

As Xcode is also the recommended way to compile OLX on MacOSX, [this is described here in the compile section already](/wiki/index.php/Compiling_OpenLieroX_on_Mac_OS_X/).
{% endraw %}
