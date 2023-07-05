---
layout: post
title:  "Unreal Engine - VisualizeInputEventPlugin"
author: dave
date:   2023-05-29 17:14:58 +0200
categories: UnrealEngine Plugins
tags: [UnrealEngine, Plugins, Games, Movies]
---

## Introduction
![VIEPlugin\_Demo](../../assets/img/projects/uevisualizeinputeventplugin/UE_VIE_Plugin-Screen-Featured-1920x1080-2023-06-27.png){: width="65%" }
_VisualizeInputEventPlugin first impression_

Unreal Engine Visualize Input Event Plugin. This Plugin visualizes Input Events such as Key-Presses, Mouse-Clicks and Gamepad Events from all the Unreal Engine Editors as well as all the Level Viewports. The functionality is useful specially if you are making learning videos or tutorials and want the viewers to see which Keyboard-Key you pressed, which Mouse-Button you clicked or Gamepad Event was fired. The functionality of the plugin is extensively configurable through its settings from the plugin toolbar menu which are saved in a config ini file. Checkout this documentation for more informations. Even though there is a somewhat similar yet very basic functionality built into Unreal Engine, this Plugin offers quite a few more options and settings to customize your visualization of the input events from the Unreal Editor. Give it a try and enjoy this very useful Unreal Engine extension.

I really appreciate that you download the plugin and give it a test. If you experience any problem or missing functionality please don't hesitate to contact me directly and tell me about your urge. On the other hand - if you are comfortable with the extension and you are confident with it's features and functionality it would of course be great if you could give me a short feedback as well or drop a comment on the Plugin-Page of the EPIC Marketplace. Any feedback is really welcome.

## Details

### Features
- Visualize Keyboard Key Presses, Mouse Clicks and Game Pad Events
- Show Events in Editor while Development as Notification
- Show Events in Level Viewport as OnScreenMessage while Development
- Show Events in OutputLog while development

#### The Plugin captures events from all Editors and Viewports
- All Editors
- All Viewports
- etc. ...

#### Extensively configurable using config ini file
- Enable / Disable Plugin for whole Project
- Enable / Disable show Keyboard Events
- Enable / Disable show Mouse Clicks
- Enable / Disable show Game Pad Events
- Choose whether to show as Notification in Editor mode
- Choose whether to show as OnScreenMessage in Editor mode
- Choose whether to show in OutputLog
- Choose the timeout of how long to display the information
- Many other detail settings for the different logging functionalities (see online documentation below)

### Code Modules
The Plugin is fully written in C++ and OpenSource. You can amend the source if you like and tweak or extend it to your needs and whishes.

#### VisualizeInputEventPlugin
- Type: Editor
- LoadingPhase: Default

#### VisualizeInputEventInput
- Type: Editor
- LoadingPhase: PostEngineInit

### Other Details
- Number of C++ Classes: 8
- Network Replicated: No - not needed
- Supported Development Platforms: macOS, Linux, Win64
- Supported Target Build Platforms: macOS, Linux, Win64
- Documentation: [VIE Plugin Documentation](https://kimhauser.ch/index.php/projects/unreal-engine/visualize-input-event-plugin){:target="_blank" rel="noopener"}


## EPIC Marketplace Download
- [Download Visualize Input Event Plugin (VIE Plugin)](https://www.unrealengine.com/marketplace/en-US/product/26796b2f61ac41509e0195402d4d386f){:target="_blank" rel="noopener"} - From EPIC Marketplace


## Youtube-Movie
### Introduction / Demo
- [VIE Plugin Introduction on Youtube](https://youtu.be/eqyuU1cIx8I){:target="_blank" rel="noopener"}

<div class="container-responsive-iframe">
  <iframe class="responsive-iframe" src="https://www.youtube.com/embed/eqyuU1cIx8I" title="YouTube video player" width="90%" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## Documentation Visualize Input Event Plugin for Unreal Engine 
### Installation of the Plugin
1. First visit the EPIC Marketplace with the EPIC Launcher and Search for **Visualize Input Event Plugin** (The marketplace URL of the plugin is: "com.epicgames.launcher://ue/marketplace/product/26796b2f61ac41509e0195402d4d386f")
2. Download and install the Plugin to your Unreal Engine
3. Run the Unreal Engine and create a new project or open an existing one
4. Goto menu **Edit>Plugins** and search for **Visualize Input Event Plugin**. Activate it. After that you will have to restart the Unreal Engine to successfully load the plugin. Do so.
5. After the resstart you will see a new icon in the menubar of the Unreal Editor.

## Version history 
### 1.0.0 / 1.0.0a - 2023-07-04
Initial release version of the plugin for Unreal Engine 5.1 (1.0.0) and Unreal Engine 5.2 (1.0.0a).

Created by Kim David Hauser, [https://kimhauser.ch](https://kimhauser.ch){:target="_blank" rel="noopener"} - 2023-07-03 (Unreal Engine 5.2)
