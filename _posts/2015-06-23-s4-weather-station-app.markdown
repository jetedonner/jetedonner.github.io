---
layout: post
title:  "S4 Weather Station App"
author: dave
date:   2015-06-23 20:42:33 +0200
categories: Projects Utility Android
tags: [Games, macOS]
---

## Introduction
![S4WeatherStation](../..//assets/img/projects/s4weatherstation/S4-weather-station-head_20140308_small.jpg){: width="1593" height="703" }
_Main view of S4 Weather Station App (Camera view / Weather Info Overlay)_


## Description
The S4 Weather Station app makes use of the ambient sensors of the Samsung Galaxy S4 or Galaxy Note 3 and lets you take a snapshot with the camera of the smart devic together with an overlay of the ambient weather condition information. You can share the picture via Google+, Twitter and Facebook or just save it on the smart device. This version also has a basic gallery function. As of now the Samsung Galaxy S4 and Samsung Galaxy Note 3 are the only two smart devices supporting all of the features of S4 Weather Station. Please give me feedback to <kim@kimhauser.ch> about the app and devices you got it running on. Thank you!

## Features
Sensor values and conversions
- Temperatur: Celsius, Fahrenheit, Kelvin, Rankine, Reamur
- Pressure:
  - Air pressure: mBar / hPa, psi, torr, atm
  - Ground pressure: kg/cm², lb/in²
- Humidity:
  - Relative (sensor)
  - Absolute: g/m³, gr/ft³
- Light: lux, foot candle

## Images
![S4WeatherStation](../..//assets/img/projects/s4weatherstation/S4ws_2014-03-06-080655_640X360.jpg){: width="640" height="360" }
_(Lake of Zürich near Richterswil, shot from within train, April 2014)_

![S4WeatherStation](../..//assets/img/projects/s4weatherstation/S4ws_2014-03-09-205531_640x360.jpg){: width="640" height="360" }
_Zürich by night, May 2014_

![S4WeatherStation](../..//assets/img/projects/s4weatherstation/S4ws_2014-03-19-205732_640x360.png){: width="640" height="360" }
_Again Zürich by night, May 2014_

![S4WeatherStation](../..//assets/img/projects/s4weatherstation/S4ws_2014-03-27-190818_640x360.png){: width="640" height="360" }
_Overview of Zürich from University towards Üetliberg, May 2014_

<!--
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


## Setup without removing Player Character from Map
If you don't want to remove your Player Character from the map you can setup the plugin with the following procedure:
- Create a child class (Blueprint) of PlayerStartGameModeBase and set this class as GameMode Override in the WorldSettings in your maps Editor Outliner.
- Set your Player Character as Default Pawn Class in the Selected Game Mode Details > This way you can keep your Player Character on the map and use the functionality of the PlayerStartPlugin at the same time


## Youtube Tutorial
<iframe width="560" height="315" src="https://www.youtube.com/embed/sWwcMc0H-MU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
-->
## Download Google Play Store
[![Android App](../..//assets/img/Get_it_on_Google_play_180x62px.png){: width="180" height="62" }](https://play.google.com/store/apps/details?id=ch.kimhauser.android.s4weatherstation)

<!--
## Source code download
- <https://github.com/jetedonner/PlayerStartPlugin> - Plugin Source
- <https://github.com/jetedonner/UE4_PlayerStartDemo> - Demo Source (UE4)
- <https://github.com/jetedonner/UE5_PlayerStartDemo> - Demo Source (UE5)


`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
-->