# <span>EndSplit</span> <span>Event 282</span>

**Applies To:** [Splitter](../objects/splitter.md)

**Description**

If enabled, this event is reported when the user releases the left mouse button to signify the end of a drag operation on a [Splitter](../objects/splitter.md) object.

This event is reported for information alone. You may not disable or nullify the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|------|-----------------------------|
|`[1]`|Object|ref or character vector      |
|`[2]`|Event |`'EndSplit'` or 282          |
|`[3]`|Y     |y-position of top left corner|
|`[4]`|X     |x-position of top left corner|
|`[5]`|H     |height of the Splitter       |
|`[6]`|W     |width of the Splitter        |

See also [StartSplit](./startsplit.md), [Splitting](./splitting.md).
