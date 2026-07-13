# Introduction

Graphical output is performed using the following objects:

|Graphical Output                                                                                   ||
|----------------------------------------------------|-----------------------------------------------|
|[Circle](../../../object-reference/objects/circle)  |draws circles, arcs and pie charts             |
|[Ellipse](../../../object-reference/objects/ellipse)|draws ellipses                                 |
|[Marker](../../../object-reference/objects/marker)  |draws a series of polymarkers                  |
|[Poly](../../../object-reference/objects/poly)      |draws lines                                    |
|[Rect](../../../object-reference/objects/rect)      |draws rectangles                               |
|[Image](../../../object-reference/objects/image)    |displays or prints Bitmaps, Icons and Metafiles|
|[Text](../../../object-reference/objects/text)      |displays or prints graphical text              |

These graphical objects can be drawn in (that is, be the children of) a wide range of other objects including a Form, Static, Printer and Bitmap.

Additional graphical resources are provided by the following objects. These are unusual in that they are not visible except when referenced as the property of another object:

|Resource                                                                      ||
|------------------------------------------------------|------------------------|
|[Font](../../../object-reference/objects/font)        |loads a font            |
|[Bitmap](../../../object-reference/objects/bitmap)    |defines a bitmap        |
|[Icon](../../../object-reference/objects/icon)        |defines an icon         |
|[Metafile](../../../object-reference/objects/metafile)|loads a Windows Metafile|

Graphical objects are created, like any other object, using `⎕WC` and have properties that can be changed using `⎕WS` and queried using `⎕WG`. Graphical objects also generate certain events.
