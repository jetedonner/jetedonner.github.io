---
layout: post
title:  "Unreal Engine - TeleportSysBase"
author: dave
date:   2023-09-10 23:27:28 +0200
categories: UnrealEngine Plugins
tags: [UnrealEngine, Plugins, Games, Movies]
---

## Introduction
![TeleportSysBase](../../assets/img/projects/ueteleportplugin/TeleporterIntro_MainImage_1920x1080.png){: width="284" height="284" }
_TeleportSysBase Intro Trailer_

https://youtu.be/dpE73Q4LSMQ

The *TeleportSysBase* lets you easily implement a custom Teleportation System in your own Unreal Engine project. It features game ready Portals with meshes, textures / materials, actor blueprints, dissolving, wormhole and Lightning effects, sound effects and more. Please make sure you checkout the Demo-Project (TeleportSysBaseDemo) to get familiar with how to setup and use the plugin.

## Description
The *Teleport System Base* provides essential functionalities (C++ classes, functions and content) and assets to support you to easily create and implement your own teleportation system in your game projects. It's fully replicated, so you can also use it in your multiplayer projects. The Plugin comes with the library-core fully written in C++ and also some game ready sample contents and blueprints. The samples content features different portal types, different wormhole types / examples as well as many different dissolving effects and lightning implementation examples ready to be extended or implemented by using C++ or with your own Blueprints. You'll also get example sound effects for fading in and out the transported character during the teleportation process.

## Install the UETeleportPlugin
1. Fire up the Epic Game Launcher
2. Goto Marketplace and search for *TeleportSysBase* - Add it to your cart and checkout
3. After the Plugin is downloaded you can add it to your (new) projects by opening the PluginManager in the Unreal Editor and searching for *TeleportSysBase* and activating it. You will have to restart the UnrealEditor to fully activate the Plugin for your project.

## Plugin Content
The UE5_TeleportDemo comes with 9 different ready made portals. This includes the 3D models, textures / materials as well as the Blueprint for easily adding it to your level. If you like you can use this portals as they are in your project, but your free to amend them to your needs or take them as examples or guides to build you own teleporting portals.

### Included portals

#### RipplePortal

The Ripple Portal is basically a rippeling Material Effect on a plane mesh. The portal uses color effects to indicate the different teleporter modes.

![RipplePortal](../../assets/img/projects/ueteleportplugin/readme/001_RipplePortal.png){: width="284" height="284" }

**RipplePortal Files**
- BP\_RipplePortal (Actor Blueprint)
- MI\_RippleBase / M\_RippleBase (Ripple Effect Material)
- PS\_Sparks (Niagara Particle System)

#### FlatPortal
![FlatPortal](../../assets/img/projects/ueteleportplugin/readme/002_FlatPortal.png){: width="284" height="284" }

#### ButtonPortal
![ButtonPortal](../../assets/img/projects/ueteleportplugin/readme/003_ButtonPortal.png){: width="284" height="284" }

#### RingPortal
![RingPortal](../../assets/img/projects/ueteleportplugin/readme/004_RingPortal.png){: width="284" height="284" }

#### BlackholePortal
![BlackholePortal](../../assets/img/projects/ueteleportplugin/readme/005_BlackholePortal.png){: width="284" height="284" }

#### DragonPortal
![DragonPortal](../../assets/img/projects/ueteleportplugin/readme/006_DragonPortal.png){: width="284" height="284" }

#### SpinningPortal
![SpinningPortal](../../assets/img/projects/ueteleportplugin/readme/007_SpinningPortal.png){: width="284" height="284" }

#### StargateLikishPortal
![StargateLikishPortal](../../assets/img/projects/ueteleportplugin/readme/008_StargateLikishPortal.png){: width="284" height="284" }

#### SceneCapturePortal
![SceneCapturePortal](../../assets/img/projects/ueteleportplugin/readme/009_SceneCapturePortal.png){: width="284" height="284" }

### Wormholes

### Dissolve Effects

### Sound Effects


## Use the Plugin in your own project

### Credits and licensing
The UE5_TeleportPlugin is released under the [_Unreal® Engine End User License Agreement For Publishing_](https://www.unrealengine.com/en-US/eula/unreal?sessionInvalidated=true){:target="_blank" rel="noopener"}. Please make sure to read through the license agreement before releasing your projects using the UETeleportPlugin. Credits and references to the author are highly appreciated - thank you!
- [Local version of the UE End User License For Publishing](/assets/docs/ue/LICENSE){:target="_blank" rel="noopener"}


## Youtube Clips
### First Trailer
<div class="container-responsive-iframe">
  <iframe class="responsive-iframe" src="https://www.youtube.com/embed/v8Az2MHcF_g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Outtake while game play (Trailer base)
<div class="container-responsive-iframe">
  <iframe class="responsive-iframe" src="https://www.youtube.com/embed/fcvcSzapRgE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Latest demo movie (New demo project)
<div class="container-responsive-iframe">
  <iframe class="responsive-iframe" src="https://www.youtube.com/embed/M2Sblqx3VVE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<!--
## Source code download
- [Plugin source code](https://github.com/jetedonner/PlayerStartPlugin){:target="_blank" rel="noopener"} - Github repository
- [Demo project source UE4](https://github.com/jetedonner/UE4_PlayerStartDemo){:target="_blank" rel="noopener"} - Demo Source (UE4) - Github repository
- [Demo project source UE5](https://github.com/jetedonner/UE5_PlayerStartDemo){:target="_blank" rel="noopener"} - Demo Source (UE5) - Github repository
-->