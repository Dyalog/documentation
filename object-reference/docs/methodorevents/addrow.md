# <span>AddRow</span> <span>Event 152</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported by the [Grid](../objects/grid.md) object if the user presses the Cursor Down key, and the current cell ([CurCell](../properties/curcell.md))
is within the last row on the [Grid](../objects/grid.md). The default
action is to append a new row to the contents of the [Grid](../objects/grid.md).
If you attach a callback function to this event and have it return a value of 0,
a new row will not be appended to the [Grid](../objects/grid.md).


The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq),
or supplied as the right argument to your callback function, is a 3 element
vector as follows :


|-----|----------|-------------------------------|
|`[1]`|Object    |ref or character vector        |
|`[2]`|Event     |`'AddRow'` or 152              |
|`[3]`|Row number|number of the new row (integer)|


An application may insert a new row into a [Grid](../objects/grid.md) by calling AddRow as a method. The argument is a 1 to 7-element array as follows:


|-----|------------|----------------------------------------|
|`[1]`|Row number  |integer                                 |
|`[2]`|Row title   |character vector or matrix              |
|`[3]`|Row height  |integer                                 |
|`[4]`|Undo flag   |0 or 1                                  |
|`[5]`|Resize flag |0 or 1                                  |
|`[6]`|Title colour|negative integer or 3-element RGB vector|
|`[7]`|Line type   |integer                                 |





If you are using default row titles, *Row title* will be ignored and the
rows will be re-labelled with default titles. If you *have* set [RowTitles](../properties/rowtitles.md),
the title you specify will be inserted. If you omit *Row title*, a blank
title will be inserted.


Similarly, if you have not previously set [CellHeights](../properties/cellheights.md),
[ResizeRows](../properties/resizerows.md), [RowTitleFCol](../properties/rowtitlefcol.md) or [RowLineTypes](../properties/rowlinetypes.md), or if you have given
them a scalar value, the corresponding parameter will be ignored. However, if
you have specified [CellHeights](../properties/cellheights.md), [ResizeRows](../properties/resizerows.md),
[RowTitleFCol](../properties/rowtitlefcol.md) or [RowLineTypes](../properties/rowlinetypes.md) to be a *vector*, the number you specify in the corresponding parameter
will be inserted into the appropriate property vector. If you omit *Row height*,
it will be assigned a default value; new values for the other properties default
to 0.


*Undo flag* (default 1) specifies whether or not the addition of the new
row may subsequently be undone by an [Undo](./undo.md) event.


To insert a new row before the first one, you must specify the *Row number* as 1 (or 0 if `⎕IO` is 0). To add a new row
after the last one, you may specify any number greater than the current number
of rows. The data in the new row will be set to 0 if the [Values](../properties/values.md) property is numeric, or to an empty character vector otherwise.


