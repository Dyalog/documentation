# <span>MouseEnter</span> <span>Event 6</span>

[**Applies To**](../methodoreventapplies/mouseenter.md)

**Description**


If enabled, this event is reported when the user moves the mouse pointer into (over) an object. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 3-element vector as follows :


|-----|-----------|------------------------------------------|
|`[1]`|Object     |ref or character vector                   |
|`[2]`|Event      |`'MouseEnter'` or 6                       |
|`[3]`|Object name|character vector (name of previous object)|


This event is generated when the user moves the mouse pointer across the boundary and into an object. The first element of the event message is the name of the object over which the mouse pointer now resides. The 3rd element of the event message contains the name of the object that was previously under the mouse pointer, or is an empty vector if the mouse pointer was not previously over a Dyalog APL/W object.



