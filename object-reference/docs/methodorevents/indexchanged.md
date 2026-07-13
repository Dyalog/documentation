# <span>IndexChanged</span> <span>Event 210</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported when the value of the Index property of a Grid has changed as a result of user interaction. The event is reported *after* the Grid has been scrolled. You may not modify or nullify the operation with a 0-return callback and you may not call IndexChanged as a method or generate this event using `⎕NQ`. To cause a Grid to scroll, use `⎕WS` to set its Index property.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'IndexChanged` or 210 |
|`[3]`|Row   |Integer.               |
|`[4]`|Column|Integer.               |



