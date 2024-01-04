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


### Our target HELLO WORLD app
For simplicity we create a simple hello world app that asks the user for a secret and checks it with a hardcoded string. We'll use this simple hello world app for our tutorials to find out how to reverse engineer macOS apps. So let's take a look at our hello world c source code

```c
// Standard include
#include <stdio.h>
// For scanf()
#include <curses.h> 
// For strcmp()
#include <string.h>

// This is the evil check function which decides if we get access or not
int checkInput(char input[256]) {

  // The secret to check against the user input
  char hardcoded_string[] = "S3CR3T";

  // Compare the value of the variable "input" with the variable "hardcoded_string"
  return strcmp(input, hardcoded_string);
}

// The main function / entry point of the executable
int main(int argc, char **argv) {

  // Variable to hold the user input
  char input[256];

  // This msg will prompt the user to enter his / her secret
  printf("Enter your secret: ");

  // Will wait for user input and store the input in the variable "input"
  scanf("%s", input);

  // Compare the value of the variable "input" with the variable "hardcoded_string"
  int result = checkInput(input); // strcmp(input, hardcoded_string);

  // If the compare of the two values succeeds (or not) show a appropriate message
  if (result == 0) {
    printf("SUCCESS\n");
  } else {
    printf("ERROR\n");
  }
  return 0;
}
```

The assembler code for our hello_world
```asm
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined entry()
             undefined         AL:1           <RETURN>
             undefined8        Stack[-0x10]:8 local_10                                XREF[2]:     100003ea5(W), 
                                                                                                   100003f33(R)  
             undefined1        Stack[-0x118   local_118                               XREF[2]:     100003ed4(*), 
                                                                                                   100003ee9(*)  
             undefined4        Stack[-0x11c   local_11c                               XREF[1]:     100003ea9(W)  
             undefined4        Stack[-0x120   local_120                               XREF[2]:     100003eb3(W), 
                                                                                                   100003ec0(R)  
             undefined8        Stack[-0x128   local_128                               XREF[1]:     100003eb9(W)  
             undefined4        Stack[-0x12c   local_12c                               XREF[2]:     100003ef5(W), 
                                                                                                   100003efb(R)  
                             _main                                           XREF[2]:     Entry Point(*), 1000080ea(*)  
                             entry
       100003e90 55              PUSH       RBP
       100003e91 48 89 e5        MOV        RBP,RSP
       100003e94 48 81 ec        SUB        RSP,0x130
                 30 01 00 00
       100003e9b 48 8b 05        MOV        RAX,qword ptr [->___stack_chk_guard]             = 10000c008
                 66 01 00 00
       100003ea2 48 8b 00        MOV        RAX=>___stack_chk_guard,qword ptr [RAX]          = ??
       100003ea5 48 89 45 f8     MOV        qword ptr [RBP + local_10],RAX
       100003ea9 c7 85 ec        MOV        dword ptr [RBP + local_11c],0x0
                 fe ff ff 
                 00 00 00 00
       100003eb3 89 bd e8        MOV        dword ptr [RBP + local_120],EDI
                 fe ff ff
       100003eb9 48 89 b5        MOV        qword ptr [RBP + local_128],RSI
                 e0 fe ff ff
       100003ec0 8b b5 e8        MOV        ESI,dword ptr [RBP + local_120]
                 fe ff ff
       100003ec6 48 8d 3d        LEA        RDI,[s_Enter_your_secret_(%d):_100003f71]        = "Enter your secret (%d): "
                 a4 00 00 00
       100003ecd b0 00           MOV        AL,0x0
       100003ecf e8 84 00        CALL       <EXTERNAL>::_printf                              int _printf(char * param_1, ...)
                 00 00
       100003ed4 48 8d b5        LEA        RSI=>local_118,[RBP + -0x110]
                 f0 fe ff ff
       100003edb 48 8d 3d        LEA        RDI,[s_%s_100003f8a]                             = "%s"
                 a8 00 00 00
       100003ee2 b0 00           MOV        AL,0x0
       100003ee4 e8 75 00        CALL       <EXTERNAL>::_scanf                               int _scanf(char * param_1, ...)
                 00 00
       100003ee9 48 8d bd        LEA        RDI=>local_118,[RBP + -0x110]
                 f0 fe ff ff
       100003ef0 e8 5b ff        CALL       _checkInput                                      undefined _checkInput()
                 ff ff
       100003ef5 89 85 dc        MOV        dword ptr [RBP + local_12c],EAX
                 fe ff ff
       100003efb 83 bd dc        CMP        dword ptr [RBP + local_12c],0x0
                 fe ff ff 00
       100003f02 0f 85 13        JNZ        LAB_100003f1b
                 00 00 00
       100003f08 48 8d 3d        LEA        RDI,[s_SUCCESS_100003f8d]                        = "SUCCESS\n"
                 7e 00 00 00
       100003f0f b0 00           MOV        AL,0x0
       100003f11 e8 42 00        CALL       <EXTERNAL>::_printf                              int _printf(char * param_1, ...)
                 00 00
       100003f16 e9 0e 00        JMP        LAB_100003f29
                 00 00
                             LAB_100003f1b                                   XREF[1]:     100003f02(j)  
       100003f1b 48 8d 3d        LEA        RDI,[s_ERROR_100003f96]                          = "ERROR\n"
                 74 00 00 00
       100003f22 b0 00           MOV        AL,0x0
       100003f24 e8 2f 00        CALL       <EXTERNAL>::_printf                              int _printf(char * param_1, ...)
                 00 00
                             LAB_100003f29                                   XREF[1]:     100003f16(j)  
       100003f29 48 8b 05        MOV        RAX,qword ptr [->___stack_chk_guard]             = 10000c008
                 d8 00 00 00
       100003f30 48 8b 00        MOV        RAX=>___stack_chk_guard,qword ptr [RAX]          = ??
       100003f33 48 8b 4d f8     MOV        RCX,qword ptr [RBP + local_10]
       100003f37 48 39 c8        CMP        RAX,RCX
       100003f3a 0f 85 0b        JNZ        LAB_100003f4b
                 00 00 00
       100003f40 31 c0           XOR        EAX,EAX
       100003f42 48 81 c4        ADD        RSP,0x130
                 30 01 00 00
       100003f49 5d              POP        RBP
       100003f4a c3              RET
                             LAB_100003f4b                                   XREF[1]:     100003f3a(j)  
       100003f4b e8 02 00        CALL       <EXTERNAL>::___stack_chk_fail                    undefined ___stack_chk_fail()
                 00 00
                             -- Flow Override: CALL_RETURN (CALL_TERMINATOR)
       100003f50 0f              ??         0Fh
       100003f51 0b              ??         0Bh
```


The pseudo code for our hello_world

```c
undefined8 entry(uint param_1)

{
  int iVar1;
  undefined local_118 [264];
  long local_10;
  
  local_10 = *(long *)PTR____stack_chk_guard_100004008;
  _printf("Enter your secret (%d): ",(ulong)param_1);
  _scanf("%s",local_118);
  iVar1 = _checkInput(local_118);
  if (iVar1 == 0) {
    _printf("SUCCESS\n");
  }
  else {
    _printf("ERROR\n");
  }
  if (*(long *)PTR____stack_chk_guard_100004008 == local_10) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  ___stack_chk_fail();
}
```

## <a id="credits"></a>Credits
- [Lief project](https://lief-project.github.io/){:target="_blank" rel="noopener"} - Library to Instrument Executable Formats
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
