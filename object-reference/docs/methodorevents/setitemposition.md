# <span>SetItemPosition</span> <span>Event 322</span>

**Description**

If enabled, this event is reported when the user drag-drops an item within a [ListView](../objects/listview.md) object. This operation may be disabled by returning 0 from a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 7-element vector as follows :

|-----|-------------|-----------------------------------------------------------------------------------------------------------------|
|`[1]`|Object       |ref or character vector                                                                                          |
|`[2]`|Event        |`'SetItemPosition'` or 322                                                                                       |
|`[3]`|Item number  |Integer. The index of the item.                                                                                  |
|`[4]`|Y-position   |Integer. New y-position of the item.                                                                             |
|`[5]`|X-position   |Integer. New x-position of the item.                                                                             |
|`[6]`|Button number|Integer. The mouse button used to perform the drag.                                                              |
|`[7]`|Shift State  |Integer: Sum of shift key codes (number)<br/>1 = Shift key is down<br/>2 = Ctrl key is down<br/>4 = Alt key is down|

**Application**

Objects: [ListView](../objects/listview.md)
