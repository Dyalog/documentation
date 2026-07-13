# <span>BCol</span> <span>Property</span>

[**Applies To**](../propertyapplies/bcol.md)

**Description**


This property defines the background colour(s) of an object.



For objects with
more than one constituent part, it may specify a set of background colours, one
for each part. A single colour is represented by a single number which refers to
a standard colour, or by a 3-element vector which defines a colour explicitly in
terms of its red, green and blue intensities.


If BCol is set to 0 (which is the default) the background colour is defined by your
current colour scheme for the object in question. For example, if you select
yellow as your MS-Windows "Menu Bar" colour, you will by default get a
yellow background in [Menu](../objects/menu.md) and [MenuItem](../objects/menuitem.md) objects, simply by not specifying BCol or by setting it to 0.


If BCol is set to `⍬` (Zilde), Dyalog APL will never paint the background of the object. If therefore the object is overlaid by another window and then exposed, its background will not be redrawn and it will simply contain whatever was previously shown on that area of the screen.



A negative value of BCol refers to a standard MS-Windows colour as described
below. Positive values are reserved for a possible future extension.


|BCol |Colour Element       |BCol |Colour Element         |
|-----|---------------------|-----|-----------------------|
|`0`  |Default              |`¯11`|Active Border          |
|`¯1` |Scroll Bars          |`¯12`|Inactive Border        |
|`¯2` |Desktop              |`¯13`|Application Workspace  |
|`¯3` |Active Title Bar     |`¯14`|Highlight              |
|`¯4` |Inactive Title Bar   |`¯15`|Highlighted Text       |
|`¯5` |Menu Bar             |`¯16`|Button Face            |
|`¯6` |Window Background    |`¯17`|Button Shadow          |
|`¯7` |Window Frame         |`¯18`|Disabled Text          |
|`¯8` |Menu Text            |`¯19`|Button Text            |
|`¯9` |Window Text          |`¯20`|Inactive Title Bar Text|
|`¯10`|Active Title Bar Text|`¯21`|Button Highlight       |



If BCol contains a 3-element vector, it specifies the intensity of the red,
green and blue components of the colour as values in the range 0-255. For
example, (255 0 0) is red and (255 255 0) is yellow.


Note that the colour realised depends upon the capabilities of the display
adapter and driver, and the current Windows colour map.


For a [Button](../objects/button.md), BCol is only effective if the
[Style](style.md) is `'Radio'` or `'Check'` and is ignored if the [Style](style.md) is `'Push'`.


It is recommended that you only use **pure** background colours in [Combo](../objects/combo.md) and [Edit](../objects/edit.md) objects. This is because the text
written in these objects cannot itself have a dithered background.


For the [Ellipse](../objects/ellipse.md), [Poly](../objects/poly.md) and [Rect](../objects/rect.md) objects, BCol specifies the background
colour of the line drawn around the perimeter of the object and is effective
only when a non-solid line ([LStyle](lstyle.md) 1-4) is
used. It also specifies the colour used to fill the spaces between hatch lines
if a hatch fill ([FStyle](fstyle.md) 1-6) is used.


