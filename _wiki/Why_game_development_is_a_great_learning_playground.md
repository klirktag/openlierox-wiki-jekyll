---
title: Why game development is a great learning playground
archived_url: "https://web.archive.org/web/20140824201002/http://www.openlierox.net/wiki/index.php/Why_game_development_is_a_great_learning_playground"
last_modified: "23:57, 13 May 2011"
---
{% raw %}
I often stated that game development is a great way to learn coding. Despite the advertisement to [source code contribution](/wiki/index.php/Contribute_to_the_source_code/) to [OpenLieroX](/wiki/index.php/OpenLieroX/), there are indeed really a lot of good reasons why you can learn a lot by game development. And not only about coding itself, but also about advanced algorithms of various sorts and much more. I will present a list on this page.

If you compare it to the learning value of working on any tool or whatever other application, in most cases you will learn more by developing a game because games include a very wide area of technics while most other applications are mostly very limited in the amount of theories and technics involved.

# Computer science

## Coding

Of course the most basic part is the coding itself. That includes the [programming language](http://en.wikipedia.org/wiki/Programming_language) and getting used to it. Learning a programming language is not only learning the syntax and semantics - it is also about how you do it right.

In a medium/big sized game (and often even in small), there are often a bunch of different languages used together. In the OpenLieroX project, you will find applications of at least these languages:

* [C++](http://en.wikipedia.org/wiki/C%2B%2B). Most of the game and its core is written with it.
* [C](http://en.wikipedia.org/wiki/C_(programming_language)). Some rare parts of the game are C code.
* [Assembler](http://en.wikipedia.org/wiki/Assembly_language). Some performance critical parts of the game are written in Asm.
* [Lua](http://en.wikipedia.org/wiki/Lua_(programming_language)). We use Lua for ingame scripting.
* [Python](http://en.wikipedia.org/wiki/Python_(programming_language)). The [dedicated script](/wiki/index.php/Dedicated_script/) and a few other scripts use Python.
* [Bash](http://en.wikipedia.org/wiki/Bash_(Unix_shell)) / [Zsh](http://en.wikipedia.org/wiki/Z_shell). Many scripts to do some management (like [preparing release packages and distributing them](/wiki/index.php/Development/)) are using either Bash or Zsh.
* [CMake](http://en.wikipedia.org/wiki/CMake). Our build system uses it.
* [PHP](http://en.wikipedia.org/wiki/PHP). Our homepage uses it and also the reference implementation of the HTTP masterserver.

### Libraries

Knowing programming languages is not enough. Most languages also come with their own standard library but in many cases, you also need some external libraries or frameworks.

Here a list of libraries that the OpenLieroX core uses.

* [C standard library](http://en.wikipedia.org/wiki/C_standard_library)
* [STL](http://en.wikipedia.org/wiki/Standard_Template_Library)
* [Boost](http://en.wikipedia.org/wiki/Boost_C%2B%2B_Libraries)
* [SDL](http://en.wikipedia.org/wiki/Simple_DirectMedia_Layer). This is for initialising the window/screen, doing graphics operations and handling user input.
* SDL_image. For some more image formats.
* GD. Another lib for various image formats and image handlings.
* HawkNL. For networking (TCP/UDP).
* [zlib](http://en.wikipedia.org/wiki/Zlib). Compression.
* libzip. ZIP support.
* libxml2. XML support.
* libcurl. HTTP support.
* [OpenAL](http://en.wikipedia.org/wiki/OpenAL). For sound.
* ALUT. For initialising the OpenAL environment and WAV support.
* libvorbis/libogg. For Vorbis OGG support.

For the other languages, we mostly restrict ourself to the standard library.

### Cross platform

If you don't want to restrict yourself to only one platform (like Linux or MacOSX or even Windows), you need to write your code in a way that it is mostly cross platform.

One important point is that the dependencies and libraries you are using are all also cross platform, i.e. available for most or all platforms. If you take a look at the list of libraries we are using, you will find that this is mostly the case.

In practice, this is not all. You will face problems that some things will just behave and work different depending on the platform. Also the platforms themself are by purpose somewhat different and handle things differently. So you will still end up in having different solutions and code paths in these cases for different platforms.

By working on a cross platform project like OpenLieroX, you will learn how to deal with such problems. We have a special article about this topic: [Port OpenLieroX to another system](/wiki/index.php/Port_OpenLieroX_to_another_system/)

### Architecture independence

This is somewhat related to cross platform. If you don't want to restrict yourself to one architecture (like [x86](http://en.wikipedia.org/wiki/X86) 32bit) you need to write your code in a way that it is architecture independent. As some platforms (like iPhone or Playstation) are naturally running on a different architecture (like [arm](http://en.wikipedia.org/wiki/ARM_architecture) or [ppc](http://en.wikipedia.org/wiki/PowerPC)), you are often forced to write architecture independent if you want to support those.

OpenLieroX should run on pretty much every architecture. Problems you are facing are for example about big/little endianness and 32bit versus 64bit.

### Protocols and file formats

In many cases, knowledge of protocols and file formats can be usefull, even if a library is doing all the handling for you. In some cases, you even need to implement some basic support for yourself.

Here a list of protocols or file formats you most likely will at least get a bit in touch with at OpenLieroX:

* [TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol), [UDP](http://en.wikipedia.org/wiki/User_Datagram_Protocol)
* [HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), [SMTP](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), [DNS](http://en.wikipedia.org/wiki/Domain_Name_System)
* INI, [XML](http://en.wikipedia.org/wiki/XML), MP3

Of course, OpenLieroX introduces also some own protocols (for networking) and file formats ([maps](/wiki/index.php/Levels/) and [mods](/wiki/index.php/Mod/)).

## Algorithms and data structures

You will need and learn all of the basic [algorithms](http://en.wikipedia.org/wiki/Algorithm) and [data structures](http://en.wikipedia.org/wiki/Data_structure). That are at least:

* linked lists, hash maps, vectors, stacks, queues, sets, trees
* sort, search, ...

## Graphics

When writing [graphics](http://en.wikipedia.org/wiki/Computer_graphics) related code, you are dealing with a wide range of topics, many of them being mathematical. Despite the mathematical part, you are often also dealing with performance problems and optimisations because this is often the most performance critical part. So you need to learn how to optimise your code and at the same time keep it maintainable.

Depending if your game is [2D](http://en.wikipedia.org/wiki/2D_computer_graphics) or [3D](http://en.wikipedia.org/wiki/3D_computer_graphics), the type of mathematics you are applying differs a bit (and probably 3D graphics need even some more deep knowledge of [Linear Algebra](http://en.wikipedia.org/wiki/Linear_algebra)) but there is also a big intersection.

## Audio

You learn about the basic calculation and principles how to calculate the sound modifications when you want to get a 3D sound experience.

## Artificial intelligence

The most obvious application of artificial intelligence in games is the computer enemy. AI in games and AI in general is really a topic for itself. Maybe the biggest and most important of all things which you learn by game development but that is up to your own focus.

Also, the subtopics of AI you can apply in a game depends a bit on the type of game. But in most cases, that are at least:

* [Planning](http://en.wikipedia.org/wiki/Planning) and [problem solving](http://en.wikipedia.org/wiki/Problem_solving)
* [Searching](http://en.wikipedia.org/wiki/Search_algorithm) and [pathfinding](http://en.wikipedia.org/wiki/Pathfinding) (e.g. [A*](http://en.wikipedia.org/wiki/A*_search_algorithm))
* [Learning](http://en.wikipedia.org/wiki/Machine_learning) (all kinds of: [supervised](http://en.wikipedia.org/wiki/Supervised_learning), [reinforced](http://en.wikipedia.org/wiki/Reinforcement_learning) and [unsupervised](http://en.wikipedia.org/wiki/Unsupervised_learning))
* [Knowledge representation](http://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning)
* [Pattern matching](http://en.wikipedia.org/wiki/Pattern_matching) and [recognition](http://en.wikipedia.org/wiki/Pattern_recognition)
* [Cognitive science](http://en.wikipedia.org/wiki/Cognitive_science)
* [Natural language processing](http://en.wikipedia.org/wiki/Natural_language_processing)

OpenLieroX has some advanced searching functions (sort of A* in an almost continuous space) and a bunch of hardcoded strategies and plans. We are planning to integrate much more soon, like a self-learning bot (based on [neural networks](http://en.wikipedia.org/wiki/Artificial_neural_network)) and also a [genetically engineered](http://en.wikipedia.org/wiki/Genetic_algorithm) bot. Also some basic support of natural language processing is planned so that the bot can chat.

## Game theory

[Game theory](http://en.wikipedia.org/wiki/Game_theory) deals with theoretical questions about strategies and states of games. If you want to answer questions like if there is a strategy for your game where you always will win - that is game theory.

Game theory also matters for some of the artificial intelligence applications.

## Networking

If you want to support some sort of multiplayer over a network (like the Internet), you need to know a bit about networking. It is not just about encoding and serializing your data and transfer it somehow over network. A game often needs very low latency. You are usually dealing with problems like:

* [synchronisation of time](http://en.wikipedia.org/wiki/Clock_synchronization) (and events in time)
* synchronisation of the game world state
* unreliable data channel

## Operating systems

How [operating systems](http://en.wikipedia.org/wiki/Operating_system) work is also a whole huge topic for itself. You will scratch many parts of this because a game often has many low level parts in its code where you must know some basics about operating systems. Esp, that is:

* File operations and [file systems](http://en.wikipedia.org/wiki/File_system)
* [Pipes](http://en.wikipedia.org/wiki/Pipeline_(computing))
* [Multithreading](http://en.wikipedia.org/wiki/Multithreading)
* [Memory](http://en.wikipedia.org/wiki/Computer_memory)

## Memory handling

In case you need to handle with huge amounts of memory, you need to know about memory optimisations and how a computer program usually handles the [memory allocations](http://en.wikipedia.org/wiki/Dynamic_memory_allocation) on a low level.

We at OpenLieroX esp. considered once to apply parts of [jemalloc](http://people.freebsd.org/~jasone/jemalloc/bsdcan2006/jemalloc.pdf).

OpenLieroX also can be build as a special debug version with our own [malloc](http://en.wikipedia.org/wiki/Malloc) implementation. (See file memstats.cpp.)

## Parallel computing

[Parallel computing](http://en.wikipedia.org/wiki/Parallel_computing) is where many computations are done simultaniosly in parallel. Games often need to make a lot of very heavy and intense calculations. The trend of computers is to have [multiple CPUs](http://en.wikipedia.org/wiki/Multiprocessing) (or [cores](http://en.wikipedia.org/wiki/Multi-core_processor)) instead of having a single one. To use them all, it is mandatory to write your code in a way that several parts can be executed in parallel. Despite the need for it, it also often leads to more clean code (if you do it right).

So, what you will learn is how to do parallel computing in general. That is both theoretic knowledge and practical knowledge. In the practice, parallel computing is often solved via multiple [threads](http://en.wikipedia.org/wiki/Thread_(computer_science)), i.e. [multithreading](http://en.wikipedia.org/wiki/Multithreading). The interesting parts are about how you synchronise your threads and how you communicate your data from one thread to another in a [safe way](http://en.wikipedia.org/wiki/Thread_safety).

## Version control

You will learn how to work with some kind of [version control](http://en.wikipedia.org/wiki/Revision_control) system which manages all your source code files and often also other resources of your project. It will keep track over all changes in all files and will make it possible that multiple people can work on the same code. With the history of the changes, you will be able to see what person has done what changes and you can hunt down bugs to specific changes. You can also see what person has written which parts of a source file and thus ask him about some details.

Such a system is even very helpfull and nice to have if you work alone on a project. And it is absolutely mandatory once you work in a team.

In OpenLieroX, we use [Git](http://en.wikipedia.org/wiki/Git_(software)) - a very powerfull [distributed revision control](http://en.wikipedia.org/wiki/Distributed_revision_control_system) system. Learning Git is really a whole topic for itself.

# Design

## Media

A game usually needs graphics, sounds, levels or other media. Those need to be created and designed.

## Story

Depending on the type of game, you need a story.

# Teamwork

A project of the size of OpenLieroX needs teamwork. Various people doing various different tasks (coding, designing, distribution, support, testing) need to coordinate. This is even more important for the coding which is the biggest of those tasks. Once there are multiple people working on the same code, they need to coordinate. The source code version control management system is very central for this.

# Management

A project like OpenLieroX also needs some noteable time for general [mangement and other things](/wiki/index.php/Development/). Here some points:

* [Issue/bug tracking](https://github.com/albertz/openlierox/issues)
* Releasing (prepare the packages for major platforms and distribution)
* Documentation about interfaces (levels, mods, scripting)
* Support for players
* Development discussions
* Version milestone planning
{% endraw %}
