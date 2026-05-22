---
title: Contribute to the source code
archived_url: "https://web.archive.org/web/20140824221835/http://www.openlierox.net/wiki/index.php/Contribute_to_the_source_code"
last_modified: "19:55, 25 May 2011"
---
{% raw %}
**Contributing to the source code** of [OpenLieroX](/wiki/index.php/OpenLieroX/) is the most important way of how you can [contribute](/wiki/index.php/Contribute/) to the project.

# Why

* [Learning to code](/wiki/index.php/Learning_to_code/)

# Where to start

## Contact

You should register to our [mailinglist](/wiki/index.php/Mailinglist/) and maybe leave a short mail there to introduce yourself.

For many cases, chatting with the developers is better than mails. Get some IM (Jabber, GTalk, ICQ, ...) contact details [here](/wiki/index.php/Talk_with_the_developers/).

There is also a [typical developer introduction talk](/wiki/index.php/Typical_developer_introduction_talk/) where you can find many frequently asked questions answered.

Also, to get more in touch with the gamer community behind the game, you might also ask in the [forum](/forum).

## Fetch the code

The first thing you need is the [OpenLieroX source code](/wiki/index.php/OpenLieroX_source_code/). Read here: [Obtaining OpenLieroX source from Git](/wiki/index.php/Obtaining_OpenLieroX_source_from_Git/)

You should also register on [GitHub](https://github.com). This is needed for all real work, i.e. pushing any source code commits online or making entries in the issue tracker.

## Setting up the environment

For a beginner, this is often the most complicated part. It is often not straightforward how you setup an [IDE](/wiki/index.php/IDE/) / Editor / [Compiler](http://en.wikipedia.org/wiki/Compiler) to compile the [OpenLieroX source code](/wiki/index.php/OpenLieroX_source_code/). This is somewhat silly but you have to get through that. (The *Compiler* will convert the OLX source code into an executable binary; on Windows, that is an *EXE*-file.)

The [IDE](/wiki/index.php/IDE/) is the *editor* where you edit the code. In theory, you could also use a simple text editor; however, an IDE will be mure more helpfull and easy to use. Read further here: [IDE](/wiki/index.php/IDE/)

In some cases (like MSVC), the IDE is bundled together with the compiler. In some other cases (on Linux), they are highly seperated and independent from each other. That means that setting up the compiling is in some cases (like MSVC or Xcode) the same as setting up the IDE, in some cases (like on Linux) independent.

However, compiling the source code is the most important thing you need to be able to do. You cannot do anything if you are not able to do this. Read about that here: [Compile OpenLieroX](/wiki/index.php/Compile_OpenLieroX/)

## Get an overview over the code

To be able to do something usefull with the code, it is very helpfull / mandatory that you have a rough overview over the code. We have written a special article just about this: [OpenLieroX source code](/wiki/index.php/OpenLieroX_source_code/)

# Working with the code

The very first thing to start is of course to get the [code to compile](/wiki/index.php/Compile_OpenLieroX/). I assume at this point that you have gotten at least so far.

## Starting hints

Some starting hints to get used to the code:

* Read the [code-overview](/wiki/index.php/OpenLieroX_source_code/#overview_of_the_code).
* [Talk to the developers](/wiki/index.php/Talk_to_the_developers/).
* Look at recent [Git](/wiki/index.php/Git/) commits and their changes.
* Configure your [IDE](/wiki/index.php/IDE/). That will help you a lot on working on it.
* Take a look at the [GitHub issue tracker](https://github.com/albertz/openlierox/issues).
* There are also some random TODOs in the code itself.
* Make some cleanups. I marked the most terrible parts which have to be recoded but there are much more which don't look that nice.
* Start some new feature.

## What you can do

Here is a rough list about what could be done.

* More or less somewhat complicated entries in the issue tracker which are good starting tasks for newcomers are marked [here](https://github.com/albertz/openlierox/issues?labels=medium-complicated-but-good-start&sort=created&direction=asc&state=open&page=1).
* Simple tasks in the issue tracker are marked [here](https://github.com/albertz/openlierox/issues?labels=simple&sort=created&direction=asc&state=open&page=1). Very simple tasks are marked [here](https://github.com/albertz/openlierox/issues?labels=very-simple&sort=created&direction=asc&state=open&page=1).
* [Port OpenLieroX to another system](/wiki/index.php/Port_OpenLieroX_to_another_system/). Like your mobile phone or your gaming console. Or whatever else you might want to play it on.
* Add original Liero support. [Gusanos](/wiki/index.php/Gusanos/) worm physics is already pretty close but we lack a physically close mod (the LX Classic mod is somewhat different in physics). Request for that was made on LXA [here](/forum/index.php/topic,12991). See the [issue tracker entry about this](https://github.com/albertz/openlierox/issues/745) for further details.
* Improve the bot AI (artificial intelligence) or add your complete own bot AI implementation. You can compete against the current implementation (which is already quite good).

Or just play a bit with OpenLieroX and be creative about what could be improved / added.

## Pushing your changes online

As a newcomer, you should [fork the project](https://github.com/albertz/openlierox/) on [GitHub](/wiki/index.php/GitHub/) and then you can freely just push all the changes to your fork. Then, when you have something done, you can make a pull request via GitHub and we can review your changes and if they are good, we can merge them into the original source. This is all very simple, just try it out!

You should also read [Git#Working_on_the_code](/wiki/index.php/Git/#working_on_the_code) and the basic [code style guide](/wiki/index.php/OpenLieroX_source_code/#style_guidelines).

Once we see that you have learned how to make good commits and not to mess around with the repository, we can also give to direct access to the official Git repository.
{% endraw %}
