---
title: Chat commands
archived_url: "https://web.archive.org/web/20130212063557/http://www.openlierox.net:80/wiki/index.php/Chat_commands"
last_modified: "12:16, 12 November 2009"
---
{% raw %}
Chat commands can be entered in chat and start with "/".

For most commands, you need to be authorized on the server to execute them. To get authorized, there is the "/login" command. Just type "/login <password>", where "<password>" is the [password](/wiki/index.php/Password/) you have set in your [options.cfg](/wiki/index.php/Options.cfg/). Once you are authorized, you can give also the authorization to other clients on the server, with "/authorize <worm>".

Here some other commands (incomplete list yet, feel free to extend):

```
/start - starts the game
/lobby - return to lobby
/map <map> - sets a map
/mod <mod> - sets a mod
/setvar <var> <value> - sets a variable
/ded <cmd> - executes a dedicated command
```

See the [list of variables](/wiki/index.php/Variables/) for further information about the variables. See [list of commands](/wiki/index.php/Commands/) for further information about the dedicated commands.

There is also autocompletion via chat commands. Just press the TAB-key at some point. You can use that to get a more full list of all chat commands.

For some commands, like "/setvar", "/ded", "/map" or "/mod", it also works for the parameters. For example, you can type

```
/map Castle[TAB]
```

and it will automatically complete. In case of "/ded", it even works for all dedicated commands and even their parameters.

Here some more from an older documentation:

* /kick - Kicks a player from the server.

```
/kick player
/kick id # "reason"
/kick id # kick player
Where # is the number next to the name of the player in the scoreboard.
```

* /ban - Bans a player from the server.

```
/ban player
/ban "player name"
/ban id #
```

* /mute - Mutes a player on the server

```
/mute player
/mute "player name"
/mute id #
```

* /unmute - Unmutes a player on the server

```
/unmute player
/unmute "player name"
/unmute id #
```

* /setname - Sets the name of yourself or player.

```
/setname name (Beta3-4, use /setmyname in Beta5+)
/setname "your name" (Beta3-4, use /setmyname in Beta5+)
/setmyname name (beta5+ only)
/setmyname "your name" (beta5+ only)
/setname id # "Name of player" (only for host in Beta5+)
```

* /setskin - Sets the skin of yourself or player.

```
/setskin "skinname.png" (Beta3-4, use /setmyskin in Beta5+)
/setmyskin "skinname.png" (beta5+ only)
/setskin id # "skinname.png" (only for host in Beta5+)
```

* /setcolor - Sets the color of yourself or other player

```
/setcolor R G B (Beta3-4, use /setmycolour in Beta5+)
/setcolour R G B (Beta3-4, use /setmycolour in Beta5+)
/setmycolor R G B (beta5+ only)
/setmycolour R G B (beta5+ only)
/setcolor id # R G B (only for host in Beta5+)
/setcolour id # R G B (only for host in Beta5+)
R G B - Red Green Blue value, between 0 and 255
```

* /pm - Sends a private message to a player

```
/pm "player name" "message"
/private "player name" "message"
/pm id # "message"
/private id # "message"
```

* /teampm - Sends a message to your team

```
/teampm "message" (beta5+ only)
/teamchat "message"
```

* /suicide - suicide yourself

```
/suicide - suicide yourself (beta3+)
/suicide # - suicide yourself several times (beta3+)
```

* /spectate - spectate the game

```
/spectate - sets your lives to 0 and suicides, so you won't spawn any more (beta6+)
```
{% endraw %}
