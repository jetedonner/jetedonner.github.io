---
layout: post
title:  "LLDBPyGUI - GUI for LLDB Debugger Python API with PyQt6"
author: dave
date:   2024-02-12 05:46:45 +0200
categories: [Debugger, LLDB]
tags: [Debugger, LLDB, PyQt6]
published: true 
---
# LLDBPyGUI
(former pyLLDBGUI

![LLDBPyGUI](../../assets/img/projects/lldbpygui/LLDBPyGUI-MainView-2024-02-28.png)

## Synopsis
LLDBPyGUI is a longtime missed gui of mine for the opensource debugger (framework) LLDB. While LLDB comes with a comperhensive set of tools and also a C++ and Python API. I lacks of providing a useful (at least for me) GUI as it's only working as a terminal application at this day of age. So I took some time and started a GUI wrapper project that is using the Python API of LLDB and began to implement a UI with the help of PyQt6. The project is still in a really early prototype stage at the moment, but I didn't want to let you miss the idea of mine and give you a short sneak-preview of the tool I have in mind.

## Movie Trailer
<div class="container-responsive-iframe">
<iframe class="responsive-iframe" src="https://www.youtube.com/embed/WGJYLz1r118" title="Python GUI for the LLDB Debugger Python API" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Features
- General info about the target
- Disassembler / Debugger
- Stacktrace viewer
- Break- and Watchpoints
- Register / Variable viewer
- Synchronized source code
- Memory viewer
- Search function
- Commands interface

## Documentation

## Download / Github
- [Source code at GitHub](https://github.com/jetedonner/pyLLDBGUI)
<!-- - Zip file from mirror -->

## <a id="credits"></a>Credits
- [developer.arm.com](https://developer.arm.com/documentation){:target="_blank" rel="noopener"}
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O){:target="_blank" rel="noopener"}