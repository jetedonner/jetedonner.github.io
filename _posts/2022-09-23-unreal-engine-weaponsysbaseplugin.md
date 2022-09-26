---
layout: post
title:  "Unreal Engine - WeaponSysBasePlugin"
author: dave
date:   2022-09-23 10:02:33 +0200
categories: UnrealEngine Plugins
tags: [UnrealEngine]
---
The `UE4 WeaponSysBase Plugin` provides you with many base classes and features to quickly and easily creating and implementing your own weapon system for your Unreal Engine Game

## Description
The "Weapon System Base" provides you with some very basic and useful classes and features to create your own Weapon System for a UE4 game. You'll find base classes for WeaponTypes, Weapons, Projectiles as well as hitable character and actor base classes, a floatable healthbar and also a dissolving material that you can use to destroy an actor on death. Just derive from the base classes and adjust the settings like Damage-Factor, Projectile-Speed, Ammo Count in inventory, Ammo Count in Clip, Clip Size, Firing Sound, Impact Sound, Impact Particle Effect, etc ... I strongly recommend you to download the sample project at "" to see how the Weapon System works and is implemented in a real game project.

## Installation and Configuration
1. Download the Plugin from [GitHub - UE4_WeaponSystemPlugin](https://github.com/jetedonner/UE4_WeaponSystemPlugin) or the [EPIC Marketplace](https://www.unrealengine.com/marketplace/en-US/store) and [install it to your Engine](https://docs.unrealengine.com/5.0/en-US/working-with-plugins-in-unreal-engine/) or your new Project.

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
