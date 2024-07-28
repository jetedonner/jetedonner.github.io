---
layout: post
title:  "BotSec - PHP script for denying Search-Bots"
author: dave
date:   2024-07-28 19:28:14 +0200
categories: [Projects, HTML]
tags: [Projects, HTML]
published: true
---

# botsec - Deny unwanted search-bots
 A PHP script for denying and redirecting unwanted search bots which may be causing a huge traffic on your website. You may use, copy, amend and redistribute this PHP script in all your projects whether it's personal or commercial. The script is licensed under [MIT license](https://opensource.org/license/mit){:target="_blank" rel="noopener"} and freely available for everyone.

- [BotSec - A PHP script for denying Search-Bots and reducing unwanted web-traffic](https://botsec.kimhauser.ch){:target="_blank" rel="noopener"}

This is an example usage of the "botsec.php" script. It'll redirect you to [https://google.com](https://google.com){:target="_blank" rel="noopener"} if the user-agent of the request is in the array to check.

## Source on GitHub
- [botsec on GitHub](https://github.com/kimhauser/botsec){:target="_blank" rel="noopener"}

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

# Credits
## Author / Members
- [Kim David Hauser](mailto:kim@kimhauser.ch){:target="_blank" rel="noopener"}
