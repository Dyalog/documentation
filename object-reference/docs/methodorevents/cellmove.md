# <span>CellMove</span> <span>Event 151</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

If enabled, this event is reported when the user attempts to position the cursor over a cell in a [Grid](../objects/grid.md) by clicking the left mouse button or by pressing a cursor movement key. The purpose of this event is to allow an application to perform some action prior to the user entering a cell,  to inhibit entry to a cell, or to deny exit from the current cell.

The default action is to position the user on the new cell. This action can be prevented by returning a 0 from the callback function attached to the event.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is an 8 element vector as follows :

|-----|---------------|------------------------------------|
|`[1]`|Object         |ref or character vector             |
|`[2]`|Event          |`'CellMove'` or 151                 |
|`[3]`|New cell row   |integer                             |
|`[4]`|New cell column|integer                             |
|`[5]`|Scroll flag    |0 or 1                              |
|`[6]`|Selection flag |0, 1 or 2                           |
|`[7]`|Mouse flag     |0 or 1                              |
|`[8]`|Changed flag   |0 or 1 (relates to **current** cell)|
|`[9]`|New value      |new value of **current** cell or `⍬`|

The 5<sup>th</sup> element of the event message is 1 if switching to the new cell would cause the [Grid](../objects/grid.md) to scroll.

The 6<sup>th</sup> element of the event message is 1 if the user is moving to the new cell by extending the selection. It is 2 if the user selects an entire row or column (by clicking on a title), which moves the current cell to the first one in the selection.

The 7<sup>th</sup> element of the event message is 1 if the mouse is used to switch to a new cell.

The 8<sup>th</sup> element of the event message is 1 if the user is attempting to move to the new cell from another cell in the Grid having typed in (as if to alter)  the current cell.

The 9<sup>th</sup> element of the event message is the intended new value in the current cell or `⍬` (zilde) if *Changed flag* is 0.

The CellMove event may be used to validate and refuse changes as the user navigates between cells.  See also [CellChange](cellchange.md).

An application can position the user on a particular cell in a [Grid](../objects/grid.md) by calling CellMove as a method. If so, the argument need contain only the *New cell row* and *New cell column* parameters.
