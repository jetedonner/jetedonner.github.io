---
layout: post
title:  "CSS ONLY Floating Menu Button"
author: dave
date:   2023-02-21 20:15:05 +0200
categories: [Projects, HTML]
tags: [Projects, Snippets, HTML]
published: true
---

# CSS Code Snippets
Some small and simple code snippets from me.

## CSS (only) Floating Menu Button
This small snippet shows a CSS ONLY animated floating menu button. 

![Codepen of CSSOnly Floating Menu Button](../../assets/img/snippets/CSSOnly-Floating-Menu-Button-Codepen_2023-04-14.png){: width="333" height="462" }

## Example
You can build and run this yourselfs, just copy the following code to its appropriate file and try it yourselfs. Happy coding!

### CSS File
Save i.e. as "main.css"
```css
.menu-div {
  position: absolute;
  bottom: 20px;
  right: 20px;
  display: inline-grid;
}

.menu-div .icon-bar:nth-of-type(2) {
  top: 2px;
}

.menu-div .icon-bar:nth-of-type(3) {
  top: 4px;
}

.menu-div .icon-bar {
  position: relative;
  transition: all 500ms ease-in-out;
  width: 20px;
  display: block;
  height: 2px;
  background-color: white;
}

.menu-div:hover .icon-bar:nth-of-type(1) {
  transform: translateY(6px) rotate(45deg);
}

.menu-div:hover .icon-bar:nth-of-type(2) {
  background-color: transparent;
}

.menu-div:hover .icon-bar:nth-of-type(3) {
  transform: translateY(-6px) rotate(-45deg);
}

.menu-div .menu-toggle {
  transition: all 500ms ease-in-out;
}

.menu-div:hover .menu-toggle {
  transform: rotate(-180deg);
}

.menu-toggle {
  width: 50px;
  height: 50px;
  padding-left: 10px;
  border-radius: 50%;
  z-index: 100;
  background-color: lightblue;
  border: 0px;
}

.menu-item {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-left: 4px;
  transition: all 750ms ease-in-out;
  transition-property: opacity, bottom;
  position: absolute;
  opacity: 0;
  bottom: -5px;
  z-index: 99;
  border: 0px;
  color: white;
  padding-top: 0px;
  padding-left: 6px;
}

.menu-div:hover .menu-item:nth-of-type(1) {
  bottom: 55px;
}

.menu-div:hover .menu-item:nth-of-type(2) {
  bottom: 100px;
}

.menu-div:hover .menu-item:nth-of-type(3) {
  bottom: 145px;
}

.menu-div:hover .menu-item:nth-of-type(4) {
  bottom: 190px;
}

.menu-div:hover .menu-item:nth-of-type(5) {
  bottom: 235px;
}

.menu-div:hover .menu-item {
  opacity: 1;
}

.menu-div .icon-bar {
  margin-left: 5px;
  position: relative;
}

button {
  position: relative;
}

button:is(.menu-item):active:after {
  content: attr(title);
  padding: 10px;
  border: 0px;
  border-radius: 7px;
  top: 50%;
  right: 50%;
  background: #00000077;
  color: #ffffff;
  position: fixed;
  transform: translate(50%, -50%);
}
```

### HTML File
Save i.e. as index.html (and don't forget to include the above CSS file)
```html
<!DOCTYPE html>
<html>
	<head>
		<link href="main.css" rel="stylesheet" />
	</head>
	<body>
		<h2 style="font-family: Helvetica">CSS-ONLY Animated Floating Menu Button</h2>
		<small style="font-family: Helvetica">This small snippet shows you how to implement a animated floating menu button - only using pure CSS and HTML. No libraries - what so ever needed. The menu button is fully responsive and also work on mobile devices like tablets and phones.</small>
		<div class="menu-div" id="divMenu" style="">
		  <button type="button" class="menu-item" style="background-color: lightgreen;" title="Fifth menu item!">
		    !
		  </button>
		  <button type="button" class="menu-item" style="background-color: lightsalmon;" title="Fourth menu item!">
		    E
		  </button>
		  <button type="button" class="menu-item" style="background-color: lightsteelblue;" title="Third menu item!">
		    V
		  </button>
		  <button type="button" class="menu-item" style="background-color: lightseagreen;" title="Second menu item!">
		    A
		  </button>
		  <button type="button" class="menu-item" style="background-color: lightcoral;" title="First menu item!">
		    D
		  </button>
		  <button type="button" class="menu-toggle" data-target=".menu-div">
		    <span class="icon-bar" style="top: -4px;"></span>
		    <span class="icon-bar" style="top: 0px;"></span>
		    <span class="icon-bar" style="top: 4px;"></span>
		  </button>
		</div>
	</body>
</html>
```

The menu expands on hover and the burger icon of the menu button animates to an "X". No libraries are needed. JavaScript is needed only for setting the "active" state / CSS-Class to the menu, beside that no JS is needed and only pure CSS is used to render and animate this nice little menu.

Use and ammend the code as you like. The source is provided "AS IS" no warranty. The source is free for all your projects and plans whether it's' free or commercial. A reference to the author is highly appreciated.

<iframe width="420" height="315" src="https://www.youtube.com/embed/WS7bLdwmnsM" frameborder="0" allowfullscreen></iframe>

- [_Codepen.io article / SourceCode_](https://codepen.io/kimdhauser/pen/PodNZeQ){:target="_blank" rel="noopener"}
- [_Youtube Demo Video_](https://youtu.be/WS7bLdwmnsM){:target="_blank" rel="noopener"}