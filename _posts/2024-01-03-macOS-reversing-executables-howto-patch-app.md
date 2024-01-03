---
layout: post
title:  "Reverse Engineering macOS - How to patch app"
author: dave
date:   2024-01-03 19:02:38 +0200
categories: [Reverse Engineering, macOS]
tags: [Reverse Engineering, macOS, Patch app]
published: true 
---

## Synopsis
This post is a basic introduction about how to patch a simple macOS app. It shows you how to disassemble a macOS app with Ghidra, identify the sweet spot and apply the patch. Just follow the tutorial and implement the needed files yourself or download the final files to inspect them on your own.

## Problem description
Some times you might run in a situation where you want to be able to amend a existing exectuable on macOS and extend or edit its behavior.

## <a id="credits"></a>Credits
- [Lief project](https://lief-project.github.io/){:target="_blank" rel="noopener"} - Library to Instrument Executable Formats
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
