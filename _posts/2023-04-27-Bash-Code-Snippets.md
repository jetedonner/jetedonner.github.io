---
layout: post
title:  "BASH code snippets"
author: dave
date:   2023-04-27 20:15:05 +0200
categories: Projects BASH
tags: [Projects, Snippets, BASH]
published: true
---

# BASH Code Snippets
Some small and simple code snippets from me.

## Bash script to replace a string in a file with the filename 
This was usefull for me to replace some header comments for .h / .cpp files when I used copy paste to insert a standart header to the sourcfiles and then wanted to adjust the text reflecting the filename.


```console
for f in $(find . -name '*.h'); 
do 
	search="Dbg.h"
	full="$f"
	basename "$f"
	n="$(basename -- $f)"
	sed -i '' -e "s/  \\"$search"/  \\"$n"/g" "$full"
done

for f in $(find . -name '*.cpp'); 
do 
	search="Dbg.cpp"
	full="$f"
	basename "$f"
	n="$(basename -- $f)"
	sed -i '' -e "s/  \\"$search"/  \\"$n"/g" "$full"
done
```
### Description of the script
In this example the script searches for all ".h" and ".cpp" files and then replaces the string "  Dbg.h" or "  Dbg.cpp" with its actual filename. Paste the code into a "example.sh" file, "chmod +x example.sh" and then execute it in the parent directory of the location where the files you want to amend are placed in.