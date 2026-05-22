---
title: "Lua:particle"
archived_url: "https://web.archive.org/web/20100618081405/http://www.openlierox.net:80/wiki/index.php/Lua:particle"
last_modified: "15:12, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:particle).

###### Class Particle

(inherits from [Object](/wiki/index.php/Lua_object/))

##### See also:

[NetworkParticleEvent:send](/wiki/index.php/Lua_networkparticleevent/#send), [network_particle_event](/wiki/index.php/Lua_global/#network_particle_event)

##### set_angle

```
 set_angle(angle)
```

Changes the angle of the particle to //angle//.

##### set_replication

(available from version 0.9c)

```
 set_replication(type, state)
```

If the particle is network-aware, this function turns on or off replication
of different aspects of the particle's state.

Note that this function can only affects things for
which replication is activated in the omfgScript of the particle type.

Since the server has authority over particle replication, this function will
have no affect on clients.

//type// can be one of the following:
Particle.Position : replication of position.

//state// is either true or false, where true turns on replication and false turns it off.
{% endraw %}
