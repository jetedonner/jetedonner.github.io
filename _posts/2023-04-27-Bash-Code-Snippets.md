---
layout: post
title:  "BASH code snippets"
author: dave
date:   2023-04-27 18:15:05 +0200
categories: [Projects, BASH]
tags: [Projects, Snippets, BASH]
published: true
---

# BASH Code Snippets
Some small and simple code snippets from me.

## Bash script to replace a string in a file with the filename 
This was usefull for me to replace some header comments for .h / .cpp files when I used copy paste to insert a standart header to the sourcfiles and then wanted to adjust the text reflecting the filename.


```console
#==========================================================
# replaceHeader.sh 
#
# Author: 	DaVe inc. Kim David Hauser (kimhauser.ch)
# Date: 	2023-04-27 19:32:59
#
# Description:
# Replace a variable file content string with its filename
#==========================================================

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
In this example the script searches for all ".h" and ".cpp" files in a directory (recursively) and then replaces the file content string "  Dbg.h" or "  Dbg.cpp" with its actual filename (only filename no path).

### How to use the script
Paste the code into a "replaceHeader.sh" file, and adjust the nessesary variables (search, '*.h' and '*.cpp'). Then make it executable with console command "chmod +x replaceHeader.sh" and then execute it in the parent directory of the location where the files you want to amend are placed in.

### Download script
[_Download replaceHeader.sh script_](https://kimhauser.ch/downloads/github/replaceHeader.sh)