---
layout: post
title:  "UE5 Customization - Get properties from parent object"
author: dave
date:   2024-09-15 19:46:15 +0200
categories: [UnrealEngine, Articles]
tags: [UnrealEngine, Articles]
published: false 
---

# UE5 Struct Customization - Get properties from parent object in a struct customization
 This article intends to help you with property type customization of structs (USTRUCT) in unreal engine 5. Especially with how to get parent properties in a detail property customization of a custom struct. This information and affiliated projects are licensed under [MIT license](https://opensource.org/license/mit){:target="_blank" rel="noopener"} and freely available for everyone.

## Article Overview
- Introduction
- Basic UE5 customization setup in C++
- Get the parent object (UObject)
- Editor layout
- Source on GitHub

## Introduction

## Basic UE5 customization setup in C++

## Get the parent object (UObject)

## Editor layout

## Source on GitHub
- [botsec on GitHub](https://github.com/jetedonner/botsec){:target="_blank" rel="noopener"}

# Credits
## Author / Members
- [Kim David Hauser](mailto:kim@kimhauser.ch){:target="_blank" rel="noopener"}




## Implementation of the script
* Open the file **botsec.php** and amend the array **$agentsToDeny** in the script with your own search-bots you want to deny
* Also change the **$redirectLocation** variable to a location you want the bots to be redirected to if needed
* Upload or place the script to your webserver where your root or main index.php file (or any other script you want the function to apply) is. 
* Inlcude the botsec.php file like so:

```php
<?php
    require("botsec.php");
?>
```
* That's it. Every request to the website including the **botsec.php** script from a user-agent which is in the **$agentsToDeny** array is now beeing redirected to the URL stated in the **$redirectLocation** variable

## Testing the script
You can test the botsec.php script with your own User-Agents like so:

1. Copy the files to a directory of your choice
2. Amend the User-Agents array $agentsToDeny in <?= $botsecScript ?> with you own
3. Goto the directory containing the files in a terminal
4. Execute "php -S 127.0.0.1:8888" in the terminal
5. Open the address "127.0.0.1:8888" with your Webbrowser of choice
6. Now you should see the success message
7. With Google Chrome you can amend the User-Agent for the Request like so
    1. Open the developer console of Google Chrome with CMD+Option+J
    2. In the developer console click the three dots in the upper right corner
    3. Click on "More Tools" > "Network Conditions"
    4. In the bottom panel you should see the User-Agent and you can chnge it


