# Introduction

Graphical output is performed using the following objects:

|Graphical Output                                                                                   ||
|----------------------------------------------------|-----------------------------------------------|
|[Circle](../../object-reference/objects/circle.md)  |draws circles, arcs and pie charts             |
|[Ellipse](../../object-reference/objects/ellipse.md)|draws ellipses                                 |
|[Marker](../../object-reference/objects/marker.md)  |draws a series of polymarkers                  |
|[Poly](../../object-reference/objects/poly.md)      |draws lines                                    |
|[Rect](../../object-reference/objects/rect.md)      |draws rectangles                               |
|[Image](../../object-reference/objects/image.md)    |displays or prints Bitmaps, Icons and Metafiles|
|[Text](../../object-reference/objects/text.md)      |displays or prints graphical text              |

These graphical objects can be drawn in (that is, be the children of) a wide range of other objects including a Form, Static, Printer and Bitmap.

Additional graphical resources are provided by the following objects. These are unusual in that they are not visible except when referenced as the property of another object:

|Resource                                                                      ||
|------------------------------------------------------|------------------------|
|[Font](../../object-reference/objects/font.md)        |loads a font            |
|[Bitmap](../../object-reference/objects/bitmap.md)    |defines a bitmap        |
|[Icon](../../object-reference/objects/icon.md)        |defines an icon         |
|[Metafile](../../object-reference/objects/metafile.md)|loads a Windows Metafile|

Graphical objects are created, like any other object, using `⎕WC` and have properties that can be changed using `⎕WS` and queried using `⎕WG`. Graphical objects also generate certain events.
