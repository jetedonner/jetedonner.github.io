---
layout: post
title:  "Reverse Engineering macOS - How to insert a section into app"
author: dave
date:   2024-01-06 12:24:34 +0200
categories: [Reverse Engineering, macOS]
tags: [Reverse Engineering, macOS, Insert section]
published: true 
---

## Synopsis
This post is a basic introduction about how to insert a section into a simple macOS app. It shows you how to disassemble a macOS app with Ghidra, prepare a raw code file with the content for the new section and then how to insert the new section into the app with LIEF. Just follow the tutorial and implement the needed files yourself or download the final files to inspect them on your own.

## Problem description
If patching a file is not an option and / or you want to add a bigger piece of code to an existing app and there is not enough space available to modify the existing app as it is, you might want to insert a new section in to the app and place and reference your new code from there. This tutorial shows you just that and how to achive this with the help of LIEF.


## Tutorial - How to insert a new section into a macOS App 
### Examining and disassembling the App

Of course again you will have to make the newly patched app executable again and recodesign it to get it running. But that's basically it. Try it yourself and play around with the LIEF script to get a feeling how it works.


## <a id="credits"></a>Credits
- [Lief project](https://lief-project.github.io/){:target="_blank" rel="noopener"} - Library to Instrument Executable Formats
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
