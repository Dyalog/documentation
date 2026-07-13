# <span>FillCol</span> <span>Property</span>



**Applies To:** [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md)

**Description**


This property defines the fill colour in a graphics object.



If [FStyle](fstyle.md) is 0 (solid fill) FillCol defines the colour with which the object is filled. If [FStyle](fstyle.md) is in the range 1-6 (pattern fill) it defines the colour of the lines that make up the pattern. The areas between the lines are filled using the colour specified by [BCol](bcol.md), or are left undrawn (transparent) if [BCol](bcol.md) is not specified. If [FStyle](fstyle.md) contains the name of a [Bitmap](../objects/bitmap.md) object, the value of FillCol is ignored.


A single colour is represented by a single number which refers to a standard colour, or by a 3-element vector which defines a colour explicitly in terms of its red, green and blue intensities. A negative value of FillCol refers to a standard MS-Windows colour as described below. Positive values are reserved for a possible future extension.


|FillCol|Colour Element       |FillCol|Colour Element         |
|-------|---------------------|-------|-----------------------|
|`0`    |Default              |`¯11`  |Active Border          |
|`¯1`   |Scroll Bars          |`¯12`  |Inactive Border        |
|`¯2`   |Desktop              |`¯13`  |Application Workspace  |
|`¯3`   |Active Title Bar     |`¯14`  |Highlight              |
|`¯4`   |Inactive Title Bar   |`¯15`  |Highlighted Text       |
|`¯5`   |Menu Bar             |`¯16`  |Button Face            |
|`¯6`   |Window Background    |`¯17`  |Button Shadow          |
|`¯7`   |Window Frame         |`¯18`  |Disabled Text          |
|`¯8`   |Menu Text            |`¯19`  |Button Text            |
|`¯9`   |Window Text          |`¯20`  |Inactive Title Bar Text|
|`¯10`  |Active Title Bar Text|`¯21`  |Button Highlight       |


If instead, FillCol contains a 3-element vector, it 
specifies the intensity of the red, green and blue components of the colour as 
values in the range 0-255. For example, (255 0 0) is red and (255 255 0) is 
yellow. Note that the colour realised depends upon the capabilities of the 
display adapter and driver, and the current Windows colour map.


FillCol may also be a vector of 3-element vectors specifying a set of colours for the constituent parts of the object. For example, a [Poly](../objects/poly.md) object consisting of four polygons, may have a FillCol property of four 3-element vectors.


