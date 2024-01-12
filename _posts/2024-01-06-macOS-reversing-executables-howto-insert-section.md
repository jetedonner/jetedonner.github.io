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

### The goal of this tutorial and its plan
As a target app for this tutorial we can use the same original hello_world app we built for the last tutorial "Reverse Engineering macOS - How to patch app". Please make sure you use the original unpatched app and not an edited or patched version as this would render unexpected results. The plan of this tutorial is to add a new section with our own new check function, that always will validate our secret successfully, no matter what the user enters after the prompt. For this we basically need just a simple check function with the same signature as the original checkInput() function from the hello_world app. This function does nothing else but just return true (0x0) and then gets back to the main function that called it. To generate the code we want to insert into the new section we first build a little helper app that is written in c and then decompiled to get the binary (hex) representation of the new check function. We then can extract this part of the helper app and just add it to the new section we insert with the help of LIEF. So that's about it. Everything clear till now? Yes?! - So let's start.

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

### Check the target hello_world app in Ghidra

Once again open the original hello_world from our last tutorial in Ghidra and disassemble it. Goto the main function and find the call to \_checkInput(). 

```nasm

       100003ed0 48 8d 3d        LEA        RDI,[s_Enter_your_secret:_100003f7b]             = "Enter your secret:\n"
                 a4 00 00 00
       100003ed7 b0 00           MOV        AL,0x0
       100003ed9 e8 84 00        CALL       <EXTERNAL>::_printf                              int _printf(char * param_1, ...)
                 00 00
       100003ede 48 8d b5        LEA        RSI=>local_118,[RBP + -0x110]
                 f0 fe ff ff
       100003ee5 48 8d 3d        LEA        RDI,[s_%s_100003f8f]                             = "%s"
                 a3 00 00 00
       100003eec b0 00           MOV        AL,0x0
       100003eee e8 75 00        CALL       <EXTERNAL>::_scanf                               int _scanf(char * param_1, ...)
                 00 00
       100003ef3 48 8d bd        LEA        RDI=>local_118,[RBP + -0x110]
                 f0 fe ff ff
       100003efa e8 61 ff        CALL       _checkInput                                      undefined _checkInput()
                 ff ff
       100003eff 89 85 dc        MOV        dword ptr [RBP + local_12c],EAX
                 fe ff ff
       100003f05 83 bd dc        CMP        dword ptr [RBP + local_12c],0x0
                 fe ff ff 00
       100003f0c 0f 85 13        JNZ        LAB_100003f25
                 00 00 00
       100003f12 48 8d 3d        LEA        RDI,[s_SUCCESS_100003f92]                        = "SUCCESS\n"
                 79 00 00 00
       100003f19 b0 00           MOV        AL,0x0
       100003f1b e8 42 00        CALL       <EXTERNAL>::_printf                              int _printf(char * param_1, ...)
                 00 00
       100003f20 e9 0e 00        JMP        LAB_100003f33
                 00 00


```

What we need is the **Instruction Pointer** and the **address of the call to \_checkInput()**. The address of the call to \_checkInput() in my case is 0x100003efa and the instruction pointer at the time this call instruction will be executed is at the next instruction to the call of \_checkInput() - in my case 0x100003eff. We need this two values because we want to update the argument to the call of \_checkInput() with the offset of the new \_checkOK() function to the current instruction pointer. If we have this values we can proceed to prepare our LIEF script for modifieing and inserting the new section to our hello_world app.


### Prepare the LIEF script for inserting the section

Create a neW python script named **insert_section.py** and insert the following code as its content, save the file in the same directory as the other files.

```python

import lief # Standard LIEF import
import subprocess # For chmod and codesign calls

# Open the original hello_world target
app = lief.parse("./hello_world")

# Open the binary file with the code for the new section
raw_shell = None
with open("./new_section.raw", "rb") as f:
    raw_shell = list(f.read())

# Get the __TEXT segment for offset calculations
__TEXT = app.get_segment("__TEXT")

# Create new section and add it
section = lief.MachO.Section("__shell", raw_shell)
section.alignment = 2
section += lief.MachO.SECTION_FLAGS.SOME_INSTRUCTIONS
section += lief.MachO.SECTION_FLAGS.PURE_INSTRUCTIONS
section = app.add_section(section)

# Calculate the offset of instruction pointer to new fucntion code address
new_target_addr = section.virtual_address + __TEXT.virtual_address
relativeOffset = new_target_addr - 0x100003eff

# Debug output the calculations for offset and argument hex values
print(f'New Section-Addr: {hex(new_target_addr)} / Offset: {hex(relativeOffset)}')
print(f'Call-Argument: {hex(relativeOffset)[8:]}, {hex(relativeOffset)[6:8]}, {hex(relativeOffset)[4:6]}, {hex(relativeOffset)[2:4]}')

# Patch the call argument with the hex values for the offset to the new _checkOK() function code (hex pairs in reverse order)
# We patch @ 0x100003efb because that's where the offset argument hex value starts
app.patch_address(0x100003efb, [int(hex(relativeOffset)[8:], 16), int(hex(relativeOffset)[6:8], 16), int(hex(relativeOffset)[4:6], 16), int(hex(relativeOffset)[2:4], 16)])

app.remove_signature()

# Save the new app
newFilename = "hello_world_with_new_section"
app.write("./" + newFilename)

# Make it executable and codesign
subprocess.run(["chmod", "+x", "./" + newFilename])
subprocess.run(['codesign', '--verbose=4', '--timestamp', '--strict', '--options', 'runtime', '-s', 'Apple Development', newFilename , '--force'])

```

For the ease of use we can add the call to chmod and codesign to the python script, just import subprocess and add the last two lines to the LIEF script.

### Insert the section / code with the LIEF script

```bash
dave@Aeon insert_section % python3 insert_section.py
```

Test the newly created app with new section and \_checkOK() function.

```bash
dave@Aeon insert_section % ./hello_world_with_new_section
Enter your secret:
12345 // Or anything else
SUCCESS
```

The new App should now accept any secret you enter. If not, go through the last steps and try to analyse what could went wrong. You should get a command line output something like above.

### Reroute the call to new checkOK function manually

Another way to reroute the call to our new \_checkOK() function is to use Ghidra to patch the file. If you followed alone the previouse tutorial you should have a basic picture how to do this with Ghidra. Anyway, here are the rouge steps to get the job done.

1. Open the file hello_world_with_new_section in Ghidra.
2. Check that the new section and code is contained in this executable.
3. Find the spot in the main function where the check is called.
4. Patch the call instruction to execute the new insert check function begins.
5. Export the patches Version of the App as new binary.
6. Make it executable and sign it.
7. Test it!


## <a id="credits"></a>Credits
- [Lief project](https://lief-project.github.io/){:target="_blank" rel="noopener"} - Library to Instrument Executable Formats
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
