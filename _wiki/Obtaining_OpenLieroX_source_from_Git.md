---
title: Obtaining OpenLieroX source from Git
archived_url: "https://web.archive.org/web/20110721112411/http://www.openlierox.net/wiki/index.php/Obtaining_OpenLieroX_source_from_Git"
last_modified: "12:16, 16 May 2011"
categories: [How To]
---
{% raw %}
As of October 2009, the OpenLieroX project has migrated to [Git](http://en.wikipedia.org/wiki/Git_(software)). Git can be used to keep your local source code copy updated with the development. This How To explains a basic usage of this tool together with [OpenLieroX](/wiki/index.php/OpenLieroX/).

As of May 2011, the Git repository has been moved to [GitHub](/wiki/index.php/GitHub/).

Go to [OpenLieroX on GitHub](https://github.com/albertz/openlierox) and copy the appropriate Git URL (e.g. `git://github.com/albertz/openlierox.git`).

## Windows

First please install [Tortoise GIT](http://code.google.com/p/tortoisegit/). Tortoise Git is a Windows Explorer extension that enables you to use Git from Explorer context menu.
Create a folder where you want to have the sources located. After it's created, right-click it and choose Clone... To the address bar and enter the Git URL (see above).

Cloning the repository is the initial download of the newest code. As Git is decentral, it means that you have a full copy of the repository, including all the history. Cloning a repository is the first thing you have to do.

The code will be downloaded. Any time you want to download the updates, choose Tortoise Git -> Pull... from the context menu. As a branch choose the version you are interested in. Most probably this will be the master branch.

You should then switch to some branch. We don't really use the master branch. All main versions have different branches, i.e. there are branches for 0.57, 0.58 and 0.59. If you want to do actually something with the code, you should always work with the newest branch (at the time of writing, 0.59).

## Mac OS X, Linux, BSD, ...

Install the official Git client (<http://git-scm.com/download>) and run the command:

`git clone <git-url>`

This will download the sources in openlierox directory.

Most recommended branch to choose is the branch of the most recent version (at the time of writing, this is 0.59).

`git checkout -b 0.59 origin/0.59 --track`

To update your local repository to the newest code means to pull all changes from the remote repository or branch.

`git pull`
{% endraw %}
