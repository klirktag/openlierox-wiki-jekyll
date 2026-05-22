---
title: Gusanos Maps
archived_url: "https://web.archive.org/web/20110721112938/http://www.openlierox.net/wiki/index.php/Gusanos_Maps"
last_modified: "12:37, 31 January 2010"
---
{% raw %}
[Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:mapping_docs:level_format).]

Each [Gusanos](/wiki/index.php/Gusanos/) map is just a directory. Just create a directory of the desired map name in the *levels*-directory.

# Level directory structure

Inside this map-directory you need three files: config.cfg, level.png, and material.png. Depending on needs you can use additional files such as: background.png, lightmap.png, and paralax.png.

### config.cfg

This file contains imformation on where the worm spawns, and other object related things. This file must be present in a level folder or Gusanos will not recognise the folder as a level. You can also setup team bases (as for [Game modes](/wiki/index.php/Game_modes/) like CTF) or specify spawnpoints for specific teams.

###### Some examples

* [config.cfg example](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/poo/config.cfg;h=0f6efbeea5132d93c45aa84fa8aa0ed086758c48;hb=master)
* [config.cfg example of CTF map (with team spawn bases)](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/ctf_poo/config.cfg;h=9c886e857d4d0d19f957e564975cd30e8c03440f;hb=master)
* [config.cfg of dark map (base)](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/base/config.cfg;h=8a5d08ce44bf749d9a17e0fdc47e776c66bfd3a7;hb=master)

### level.png

This image contains the artwork that is visable when playing the map; it can be any size and any colour depth.

Note: If you use only a few colors for your map (such as shades of brown and gray) you might want to optimize the color palette to reduce the final size of the map (but be careful!).

Note: if you intend to make a map based on a JPEG image, you should make sure it has good quality by zooming in a few times and looking for artifacts. JPEG (unlike PNG) is a lossy compression format, and too much compression makes an image look like crap, especially on low screen resolutions as GUSANOS uses. Consider resizing the JPEG to become smaller rather than cropping it to increase quality.

###### Some examples

* [level.png example](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/koala/level.png;h=948834e7c5c8922c70606c13ba3200aeadb8065d;hb=master)
* [level.png of base-map](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/base/level.PNG;h=fa7baadd780a3453e272941206145c878954f951;hb=master)

### material.png

This file contains all the information on how objects should interact with the level, it acts as a mask for level.png, telling Gusanos which parts of the map are passable and destructable.

This image should be in png format at the same size as level.png, and use an indexed colour palette (256 colors max). The colours in the palette are irrelevant, what matters is which index of the palette they are. For example: to make a square that is impassable the first colour in the palette (0 index) should be used.

<table>
<tr>
<th> Index
</th><th> Material
</th><th> Description
</th></tr>
<tr>
<td>#0
</td><td> Rock
</td><td> Solid.
</td></tr>
<tr>
<td>#1
</td><td> Background
</td><td> Air.
</td></tr>
<tr>
<td> #2
</td><td> Dirt
</td><td> Destructible.
</td></tr>
<tr>
<td> #3
</td><td> Special dirt
</td><td> Destructible. Worms can go through it but particles can't.
</td></tr>
<tr>
<td> #4
</td><td> Special rock
</td><td> Solid. Worms can't go through it but particles
</td></tr>
</table>

###### Some examples

* [material.png example](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/dn_skill/material.png;h=3dc626983aa5b6e160156d4354fa044372c1964d;hb=master)
* [material.png with dirt](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/utopia/material.png;h=4b92d65f94c0dc76f009b157d2e47476184423a0;hb=master)
* [material.png example with some more materials](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/dn_skill/material.png;h=3dc626983aa5b6e160156d4354fa044372c1964d;hb=master)
* [material.png of gears2](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/gears2/material.png;h=05a36f4bc7ad1483cccf4c79fa292f83ca58b34c;hb=master)

(The colors you see are just random because of some custom palette in it.)

Note: Annoyingly some programs will try to optimise the pallete and destroy the order, thus b0rking your level, so be careful.

### background.png

This image is used to work out what should be displayed when destructable terrain is removed. You only need to draw anything in places where dirt is in the material file.

This image should be in png format at the same size as level.png.

###### Some examples

* [background.png of gears2](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/gears2/background.png;h=898fbecb839d440d5ac5b1960029c9358a13609e;hb=master)

### lightmap.png

This image is used to darken the level and all object sprites in it.

This image should be in png format at the same size as level.png, and be a greyscale image. Where white is normal brightness and black is not visible. It will only be used when in the config.cfg file the line: 'dark_mode = 1' is present.

###### Some examples

* [lightmap.png of base](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/base/lightmap.PNG;h=591c5859dc49da0e16f00bf8316ed6219db7e96d;hb=master)
* [lightmap.png of gew](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/gew/lightmap.png;h=1a9bcf05dc325cede52845698f96a1a3d54ee683;hb=master)
* [lightmap.png of mars](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/mars/lightmap.png;h=a121e7a49e47bce8ad915eb7a9897915b1b61d65;hb=master)

### paralax.png

This image is used as a background to the level that moves in the opposite direction to the worm, it will display under any magenta (255,0,255) pixels in level.png.

This image should be in png format and should be bigger than 320*240. The smaller the paralax, the further away the background will seem.

###### Some examples

* [paralax.png of base](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/base/paralax.png;h=da38d6ef60030094308cc34303472f21df74fd83;hb=master)
* [paralax.png of mars](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/mars/paralax.png;h=10e85707baf2563f041c2512cc5cf859f0ab6c5c;hb=master)
* [paralax.png of utopia](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob_plain;f=share/gamedir/levels/utopia/paralax.png;h=482d27d947b0792d32f4ba370308f3a9787e95f0;hb=master)

# Dynamic elements

Any map can have its own objects. These are all the same as in Gusanos mods. Refer to [Gusanos Modding](/wiki/index.php/Gusanos_Modding/) for more information.

A map can have these mod-like directory structure:

* fonts/
* scripts/
  * map_<mapname>.lua : [Lua](/wiki/index.php/Lua/) init-function
* objects/
* sounds/
* sprites/
* mapeffects/

Via specifing some mod specific file (like ninjarope.obj), the map file will overload the mod behaviour.

# Tutorials

* [Implementing dark mode and lights](/wiki/index.php/Gusanos_Tutorial_Implementing_dark_mode_and_lights/)
{% endraw %}
