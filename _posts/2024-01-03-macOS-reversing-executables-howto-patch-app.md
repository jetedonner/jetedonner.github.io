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
This post is a basic introduction about how to patch a simple macOS app. It shows you how to disassemble a macOS app with [Ghidra](https://github.com/NationalSecurityAgency/ghidra), identify the sweet spot and apply the patch manually and alternatively with the help of [LIEF](https://lief-project.github.io/). Just follow the tutorial and implement the needed files yourself or download the final files to inspect them on your own.

## Problem description
Some times you might run in a situation where you want to be able to amend a existing exectuable on macOS and extend or edit its behavior. Most of the times this amendment involves just a tiny little Spot or Part of the App and you really litteraly just need to flip one or two bytes. This is where patching an App comes into play. Here I gona show you some basic techniques how to do that.

## Tutorial - How to patch a macOS App 
### Examining and disassembling the App
First Thing you want to Do when it comes to modifying an App is examining the original files. And there are quite a few free and preinstalled Tools in our toolbelt that will help US with this analysis. macOS, since Switching from ppc base to darwin has a lot of app we well know from the Linux World. As a first Thing to do I would install XCode and its command line Tools as well as homebrew because it will offer you a wide range of posibilities with it's development environment and helper Tools. I also strongly advice you to Update python and get the latest Version via homebrew.

#### First inspection of the App
If the app you want to Analyse is an "*.app" bundle you will First have to show its content in finder and Goto the subfolder Content>MacOS here is the place where you will find the main executable that is launched when you open the app by double-clicking or such. This is also the executable you should disassemble First when You start your Reversing project.


### Our target HELLO WORLD app
For simplicity we create a simple hello world app that asks the user for a secret and checks it with a hardcoded string. We'll use this simple hello world app for our tutorials to find out how to reverse engineer macOS apps. So let's take a look at our hello world c source code ... (You also can downlaod all the files from this tutorial at the end of this page).

Create the hello world app by creating a file called hello_world.c with the following code in it:
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
  printf("Enter your secret:\n");

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

Compile the source code hello_world.c with:
```bash
clang -target x86_64-apple-macos -arch x86_64 -o hello_world hello_world.c
```

Make the file hello_world executable with:
```bash
chmod u+x hello_world 
```

Let's see what our executable hello_world looks like when we run it. Run it with ./hello_world
```bash
dave@Aeon patching_macOS_app % ./hello_world       
Enter your secret:
12345
ERROR
dave@Aeon patching_macOS_app % ./hello_world
Enter your secret:
S3CR3T
SUCCESS
dave@Aeon patching_macOS_app % 
```

The pseudo code for our hello_world. If we compare it to our original c source code we'll find, that the pseudo code is really close to the orignal.

```c
undefined8 entry(void)

{
  int iVar1;
  undefined local_118 [264];
  long local_10;
  
  local_10 = *(long *)PTR____stack_chk_guard_100004008;
  _printf("Enter your secret:\n");
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

One thing we discover here is the assignment of **PTR____stack_chk_guard_100004008** to var local_10. So what is this and why did the compiler insert it to the binary during compilation?

> Stack_chk_guard is a security feature used in C and C++ programs to protect against stack-based buffer overflow attacks. A stack-based buffer overflow attack occurs when malicious code overflows a buffer on the stack, causing it to overwrite other memory locations on the stack and potentially taking control of the program execution.
> 
> Stack_chk_guard works by placing a random value, called a canary, on the stack before each function is called. When the function returns, the canary value is read and compared to the original value. If the canary value has changed, it indicates that the stack has been corrupted and the program is terminated.
> 
> This canary value is typically stored in a reserved symbol called \_\_stack_chk_guard. When a program is compiled with stack_chk_guard enabled, the compiler will insert code to store and compare the canary value. This code is transparent to the programmer and does not require any changes to the program's source code.


The assembler code for our hello_world main (entry) function
```nasm
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined entry()
             undefined         AL:1           <RETURN>
             undefined8        Stack[-0x10]:8 local_10                                XREF[2]:     100003eb5(W), 
                                                                                                   100003f3d(R)  
             undefined1        Stack[-0x118   local_118                               XREF[2]:     100003ede(*), 
                                                                                                   100003ef3(*)  
             undefined4        Stack[-0x11c   local_11c                               XREF[1]:     100003eb9(W)  
             undefined4        Stack[-0x120   local_120                               XREF[1]:     100003ec3(W)  
             undefined8        Stack[-0x128   local_128                               XREF[1]:     100003ec9(W)  
             undefined4        Stack[-0x12c   local_12c                               XREF[2]:     100003eff(W), 
                                                                                                   100003f05(R)  
                             _main                                           XREF[2]:     Entry Point(*), 1000080ea(*)  
                             entry
       100003ea0 55              PUSH       RBP
       100003ea1 48 89 e5        MOV        RBP,RSP
       100003ea4 48 81 ec        SUB        RSP,0x130
                 30 01 00 00
       100003eab 48 8b 05        MOV        RAX,qword ptr [->___stack_chk_guard]             = 100010008
                 56 01 00 00
       100003eb2 48 8b 00        MOV        RAX=>___stack_chk_guard,qword ptr [RAX]          = ??
       100003eb5 48 89 45 f8     MOV        qword ptr [RBP + local_10],RAX
       100003eb9 c7 85 ec        MOV        dword ptr [RBP + local_11c],0x0
                 fe ff ff 
                 00 00 00 00
       100003ec3 89 bd e8        MOV        dword ptr [RBP + local_120],EDI
                 fe ff ff
       100003ec9 48 89 b5        MOV        qword ptr [RBP + local_128],RSI
                 e0 fe ff ff
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
                             LAB_100003f25                                   XREF[1]:     100003f0c(j)  
       100003f25 48 8d 3d        LEA        RDI,[s_ERROR_100003f9b]                          = "ERROR\n"
                 6f 00 00 00
       100003f2c b0 00           MOV        AL,0x0
       100003f2e e8 2f 00        CALL       <EXTERNAL>::_printf                              int _printf(char * param_1, ...)
                 00 00
                             LAB_100003f33                                   XREF[1]:     100003f20(j)  
       100003f33 48 8b 05        MOV        RAX,qword ptr [->___stack_chk_guard]             = 100010008
                 ce 00 00 00
       100003f3a 48 8b 00        MOV        RAX=>___stack_chk_guard,qword ptr [RAX]          = ??
       100003f3d 48 8b 4d f8     MOV        RCX,qword ptr [RBP + local_10]
       100003f41 48 39 c8        CMP        RAX,RCX
       100003f44 0f 85 0b        JNZ        LAB_100003f55
                 00 00 00
       100003f4a 31 c0           XOR        EAX,EAX
       100003f4c 48 81 c4        ADD        RSP,0x130
                 30 01 00 00
       100003f53 5d              POP        RBP
       100003f54 c3              RET
                             LAB_100003f55                                   XREF[1]:     100003f44(j)  
       100003f55 e8 02 00        CALL       <EXTERNAL>::___stack_chk_fail                    undefined ___stack_chk_fail()
                 00 00
                             -- Flow Override: CALL_RETURN (CALL_TERMINATOR)
       100003f5a 0f              ??         0Fh
       100003f5b 0b              ??         0Bh

```

The disassembled code for the **checkInput()** function which is called from the main function after user types his secret
```nasm
                             //
                             // __text 
                             // __TEXT
                             // ram:100003e60-ram:100003f5b
                             //
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined _checkInput()
             undefined         AL:1           <RETURN>
             undefined8        Stack[-0x10]:8 local_10                                XREF[2]:     100003e68(W), 
                                                                                                   100003e89(R)  
             undefined1        Stack[-0x11]:1 local_11                                XREF[1]:     100003e86(W)  
             undefined2        Stack[-0x13]:2 local_13                                XREF[1]:     100003e7c(W)  
             undefined4        Stack[-0x17]:4 local_17                                XREF[2]:     100003e72(W), 
                                                                                                   100003e8d(*)  
                             _checkInput                                     XREF[3]:     Entry Point(*), 
                                                                                          entry:100003efa(c), 1000080e8(*)  
       100003e60 55              PUSH       RBP
       100003e61 48 89 e5        MOV        RBP,RSP
       100003e64 48 83 ec 10     SUB        RSP,0x10
       100003e68 48 89 7d f8     MOV        qword ptr [RBP + local_10],RDI
       100003e6c 8b 05 02        MOV        EAX,dword ptr [s_S3CR3T_100003f74]               = "S3CR3T"
                 01 00 00
       100003e72 89 45 f1        MOV        dword ptr [RBP + local_17],EAX
       100003e75 66 8b 05        MOV        AX,word ptr [s_3T_100003f74+4]                   = "3T"
                 fc 00 00 00
       100003e7c 66 89 45 f5     MOV        word ptr [RBP + local_13],AX
       100003e80 8a 05 f4        MOV        AL,byte ptr [s__100003f74+6]                     = ""
                 00 00 00
       100003e86 88 45 f7        MOV        byte ptr [RBP + local_11],AL
       100003e89 48 8b 7d f8     MOV        RDI,qword ptr [RBP + local_10]
       100003e8d 48 8d 75 f1     LEA        RSI=>local_17,[RBP + -0xf]
       100003e91 e8 d8 00        CALL       <EXTERNAL>::_strcmp                              int _strcmp(char * param_1, char
                 00 00
       100003e96 48 83 c4 10     ADD        RSP,0x10
       100003e9a 5d              POP        RBP
       100003e9b c3              RET
       100003e9c 0f              ??         0Fh
       100003e9d 1f              ??         1Fh
       100003e9e 40              ??         40h    @
       100003e9f 00              ??         00h

```

In the disassembly we can see the **call to compare with CMP at 0x 100003efb** (after CALL checkInput at 0x100003ef0) and **decicion with JNZ at 0x100003f02** which is the point where the app decides if we entered the correct secret or not. So the answere to this challenge is quite simple. If we want to go the easiest way to get to the success functionality, we just have to make the app always go to the success branch. We can do this simply by NOP-ing out the descision branch. This is not very fancy, but yet very effective. 

### Patch using Ghidra
What we wana do in this situation is to **NOP the complete instruction "JNZ LAB_100003f1b"**. So we can do this by overwritting the instruction with the hex values "90" which is the opcode for NOP. The decision will look as follows after editing:

```nasm
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


       // START OF NOP MODIFICATION
       
       100003f0c 90              NOP
       100003f0d 90              NOP
       100003f0e 90              NOP
       100003f0f 90              NOP
       100003f10 90              NOP
       100003f11 90              NOP

       // END OF NOP MODIFICATION


       100003f12 48 8d 3d        LEA        RDI,[s_SUCCESS_100003f92]                        = "SUCCESS\n"
                 79 00 00 00
       100003f19 b0 00           MOV        AL,0x0
       100003f1b e8 42 00        CALL       <EXTERNAL>::_printf                              int _printf(char * param_1, ...)
                 00 00
       100003f20 e9 0e 00        JMP        LAB_100003f33
                 00 00

```

After you modified the assembly you have to write the code back to an executable. In Ghidra you can do this by clicking on Menu "File" > "Export Programm...". On the following screen you can choose a export location, the new filename and most important, the file type. Choose "Original File" as Format and click "Ok". When everything went fine, you will find a new executable at the choosen location. Before you can run it you will have to make it executable with:

```bash
dave@Aeon patching_macOS_app % chmod u+x hello_world_new
```

You also will have to code sign the app so it successfully runs. Do this with the following command:

```bash
dave@Aeon patching_macOS_app % codesign --verbose=4 --timestamp --strict --options runtime -s "Apple Development" hello_world_new --force
```

After that, your new executable is ready to run. Start the patched app - enter any secret you like and you will see something like the following:

```bash
dave@Aeon patching_macOS_app % ./hello_world_new
Enter your secret:
12345
SUCCESS
dave@Aeon patching_macOS_app % 

```

SUCCESS - yes, that's what we wanted to see and it's what we get. Due to the fact, that we NOPED the JNZ instruction to the error branch of the app away, the programm will always goto the success branch, no matter what we enter as secret. That's it - really simple and very basic, but also very effectiv indeed. 

You can go ahead an play around with the hello_world app on your own to i.e. store the return value of the strcmp() function in checkInput() into a variable and then return this variable as result of checkInput(). From this you can again load the compiled hello_world into Ghidra and i.e. modify the checkInput() function in a way it always returns 0x0 so the following check in the main() function always succeeds.

```c
// This is the evil check function which decides if we get access or not
int checkInput(char input[256]) {

  // The secret to check against the user input
  char hardcoded_string[] = "S3CR3T";

  // Compare the value of the variable "input" with the variable "hardcoded_string"
  int retVal = strcmp(input, hardcoded_string);

  // Return the result of strcmp()
  return retVal; // Patch this in disassembly so it always returns 0x0;
}
```

Another thing you could do, is to modify the string **"s_S3CR3T_100003f74" at 0x100003f74** to hold another secret you choose by modifying the string data in the \_\_cstring section.

```nasm
                             //
                             // __cstring 
                             // __TEXT
                             // ram:100003f74-ram:100003fa3
                             //
                             s_3T_100003f78                                  XREF[1,2]:   _checkInput:100003e6c(R), 
                             s__100003f7a                                                 _checkInput:100003e75(R), 
                             s_S3CR3T_100003f74                                           _checkInput:100003e80(R)  
       100003f74 53 33 43        ds         "S3CR3T"
                 52 33 54 00

```
It's up to you to push the posibilities of patching this demo app further and get more experience.


### Patch using LIEF
To patch the app you also can use LIEF. This is particullarly usefull if you want to automate certain tasks and / or have mutliple files with recurring tasks you want to execute. You can i.e. write a little python script for using LIEF to patch the app that looks someting like this:

```python
import lief

# Open the original executable as LIEF binary
app = lief.parse("./hello_world")

# Patch the location of the JNZ decision with NOPs
app.patch_address(0x100003f0c, [0x90, 0x90, 0x90, 0x90, 0x90, 0x90])

# Remove original code signature of the executable
app.remove_signature()

# Create a new executable and save it to the filesystem
app.write("./hello_world_lief_patched")
```

Of course again you will have to make the newly patched app executable again and recodesign it to get it running. But that's basically it. Try it yourself and play around with the LIEF script to get a feeling how it works.

## Download files
Here you can find all files we use during this tutorial. The executables are compiled on macOS 14.2 M1 (ARM64).

- Hello World App 
	- [Source Code (hello_world.c)](http://archaic.kimhauser.ch/downloads/reversing/tutorials/01-patch-macos-app/hello_world.c.zip)
	- [Original Executable (macOS ARM64)](http://archaic.kimhauser.ch/downloads/reversing/tutorials/01-patch-macos-app/hello_world.zip)
	- [Patched Executable (macOS ARM64)](http://archaic.kimhauser.ch/downloads/reversing/tutorials/01-patch-macos-app/hello_world_lief_patched.zip)
- [LIEF python script for patching the Hello World App](http://archaic.kimhauser.ch/downloads/reversing/tutorials/01-patch-macos-app/patch_hello_world.py.zip)
- [Complete file collection (all files in one archive)](http://archaic.kimhauser.ch/downloads/reversing/tutorials/01-patch-macos-app/01-patch-macos-app-2024-02-03.zip)


## <a id="credits"></a>Credits
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra)
- [Lief project](https://lief-project.github.io/){:target="_blank" rel="noopener"} - Library to Instrument Executable Formats
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
