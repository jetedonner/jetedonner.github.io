---
layout: post
title:  "iOS - Demistified Part A"
author: dave
date:   2023-11-20 20:17:54 +0200
categories: [iOS, Demistified Part A]
tags: [Reversing, iOS, Demistified Part A]
---

## Introduction - What about

WHAT IS THIS ABOUT:

This is my first real deep endavour in iOS reversing and I want to let you be part of my troubles and successes. The article should be used as a map for your journey in reversing iOS.


### Tools
#### nm
```console
dave@Aeon MacOS % nm --help
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

## Credits
- [_apple.com_](https://www.apple.com){:target="_blank" rel="noopener"}