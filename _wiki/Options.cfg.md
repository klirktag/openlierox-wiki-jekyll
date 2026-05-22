---
title: Options.cfg
archived_url: "https://web.archive.org/web/20100527042321/http://www.openlierox.net:80/wiki/index.php/Options.cfg"
last_modified: "11:55, 12 November 2009"
---
{% raw %}
The file *options.cfg* (or more exact *cfg/options.cfg*) is the main configuration file of OLX. After first start of OLX, OLX will create that file automatically for you and save it in your home directory, i.e. depending on your system, common to most other applications:

On Windows:

```
My Documents\OpenLieroX\cfg\options.cfg
```

On Linux/Unix:

```
~/.OpenLieroX/cfg/options.cfg
```

On MacOSX:

```
~/Library/Application Support/OpenLieroX/cfg/options.cfg
```

The file *options.cfg* is mostly like the common INI-fileformat. The fileformat should be selfexplanatory.

If OLX finds such a file in any of its searchpaths, wherbey the above paths have highest priority, it will load them automatically. See the search path system for further information about how OLX determines where it loads a file from.

If you want to redistribute OLX with an own set of default settings, you can place an own *cfg/options.cfg* into the OLX-path (see the search path system about why and how this works). This could make sense for projects like PortableApps when you even want to make the *options.cfg* portable by overwriting the default order of search paths. Your customized *options.cfg* doesn't need to be complete - OLX will just use the default options if you did not specify them.

There is also the possibility to load a config ingame and to save the config ingame, or to save only a specific section. These are the related [ingame commands](/wiki/index.php/Commands/):

```` ```
loadConfig [<file>] - loads the config
saveConfig [<file>] - saves the current config
saveConfigSection <section> <file> - saves only the specified section
``` ````

For example, you can save your current game settings:

```
saveConfigSection GameOptions.GameInfo preset1.cfg
```

And load it via:

```
loadConfig preset1.cfg
```
{% endraw %}
