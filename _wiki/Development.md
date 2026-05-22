---
title: Development
archived_url: "https://web.archive.org/web/20120425105227/http://www.openlierox.net:80/wiki/index.php/Development"
last_modified: "23:54, 13 May 2011"
---
{% raw %}
This is a rough overview of the development of [OpenLieroX](/wiki/index.php/OpenLieroX/).

In case you want to **contribute** to the development of OpenLieroX, read here: [Contribute](/wiki/index.php/Contribute/)

# Versions

First, [read this](/wiki/index.php/OpenLieroX/#versions). We keep all main version (like 0.57, 0.58, 0.59) seperated and also work seperatly on them. [Git](/wiki/index.php/Git/) helps us a lot to do this. If there are some things we implement in one version (like 0.58), Git allows us to also take these changes and apply them to a later version (like 0.59).

Right now, we work in a way, that all really big new things go into a completly new version (which was not released yet, like 0.60) and all other things go into the existing branches. More about this [here](/forum/index.php/topic,12643.0.html).

# Communication

There are several ways we communicate with each other.

## Development Discussions

For longer discussions which are important for the whole development team, we use the [OpenLieroX development mailinglist](/wiki/index.php/Mailinglists/).

## Chats

For some group chat discussions, we use the #LieroX [IRC](/wiki/index.php/IRC/) channel (but only rarely).

Or we just chat directly with each other via Jabber/ICQ.

There is also a [Twitter feed](http://twitter.com/openlierox) where everybody can make random small announcements.

## Community

And of course, we also use the [forum](/forum/index.php). The forum is also the main place for interaction between the whole LX community and the development team. We post requests about some needed graphics / sounds there, we make the announces there (the news on openlierox.net are linked to that forum) and we discuss with the community about the different OpenLieroX versions.

## Bug reports

Bug reports are posted and managed at the [GitHub issue tracker for OpenLieroX](https://github.com/albertz/openlierox/issues). Any bug report should be posted there. We also try to get all users to post their bugs directly in the tracker, instead of just writing it somewhere in the forum.

Each bug has some priority from 1 to 9, where 9 is the most serious one. All kind of crashes will always get the priority 9. We really try hard to fix all bugs with priority >=8 for a next release.

Automatic crash reports are posted to our [crash mailinglist](/wiki/index.php/Mailinglists/). They are not posted automatically on the bug tracker yet. Somebody must review them (mostly that is Albert but everybody is supposed to look at them and could do that) and post them manually on the tracker.

## Feature requests

We use the [GitHub issue tracker](https://github.com/albertz/openlierox/issues) also for feature requests.

People also post often some requests at the forum but this is kind of random and mostly will get forgotten. Or it is a big feature which is anyway known to everyone. In that case, the forum is mostly used to discuss about it. In many cases, features which change the gameplay a lot, even if they are optional, are not accepted by the community.

# Coding

[Git](/wiki/index.php/Git/) is the base we use to work together on the same code.

We don't really have any strict guideline of writing code. Most important is that it is clean and robust. We hate any type of hacks in the code or errorprone code. When introducing new general code, we try to design them in a way that it is impossible to use them in a wrong way.

Everybody can support us in working with the code. Just leave [us](/wiki/index.php/OpenLieroX/#current_developers) a message and you get write access to the code. You can also just send us some patches if you prefer that. Because of Git, it is trivial to undo some mistake, so don't be too afraighten to upload something wrong. Most other developers will review the changes and give comments about them if something is wrong about it. While not really having strict rules, there are some [very basic rules](/wiki/index.php/Git/#working_on_the_code) you should follow!

[Read further here to get some overview of our code](/wiki/index.php/OpenLieroX_source_code/).

# Resources

There are several kinds of resources in OLX, like the menu graphics and general sounds - and all the ingame sounds ("3 frags left", "1 minute to play", worm death, explosions, etc.). Then there are maps and mods which can provide own sounds and own graphics.

Most of the base resources were already there from the [LieroX](/wiki/index.php/LieroX/) project. Some (like the menu theme) were remade for the OLX project. The old LieroX theme and the current default theme, and all other base resources belong to the OLX project.

The dirt map and the Liero classic mods are the only map/mods which belong to OLX itself. All other maps/mods were made completly independent from the OLX project - they are just also packed into the OLX release packages.

In case of [Gusanos](/wiki/index.php/Gusanos/): The main Gusanos mod afaik is from the Gusanos developers, all other Gusanos mods and all Gusanos maps are from independent people.

The mods/maps in the openlierox [Git](/wiki/index.php/Git/) repository are exactly those which are in the release packages. Before you are going to include a new mod/map into the openlierox repository, please reconsider it carefully and if you are unsure, ask. We don't want it to blow up too much. It is already pretty big.

There are also extra external packages for maps / mods / skins, maintained by the OLX team.
{% endraw %}
