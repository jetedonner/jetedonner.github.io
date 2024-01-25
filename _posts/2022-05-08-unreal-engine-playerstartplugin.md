---
layout: post
title:  "Unreal Engine - PlayerStartPlugin"
author: dave
date:   2022-05-08 20:42:33 +0200
categories: [UnrealEngine, Plugins]
tags: [UnrealEngine, Plugins, Games]
---

## Introduction
![PlayerStartPlugin](../../assets/img/projects/playerstartplugin/PlayerStartPlugin_284x284_02.png){: width="284" height="284" }
_PlayerStartPlugin in the WorldSettings Editor_

The PlayStartPlugin for Unreal Engine version 4 or 5 enables you to easily setup, manage and switch between multiple PlayerStarts for your Maps / Levels in a Game. This is done via the WorldSettings in the Editor Outliner.

## Description
You can inherit your Projects WorldSettings Class from the custom PlayerStartWorldSettings class provided by this Plugin. The system then automatically loads all available PlayerStarts and you can choose your default with a ComboBox in the WorldSettings in the Editor Outliner. Please check out the following documentation on how to include and implement and use the PlayStartPlugin in your own projects.

## Install the PlayerStartPlugin
1. Fire up the Epic Game Launcher
2. Goto Marketplace and search for PlayerStartPlugin - Add it to your cart and checkout
3. After the Plugin is downloaded you can add it to your projects by opening the PluginManager in the Unreal Editor and searching for PlayerStartPlugin and activating it

## Use in your own projects

1. To get the plugins functionality you need to use the customized WorldSettings for your map / level
Open ProjectSettings and setup the custom WorldSettings PSWorldSettingsBase as default - you can also create a own subclass and use that as WorldSettings.
2. Restart the Project / Unreal Editor (Important!)
To automatically start the level from your selected PlayerStart you have to use the custom GameMode PlayerStartGameModeBase the plugin provides - or you can create a own subclass of this GameMode Class and then use that as GameMode.
3. Now you can add your PlayerStarts to the map / level and they will be available for selection in the Editor Outliner
4. After that you can set your disiered PlayerStart in the Editor Outliner like so
5. Now your all setup! You can start the game with the Play button to test the setup PlayerStart or you can discover and goto the selected PlayerStart in Edit Mode by clicking on the GoTo PlayerStart button in the Editor Outliner

### Credits and licensing
The UE PlayerStartPlugin is released under the [_Unreal® Engine End User License Agreement For Publishing_](https://www.unrealengine.com/en-US/eula/unreal?sessionInvalidated=true){:target="_blank" rel="noopener"}. Please make sure to read through the license agreement before releasing your projects using the PlayerStartPlugin. Credits and references to the author are highly appreciated - thank you!
- [Local version of the UE End User License For Publishing](/assets/docs/ue/LICENSE){:target="_blank" rel="noopener"}

## Setup without removing Player Character from Map
If you don't want to remove your Player Character from the map you can setup the plugin with the following procedure:
- Create a child class (Blueprint) of PlayerStartGameModeBase and set this class as GameMode Override in the WorldSettings in your maps Editor Outliner.
- Set your Player Character as Default Pawn Class in the Selected Game Mode Details > This way you can keep your Player Character on the map and use the functionality of the PlayerStartPlugin at the same time

## Youtube Tutorial
<div class="container-responsive-iframe">
  <iframe class="responsive-iframe" src="https://www.youtube.com/embed/AiyZcPeSFOo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Source code download
- [Plugin source code](https://github.com/jetedonner/PlayerStartPlugin){:target="_blank" rel="noopener"} - Github repository
- [Demo project source UE4](https://github.com/jetedonner/UE4_PlayerStartDemo){:target="_blank" rel="noopener"} - Demo Source (UE4)
- [Demo project source UE5](https://github.com/jetedonner/UE5_PlayerStartDemo){:target="_blank" rel="noopener"} - Demo Source (UE5)
