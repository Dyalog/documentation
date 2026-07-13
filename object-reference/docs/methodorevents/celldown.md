# <span>CellDown</span> <span>Event 161</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

If enabled, this event is reported when the user presses a mouse button down whilst over a cell in a [Grid](../objects/grid.md). The purpose of this event is to allow an application to display a pop-up [Menu](../objects/menu.md) or a [Locator](../objects/locator.md) over a cell in a [Grid](../objects/grid.md) or to take some other special action.

The default action is to generate a [CellMove](./cellmove.md) event which will then position the user on the new cell. This action can be prevented by returning 0 from the callback function, in which case the normally ensuing [CellMove](./cellmove.md) event will not occur.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is an 9 element vector as follows :

|-----|-----------|-----------------------------------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                                              |
|`[2]`|Event      |`'CellDown'` or 161                                                                                  |
|`[3]`|Y          |y-position of mouse (number)                                                                         |
|`[4]`|X          |x-position of mouse (number)                                                                         |
|`[5]`|Button     |button pressed (number) 1 = left button 2 =        right button 4 = middle button                    |
|`[6]`|Shift State|sum of shift key codes (number) 1 = Shift key        is down 2 = Ctrl key is down 4 = Alt key is down|
|`[7]`|Cell row   |integer                                                                                              |
|`[8]`|Cell column|integer                                                                                              |
|`[9]`|Title index|integer                                                                                              |

The y and x position of the mouse are reported relative to the top-left corner of the [Grid](../objects/grid.md).

The cell row and column are `⎕IO` dependent

If the user clicks over a row *title*, the value reported for the column is `¯1`, and the value reported for Title index is the index of that row title in [RowTitles](../properties/rowtitles.md), or, if [RowTitles](../properties/rowtitles.md) is not defined, the row number. Column titles are handled in a similar fashion.

An application **can** position the user on a particular cell in a [Grid](../objects/grid.md) by calling CellDown as a method, but it is recommended that a [CellMove](./cellmove.md) event is used instead.
