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
Some times you might run in a situation where you want to be able to amend a existing exectuable on macOS and extend or edit its behavior. Most of the times this amendment involves just a tiny little Spot or Part of the App and you really litteraly just need to flip one or two bytes. This is where patching an App comes into play. Here I gona show you some basic techniques how to do that.

## Tutorial - How to patch a macOS App 
### Examining and disassembling the App
First Thing you want to Do when it comes to modifying an App is examining the original files. And there are quite a few free and preinstalled Tools in our toolbelt that will help US with this analysis. macOS, since Switching from ppc base to darwin has a lot of app we well know from the Linux World. As a first Thing to do I would install XCode and its command line Tools as well as homebrew because it will offer you a wide range of posibilities with it's development environment and helper Tools. I also strongly advice you to Update python and get the latest Version via homebrew.

#### First inspection of the App
If the app you want to Analyse is an "*.app" bundle you will First have to show its content in finder and Goto the subfolder Content>MacOS here is the place where you will find the main executable that is launched when you open the app by double-clicking or such. This is also the executable you should disassemble First when You start your Reversing project.

## <a id="credits"></a>Credits
- [Lief project](https://lief-project.github.io/){:target="_blank" rel="noopener"} - Library to Instrument Executable Formats
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
