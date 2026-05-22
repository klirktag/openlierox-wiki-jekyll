---
title: Script cheatsheet
archived_url: "https://web.archive.org/web/20100506015014/http://www.openlierox.net:80/wiki/index.php/Script_cheatsheet"
last_modified: "17:22, 1 April 2008"
categories: [Guides]
---
{% raw %}
# Scripting Cheatsheet

Commands for scripting.

### Files

```` ```
Main.txt     = The main script text file, must be in a mod.
w_*.txt      = Usually a weapon script text file.
p_*.txt      = Usually a projectile script text file.
``` ````

### Other

Order of variable settings does not matter as long as they are under the correct group.
When leaving out a variable setting it usually defaults to 0 (else noted).
It does not usually matter if you use capitals or not in the scriping.

```` ```
[]           = Different sections of the script code.
#            = Comment, all text after on same line will not be compiled.
¬∞            = Angle, 360 is one full rotation.
bool         = boolean variable, can have value true or false.
classic      = the value in classic mod.
def          = default value, if you dont use this the value get the default value.
float        = floating point variable (decimals).
int          = interger variable (no decimals).
less         = must be less than that value to work.
max          = maximum working value of the variable.
min          = minimum working value of the variable.
more         = must be more than that value to work.
ms           = milli seconds (1000ms = 1s).
px           = pixels (with double resolution, which makes 320 is one screen in width).
RGB          = Red 0-255, Green 0-255, Blue 0-255 (eg 128,255,64).
s            = seconds.
``` ````

* When using sound effect if first look for the file in you <modname>/sfx folder,

if it does not find it there it looks in data/sound.

* When using sound effect if first look for the file in you <modname>/gfx folder,

if it does not find it there it looks in data/gfx.

### Main File

```` ```
[General]    = General mod settings.
ModName      = Name of the mod that will show up in the mod list.
               If you use more than one word you must incapselate it with
               "" when you compile.

[Weapons]    = Weapon list settings.
NumWeapons   = Number of weapons the mod contains (int, min 1).
Weapon#      = File name of a weapon. Replace # with an interger for each weapons.
               Use same amount of lines as the NumWeapons is.
               Weapon1 shows up first in the list when you choose weapons,
               Weapon2 comes in second place and so on.
               If a weapon a filename is wrong or miss a Weapon# the weapon will be
               blank, but the game will still run with defualt values on the weapon.

[NinjaRope]  = The Ninja Rope setting.
RopeLength   = The max lenght on the rope when you throw in px (int, classic 300).
               Note, you can max throw the rope about 900 in right up in the air.
RestLength   = The min lenght the rope will have when you hang by it in px
                        (int, classic 27).
Strength     = How hard it will drag you until you have reached min length
                      (float, classic 4.5).

[Worm]       = Settings on all worms.
AngleSpeed   = How fast it can change direction of the aim (classic 150, less is slower).
GroundSpeed  = How fast it moves on land (classic 8, less is slower).
AirSpeed     = How fast it moves in air (classic 4, less is slower).
               Note: A bug makes air speed is also used on ground.
               Negative walues will give some strange results on both speeds.
Gravity      = How much the gravity affect it, (classic 100, 0 is no gravity,
               and negative number will make it moves upwards instead).
JumpForce    = How fast it will jump (classic -65, possetive will make it bounce first).
AirFriction  = How much the air slows it down (float, min 0, max 1, classic 0).
GroundFriction = How much ground slows it down (float, min 0, max 1, classic 0.4).
``` ````

### Weapon File

```` ```
[General]    = Must be in a weapon/projectile scrip file. Main settings.
Name         = Name that will show up in weapon list.
Type         = Use "Type = WPN_BEAM" of you want to use beam weapon.
*Class       = Can be:
                    WCL_AUTOMATIC
                    WCL_CLOSERANGE
                    WCL_GRENADE
                    WCL_MISSILE,
                    WCL_POWERGUN.
                    Just used for future reference.
Recoil       = How much you will fly backwards when you shoot.
               Negative will make you fly forward instead.
Recharge    = Time it takes to reload weapon the more the faster
               (float, min 0, def 0, 10s/number).
               Example: 1 = 10s, 0.5 = 20s, 2 = 5s, 10 = 1s.
Drain       = How much each shot will drain in percent.
               When more than 100 have been used you must reload to shoot again.
               Note the "more", if it have drained 100 you can still shoot one more time,
               it needs to be just over it for just one shot, eg 100.001.
ROF          = Rate of Fire, delay between shots in same clip, in ms (int, min 1, def 1).
Sound        = A sound file that will be played when the weapon is fired.
LaserSight   = Shows a dottet line directly at where the player aims.

[Beam]       = Creates a beam with some setings.
               Ignores Recoil, Sound and LaserSight in General.
Damage       = Size of the damage on dirt (int).
PlayerDamage = Damage player will take when hit (int).
Colour       = Color of the whole beam (RGB).
Length       = Length of the beam in px (int, use 999999 to have no end of the beam).
``` ````

### Weapon and Projectile Files

```` ```
[Projectile] = Creates a projectile with some settings.

Amount       = How many projectiles that will be created each time
               (int, min 1, max 2047, def 0).
Speed        = How fast the projectiles moves (def 0).
               More than 1000 can usually pierce through materials.
               Moves backwards with a negative number.
SpeedVar     = Randomly extra or less in speed (def 0).
               Example 10 can give 0-10 extra speed or 0-10 less speed.
*Spread       = How much randlomly each projectile can spread at both direction from
                       the middle in ¬∞
                      (float, min 0, max 180). In v0.55b 0 spread works correctly.
Projectile   = The name of the projectile file that will be loaded.
Angle        = In wich direction the projectile start to move in ¬∞,
               0 is to the right, 90 is down, -90 is up, 180 is left.
               Variable ignored in the weapons first projectiles and in trail.
Useangle     = Bool (def false), when true use last projectiles angle (+ Angle variable)
               instead of using absolute angle.
               Variable ignored in the weapons first projectiles and in trail.
``` ````

### Projectile File

```` ```
[General]    = Main settings on the projectile.
Type         = Can have values: PRJ_IMAGE or PRJ_PIXEL.
               PRJ_IMAGE followed by Image in new line to use an image,
               PRJ_PIXEL followed by Colour1 and optional Colour2 if you
               want pixel graphics.
Image        = Name of the image file that will be used on the projectile.
Colour1      = The RGB value of the pixels (def black).
Colour2      = Use this if you want some variation on the pixel colors (def not used).
Trail       = Everything but TRL_PROJECTILE and TRL_NONE use hard coded images.
               Can have values:
               TRL_CHEMSMOKE = Green smoke effects.
               TRL_DOOMSDAY = tiny fire trail.
               TRL_EXPLOSIVE = big explosion trail.
               TRL_NONE = have no trail.
               TRL_PROJECTILE = have a trail that is defined in [ProjectileTrail].
               TRL_SMOKE = use the smoke.png trail (hardcoded).
Gravity      = How much gravity effects the projectile (0 = nothing, 100 = full, 200 =
               double effect, negative value will make it moves upwards instead of
               downwards).
Dampening    = Multiplies with projectile speed each frame (float, 1.0 = no effect,
               less than 1.0 slows it down, more than 1.0 accelerate the projectile,
               def 1.0).
Timer        = In how many seconds the [Time] trigger will be used, in s (float).
*TimerVar    = Radom time length variance.
Rotating     = Bool (def false). If the projectile will rotate when it moves.
               If true also use RotIncrement and RotSpeed.
*RotIncrement = How many rotated images there is in the file in ¬∞.
               For 4 direction 90, for 8 45, for 16 23.
RotSpeed     = How fast the rotation will be, the higher value the faster (int).
               Also rotates slower the slower the projectile moves.
UseAngle     = Bool (def false), when true the graphics will be dependent on
                     the projectiles angle, If true also use AngleImages.
UseSpecAngle = Don't know the difference between this and UseAngle except it
                          show some directions wrong.
AngleImages  = Tells how many direction images there is in the file.
               These amount of directions seams to work best: 10, 18, 34, 66.
Animating    = Bool, when true use also AnimRate and AnimType
AnimRate     = How long each frame in the animation will be shown, the less the slower.
AnimType     = Can have values ANI_ONCE, ANI_LOOP, ANI_PINGPONG.
               ANI_ONCE = Animate from left to right then the projectile
                                   dissaperes.
               ANI_LOOP = Animate from left to right again and again until
                                   projectile dissaperes.
               ANI_PINGPONG = Animate from left to right and back again
                                           then dissaperes.

[Hit]        = Setting on what will happen when a projectile hits a wall
                  (both dirt and rock).
Type        = Can have values: Bounce, Carve, Dirt, Explosion, GreenDirt, Nothing
                  (def Nothing).
               Bounce = will make the projectile bounce on the material
                               (use BounceCoeff too).
               Carve = damage walls without showing some animation.
               Dirt = will make 3 dirt circles around it.
               Explode = use the "Explosion.png" in different sizes depending on damage.
               GreenDirt = makes a tiny green dirt.
               Nothing = will make the projectile moves through dirt and rock
                               (max speed around 50).
Damage      = How much that will be removed on dirt (int, def 0).
               In LieroX v0.50b it also damage the player in same damage
               (instead of just 1 as it was before).
               Maximum damage is 15 (image bug if higher)
               Use Damage = -1 if you don't want to show a small explosion image.
BounceCoeff  = How much the projectile will loose in speed when it bounce (float,
               1.0 = no speed loss, 0.0 all speed loss, over 1.0 it gets faster
               after each bounce).
BounceExplode = If the projectile explodes every time it bounce
                 (int, the higher, the bigger removal).
                 If it is slow or have low angle it can carve through much dirt
                 (a bug that it gets faster when it bounces).
Projectiles  = Bool (def false). If true and "Type = Explosion"
                  the [Projectile] will trigger.
Shake        = How much the whole level will shake (def 0).
Sound        = Sound file that will be used.

[PlayerHit]  = What will happen when a projectile hits a player
               (both computer and human).
               Only the Type variale works differently compared to [Hit].
Type         = Can have values: Explosion, Injure, Nothing (def Nothing).
               Explode with show exploding animation but max do 5 damage.
               Injure will hurt the player directly with no max damage.
               Nothing will just pass though the player
               (but the same time also ignore wall hits).
               Both Explode and Injure can trigger a [Projectile].

[Time]       = What will happen when a projectile have a certain age.
               Using same variables like [Hit] and [PlayerHit] with an exception of
               Sound that unfortunatly does not work.

[ProjectileTrail] = When "Trail = TRL_PROJECTILE" is stated in [General].
UseProjVelocity = Bool, true if the trail will use the speed of the projectile it
                shoots from.
Delay        = Delay between each projectile in the trail, in ms
``` ````
{% endraw %}
