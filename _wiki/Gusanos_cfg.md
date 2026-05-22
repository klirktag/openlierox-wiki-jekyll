---
title: "Gusanos:cfg"
archived_url: "https://web.archive.org/web/20110721124644/http://www.openlierox.net/wiki/index.php/Gusanos:cfg"
last_modified: "12:34, 31 January 2010"
---
{% raw %}
# Configuration files

Configuration files are the .cfg files located in the folder of the [Gusanos](/wiki/index.php/Gusanos/) mod used. Those can be used to store a sequence of instructions to be later read by Gusanos the same way as typed in the console. The following default files are used in the initialization:

1. -- config.cfg -- runs before Gusanos is first initialized.

   :   -- config-ded.cfg -- run before the dedicated server is first initialized.
2. -- mod.cfg -- runs after a map is changed (even when Gusanos is starting).
3. -- autoexec.cfg -- runs after Gusanos is first initialized.

   :   -- autoexec-ded.cfg -- runs after the dedicated server is first initialized.

The [Exec](/wiki/index.php/Gusanos_console_commands/#exec) instruction can be used to run a configuration file.

# Syntax

[Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:console_docs:omfgconsole).]

##### Using the console

The //console// is a command-line interface in which you can send instructions to interact with the game. Gusanos has its own console system which cannot be access by the user and is only used internally by Gusanos mods/maps.

##### Command-line syntax

An //instruction// or //command// is an aliase used to call a function previously defined in the console. Commands can contain this set of characters in their names:

```
 [A-Za-z0-9_]
```

The full list of instructions can be found in the [console commands](/wiki/index.php/Gusanos_console_commands/) page.

A //parameter// is one of the values that is supported by an instruction. An instruction can contain more than one parameter value separated by the space or return characters. Example:

```
 say hello -- "say" is the command, "hello" is a parameter value.
```

The //data type// of a parameter is the type of information that can be used in a parameter of an instruction. As this is a command-line interface, string is always the data type, but it is more useful to describe the data types of the original function or the data types that best describe the range of answers supported. Some types used by the documentation:

^ Data type ^ Description ^
^ bool | Supports only numbers 0 (for False) and 1 (for True). |
^ int | Supports only integer numbers (whole numbers). |
^ float | Supports only floating point numbers up to 6 decimal digits. |
^ string/words | Supports a string of characters. |
^ enum | Supports a limited choice of options from a list. |

Depending on the answers supported by a parameter, its //parameter value// can contain this set of characters:

```
 [A-Za-z0-9_"\]
```

The double quotes and the back-slash characters are special in this case. Whenever a parameter value is started with a double quotes character, the parameter value will only end until another double quotes character is used:

```
 Say "I sheep now"
```

The back-slash character is used to escape characters, like itself and the double quotes character.

```
 Say "And he said \"WTF?\""
```

An //instruction block//, a //command block//, or simply a //code block// is a block combining the instruction and all parameters it supports. Instruction blocks have to be either separated by new line or ";" characters. Example:

```
 Game default;Map poo
```

Special types of instructions exist:

```
 * A //variable// stores information of one parameter. Examples are game physics variables, like the following:
```

```
   P0_Name "GusPlayer"
```

```
 * An //action// is a command that can be activated and later deactivated. Those start with "+" or "-" characters along with their names. The "+" character activates the action, and "-" character deactivates it. Examples are player actions, like the following:
```

```
   +P0_Fire -- holds the fire button
   -P0_Fire -- releases the fire button
```

For both special types, the full list of actions can be found in the [console commands](/wiki/index.php/Gusanos_console_commands/) page, and the list of variables in the [console variables](/wiki/index.php/Gusanos_console_variables/) page.

The console does not need to have only instructions, it can also have comments. //Comments// clarify the instruction it is describing. A comment starts with two "-" (dash) characters. Comments can only come right before the instruction block separator character. Example:

```
 Say "My bad :(" --sends text to other users
 VID_Fullscreen 1 --makes the game to be in fullscreen mode; VID_DoubleRes 1 --activates the double resolution mode
```

The return value of an instruction block can be used as text for other purposes. To do that, enclose the instruction block with "{" and "}" (bracket) characters, like in the example below:

```
 -- Code to use the server name as the name of the player (useful in dedicated servers):
 P0_Name {NET_Server_Name}
```

This is an one-time assignment, so if the return value of the [NET_Server_Name](/wiki/index.php/Gusanos_console_variables/#net_server_name) variable is changed after being assigned, the [P0_Name](/wiki/index.php/Gusanos_console_variables/#p0_name) variable value will not be changed.

##### Console messages

//Console messages// are messages that shown in the console mostly for debugging purposes. Basic console messages are syntax errors but can be composed of these types of messages:

//Syntax errors// appear when a syntax that is not proper is used and is not recognized by the console. An extra message is used to identify where the error can be found in the line. Example:

```
 ]"Test
 "Test
 ^
 Expected EOF
```

//User messages// are messages given by the use of the [Echo](/wiki/index.php/Gusanos_console_commands/#echo) instruction in the command-line, any other console instructions or by LUA instructions. Those always appear between "<" and ">" characters. Example:

```
 ]Game
 <GAME <MODGAME> : SET THE MOD TO LOAD THE NEXT MAP CHANGE>
```

//Player messages// are messages sent by users by using the [Say](/wiki/index.php/Gusanos_console_commands/#echo) instruction, or by LUA instructions. Those always show the player name between "<" and ">" characters and the player message right beside it.

```
 ]Say "WTF?"
 <GusPlayer> WTF?
```

//Worm death messages// are messages that appear on the bottom-left corner of the screen, principally to indicate which worms died recently. Those messages may also appear in the console if the console variable [CL_Log_Death_Messages](/wiki/index.php/Gusanos_console_variables/#cl_log_death_messages) has the value of "1". Those messages always have the same kind of syntax as the following:

```
 <playername> commited suicide
 <playername> got killed by <playername2>
 <playername> got killed by �05anonymous
```

The last one only happens after a map effect kills the worm (it also has color, as described in the section below). Example:

```
 bot got killed by GusPlayer
 bot(2) got killed by �05anonymous
 GusPlayer commited suicide
```

##### Typing aids

The Gusanos console has many typing aids that can be used by the user. The following are examples of those:

#### Instruction names completion feature

The console supports the feature of completing the instruction name being typed or suggesting one from what is being typed. To use it, type the first letters of an instruction, and then press the "Tab" key. If there is only one suggestion, Gusanos will automatically type the rest of the instruction's name. If there is more than one, it will show a list of them.

#### Key combinations for text typing

The console supports key combinations that specially for text typing. The following is a list of all key combinations that can be used to produce a new character in the console:

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

Those characters still obey the orignal role as system characters have. For example, the character num. 8 is used as backspace, so when you press its respective key combination, the last letter before the caret is removed, like the original backspace button does.

#### Text colors

//Text colors// specify the color of the text to be shown in the console. This does not work for instructions, but it works in parameter values and comments. To use it, use the character "�" or use Ctrl+K (as seen in the list of console key combinations) and type the wished color index number:

^ Index ^ Name ^ Red ^ Green ^ Blue ^ in #RRGGBB format ^
^ 00 | White | 255 | 255 | 255 | #FFFFFF |
^ 01 | Black | 0 | 0 | 0 | #000000 |
^ 02 | Red | 255 | 0 | 0 | #FF0000 |
^ 03 | Green | 0 | 255 | 0 | #00FF00 |
^ 04 | Blue | 0 | 0 | 255 | #0000FF |
^ 05 | Yellow | 255 | 255 | 0 | #FFFF00 |
^ 06 | Cyan | 0 | 255 | 255 | #00FFFF |
^ 07 | Magenta | 255 | 0 | 255 | #FF00FF |
^ 08 | Dark gray | 64 | 64 | 64 | #404040 |
^ 09 | Light gray | 192 | 192 | 192 | #C0C0C0 |
^ 10 | Brown | 128 | 0 | 0 | #800000 |
^ 11 | Dark green | 0 | 128 | 0 | #008000 |
^ 12 | Dark blue | 0 | 0 | 128 | #000080 |
^ 13 | Dark yellow | 128 | 128 | 0 | #808000 |
^ 14 | Dark cyan | 0 | 128 | 128 | #008080 |
^ 15 | Dark magenta | 128 | 0 | 128 | #800080 |
{% endraw %}
