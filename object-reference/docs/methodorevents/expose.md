# <span>Expose</span> <span>Event 32</span>

[**Applies To**](../methodoreventapplies/expose.md)

**Description**

If enabled, this event is reported when part or all of the object's window is exposed to view. Under normal circumstances, APL repaints the exposed region automatically. However, if you have drawn unnamed graphical objects (which are **not** managed by APL) you should use this event to redraw them when required. Note that APL will itself repaint any **named** objects in the region before reporting the event.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|------|-----------------------------------------------|
|`[1]`|Object|ref or character vector                        |
|`[2]`|Event |`'Expose'` or 32                               |
|`[3]`|Y     |y-position of top-left corner of exposed region|
|`[4]`|X     |x-position of top-left corner of exposed region|
|`[5]`|H     |height of exposed region                       |
|`[6]`|W     |width of exposed region                        |

This event **cannot** be disabled by setting its action code to `¯1`. Similarly, setting the result of a callback function to 0 has no effect on it.
