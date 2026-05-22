---
title: "Lua:networkgameevent"
archived_url: "https://web.archive.org/web/20100618082256/http://www.openlierox.net:80/wiki/index.php/Lua:networkgameevent"
last_modified: "15:12, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:networkgameevent).

###### Class NetworkGameEvent

##### See also:

[bindings.gameNetworkInit](/wiki/index.php/Lua_global/#bindings.gamenetworkinit), [network_game_event](/wiki/index.php/Lua_global/#network_game_event), [network_game_event](/wiki/index.php/Lua_global/#network_game_event)

##### send

```
 send([data[, connection[, mode[, rules]]]])
```

Sends a game event to one or more computers.

//data// is a bitstream to [send](#send) with the event.

//connection// is a connection ID to [send](#send) the event on. If it's 0, the //rules// parameter decides who to [send](#send) to.

//mode// is one of these values (default is SendMode.ReliableOrdered):
SendMode.ReliableUnordered : The events always arrive, but may come in a different order than sent.
SendMode.ReliableOrdered : The events always arrive and in the order sent.
SendMode.Unreliable : The events may or may not arrive and in any order.

//rules// decides what computers to [send](#send) the event to if //connection// is 0 or left out.
It can be any (or sometimes a sum) of:
RepRule.Auth2All : Event is sent from the server to clients.
RepRule.Auth2Owner : Event is sent from the server to clients owning the node.
RepRule.Auth2Proxy : Event is sent from the server to clients not owning the node.
RepRule.None : Event is not sent.
RepRule.Owner2Auth : Event is sent from clients owning the node to the server.

A valid combination is (RepRule.Owner2Auth + RepRule.Auth2All) which sends the event
from owners to the server or from the server to all clients (depending on if we're the server or not).
{% endraw %}
