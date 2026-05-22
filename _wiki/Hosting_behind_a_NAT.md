---
title: Hosting behind a NAT
archived_url: "https://web.archive.org/web/20100620113817/http://www.openlierox.net:80/wiki/index.php/Hosting_behind_a_NAT"
last_modified: "15:49, 13 October 2009"
categories: [Guides]
---
{% raw %}
OpenLieroX 0.57 beta 5 and above allow people that are behind a [NAT](http://en.wikipedia.org/wiki/Network_address_translation) or [Firewall](http://en.wikipedia.org/wiki/Firewall) to host their own server that is accessible by other people from the Internet. No [port forwarding](http://en.wikipedia.org/wiki/Port_forwarding) or any other setup is necessary.

## Enabling the feature

This feature is enabled by default, no special actions need to be done.

## Restrictions

[OpenLieroX](/wiki/index.php/OpenLieroX/) is using the [hole punching algorithm](http://en.wikipedia.org/wiki/UDP_hole_punching) to enable connections through a NAT/Firewall.
This algorithm does not work with so-called [symmetric NAT/Firewall](http://en.wikipedia.org/wiki/Symmetric_NAT#Types_of_NAT) which is commonly used in big corporations.
Even if you are behind a symmetric NAT and want to host, people might be able to join your server. However, they must have their OpenLieroX port (23400) forwarded.

Because of the nature of the algorithm, ping cannot be determined in the serverlist. Therefore servers behind a NAT/Firewall display with a blue icon in [OpenLieroX](/wiki/index.php/OpenLieroX/) server list and a N/A ping.

Current versions of OpenLieroX do not allow viewing advanced server details of a server behind a NAT/Firewall. This is planned for future versions of [OpenLieroX](/wiki/index.php/OpenLieroX/).

This feature works only in OpenLieroX beta 5 and newer. Older versions (including [LieroX](/wiki/index.php/LieroX/)) ignore servers behind a NAT/Firewall.

## Troubleshooting

If your server does not appear in the server list, there are multiple things that could cause this:

* You are missing the udpmasterservers.txt file in OpenLieroX\cfg. Re-download OpenLieroX if that is the case
* Your network administrator blocked [UDP protocol](http://en.wikipedia.org/wiki/User_Datagram_Protocol). Not much you can do about this, OpenLieroX requires UDP to work.

## Extensions

* OpenLieroX 0.57 beta 8 improved the speed of joining a server behind NAT.
* OpenLieroX 0.58 beta 2 added a possibility to send wants-to-join messages.
{% endraw %}
