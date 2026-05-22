---
title: Weapon examples
archived_url: "https://web.archive.org/web/20200223053150/http://www.openlierox.net:80/wiki/index.php/Weapon_examples"
last_modified: "02:29, 30 April 2008"
---
{% raw %}
Please add on any examples you wanna add. Simple, hard, just make sure to make it readable and all the code should be between <pre><code>text</code></pre> tags. ;)

## Weapon Examples

**Asrack's Basic Weapon Example**
In this tutorial I will show you a a basic weapon example. This weapon will shoot a projectile file and explode when it hits the player. There will be two files to this weapon. The weapon file which we will name w_gun.txt and the projectile file which will be p_bullet.txt. For the sake of examples.

* Weapon File - "w_gun.txt"

```` ```
[General]
Name = Gun
Class = WCL_MISSILE
Recoil = 0
Recharge = 2
Drain = 25
ROF = 250

[Projectile]
Amount = 1
Speed = 300
Spread = 5
Projectile = p_bullet.txt
``` ````

* Projectile File "p_bullet.txt"

```` ```
[General]
Type = PRJ_PIXEL
Colour1 = 0, 0, 0
Trail = TRL_NONE

[Hit]
Type = Explode
Damage = 1

[PlayerHit]
Type = Explode
Damage = 3
``` ````

Compile your mod after adding this to the main.txt and test it out. Very easy weapon. =)
{% endraw %}
