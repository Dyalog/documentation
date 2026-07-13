# <span>MouseDown</span> <span>Event 1</span>

[**Applies To**](../methodoreventapplies/mousedown.md)

**Description**

If enabled, this event is reported when the user presses one of the mouse buttons. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|-----------|--------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                   |
|`[2]`|Event      |`'MouseDown'` or 1                                                        |
|`[3]`|Y          |y-position of mouse (number)                                              |
|`[4]`|X          |x-position of mouse (number)                                              |
|`[5]`|Button     |button pressed (number)<br/>1 = left button<br/>2 = right button<br/>4 = middle button|
|`[6]`|Shift State|sum of shift key codes (number)<br/>1 = Shift key is down<br/>2 = Ctrl key is down|

If you enable this event it is advisable that you ALSO enable [MouseUp](./mouseup.md) events. Otherwise, the slight delay in running your callback function will cause the down and up sequence to be **reversed**.

In a graphical object ([Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Image](../objects/image.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md) and [Rect](../objects/rect.md)), the position of the mouse is reported relative to the top-left corner of its bounding rectangle.
