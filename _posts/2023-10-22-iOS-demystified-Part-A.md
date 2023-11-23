---
layout: post
title:  "iOS Internals - iOS demistified Part A"
author: dave
date:   2023-11-20 20:17:54 +0200
categories: [iOS Internals, iOS Demistified Part A]
tags: [Reversing, iOS Internals, iOS Demistified Part A]
---

## Introduction - What about

WHAT IS THIS ABOUT:

This is my first real deep endavour in iOS reversing and I want to let you be part of my troubles and successes. The article should be used as a map for your journey in reversing iOS.

### Articles 
#### History of Jailbreak
Some very useful informations about the history of jailbreaking the iOS with detailed explaination
- https://medium.com/@iponurovskiy/ios-jailbreaks-history-part-1-93797400c24 (Part 1) (mirror)
- https://medium.com/@iponurovskiy/%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B4%D0%B6%D0%B5%D0%B9%D0%BB%D0%B1%D1%80%D0%B5%D0%B9%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-ios-%D1%87%D0%B0%D1%81%D1%82%D1%8C-2-9c1b234fc500 (Part 2) (mirror)

### Supporting Projects
- https://github.com/Maxmad68/swift-libimobiledevice
- https://github.com/Shakshi3104/DeviceHardware
- https://github.com/anatoliyv/AssistantKit
- https://github.com/Arti3DPlayer/USBDeviceSwift
- https://github.com/4eleven7/iMobileDevice
- 

### Tools
#### nm
nm (name mangling) is a Unix command used to dump the symbol table and their attributes from a binary executable file (including libraries, compiled object modules, shared-object files, and standalone executables). The output from nm distinguishes between various symbol types.

This is a nice little tool which shows you useful informations about the symbol table of a library or executable on Linux and macOS.

```console
nm --help
OVERVIEW: LLVM symbol table dumper

USAGE: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/nm [options] <input object files>

OPTIONS:
  -A                Alias for --print-file-name
  -a                Alias for --debug-syms
  -B                Alias for --format=bsd
  -C                Alias for --demangle
  --debug-syms      Show all symbols, even debugger only
  --defined-only    Show only defined symbols
  --demangle        Demangle C++ symbol names
  --dynamic         Display dynamic symbols instead of normal symbols
  -D                Alias for --dynamic
  --export-symbols  Export symbol list for all inputs
  --extern-only     Show only external symbols
  --format=<format> Specify output format: bsd (default), posix, sysv, darwin, just-symbols
  -f <format>       Alias for --format
  -g                Alias for --extern-only
  --help            Display this help
  -h                Alias for --help
  -j                Alias for --format=just-symbols
  -m                Alias for --format=darwin
  --no-demangle     Don't demangle symbol names
  --no-llvm-bc      Disable LLVM bitcode reader
  --no-sort         Show symbols in order encountered
  --no-weak         Show only non-weak symbols
  --numeric-sort    Sort symbols by address
  -n                Alias for --numeric-sort
  -o                Alias for --print-file-name
  --portability     Alias for --format=posix
  --print-armap     Print the archive map
  --print-file-name Precede each symbol with the object file it came from
  --print-size      Show symbol size as well as address
  -P                Alias for --format=posix
  -p                Alias for --no-sort
  --quiet           Suppress 'no symbols' diagnostic
  --radix=<radix>   Radix (o/d/x) for printing symbol Values
  --reverse-sort    Sort in reverse order
  -r                Alias for --reverse-sort
  --size-sort       Sort symbols by size
  --special-syms    Do not filter special symbols from the output
  -S                Alias for --print-size
  -t <radix>        Alias for --radix
  --undefined-only  Show only undefined symbols
  -U                Alias for --defined-only
  -u                Alias for --undefined-only
  --version         Display the version
  -V                Alias for --version
  -v                Alias for --numeric-sort
  -W                Alias for --no-weak
  -X <value>        Specifies the type of ELF, XCOFF, or IR object file to examine. The value must be one of: 32, 64, 32_64, any (default)

llvm-nm Mach-O Specific Options:
  --add-dyldinfo    Add symbols from the dyldinfo not already in the symbol table
  --add-inlinedinfo Add symbols from the inlined libraries, TBD only
  --arch=<value>    architecture(s) from a Mach-O file to dump
  --dyldinfo-only   Show only symbols from the dyldinfo
  --no-dyldinfo     Don't add any symbols from the dyldinfo
  -s                Dump only symbols from this segment and section name
  -x                Print symbol entry in hex

llvm-nm XCOFF Specific Options:
  --no-rsrc Exclude resource file symbols (__rsrc) from the export symbol list.

Pass @FILE as argument to read options from FILE.
```

### CLI
#### irecovery
- libirecovery % ./tools/irecovery -vvv -s

#### libimobiledevice
- libimobiledevice % ./tools/idevice_id

#### usbmuxd
- usbmuxb % ./usbmuxd

```console
src % sudo ./usbmuxd -v -f  
[20:57:57.571][3] usbmuxd v1.1.1-56-g360619c starting up
[20:57:57.572][4] Creating socket
[20:57:57.572][4] Listening on /var/run/usbmuxd
[20:57:57.572][2] chmod(/var/db/lockdown, 02775) failed: Operation not permitted
[20:57:57.572][4] Initializing USB
[20:57:57.572][3] Using libusb 1.0.26
[20:57:57.576][4] Registering for libusb hotplug events
[20:57:57.576][4] Found new device with v/p 05ac:12a8 at 1-1
[20:57:57.576][4] Requesting current mode from device 1-1
[20:57:57.576][4] 1 device detected
[20:57:57.576][3] Initialization complete
[20:57:57.577][3] Found CDC-NCM and Apple USB Multiplexor in device 1-1 configuration 5
[20:57:57.577][4] Received response 5:3:3:0 for get_mode request for device 1-1
[20:57:57.577][2] Skipping switch device 1-1 mode from 3 to 3
[20:57:57.577][3] Found usbmux interface for device 1-1: 1
[20:57:57.577][4] Found interface 1 with endpoints 04/85 for device 1-1
[20:57:57.577][2] Could not claim interface 1 for device 1-1: LIBUSB_ERROR_ACCESS
[20:57:57.577][2] Cannot find device entry while removing USB device 0x126705780 on location 0x10001
[20:58:05.637][4] Found new device with v/p 05ac:12a8 at 1-1
libusb: warning [darwin_open] USBDeviceOpen: another process has device opened for exclusive access
[20:58:05.637][4] Requesting current mode from device 1-1
[20:58:05.645][4] Received response 3:3:3:0 for get_mode request for device 1-1
[20:58:05.645][2] Switching device 1-1 mode to 3
[20:58:05.796][2] Cannot find device entry while removing USB device 0x116604080 on location 0x10001
[20:58:05.796][2] Cannot find device entry while removing USB device 0x116604080 on location 0x10001
[20:58:06.606][4] Found new device with v/p 05ac:12a8 at 1-1
libusb: warning [darwin_open] USBDeviceOpen: another process has device opened for exclusive access
[20:58:06.607][4] Requesting current mode from device 1-1
[20:58:06.607][4] Client 7 accepted
[20:58:06.607][2] Attempted to connect to nonexistent device 31
[20:58:06.608][4] Client 8 accepted
[20:58:06.608][3] Found CDC-NCM and Apple USB Multiplexor in device 1-1 configuration 5
[20:58:06.608][4] Received response 5:3:3:0 for get_mode request for device 1-1
[20:58:06.608][2] Skipping switch device 1-1 mode from 3 to 3
[20:58:06.608][3] Found usbmux interface for device 1-1: 1
[20:58:06.608][4] Found interface 1 with endpoints 04/85 for device 1-1
[20:58:06.629][2] Could not claim interface 1 for device 1-1: LIBUSB_ERROR_ACCESS
[20:58:06.629][2] Cannot find device entry while removing USB device 0x106604080 on location 0x10001
[20:58:06.629][4] Client 7 connection closed
[20:58:06.629][4] Client 7 is going to be disconnected
[20:58:06.630][4] Client 7 accepted
...
[20:58:06.766][4] Client 8 connection closed
[20:58:06.766][4] Client 8 is going to be disconnected
```


## Credits
- [_Linus Torvalds_](https://github.com/torvalds){:target="_blank" rel="noopener"} / [_Linux_](https://linux.com/torvalds){:target="_blank" rel="noopener"}
- [_apple.com_](https://www.apple.com){:target="_blank" rel="noopener"}
- [_microsoft.com_](https://www.microsoft.com){:target="_blank" rel="noopener"}
- [_google.com_](https://www.google.com){:target="_blank" rel="noopener"}
