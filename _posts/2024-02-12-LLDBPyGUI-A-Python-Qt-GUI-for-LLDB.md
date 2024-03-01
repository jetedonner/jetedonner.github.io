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

## Requirements
- lldb version 18.0.0
```bash
ave@Aeon ~ % lldb --version
lldb version 18.0.0git (https://github.com/llvm/llvm-project.git revision 7e0c5266309c1d2a0e6d766834415dff5cb65e47)
  clang revision 7e0c5266309c1d2a0e6d766834415dff5cb65e47
  llvm revision 7e0c5266309c1d2a0e6d766834415dff5cb65e47
```
 
## How to install and run the app
To install the LLDBPyGUI app to LLDB you have to amend the .lldbinit file in you users home directory like so:

```bash
command script import /<pathToScript>/lldbpyGUI.py
```
(~/.lldbinit file)

To run the python app start a lldb instance with
```bash
ave@Aeon ~ % lldb
[+] Loaded LLDBPyGUI version 0.0.1 - ALPHA PREVIEW (BUILD: 689)
(LLDBPyGUI) spg
```

### Disclaimer
Please keep in mind, that this release is only a really early Alpha release version that is intend to give you a first preview of what the app will look and function like. There is no waranty or garantie of working functionality or working feature what so ever. Anyhow every feedback or input from your side is very welcome as this will give me an idea what is important to you as an end user. So please feel free to send me any feedback about the app. Thank you!

## Documentation

## Download / Github
- [Source code at GitHub](https://github.com/jetedonner/pyLLDBGUI)
<!-- - Zip file from mirror -->

## <a id="credits"></a>Credits
- [developer.arm.com](https://developer.arm.com/documentation){:target="_blank" rel="noopener"}
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O){:target="_blank" rel="noopener"}
