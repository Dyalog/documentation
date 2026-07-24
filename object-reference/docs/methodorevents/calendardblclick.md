# <span>CalendarDblClick</span> <span>Event 273</span>

**Description**

If enabled, this event is reported when the user double-clicks the left mouse
button over a [Calendar](../objects/calendar.md) object.

This event is reported for information alone. You may not disable or nullify
the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.

The event message reported as the result of `⎕DQ`,
or supplied as the right argument to your callback function, is a 5-element
vector as follows :

|-----|------------|--------------------------------------------------|
|`[1]`|Object      |ref or character vector                           |
|`[2]`|Event       |`'CalendarDblClick'` or 273                       |
|`[3]`|Item Number |integer                                           |
|`[4]`|Mouse Button|integer                                           |
|`[5]`|Shift State |integer. Sum of 1=shift key, 2=ctrl key, 4=Alt key|
|`[6]`|Element Type|integer                                           |

For the meaning of elements 3 and 6, see [CalendarDown](./calendardown.md).

**Application**

Objects: [Calendar](../objects/calendar.md)
