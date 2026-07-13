# <span>MouseDblClick</span> <span>Event 5</span>

[**Applies To**](../methodoreventapplies/mousedblclick.md)

**Description**

If enabled, this event is reported when the user presses and then releases a mouse button twice within a short space of time. The duration of this time is set through the Windows Control Panel.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|-----------|---------------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                          |
|`[2]`|Event      |`'MouseDblClick'` or 5                                                           |
|`[3]`|Y          |y-position of mouse (number)                                                     |
|`[4]`|X          |x-position of mouse (number)                                                     |
|`[5]`|Button     |button double clicked (number)<br/>1 = left button<br/>2 = right button<br/>4 = middle button|
|`[6]`|Shift State|sum of shift key codes (number)<br/>1 = Shift key is down<br/>2 = Ctrl key is down       |

In a graphical object ([Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Image](../objects/image.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md) and [Rect](../objects/rect.md)), the position of the mouse is reported relative to the top-left corner of its bounding rectangle.

If you enable [MouseDown](./mousedown.md) and [MouseUp](./mouseup.md) events in addition to MouseDblClick events, double-clicking a mouse button will generate the following sequence of events :

1. [MouseDown](./mousedown.md)
2. [MouseUp](./mouseup.md)
3. MouseDblClick
4. [MouseUp](./mouseup.md)
