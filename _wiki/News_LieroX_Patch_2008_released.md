---
title: "News:LieroX Patch 2008 released"
archived_url: "https://web.archive.org/web/20110721115315/http://www.openlierox.net/wiki/index.php/News:LieroX_Patch_2008_released"
last_modified: "15:07, 6 April 2008"
---
{% raw %}
Template:NewsArticle
On april 5:th 2008 DarkCharlie annouced the release of LieroX Patch 2008.
The patch was made for those who are using the original LieroX v0.56b to improve upon security issues and bugfixes.

Below follows a full list of the improvements made as stated in the [announcement thread](http://lxalliance.net/forum/index.php?topic=9944.msg112548#msg112548|) on [LXA](/wiki/index.php/LXA/).

## Fixes

* Error loading mod bug
* Crash in server info dialog
* Crash when leaving host and joining a server instead
* Crash when changing from bigger level to a smaller level when hosting/playing on a server
* Crash when right-clicking the most bottom server in the server list
* Crash when using filtered level
* Bad repainting of game info and player list in lobby
* Server spawning banned weapons as bonuses
* Server sending wrong server info while loading
* Server list shows all servers "down" with some routers/modems even though they are up
* Keys are not randomly ignored when typing
* Wrong shadows in some levels
* %n%n%n crashes
* Random weapons do not select banned weapons anymore
* Bots don't select banned weapons
* Carving worms make tunnels instead of seldom holes
* Self shooting on big velocities
* Text ingame not wrapped correctly
* Rope shaking when hooked at player (only for OLX beta 4/5 and this patch though)
* Shooting with banned weapons is not possible anymore
* Ready controls in lobby don't reset when someone joins
* Teams in lobby don't screw when returning back to lobby anymore
* Serverlist accidentally jumping up
* Serverlist sometimes not loaded even though the masterserver is up
* Numeric keyboard gets recognized
* Host can't kick himself/time out or leave
* Capping the FPS in a correct way
* Removing junk projectiles - invisible projectiles that get never destroyed and make the game more and more laggy
* Memory leaks (wasting your RAM)
* "Player has connected" message not displayed correctly sometimes
* All known security vulnerabilities
* Loads of client/server crashes due to bad network data
* Anti-cheat features (infinite lives hack with suicide, killing in lobby and more)
* Options get saved when clicking on "Back" button
* ALT-F4/close button work correctly everywhere now
* No Tag gametype messages displayed when playing deatchmatch
* Probably more Smiley

## Improvements

* Removed some slow code which makes the FPS better
* Enhanced textbox and ingame chat (same as in OLX)
* Added mouse wheel support
* Improved drop-down list
* Added suicide command to make it possible to return to the game if you stuck out of the level
* Console opens also when pressing F1
* Console works also for client
* Optional possibility to accept "wants to join" messages, off by default, can be enabled in config file under [Network]
* The server sends info about lives, IP addresses and its version just like the modern OLXs
* Added ping (was needed for some network fixes so I decided to add an option to show it), enable it in Options -> System
* Reset button in Weapon Options cycles all weapons through Banned/Bonus/Enabled states, instead of making them all enabled
* Level and mod lists get re-filled when ALT-TABbing to LX so you don't need to rehost when downloading a new mod/level
* Removed screenshot limit
{% endraw %}
