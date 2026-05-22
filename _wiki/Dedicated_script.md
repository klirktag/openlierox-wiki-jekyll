---
title: Dedicated script
archived_url: "https://web.archive.org/web/20101228145313/http://www.openlierox.net/wiki/index.php/Dedicated_script"
last_modified: "10:18, 14 November 2009"
---
{% raw %}
You can easily write own scripts for the [dedicated server](/wiki/index.php/Dedicated_server/) (we call this part the dedicated control). You can write that in any language you want. We concentrate on Python here to give some easy examples but it really doesn't matter, as long as you can read from stdin and write to stdout.

The protocol is very simple. It also doesn't really matter how your Python script is structured or looks like. You are reading any input from OLX via stdin and you give commands (or make requests for some data) via stdout.

You also don't have to overwrite scripts/dedicated_control. You can set whatever script you want to use in your [options.cfg](/wiki/index.php/Options.cfg/). Or you can also set that also via commandline, like:

```` ```
openlierox -dedicated -script my_own_script.py
``` ````

More concrete, two examples about the protocol:

You put `"getvar GameOptions.GameInfo.TimeLimit\n"` on stdout, for example with this Python command:

```` ```
print "getvar GameOptions.GameInfo.TimeLimit"
``` ````

If the timelimit is 6, then OLX will put the response `":6\n.\n"` (without `"`) to stdin of your script. In general, there is a list of return values, all beginning with `":"` and ended by `"\n"`, and this list finished by a `".\n"`. We are handling this in the [io-part in our dedicated scripts](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob;f=share/gamedir/scripts/dedicated_control_io.py;hb=HEAD). Here a simplified version which does that:

```` ```
def getRawResponse():
	ret = sys.stdin.readline().strip()
	if ret != "":
		return ret
	else:
		sys.stderr.write("Dedicated_control: OLX terminated, exiting\n")
		sys.exit(1)
	return ""

def getResponse():
	ret = []
	resp = getRawResponse()
	while resp != ".":
		if not resp.startswith(':'):
			sys.stderr.write("Dedicated_control: bad OLX dedicated response: " + resp + "\n")
		else:
			ret.append( resp[1:] )
		resp = getRawResponse()
	return ret
``` ````

You would call getResponse here and it will wait until OLX has finished the command and returns a list of all return values. For example, the full code to get the current timelimit from OLX:

```` ```
print "getvar GameOptions.GameInfo.TimeLimit"
timelimit = int(getResponse()[0])
``` ````

Not all commands have return values. They just return `".\n"`. In that case, getResponse() == []. But in any way, you should wait for the command completion.

Another example:

```` ```
print "startlobby"
getResponse()
print "addbots 2"
getResponse()
print "startgame"
getResponse()
``` ````

This would start a game with two bots.

The commands you can execute are the same you can also execute in the ingame console or also directly at stdin of OLX or also via the chat command "/ded <cmd>". You get a full list with the command "help" or "longhelp". Read [Dedicated server](/wiki/index.php/Dedicated_server/) or [Commands](/wiki/index.php/Commands/) for further information.

Btw., as said, the io-part of our scripts wrap a lot of OLX-commands already in some handy functions. For example, there is:

```` ```
def RawSendCommand(X):
	print X

def SendCommand(cmd):
	RawSendCommand(cmd)
	return getResponse()

def getVar(var):
	ret = SendCommand( "getvar %s" % var )
	if len(ret) == 0: # var does not exist
		return ""
	return ret[0]

def getGameType():
	return int(getVar("GameOptions.GameInfo.GameType"))
``` ````

In addition to this, for example after you have started the game, you should idle and wait for any new signals by OLX. You do that by just executing the command `"nextsignal"`. Those signals you are returning here are any ingame events, like "backtolobby" or "lobbystarted" or whatever.

The very complete list of all signals can just be read from the [C++ source](http://openlierox.git.sourceforge.net/git/gitweb.cgi?p=openlierox/openlierox;a=blob;f=src/server/DedicatedControl.cpp;hb=HEAD). Just search for "pushSignal" in there. You will find stuff like:

```` ```
void Sig_LobbyStarted() { pushSignal("lobbystarted"); }
``` ````

But you can safely also ignore most signals and for example just wait for "backtolobby". You can also look in our official script, how we handle the signals, in dedicated_control_handler.py at signalHandler.

Here a simple example for your mainloop, with the given functions above (we only use SendCommand here):

```` ```
SendCommand("startlobby")
SendCommand("startgame")
while True:
	nextsignal = SendCommand("nextsignal")
	if nextsignal[0] == "backtolobby":
		# next round!
		SendCommand("startgame")
``` ````

It is often handy for debugging to print some debugging messages. You cannot use print here because all those output would go to OLX and OLX will try to interpret that as a command.

We have introduced a special command `"msg"` for this. For example, if you want to inform about what signal you have gotten (to get some idea about what you could handle), you could use this sample loop:

```` ```
SendCommand("startlobby")
SendCommand("startgame")
while True:
	nextsignal = SendCommand("nextsignal")
        SendCommand("msg \"got signal: %s\"" % repr(nextsignal))
``` ````

If any question, just ask in the forums.
{% endraw %}
