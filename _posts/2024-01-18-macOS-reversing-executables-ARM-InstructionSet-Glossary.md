---
layout: post
title:  "Reverse Engineering macOS - ARM Instruction set glossary"
author: dave
date:   2024-01-07 19:32:13 +0200
categories: [Reverse Engineering, macOS]
tags: [Reverse Engineering, macOS, ASM Instructions]
published: true 
---

## Synopsis
This post is a quick guide to the ARM A-profile A64 Instruction set with simple explaination of their function. The complete documentation of the ARM A-profile A64 instruction set with lots of more information can be found at [developer.arm.com](https://developer.arm.com/documentation){:target="_blank" rel="noopener"}

## Overview
If patching a file is not an option and / or you want to add a lot of new code to an existing app and adding a new section is not an option, then you might want to inject a new library into an exeisting app and the call the code from this library. This tutorial shows you just that and how to achive this with the help of LIEF and Ghidra.


## Instructions

### ADD (immediate)
Add (immediate) adds a register value and an optionally-shifted immediate value, and writes the result to the destination register.

#### Example
```nasm
add    x4, x3, #0x1
```

#### Explaination
Adds 0x1 to x3 and stores the result in x4.

```doc
ADD <Xd|SP>, <Xn|SP>, #<imm>{, <shift>}
```

### SUB (immediate)
Subtract (register) subtracts an optionally-shifted register value from a register value, and writes the result to the destination register.

#### Example
```nasm
sub    x1, x17, #0x32
```

```doc
SUB{<c>}{<q>} {<Rd>,} <Rn>, <Rm>, RRX
```

#### Explaination
Subtracts the value 0x32 from x17 and stores the result in x1.

### STRB (register)
Store Register Byte (register) calculates an address from a base register value and an offset register value, and stores a byte from a 32-bit register to the calculated address. For information about memory accesses, see Load/Store addressing modes.

```doc
STRB <Wt>, [<Xn|SP>, <Xm>{, LSL <amount>}]
```
#### Example

```nasm
strb   w17, [x6, #0x1]
```

#### Explaination
Calculates a new address with x6 offest by 0x1 and stores the value of w17 at this address.

#### Documentation
[developer.arm.com](https://developer.arm.com/documentation/ddi0602/2023-12/Base-Instructions/STRB--register---Store-Register-Byte--register--?lang=en)

## <a id="credits"></a>Credits
- [developer.arm.com](https://developer.arm.com/documentation){:target="_blank" rel="noopener"}
- [Mach-O Wikipedia](https://en.wikipedia.org/wiki/Mach-O){:target="_blank" rel="noopener"}
