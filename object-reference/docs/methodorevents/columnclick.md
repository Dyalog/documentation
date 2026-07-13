# <span>ColumnClick</span> <span>Event 320</span>



**Applies To:** [ListView](../objects/listview.md)

**Description**


If enabled, this event is reported when the user clicks on the column heading in a [ListView](../objects/listview.md) object. This event may not be disabled or affected by a callback function in any way.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 5-element vector as follows :


|-----|-------------|----------------------------------------------------------------------------------|
|`[1]`|Object       |ref or character vector                                                           |
|`[2]`|Event        |`'ColumnClick'` or 320                                                            |
|`[3]`|Column number|Integer                                                                           |
|`[4]`|Button       |button pressed (number)<br/>1 = left button<br/>2 = right button<br/>4 = middle button |
|`[5]`|Shift State  |sum of shift key codes (number)<br/>1 = Shift key is down<br/>2 = Ctrl key is down|



