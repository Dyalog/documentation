# <span>GestureTwoFingerTap</span> <span>Event 496</span>

[**Applies To**](../methodoreventapplies/gesturetwofingertap.md)

**Description**

This event is reported when the user taps two fingers at the same time on an object

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 5-element vector as follows :

|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'GestureTwoFingerTap'` or 496|
|`[3]`|Flags|integer which reports the state of the gesture|
|`[4]`|Location|2-element integer vector containing the y and x-position respectively of the point midway between the two fingers. These are reported in pixel coordinates relative to the origin (top-left corner) of the object reporting the event..|
|`[5]`|Distance|2-element integer vector containing the high and low parts (words) of a 64-bit integer that indicates the distance between the two fingers.|

The Flags parameter [3] which reports the state of the Gesture, is always an integer with the value 5 (*GF_BEGIN+GF_END*).

|----------|-----|-----------------------|
|Name      |Value|Description            |
|`GF_BEGIN`|1    |A gesture is starting. |
|`GF_END`  |4    |A gesture has finished.|

The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).

Returning zero from the callback disables any default handling by the operating system.
