# Colour

Colours are specified using the FCol (foreground colour) and BCol (background colour) properties. Graphical objects have an additional FillCol (fill colour) property.

A single colour may be specified in one of two ways, either as a negative integer that refers to one of a set of standard Windows colours, or as a 3-element numeric vector. The latter specifies a colour directly in terms of its red, green and blue intensities which are measured on the scale of 0 (none) to 255 (full intensity). Standard Windows colours are:

|Colour Element                     ||Colour Element                       ||
|--------------|---------------------|--------------|-----------------------|
|`0`           |Default              |`¯11`         |Active Border          |
|`¯1`          |Scroll Bars          |`¯12`         |Inactive Border        |
|`¯2`          |Desktop              |`¯13`         |Application Workspace  |
|`¯3`          |Active Title Bar     |`¯14`         |Highlight              |
|`¯4`          |Inactive Title Bar   |`¯15`         |Highlighted Text       |
|`¯5`          |Menu Bar             |`¯16`         |Button Face            |
|`¯6`          |Window Background    |`¯17`         |Button Shadow          |
|`¯7`          |Window Frame         |`¯18`         |Disabled Text          |
|`¯8`          |Menu Text            |`¯19`         |Button Text            |
|`¯9`          |Window Text          |`¯20`         |Inactive Title Bar Text|
|`¯10`         |Active Title Bar Text|`¯21`         |Button Highlight       |

A colour specification of 0 (which is the default) selects the appropriate background or foreground colour defined by your current colour scheme for the object in question. For example, if you select yellow as your MS-Windows Menu Bar colour, you will get a yellow background in Menu and MenuItem objects as the default if BCol is not specified.

To select a colour explicitly, you specify its RGB components as a 3-element vector. For example:

|------------------------|-----------------------|
|`(255   0   0)` = red   |`(  0 255   0)` = green|
|`(255 255   0)` = yellow|`(192 192 192)` = grey |
|`(  0   0   0)` = black |`(255 255 255)` = white|

A colour specification of `⍬` (zilde) selects a transparent colour.
