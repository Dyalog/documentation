# <span>CellUp</span> <span>Event 162</span>

**Description**

If enabled, this event is reported when the user **releases** a mouse button down whilst over a cell in a [Grid](../objects/grid.md). This event is a companion to the [CellDown](./celldown.md) event and could be used to hide a pop-up which was displayed in response to the [CellDown](./celldown.md). The CellUp event performs no default action and may not be disabled.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 9 element vector as follows :

|-----|-----------|------------------------------------------------|
|`[1]`|Object     |ref or character vector                         |
|`[2]`|Event      |`'CellUp'` or 162                                      |
|`[3]`|Y          |y-position of mouse (number)                                              |
|`[4]`|X          |x-position of mouse (number)                                        |
|`[5]`|Button     |button released (number)<br/>1 = left button<br/>2 = right button<br/>4 = middle button |
|`[6]`|Shift State|sum of shift key codes (number)<br/>1 = Shift key is down<br/>2 = Ctrl key is down<br/>4 = Alt key is down|
|`[7]`|Cell row   |integer                                                                              |
|`[8]`|Cell column|integer                                                                               |
|`[9]`|Title index|integer    |

The y and x position of the mouse are reported relative to the top-left corner of the [Grid](../objects/grid.md).

The cell row and column are `⎕IO` dependent.

If the user clicks over a row *title*, the value reported for the column is `¯1`, and the value reported for Title index is the index of that row title in [RowTitles](../properties/rowtitles.md), or, if [RowTitles](../properties/rowtitles.md) is not defined, the row number. Column titles are handled in a similar fashion.

An application **can** position the user on a particular cell in a [Grid](../objects/grid.md) by calling [CellDown](./celldown.md) event as a method, but it is recommended that a [CellMove](./cellmove.md) event is used instead.

**Application**

Objects: [Grid](../objects/grid.md)
