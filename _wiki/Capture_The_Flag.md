---
title: Capture The Flag
archived_url: "https://web.archive.org/web/20110118203335/http://www.openlierox.net:80/wiki/index.php/Capture_The_Flag"
last_modified: "22:16, 15 November 2008"
---
{% raw %}
## Capture the Flag

Capture the Flag (CTF) is a game mode that was introduced between the releases of OpenLieroX beta 3 and beta 4 by Griffin.

It has been non-working since OpenLieroX beta 5 or 6.

## Rules

All players must capture the 'flag' and bring it back to the 'base' or hold it for as long as possible depending on the map.

A point (kill) is gained for returning the flag to the base or holding it for 15 seconds; kills gain no points.

## Maps

Turning a map into a CTF map can be done quite easily with a hex editor however there have not been any maps updated to be CTF compatible since the release of the CTF and the maps that were converted was restored to their original (non-CTF) versions not long after being uploaded to the OpenLieroX SVN Repository.
The maps that were converted and the location of where to take the flag are as follows:

Duel - Take the flag to the upper floor in the building in the centre

Section19A - Take the flag to the bunker with a flag on top of it

Snus Industry Ltd - Take the flag to the end of the campspot room

Liero Factory - Take the flag into the brown room near the top

Lamda Bunker - Take the flag into the dead-end room at the centre bottom

Base Fight - Take the flag into the bottom right corner

## Hex editing

Change the first 16 bytes to read "LieroX CTF Level" and append 6 coordinates to the end of the map (the coords must be signed shorts (2 bytes big, twos complement)).
The coordinates in order are: FlagSpawnX, FlagSpawnY, BaseTopLeftX, BaseTopLeftY, BaseBottomRightX, BaseBottomRightY.

If you want to have the Flag spawn randomly make its coordinates -1,-1 (0xFFFF, 0xFFFF) and if you don't want a map where you take the flag somewhere but instead want the worms to score by holding the flag the longest make the BaseTopLeftX coordinate -1 (0xFFFF).

For example the Duel level's data was: FF, FF, FF, FF, 92, 00, 6A, 00, AD, 00, 81, 00
This made the flag spawn randomly and set the base (place where you have to get the flag to) to the upper floor of the building in the centre of the map.
{% endraw %}
