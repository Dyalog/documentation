# <span>StartSplit</span> <span>Event 280</span>

**Applies To:** [Splitter](../objects/splitter.md)

**Description**

If enabled, this event is reported when the user depresses the left mouse button over a [Splitter](../objects/splitter.md) object to signify the beginning of a drag operation.

This event is reported for information alone. You may not disable or nullify the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'StartSplit'` or 280  |

See also [EndSplit](./endsplit.md), [Splitting](./splitting.md).
