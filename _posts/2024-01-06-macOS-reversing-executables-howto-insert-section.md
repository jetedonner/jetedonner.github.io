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

### The plan and goal of this tutorial
As a targte for this tutorial we can use the same original hello_world app we built for the last tutorial "Reverse Engineering macOS - How to patch app". Please make sure you use the original unpatched app and not an edited or patched version as this would render unexpected results. The plan of this tutorial is to add a new section with our own new check function, that always will validate our secret successfully, no matter what the user enters after the prompt. For this we basically need just a simple check function with the same signature as the original checkInput() function from the hello_world app. This function does nothing else but just return true (0x0) and then gets back to the main function that called it. To generate the code we want to insert into the new section we first build a little helper app that is written in c and the decompiled to get the binary representation of the new check function. We then can extract this part of the helper app and just add it to the new section we insert. So that's about it. Everything clear till now? Yes?! - So let's start.

### Prepare the code to insert
For the sake of simplicity the code we are going to add in the section we insert does nothing more than just return a 0x0 so we can trick the check of our secret input to think the comparsion succeeded. To create the code we are going to insert we can write a little helper app. Create a new c sourcefile **helper_app.c** that looks like this:

```c
#include <stdio.h>

int checkOK(char input[256]) { 
  return 0; 
}

int main() { 
  return 0; 
}
```

Compile the source code helper_app.c with:
```bash
dave@Aeon insert_section % clang -target x86_64-apple-macos -arch x86_64 -o helper_app helper_app.c
```

Make the file helper_app executable with:
```bash
dave@Aeon insert_section % chmod u+x helper_app 
```

To make sure the helper_app compiled ok and is runnable execute it with:
```bash
dave@Aeon insert_section % ./helper_app 
```

If there is no error (you should see no output and the programm should exit cleanly) the app is ok.

We will then use Ghidra to disassemble the helper app and visit the code of the checkOK() function. To prepare it for inserting into the new section we are going to extract the hex values which define this function. The resulting disassembly with Ghidra will look something like this:


```nasm
                             //
                             // __text 
                             // __TEXT
                             // ram:100003f80-ram:100003f9f
                             //
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined _checkOK()
             undefined         AL:1           <RETURN>
             undefined8        Stack[-0x10]:8 local_10                                XREF[1]:     100003f84(W)  
                             _checkOK                                        XREF[2]:     Entry Point(*), 100004078(*)  
       100003f80 55              PUSH       RBP
       100003f81 48 89 e5        MOV        RBP,RSP
       100003f84 48 89 7d f8     MOV        qword ptr [RBP + local_10],RDI
       100003f88 31 c0           XOR        EAX,EAX
       100003f8a 5d              POP        RBP
       100003f8b c3              RET
       100003f8c 0f              ??         0Fh
       100003f8d 1f              ??         1Fh
       100003f8e 40              ??         40h    @
       100003f8f 00              ??         00h

```

This is the code we need, more specifically the HEX values of this code. So extracte the HEX string of the function and save it to a new file called new_section.raw

```hex
5548 89e5 4889 7df8 31c0 5dc3 0f1f 4000
```

Make sure you save the code string with the right encoding (as HEX string) and as binary file otherways the hex code might be saved as string and that's not what we want. You can check the content of the new binary file new_section.raw with the **hexdump** cli command like this:

```bash
dave@Aeon insert_section % hexdump -C new_section.raw
00000000  55 48 89 e5 48 89 7d f8  31 c0 5d c3 0f 1f 40 00  |UH..H.}.1.]...@.|
00000010
dave@Aeon insert_section % 
```
NOTE: When you don't specify the '-C' argument the hex pairs are output in flipped order.

### Prepare the LIEF script for inserting the section

Create a nee python script named insert_section.py and insert the following code as its content, save the file in the same directory as the other files.

```python

import lief

app = lief.parse("./hello_world")

raw_shell = None
with open("./new_section.raw", "rb") as f:
    raw_shell = list(f.read())

__TEXT = app.get_segment("__TEXT")
section = lief.MachO.Section("__shell", raw_shell)
section.alignment = 2
section += lief.MachO.SECTION_FLAGS.SOME_INSTRUCTIONS
section += lief.MachO.SECTION_FLAGS.PURE_INSTRUCTIONS

section = app.add_section(section)
print(section)

# app.patch_address(4294982909, [232, 142, 239, 255])

# app.main_command.entrypoint = section.virtual_address - __TEXT.virtual_address
app.remove_signature()
app.write("./hello_world_new_section")

```

### Insert the section and code

```bash
dave@Aeon insert_section % python3 insert_section.py
```

### Route the function call to new code

One way to Reroute the call to our new check function is to use Ghidra to patch the file. If you followed alone the previouse tutorial you should have a basic picture how to do this with Ghidra. Anyway, here are the rouge steps to get the job done.

1. Open the file hello_world_new_section in Ghidra.
2. Check that the new section and code is contained in this executable.
3. Find the Spot in the main function where the check is called.
4. Patch the call instruction to execute the new insert check function begins.
5. Export the patches Version of the App as new binary.
6. Test it!

```bash

```

## <a id="credits"></a>Credits
- [Lief project](https://lief-project.github.io/){:target="_blank" rel="noopener"} - Library to Instrument Executable Formats
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
