---
title: Modding
archived_url: "https://web.archive.org/web/20110721114622/http://www.openlierox.net/wiki/index.php/Modding"
last_modified: "18:59, 9 May 2010"
---
{% raw %}
A gamescript, also called [Mod](/wiki/index.php/Mod/), defines the weapons you can use and their effects. That includes all the particles/projectiles the weapons are spawning, etc. A gamescript also defines some general physics parameters like the gravity and maybe other stuff.

[OpenLieroX](/wiki/index.php/OpenLieroX/) supports two different gamescript formats.

## Gusanos mod format

The [Gusanos mod format](/wiki/index.php/Gusanos_Modding/) is the most powerful. Spawned particles support a wide range of attributes and events and you can set many different action(s) you want. [Lua](/wiki/index.php/Lua/) scripting is also possible to be fully dynamic. Weapons can react on both the firestart and firestop event and can setup a custom crossair. Any particle/weapon/object can setup dynamic lighting.

Gusanos mods are supported since OpenLieroX 0.59. This is the new main format. It is highly recommended that you start any new mod as a Gusanos mod.

## LieroX gamescript format

The [LieroX gamescript format](/wiki/index.php/LieroX_Scripting/) is the oldest one in OpenLieroX. You are somewhat limited in the possible events and actions and it is often complicated to get what you want.

This format is kind of deprecated. You shoudln't write new mods in it. Use the Gusanos modding format instead.
{% endraw %}
