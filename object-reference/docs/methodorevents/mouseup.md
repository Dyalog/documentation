# <span>MouseUp</span> <span>Event 2</span>

[**Applies To**](../methodoreventapplies/mouseup.md)

**Description**

If enabled, this event is reported when the user releases one of the mouse buttons. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|-----------|---------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                    |
|`[2]`|Event      |`'MouseUp'` or 2                                                           |
|`[3]`|Y          |y-position of mouse (number)                                               |
|`[4]`|X          |x-position of mouse (number)                                               |
|`[5]`|Button     |button released (number) 1 = left button 2 = right button 4 = middle button|
|`[6]`|Shift State|sum of shift key codes (number) 1 = Shift key is down 2 = Ctrl key is down |

In a graphical object ([Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Image](../objects/image.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md) and [Rect](../objects/rect.md)), the position of the mouse is reported relative to the top-left corner of its bounding rectangle.
