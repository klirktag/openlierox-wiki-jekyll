---
title: "Gusanos:console commands"
archived_url: "https://web.archive.org/web/20100617040332/http://www.openlierox.net:80/wiki/index.php/Gusanos:console_commands"
last_modified: "11:05, 31 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:console_docs:console_commands).

**Note that there were some more commands in Gusanos but most of these were removed from OpenLieroX because Gusanos mods shouldn't use them themself anyway and OLX already provides such console command itself. The following overview shows the commands which are available in OpenLieroX.**

### Console commands:

##### Player actions

```
 * +<action> = activates when its assigned key is held.
 * -<action> = activates when its assigned key is released.
```

#### P#_Left

#### P#_Right

#### P#_Jump

#### P#_Up

#### P#_Down

#### P#_Change

#### P#_Fire

### Game commands

#### Alias

```
 Alias <newname> <variable/text>
```

Uses another name either for another variable, allowing to set the value of it, or to input text in the console. Example:

```
 Alias SvrName NET_Server_Name
 SvrName Test
```

<newname> cannot be the name of any of the built-in console instructions.

#### Bind

```
 Bind <key_name> <action>
```

Binds the given key to input the given text in the console. Example:

```
 Bind 1 "map poo"
```

#### Echo

```
 Echo <message>
```

Displays a message which is seen in the console.

#### Exec

```
 Exec <file.cfg>
```

Executes a given configuration file in the mod folder.

#### Rest

```
 Rest <milliseconds>
```

Rests Gusanos by the amount of milliseconds specified.

#### RND_Seed

```
 RND_Seed <seed_number>
```

Assigns all random generators results to the ones with the seed_number specified. Used for debugging purposes.

#### RCON

```
 RCON <command>
```

Sends an specific console command or variable value to be set in the server, when the RCON_Password console variable is set and the value is the same as set for the server. Example:

```
 RCON map pokol
```

#### Say

```
 Say <message>
```

Sends a message from the local player # 0 to all players in a game. Remember to use quotes if there are spaces in the message field.

##### Deprecated game commands (supported on 0.9b)

#### ExecScript

#### SetAltChar

#### SetChar

#### SetShiftChar

#### SwapKeys
{% endraw %}
