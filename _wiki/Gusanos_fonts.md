---
title: "Gusanos:fonts"
archived_url: "https://web.archive.org/web/20100527015941/http://www.openlierox.net:80/wiki/index.php/Gusanos:fonts"
last_modified: "13:28, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:fonts).

###### Description

//Fonts// are special types of graphic files that can be loaded into Gusanos to set the text font of the console (using [CON_Font](/wiki/index.php/Gusanos_console_variables/#con_font) console variable) or as a font resource in LUA. The font formats supported by Gusanos are .bmp and .png (image format), .lfn (LOSP font), and .lft (liero font) files. Those are described below:

###### .bmp/.png image fonts

The .bmp/.png image fonts are used by Gusanos as an easy way to create new fonts by developers, and is recommended over the other file types supported by Gusanos.

Font properties:

```
 * height: specifies the maximum character height.
 * width: specifies the maximum character width for all 256 characters that the font has to contain.
```

Notes:

```
 * Even though the image can contain colors, any color besides transparent will be considered black.
 * Gusanos uses the ASCII charset, where there are 33 special characters that are reserved but could be used in the game. Those are assigned to specific key combinations, as shown below:
```

^ Num ^ Key combinations ^ Name ^
| 0 | Any | Blank character (used when an invalid character is typed) |
| 1 | Ctrl+A | Black smiling face |
| 2 | Ctrl+B | Heart |
| 3 | Ctrl+C | Black diamond suit |
| 4 | Ctrl+D | Windmil |
| 5 | Ctrl+E | Black spade suit |
| 6 | Ctrl+F | Small plus sign |
| 7 | Ctrl+G | Small plus sign in a card |
| 8 | Ctrl+H | Small aim sign |
| 9 | Ctrl+I | Small aim sign in a card |
| 10 | Ctrl+J | Male sign |
| 11 | Ctrl+K | Female sign |
| 12 | Ctrl+L | Eighth note |
| 13 | Ctrl+M | Beamed eighth notes |
| 14 | Ctrl+N | White sun with rays |
| 15 | Ctrl+O | Right arrow head |
| 16 | Ctrl+P | Left arrow head |
| 17 | Ctrl+Q | Double dagger |
| 18 | Ctrl+R | Double exclamation mark |
| 19 | Ctrl+S | Pilcrow sign |
| 20 | Ctrl+T | Section sign |
| 21 | Ctrl+U | Macron |
| 22 | Ctrl+V | Triple dagger |
| 23 | Ctrl+W | Up arrow |
| 24 | Ctrl+X | Down arrow |
| 25 | Ctrl+Y | Right arrow |
| 26 | Ctrl+Z | Left arrow |
| 27 | Ctrl+[ | Left right arrow |
| 28 | Ctrl+Vert. Bar | Not sign |
| 29 | Ctrl+] | Up down arrow |
| 30 | Ctrl+Circumflex | Up arrow head |
| 31 | Ctrl+- | Down arrow head |
| 127 | Ctrl+Backspace | Backspace feed |

Other characters between 31 and 127, and 128 and 255 are in the "ASCII" or "DOS: United States" charset. Any character after the 127 is not used by Gusanos (to be verified).

###### .lfn fonts

This type of font was first introduced in LOSP and later passed to Gusanos.

Advantages:

```
 * Ability to use different size characters
 * Support grayscale colors.
 * Uses the "Windows: Western" charset (to be verified).
```

Disadvantages:

```
 * Difficult editing (no editor to edit this file type).
 * Doesn't support the special characters.
```

As there is no editor available, the file syntax is shown below:

^ Byte Range (Hex) ^ Var Type ^ Name ^
^ HEAD ^^^
| 00-03 | uint | Width of character rect |
| 04-08 | uint | Height of character rect |
^ CHARACTER PLACEMENT (for each item) ^^^
| 00-03 | int | character "x" position in image |
| 04-08 | int | character "y" position in image |
| 08-0B | int | character width |
| 0C-0F | int | character height |
^ GRAYSCALE IMAGE (first fill the line, then fill the next, and so on) ^^^
| 00-(width*height) | uchar | Grayscale color (00 - black to FF - white) |

There can only be 224 characters with this font type, and only the first 96 characters are used by Gusanos (to be verified).

###### .lft fonts

These fonts are used by Liero and are easily edited using the [[[1]](http://comser.liero.org.pl/wiki/index.php?title=LieroKit|LieroKit)] ([[[2]](http://www.kgivler.com/files/liero/Lk16b2.zip|download)]). You need first to have a bitmap file of the font in the proper format to later convert to a font file.

Use this type of font when you need compatibility between Liero and Gusanos.

It's very similar to the .bmp/.png file, except that:

```
 * the characters are in order from top to bottom, only then from left to right.
 * it uses 240 characters instead of 256.
 * it doesn't have the "blank" and "Up down arrow" special characters.
 * it trims the last 10 characters in the "ASCII" or "DOS: United States" charset.
```

Notes:

```
 * Even though the image can contain colors, any color besides transparent will be considered black.
 * .lft fonts use a pixel to identify the color of the character when it is selected, but it is ignored by Gusanos.
 * Any character after the 127 is not used by Gusanos (to be verified).
```
{% endraw %}
