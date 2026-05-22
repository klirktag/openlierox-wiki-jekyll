---
title: "Gusanos:console variables"
archived_url: "https://web.archive.org/web/20100617034357/http://www.openlierox.net:80/wiki/index.php/Gusanos:console_variables"
last_modified: "11:22, 31 January 2010"
---
{% raw %}
[Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:console_docs:console_variables).]

**Note that many variables of Gusanos were removed in OpenLieroX. The following overview only describes the still existing variables.**

# Console variables

##### CL_Log_Death_Messages

* * Variable type:** bool.

* * Description:** If set to 1, death messages are logged to the console.

* * Default value:** 0.

##### CL_ShowDebug

* * Variable type:** int.

* * Description:** If set to 1 useful information will be shown on the screen.

* * Default value:** 0.

##### CL_Show_Death_Messages

* * Variable type:** bool.

* * Description:** If set to 1, death messages are shown in the left-bottom corner of the screen.

* * Default value:** 1.

##### CL_Show_Map_Debug

* * Variable type:** int.

* * Description:** If set to 1, circles are drawn at worm spawn points when those are used by a map.

* * Default value:** 0.

##### NET_AutoDownloads

* * Variable type:** int.

* * Description:** If set to 1, if the next game requires a map not available in the computer, it will try to download it from the server.

* * Default value:** 1.

##### NET_Check_CRC

* * Variable type:** int.

* * Description:** If set to 1 (in the server), all clients in the next game will have their mods and maps checked against the server's for compatibility (CRC).

* * Default value:** 1.

##### P#_Aim_Accel

* * Variable type:** float.

* * Description:** The acceleration in which the aim speed will be affected with the aim up or down command.

* * Default value:** 0.129991.

##### P#_Aim_Friction

* * Variable type:** float.

* * Description:** How fast the aim speed will be lost when not moving it.

* * Default value:** 0.921665.

##### P#_Aim_Speed

* * Variable type:** float.

* * Description:** The maximum value the aim speed can reach.

* * Default value:** 1.69998.

##### P#_Rope_Adjust_Speed

* * Variable type:** float.

* * Description:** How fast the rope desired length will be change.

* * Default value:** 0.5.

##### P#_Viewport_Follow

* * Variable type:** float.

* * Description:** How fast the player viewport will follow the owned worm. Values should be between 0 and 1.

* * Default value:** 0.1.

##### RCON_Password

* * Variable type:** words.

* * Description:** Password to be used by a client user to have server privileges, like changing maps and mods, if the server specifies one. Using "" as a password in the server removes this ability. Useful for dedicated servers. To send commands to the server, use the RCON console command.

* * Default value:** "".

##### SFX_Listener_Distance

* * Variable type:** float.

* * Description:** The 3d distance the player listener will have from the plane in which objects are placed. *Note: Its a quite technical variable, you most likely wont need to use it.*

* * Default value:** 20.

##### SV_Max_Respawn_Time

* * Variable type:** int.

* * Description:** Maximum time in frames for a worm to respawn after it gets killed in seconds. If it is -1, then no maximum time will be assigned.

* * Default value:** -1.

##### SV_Max_Weapons

* * Variable type:** int.

* * Description:** Sets the number of weapons supported internally for the next game. Menus do not still get updated.

* * Default value:** 5.

##### SV_Min_Respawn_Time

* * Variable type:** int.

* * Description:** Minimum time in frames for a worm to respawn after it gets killed.

* * Default value:** 100.

##### SV_NinjaRope_Pull_Force

* * Variable type:** float.

* * Description:** Force with which the rope will pull worms when attached to ground. This is a server side variable.

* * Default value:** 0.031.

##### SV_NinjaRope_Shoot_Speed

* * Variable type:** float.

* * Description:** Speed in which the rope will be thrown. This is a server side variable.

* * Default value:** 2.

##### SV_NinjaRope_Start_Distance

* * Variable type:** float.

* * Description:** The default distance at which the rope will stop pulling the worm. This is a server side variable.

* * Default value:** 249.

##### SV_Team_Play

* * Variable type:** int.

* * Description:** If set to 1, it enables team play spawn points.

* * Default value:** 0.

##### SV_Worm_Acceleration

* * Variable type:** float.

* * Description:** Acceleration a worm will have when moving left or right. This is a server side variable.

* * Default value:** 0.03.

##### SV_Worm_Air_Acceleration_Factor

* * Variable type:** float.

* * Description:** Will multiply the worm acceleration when the worm is not touching the ground. This is a server side variable.

* * Default value:** 1.

##### SV_Worm_Air_Friction

* * Variable type:** float.

* * Description:** Friction that is always applied to the worm. This is a server side variable.

* * Default value:** 1.

##### SV_Worm_Bounce_Limit

* * Variable type:** float.

* * Description:** Minimum speed in which the worm will bounce ( Speeds smaller than this value will make the worm just stop without bouncing ). This is a server side variable.

* * Default value:** 2.

##### SV_Worm_Bounce_Quotient

* * Variable type:** float.

* * Description:** How much of the worm speed will be conserved when bouncing. This is a server side variable.

* * Default value:** 0.333.

##### SV_Worm_Box_Bottom

* * Variable type:** float.

* * Description:** The bottom coordinate of the worm hitbox relative from the worm center position. This is a server side variable.

* * Default value:** 4.

##### SV_Worm_Box_Radius

* * Variable type:** float.

* * Description:** Is how wide the worm hitbox is. This is a server side variable.

* * Default value:** 2.

##### SV_Worm_Box_Top

* * Variable type:** float.

* * Description:** The top coordinate of the worm hitbox relative from the worm center position. This is a server side variable.

* * Default value:** 3.

##### SV_Worm_Disable_Wall_Hugging

* * Variable type:** float.

* * Description:** If set to 1 worms will not stop falling if they walk against a wall. This is a server side variable.

* * Default value:** 0.

##### SV_Worm_Friction

* * Variable type:** float.

* * Description:** Friction applied to the worm when its touching ground. This is a server side variable.

* * Default value:** 0.921665.

##### SV_Worm_Gravity

* * Variable type:** float.

* * Description:** Vertical acceleration the worms will suffer in the game. This is a server side variable.

* * Default value:** 0.009.

##### SV_Worm_Height

* * Variable type:** float.

* * Description:** Height of the worm with ground collision detection ( From bottom to top ). This is a server side variable.

* * Default value:** 9.

##### SV_Worm_Jump_Force

* * Variable type:** float.

* * Description:** Speed which will be added to the worm speed when the worm jumps. This is a server side variable.

* * Default value:** 0.6.

##### SV_Worm_Max_Speed

* * Variable type:** float.

* * Description:** Maximum speed a worm can reach by walking left or right. This is a server side variable.

* * Default value:** 0.45.

##### SV_Worm_Max_Climb

* * Variable type:** int.

* * Description:** Maximum amount of pixels a worm is able to climb. This is a server side variable.

* * Default value:** 4.

##### SV_Worm_Weapon_Height

* * Variable type:** float.

* * Description:** Height of the worm weapon axis ( From the bottom ). This is a server side variable.

* * Default value:** 5.

##### SV_Worm_Width

* * Variable type:** float.

* * Description:** Width of the worm with ground collision detection ( From left to right ). This is a server side variable.

* * Default value:** 3.

##### VID_Clear_Buffer

* * Variable type:** int.

* * Description:** If set to 1, the variable used to draw images will be cleared every rendering cycle.

* * Default value:** 0.
{% endraw %}
