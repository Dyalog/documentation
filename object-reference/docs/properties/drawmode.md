# <span>DrawMode</span> <span>Property</span>

**Applies To:** [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md)

**Description**

The DrawMode property provides direct control over the low-level drawing operation performed by graphical objects.

The DrawMode property specifies the current foreground mix mode. The Windows GDI uses the foreground mix mode to combine pens and interiors of filled objects with the colours already on the screen. The foreground mix mode defines how colours from the brush or pen and the colours in the existing image are to be combined.

DrawMode affects every drawing operation performed by Dyalog APL and not just the initial drawing operation when the object is created. Many of the drawing modes are additive (the result depends not just on what is being drawn, but on what is already there) and the effects may therefore vary. For this reason, DrawMode should normally be used only with un-named graphical objects.

You could use DrawMode to move or animate graphical objects in circumstances where the standard Dyalog APL behaviour was not ideal.

DrawMode is an integer with one of the following values:

|Value|Name            |Resulting Pixel Colour                                                                     |
|-----|----------------|-------------------------------------------------------------------------------------------|
|1    |`R2_BLACK`      |Pixel is always 0.                                                                         |
|2    |`R2_NOTMERGEPEN`|Pixel is the inverse of the R2_MERGEPEN colour.                                            |
|3    |`R2_MASKNOTPEN` |Pixel is a combination of the colours common to both the screen and the inverse of the pen.|
|4    |`R2_NOTCOPYPEN` |Pixel is the inverse of the pen colour.                                                    |
|5    |`R2_MASKPENNOT` |Pixel is a combination of the colours common to both the pen and the inverse of the screen.|
|6    |`R2_NOT`        |Pixel is the inverse of the screen colour.                                                 |
|7    |`R2_XORPEN`     |Pixel is a combination of the colours in the pen and in the screen, but not in both.       |
|8    |`R2_NOTMASKPEN` |Pixel is the inverse of the R2_MASKPEN colour.                                             |
|9    |`R2_MASKPEN`    |Pixel is a combination of the colours common to both the pen and the screen.               |
|10   |`R2_NOTXORPEN`  |Pixel is the inverse of the R2_XORPEN colour.                                              |
|11   |`R2_NOP`        |Pixel remains unchanged.                                                                   |
|12   |`R2_MERGENOTPEN`|Pixel is a combination of the screen colour and the inverse of the pen colour.             |
|13   |`R2_COPYPEN`    |Pixel is the pen colour.                                                                   |
|14   |`R2_MERGEPENNOT`|Pixel is a combination of the pen colour and the inverse of the screen colour.             |
|15   |`R2_MERGEPEN`   |Pixel is a combination of the pen colour and the screen colour.                            |
|16   |`R2_WHITE`      |Pixel is always 1.                                                                         |
