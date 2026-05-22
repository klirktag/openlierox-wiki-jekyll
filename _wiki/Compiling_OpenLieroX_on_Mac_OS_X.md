---
title: Compiling OpenLieroX on Mac OS X
archived_url: "https://web.archive.org/web/20110721122622/http://www.openlierox.net/wiki/index.php/Compiling_OpenLieroX_on_Mac_OS_X"
last_modified: "18:29, 13 May 2010"
categories: [How To, Compiling OpenLieroX]
---
{% raw %}
This How To tutorial describes all the steps you need to do to compile [OpenLieroX](/wiki/index.php/OpenLieroX/). No programming knowledge is needed.

# Getting the source code

## Via GIT

The best way to get the source code is via [Git](http://en.wikipedia.org/wiki/Git_(software)). You will find more about this in [Obtaining OpenLieroX source from Git](/wiki/index.php/Obtaining_OpenLieroX_source_from_Git/).

## Via an archive

Get the current source archive from the [OpenLieroX download page](/downloads/). Unpack it to any folder you wish. This method is inferior to the above one because the source is not the most updated one.

# Getting the compiler

If you don't have it yet, you need the Xcode developer tools (just search for the application Xcode to see if you have it). It should be on your Mac OS X DVD (but could be an old version) or you can also download it from the following address: <http://developer.apple.com/technology/xcode.html>.

# Frameworks (dependencies)

Some frameworks are necessary to compile OpenLieroX. Download the specific package for Mac OS X (osx-dev-package.zip) from the following address: <https://sourceforge.net/project/showfiles.php?group_id=180059&package_id=289742>

You might also check for newer versions of SDL and the other libs. Just head to the official homepages.

Extract it and install all the contained frameworks. Some of them come with an own installer, just run it in that case. If it is the framework itself, just copy it to /Library/Frameworks.

## Boost

Grab a recent source release from here: <http://boost.org>

After extracting, open a Terminal, goto the directory, then do:

1.: ./bootstrap.sh --with-toolset=darwin

To build a binary that can run both in 32-bit and 64-bit modes, specify address-model=32_64. If you specify both of those properties, a "4-way" fat binary will be generated.

2.: ./bjam toolset=darwin link=static threading=multi architecture=combined address-model=32_64 macosx-version=10.4 macosx-version-min=10.4

# Compile

Open the OpenLieroX directory with Finder, navigate to the build/Xcode directory and double click on the Xcode project file. The whole project should open in Xcode.

A target needs to be chosen in Xcode, set it to OpenLieroX. Optionally, set the build configuration to Debug. Continue by clicking on "Build".

# Troubleshooting

If you have trouble with the compiling, visit the [corresponding forum topic](/forum/index.php/topic,12367.msg187139.html).
{% endraw %}
