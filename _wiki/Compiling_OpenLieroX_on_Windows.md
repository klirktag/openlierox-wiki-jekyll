---
title: Compiling OpenLieroX on Windows
archived_url: "https://web.archive.org/web/20110721122605/http://www.openlierox.net/wiki/index.php/Compiling_OpenLieroX_on_Windows"
last_modified: "19:21, 21 April 2010"
categories: [How To, Compiling OpenLieroX]
---
{% raw %}
This How To tutorial describes all the steps you need to do to compile [OpenLieroX](/wiki/index.php/OpenLieroX/). No programming knowledge is needed.

# Getting the source code

## Via GIT

The best way to get the source code is via [Git](http://en.wikipedia.org/wiki/Git_(software)). You will find more about this in [Obtaining OpenLieroX source from Git](/wiki/index.php/Obtaining_OpenLieroX_source_from_Git/).

## Via an archive

Get the current source archive from the [OpenLieroX download page](/official/downloads.php). Unpack it to any folder you wish. This method is inferior to the above one because the source is not the most updated one.

# Choosing the compiler

If you already have a C++ compiler, you can skip this step.
[OpenLieroX](/wiki/index.php/OpenLieroX/) currently supports four C++ compilers. However, only Visual C++ 2010 project is updated on a regular base. And the CMake file but it doesn't work out-of-the-box for MSVC yet.

## Bloodshed's DevCpp

This [IDE](http://en.wikipedia.org/wiki/Integrated_development_environment) is free and you can download it from Bloodshed's website (use the version with MinGW).
[Download Dev C++](http://www.bloodshed.net/dev/devcpp.html)

## Microsoft Visual C++ 6

Support for this compiler has been discontinued.

## Microsoft Visual C++ 2005 (Express)

Microsoft's C++ compiler and an [IDE](http://en.wikipedia.org/wiki/Integrated_development_environment). You can get an Express version for free from Microsoft. The only required thing is to register the product (to remove the 30 day limitation), but it's for free as well.
[Download Visual C++ 2005 Express](http://msdn2.microsoft.com/en-us/express/aa975050)

## Microsoft Visual C++ 2008 (Express)

Microsoft's most modern C++ compiler and an [IDE](http://en.wikipedia.org/wiki/Integrated_development_environment). You can get an Express version for free from Microsoft. The only required thing is to register the product (to remove the 30 day limitation), but it's for free as well. This is a successor of VC++ 2005.
[Download Visual C++ 2008 Express](http://www.microsoft.com/express/download/#webInstall)

## Microsoft Visual C++ 2010 (Express)

Microsoft's most modern C++ compiler and an [IDE](http://en.wikipedia.org/wiki/Integrated_development_environment). You can get an Express version for free from Microsoft. The only required thing is to register the product (to remove the 30 day limitation), but it's for free as well. This is a successor of VC++ 2005.
[Download Visual C++ 2010 Express](http://www.microsoft.com/express/download/#webInstall)

# Compiling the code

## DevCpp

Because OpenLieroX depends on some libraries, you have to install so called dependencies. Because DevCpp's update manager doesn't work well, a ZIP file was created a ZIP which contains everything you need.

* [Download the zip](https://sourceforge.net/projects/openlierox/files/dev-package-OLX/install_deps_devcpp.zip/download) (about 5 MB) and unpack it somewhere
* Install (double-click) all extracted files

NOTE: If you installed DevC++ to another directory or drive than C:\Dev-Cpp, go to Tools -> Compiler settings -> Directories -> C++ Include Files and add a new path there: <path_to_devcpp>\include\SDL.

Now you can start compiling OpenLieroX. Go to <source directory>\build\DevCpp and double-click the file OpenLieroX.dev. The project will be open in DevC++. After everything is loaded, press CTRL + F9 to compile. After the compilation finishes, your OpenLieroX.exe file is located in <OLX sources>\distrib\win32.

## Visual C++ 2005 Express

Firstly, Platform SDK has to be installed. It is freely available from Microsoft's website ([tutorial & download](http://msdn2.microsoft.com/en-us/express/aa700755)). Make sure you followed ALL the steps in the tutorial. The only thing that should not be done is creating a new project (use OpenLieroX project instead).
After Platform SDK is successfully installed, install dependencies. There is a ready self-extracting archive that will do all this work for you: [download the dependencies installer for Visual C++ 2005](https://sourceforge.net/projects/openlierox/files/dev-package-OLX/install_deps_vc2005.exe/download). Unpack (install) the package to Visual C++ directory (default C:\Program Files\Microsoft Visual Studio 8 ). Navigate to <OpenLieroX sources>\build\msvc 2005 and open Game.vcproj. Click Build -> Configuration Manager and choose "Release" in the Configuration column. Press F7 to start compilation. After a successful compilation, the OpenLieroX.exe file is located in <OpenLieroX sources>\bin\ directory. You can also run the game by pressing F5.

## Visual C++ 2008 Express

The procedure is the same as in Visual C++ 2005, the only difference is that you don't have to install Platform SDK (it's installed automatically).
First install the dependencies: [Download the dependencies installer for Visual C++ 2008](https://sourceforge.net/projects/openlierox/files/dev-package-OLX/install_deps_vc2008.exe/download) and install/unpack it to Visual C++ directory (default C:\Program Files\Microsoft Visual Studio 9.0 ). Navigate to <OLX sources>\build\msvc 2008 and open Game.vcproj. Click Build -> Configuration Manager and choose "Release" in the Configuration column. Press F7 to start compilation. After a successfull compilation the OpenLieroX.exe file is found in <OpenLieroX sources>\distrib\win32\ directory. You can also run the game by pressing F5.

## Visual C++ 2010 Express

The procedure is the same as in Visual C++ 2005, the only difference is that you don't have to install Platform SDK (it's installed automatically).
First install the dependencies: [Download the dependencies installer for Visual C++ 2010](https://sourceforge.net/projects/openlierox/files/dev-package-OLX/) and install/unpack it to Visual C++ directory (default C:\Program Files\Microsoft Visual Studio 10.0 ). Navigate to <OLX sources>\build\msvc 2010 and open Game.vcproj. Click Build -> Configuration Manager and choose "Release" in the Configuration column. Press F7 to start compilation. After a successfull compilation the OpenLieroX.exe file is found in <OpenLieroX sources>\distrib\win32\ directory. You can also run the game by pressing F5.

# Troubleshooting

If you have trouble with the compiling, visit the [corresponding forum topic](/forum/index.php/topic,6444.msg80222.html#msg80222).
{% endraw %}
