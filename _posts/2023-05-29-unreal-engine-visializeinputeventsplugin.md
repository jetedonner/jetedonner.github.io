---
layout: post
title:  "Unreal Engine - UEVisualizeInputEventPlugin"
author: dave
date:   2023-05-29 17:14:58 +0200
categories: UnrealEngine Plugins
tags: [UnrealEngine, Plugins, Games, Movies]
---

!!! UNDER CONSTRUCTION - STAY TUNED !!!

## Introduction
![UE\_VIEPlugin\_Demo](../../assets/img/projects/uevisualizeinputeventplugin/UE_EKP_Screen-Featured-894x488-2023-05-28.png){: width="284" height="284" }
_UEVisualizeInputEventPlugin first impression_

UE Input Event Visualizer Plugin. This Plugin visualises Input Events such as KeyPress and MouseClicks from the Editor as well as the Gameplay Viewport. The functionality is useful specially if you are making learning videos or tutorials and want the viewers of the videos to see what Keyboard-Key you pressed or which Mouse-Button you clicked. The functionality of the plugin is extensively configurable through its settings saved in a config ini file.

This first release version of the plugin shows keyboard and mouse click events only at the moment, but it's planed to support more input devices and events in a further version pretty soon. Anyway I really appreciate that you download the plugin and give test it to your needs. If you experience any problem or missing functionality please don't hesitate to contact me directly and tell me about your urge. Also - on the other hand - if you are comfortable with the extension and you are confident with it's features and functionality it would of course be great if you could give me a short feedback as well and / or drop a comment on the Plugin-Page of the EPIC Marketplace. Any feedback is really welcome.

## Details

### Features
- Visualize Keyboard KeyPresses / MouseClicks
- Show Events in Editor while Development as Notification
- Show Events in Gameplay Viewport as OInScreenMessage while GamePlay
- Show Events in OutputLog while development and Gameplay

#### The Plugin captures events from all Editors
- Level Editor
- Blueprint Editor
- Material Editor
- Particle Editor
- (all other editors)

#### Extensively configurable using config ini file
- Enable / Disable Plugin for Project
- Enable / Disable showing Keyboard Events
- Enable / Disable showing Mouse Clicks
- Choose whether to show as Notification in Editor mode or not
- Choose whether to show as OnScreenMessage in GamePlay mode or not
- Choose the timeout of how long to display the information

### Code Modules

#### UEVisualizeInputEventPlugin
- Type: Editor
- LoadingPhase: Default

#### UE_EditorKeyPressedInput
- Type: Editor
- LoadingPhase: PostEngineInit

### Other Details
- Number of C++ Classes: 8
- Network Replicated: No - no need
- Supported Development Platforms: macOS
- Supported Target Build Platforms: macOS, Linux, Win32, Win64
- Documentation: https://jetedonner.github.io/projects/ue/ueinputvisualizerplugin/
- Example Project: https://github.com/jetedonner/ueinputvisualizerplugin

## Youtube-Movies

### Introduction / Demos
- <https://youtu.be/fcvcSzapRgE>
- <https://youtu.be/v8Az2MHcF_g>

### Documentation / How-To use UE_InputEventVisualizerPlugin
- <https://youtu.be/v8Az2MHcF_g>

Created by Kim David Hauser, https://kimhauser.ch - 2023-05-27 (Unreal Engine 5.1)


## Install the UEVisualizeInputEventPlugin
1. Fire up the Epic Game Launcher
2. Goto Marketplace and search for UEVisualizeInputEventPlugin - Add it to your cart and checkout
3. After the Plugin is downloaded you can add it to your (new) projects by opening the PluginManager in the Unreal Editor and searching for *UEVisualizeInputEventPlugin* and activating it. You will have to restart the UnrealEditor to fully activate the Plugin for your project.

## Plugin Content
The UE5_TeleportDemo comes with 9 different ready made portals. This includes the 3D models, textures / materials as well as the Blueprint for easily adding it to your level. If you like you can use this portals as they are in your project, but your free to amend them to your needs or take them as examples or guides to build you own teleport portals.


### Latest demo movie (New demo project)
<div class="container-responsive-iframe">
  <iframe class="responsive-iframe" src="https://www.youtube.com/embed/M2Sblqx3VVE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Source code download
- [Plugin source code](https://github.com/jetedonner/PlayerStartPlugin){:target="_blank" rel="noopener"} - Github repository

## About / Credits
- Created by Kim David Hauser, https://kimhauser.ch - 2023-05-27 (Unreal Engine 5.1)
	