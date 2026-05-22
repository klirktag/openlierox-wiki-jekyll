---
title: Dedicated server
archived_url: "https://web.archive.org/web/20101228144731/http://www.openlierox.net/wiki/index.php/Dedicated_server"
last_modified: "11:02, 12 November 2009"
---
{% raw %}
The dedicated server has become quite stable and usable in the 0.58 branch. I am running several dedicated servers already since the last days, mostly even two on the same machine.

There are currently two working dedicated scripts: The default Python script (where you have voting, map/mod/preset rotation, ranking and some more stuff) and some very simple Bash script (just simple map rotation + countdown timer). The Bash script was never thought to be much powerfull and it's probably not worth to improve it. The Python script has some nice ideas and many further nice stuff could be implemented.

Or you could also implement your own script from scratch if you want. And you can use any language you prefer. It is actually quite simple. You just push any dedicated commands (= ingame console commands) and you will get the return values by these commands. You will also receive a set of events (like worm died, worm joined, and a whole lot more). More information can be read at [Dedicated script](/wiki/index.php/Dedicated_script/).

However, you could also just use the existing scripts - they do their work. There are multiple configs where you can tweak some stuff, define the level/mod list, and much more. For this, look into *cfg/dedicated_config.py* and *scripts/*.py*.

The dedicated server should already work out-of-the-box in any of the releases (Windows, Linux, MacOSX). To start it, just put "-dedicated" as a command line parameter:

```` ```
openlierox -dedicated
``` ````

Sometimes, I prefer to have a different config file for my dedicated server. For example:

```` ```
openlierox -dedicated -exec "loadConfig mydedconfig.cfg"
``` ````

By default, OLX will use the dedicated_control script (in the scripts directory). If you want to use another script, simply do this:

```` ```
openlierox -dedicated -script simple_ded_control.sh
``` ````

On Linux / Unix / MacOSX, you can also control the server via console. You can just enter any ingameconsole/dedicated command.

Probably an easier / more comfortable way to control the server is via chat commands. You have to define a password in your config file. The you can login with the chat command "/login <pw>".

The advantage of chat commands is the autocompletion. Just type "/" and some letters and press TAB, and it will autocomplete as far as possible. If there are multiple possibilities, TAB will list you those.

There are some handy commands like "/setvar" (and autocompletion also works further here, type "/setvar G" and press TAB), "/start", "/lobby", "/map", "/mod" and some more.

Then, there is also "/ded" where you can execute any of the ingame/dedicated commands. And autocompletion also works here, which is very powerfull.

To get a list of all commands, type "/ded help".

You can also reload another dedicated script ingame with the command "script <otherscript>". Or you could disable the dedicated script at all, via "script /dev/null" (works also on Windows if you wonder). This works also from command line, i.e. if you want to start OLX in dedicated mode but without any script, you can do it like this:

```` ```
openlierox -dedicated -script /dev/null
``` ````

You can also load another config file, with "loadconfig <othercfg>".

Many more things are possible, just look at "help" (or "/ded help"). Also take a look at [Commands](/wiki/index.php/Commands/).

So, if any questions, just ask in our forums. Otherwise I want to see some more dedicated server in the upcoming time. :P
{% endraw %}
