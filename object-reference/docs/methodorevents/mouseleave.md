# <span>MouseLeave</span> <span>Event 7</span>

[**Applies To**](../methodoreventapplies/mouseleave.md)

**Description**

If enabled, this event is reported when the user moves the mouse pointer out of an object. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 3-element vector as follows :

|-----|-----------|-------------------------------------|
|`[1]`|Object     |ref or character vector              |
|`[2]`|Event      |`'MouseLeave'` or 7                  |
|`[3]`|Object name|character vector (name of new object)|

This event is generated when the user moves the mouse pointer across the boundary and away from an object. The first element of the event message contains the name of the object that previously contained the mouse pointer and which generated the event when it crossed its boundary. The third element contains the name of the object which now contains the mouse pointer or is an empty vector if the mouse pointer is not now over a Dyalog APL/W object.
