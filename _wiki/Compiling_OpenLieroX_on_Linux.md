---
title: Compiling OpenLieroX on Linux
archived_url: "https://web.archive.org/web/20110721122628/http://www.openlierox.net/wiki/index.php/Compiling_OpenLieroX_on_Linux"
last_modified: "17:22, 12 August 2010"
---
{% raw %}
Hello, welcome to my short tutorial about compiling OLX on Linux :)

First, you need the source code. Either you download the source code of some of the official releases [from SourceForge](http://sourceforge.net/projects/openlierox/files/) or if you want to have the most recent code (recommended if you want to test something or want to develop on/with OpenLieroX), you can [fetch the source from Git](/wiki/index.php/Obtaining_OpenLieroX_source_from_Git/).

This is a more or less general description which you could follow on any Linux system. There are some hints here and there for some specific Linux distributions which makes your life a bit easier. If you are stuck somewhere, you could also just ask here. (But think a bit before asking dumb questions. A question like "How do I install Subversion on my system" is a dumb question. You are probably using the wrong Linux distribution if you don't know how to install applications. Try Ubuntu.)

There are also some (possibly outdated) threads for some specific systems. I will not update them in detail, so it would be best to relay on *this* thread here. But perhaps you can get some usefull information also in the following threads:

* [Compile/Run OLX on the Eee PC](http://lxalliance.net/forum/index.php/topic,9395.0.html)
* [Compile OLX on ArchLinux](http://lxalliance.net/forum/index.php/topic,12360.0.html)

For Ubuntu/Debian, there is a quick command which does all of the steps: 1. install everything you need, 2. checkout OLX from SVN and 3. compile everything:

```
 sudo apt-get install build-essential subversion cmake libsdl1.2-dev libsdl-mixer1.2-dev libsdl-image1.2-dev  libgd2-noxpm-dev zlib1g-dev  libzip-dev libxml2-dev libx11-dev ; git clone ...TODOFILLINHERE; cd openlierox ; cmake -D HAWKNL_BUILTIN=1 -D DEBUG=0 . ; make -j4
```

After extracting / fetching the source, take a look at doc/README. It could be that some of the information here are outdated (or doesn't apply to the version you downloaded). If you downloaded an old version, don't expect to get much support for it. Try the newest version or the code from SVN.

First, you need to install some further dependencies. A list of all needed dependencies are in the file DEPS. Install them via your Linux package manager.
If you don't find HawkNL or Libzip in your Linux distribution, you can use the builtin version. I'll explain that later.

*For Fedora Core 6:*
I asume you got yumex, and basic knowledge of it, so start it up as root.
After that, go find the packages of **SDL** anything, add them to the que, then search for **hawkNL**, add both of the results to the queue to.
Now search for libxml, it is a fairly standard library, i already had it even thought i rarely use my FC6.
Add **libxml2** to the queue.
I asume you already got zlib & gd, if it errors later, just do the same procedure as above but for them.

Proccess the queue.

*For Debian/Ubuntu:*

```
 sudo apt-get install build-essential
 sudo apt-get install cmake
 sudo apt-get install libsdl1.2-dev
 sudo apt-get install libsdl-mixer1.2-dev
 sudo apt-get install libsdl-image1.2-dev
 sudo apt-get install libgd2-xpm-dev
 sudo apt-get install libzip-dev
 sudo apt-get install zlib1g-dev
 sudo apt-get install libxml2-dev
 sudo apt-get install libcurl4-gnutls-dev
 sudo apt-get install libboost-dev
 sudo apt-get install libalut-dev
```

Now, in console, go to the directory of the OpenLieroX source, and type:

```
 cmake .
```

It should look something similar to this:

```
 az@server ~/Programmierung/openlierox $ cmake .
 DEBUG = ON
 DEDICATED_ONLY = ON
 G15 = OFF
 X11 = No
 HAWKNL_BUILTIN = ON
 LIBZIP_BUILTIN = OFF
 STLPORT = OFF
 GCOREDUMPER = OFF
 CMAKE_C_COMPILER = /usr/bin/gcc
 CMAKE_C_FLAGS = -ggdb -O0
 CMAKE_CXX_COMPILER = /usr/bin/c++
 CMAKE_CXX_FLAGS = -ggdb -O0
 PCH = OFF (Precompiled header, CMake 2.6 only)
 PYTHON_DED_EMBEDDED = OFF
 OLX_VERSION = 0.57_beta9_r3495
 -- Configuring done
 -- Generating done
 -- Build files have been written to: /home/az/Programmierung/openlierox
 az@server ~/Programmierung/openlierox $
```

You can change the variables which are statet there. (This output shows my specific settings, it will probably look different for you. For example you probably want to have X11=On if you want to have any graphical output.) For example, if you want to use the builtin version of HawkNL (you need that on Debian/Ubuntu), type this:

```
 cmake -DHAWKNL_BUILTIN=On .
```

Sometimes, some optional subsystems don't work on some system. For example, right now (but this may hopefully change later), Google Breakpad is not supported on Linux 64bit. If you see errors in some of the breakpad src files, just do this:

```
 cmake -DBREAKPAD=Off .
```

Now, if you are ready with that, you can start the actual compiling. Just type this:

```
 make
```

If you have multiple CPUs/Cores in your machine, you can speed the compiling up. For example this command would use 4 parallel compiling processes:

```
 make -j4
```

If everything went fine, you can start the game now with:

```
 ./start.sh
```

*If you used Git and you want to update your code, simply do this:*

```
 git pull
```

You will see which files are updated. If you see that there was any new file or any deleted file, you need to rerun CMake. Just type again

```
 cmake .
```

(CMake remembers your setting from last time, so probably you don't have to reconfigure anything.) Then, just compile it again by

```
 make
```

or

```
 make -j4
```
{% endraw %}
