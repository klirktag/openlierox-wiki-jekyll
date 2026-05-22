---
title: "Lua:bitstream"
archived_url: "https://web.archive.org/web/20100618084947/http://www.openlierox.net:80/wiki/index.php/Lua:bitstream"
last_modified: "12:28, 30 January 2010"
---
{% raw %}
Copied from [here](http://sliekas.org/basara/gusdocs/doku.php/main:modding_docs:lua:bitstream).

###### Class Bitstream

```
===== See also: =====
```

[new_bitstream](/wiki/index.php/Lua_global/#new_bitstream)

##### add_bool

```
 add_bool()
```

Extracts a boolean value from this bitstream (Returns either true or false).

##### add_int

```
 add_int(value[, bits])
```

Adds an integer to this bitstream encoded in //bits// bits.

If bits is left out, 32 bits is assumed.

##### add_string

```
 add_string(str)
```

Adds the string //str// to this bitstream.

##### decode_elias_gamma

```
 decode_elias_gamma()
```

Extracts an integer above or equal to 1 encoded using the elias gamma universal encoding.

##### dump

```
 dump(value)
```

Adds a lua object to the bitstream.

WARNING: This function is not very space efficient and can only encode tables
, strings, numbers, booleans and nil (or tables with keys and values of those types)

##### encode_elias_gamma

```
 encode_elias_gamma(value)
```

Adds an integer above or equal to 1 encoded using the elias gamma universal encoding.

##### get_bool

```
 get_bool()
```

Extracts a boolean value from this bitstream (Returns either true or false).

##### get_int

```
 get_int([bits])
```

Extracts an integer from this bitstream encoded in //bits// bits.

If bits is left out, 32 bits is assumed.

##### get_string

```
 get_string()
```

Extracts a string from this bitstream.

##### undump

```
 undump()
```

Extracts a lua object added to the bitstream using the //dump// method.
{% endraw %}
