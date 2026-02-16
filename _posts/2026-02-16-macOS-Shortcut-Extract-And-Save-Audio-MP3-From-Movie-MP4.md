---
layout: post
title:  "macOS shortcut - extract audio from movie mp4 file and save as mp3 file"
author: dave
date:   2026-02-16 22:52:50 +0200
categories: [macOS, Tools]
tags: [macOS, Tools]
published: true
---

## Introduction
![Translate and say text from chrome](../../assets/img/projects/shortcuts/Extract-Audio-As-MP3-From-Movie-MP4.png){: width="65%" }
_Extract audio from movie mp4 file and save as mp3 file - Shortcut Setup_

This macOS shortcut lets you instantly extract the audio track from any selected .mp4 movie file directly from Finder. Once triggered as a Quick Action, it takes the file you selected, converts the audio to MP3 using a built‑in shell workflow, and saves the result with the same filename but an .mp3 extension. No file pickers, no extra clicks — just a fast, reliable way to turn video files into standalone audio.

## How to install and use
### Installation (without editing)
Installation is easy. Just browse to the _Extract MP3 from Movie.shortcut_ file and doubleclick it - and done. You should have now a new "Quick action" Item in the chrome context menu when selecting a text in the finder app and doing a right click on the selection.

### Shell script
The following shell script does most of the work of this macOS Tahoe shortcut. You can put it into a "*.sh" file and use it as standalone script as well.

```bash
INPUT="$1"
DIR="$(dirname "$INPUT")"
BASE="$(basename "$INPUT" .mp4)"
OUTPUT="$DIR/$BASE.mp3"

# Convert using ffmpeg
ffmpeg -i "$INPUT" -vn -acodec libmp3lame "$OUTPUT"
```

## Github repository
- [macOS shortcuts github repo by jetedonner](https://github.com/jetedonner/macOS-shortcuts){:target="_blank" rel="noopener"}

## License
- [MIT License](https://en.wikipedia.org/wiki/MIT_License){:target="_blank" rel="noopener"}

## Credits
This macOS shortcuts was made with the help of Microsoft Copilot AI app and some elbow grease
- [Microsoft Copilot AI macOS app](https://apps.apple.com/de/app/microsoft-copilot/id6738511300){:target="_blank" rel="noopener"}