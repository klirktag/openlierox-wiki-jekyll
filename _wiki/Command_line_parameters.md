---
title: Command line parameters
archived_url: "https://web.archive.org/web/20140803233610/http://www.openlierox.net:80/wiki/index.php/Command_line_parameters"
last_modified: "11:21, 12 November 2009"
---
{% raw %}
OLX supports a set of command line parameters. You get a list (which could be incomplete though) via the parameter "-help".

This is the output of 0.58 beta8:

```
available parameters:
   -connect srv  Connects to the server
   -exec cmd     Executes the command in console
   -opengl       OpenLieroX will use OpenGL for drawing
   -noopengl     Explicitly disable using OpenGL
   -dedicated    Dedicated mode
   -nojoystick   Disable Joystick support
   -nosound      Disable sound
   -window       Run in window mode
   -fullscreen   Run in fullscreen mode
   -skin         Turns on new skinned GUI - it's unfinished yet
   -noskin       Turns off new skinned GUI
```

Esp. "-exec <cmd>" may be interesting because you can execute any command you want. See the [list of commands](/wiki/index.php/Commands/) for further information. You can have multiple "-exec" parameters.

For example, this will start up a simple [dedicated server](/wiki/index.php/Dedicated_server/) without any script:

```
openlierox -dedicated -script /dev/null -exec startlobby -exec "addbots 2" -exec startgame
```

Or if you want a shortcut to connect to your favourit server with your default worm:

```
openlierox -connect server.az2000.de
```
{% endraw %}
