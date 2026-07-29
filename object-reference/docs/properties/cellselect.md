# <span>CellSelect</span> <span>Property</span>

**Description**

The [Grid](../objects/grid.md) supports the selection of a contiguous block of cells by the user, using the mouse and/or the keyboard. The ability to select a range of cells is determined by the CellSelect property.

CellSelect may be a character vector or a vector of character vectors comprising the following:

|----------------|---------------------------|
|`'Rows'`        |User may select an entire row by clicking on a row title and may select multiple rows by dragging the mouse over contiguous row titles.            |
|`'MultiRows'`   |Same as `'Rows'` , but user may additionally select several non-contiguous rows and blocks of rows using the Ctrl key.     |
|`'Columns'`     |User may select an entire column by clicking on a column title and may select multiple columns by dragging the mouse over contiguous column titles.|
|`'MultiColumns'`|Same as `'Columns'` , but user may additionally select several non-contiguous columns and blocks of columns using the Ctrl key.    |
|`'Partial'`     |User may select any rectangular block of cells by either dragging the mouse or using Shift+cursor keys.      |
|`'MultiPartial'`|Same as `'Partial'` , but user may additionally select multiple rectangular blocks of cells using the Ctrl key.                                    |
|`'Whole'`       |User may select the entire [Grid](../objects/grid.md) by clicking in the space to the left of the column titles and above the row titles.          |
|`'Any'`         |Same as (`'Rows'` `'Columns'` `'Partial'` `'Whole'`). This is the default.                     |
|`'Multi'`       |Same as (`'MultiRows'` `'MultiColumns'` `'MultiPartial'` `'Whole'`).                                 |
|`'None'`        |User may not select any cells in the [Grid](../objects/grid.md) .         |

For example, the following expression would allow the user to select only whole rows and columns:
```apl
      gridname ⎕WS 'CellSelect' ('Rows' 'Columns')
```

Setting CellSelect to (`'Rows' 'Columns' 'Whole' 'Partial'`) is equivalent to setting it to `'Any'`.

When the user performs a selection, the [Grid](../objects/grid.md) generates a [GridSelect](../methodorevents/gridselect.md) event.

The range of cells currently selected is given by the [SelItems](selitems.md) property. You can obtain the current selection by querying this property with [`⎕WG`](../../../language-reference-guide/system-functions/wg) and you can set it with [`⎕WS`](../../../language-reference-guide/system-functions/ws).

Note that the user may delete the contents of the selected range, or cut and copy them to the clipboard by pressing Delete, Shift+Delete or Ctrl+Insert respectively. The user may also replace the current selection with the contents of the clipboard by pressing Shift+Insert.  These operations generate [GridDelete](../methodorevents/griddelete.md), [GridCut](../methodorevents/gridcut.md), [GridCopy](../methodorevents/gridcopy.md) and [GridPaste](../methodorevents/gridpaste.md) events which you may disable (by setting the event action code to `¯1` or to which you may attach a callback function.

If more than one block of cells has been selected, these operations are honoured only if the blocks begin and end on the same rows or begin and end on the same columns. If so, the data placed in the clipboard is the result of joining the blocks horizontally or vertically as appropriate.

You can also invoke these events as methods. This allows you to attach these actions to MenuItems and Buttons. For example, the following expression could be used to implement Cut as a MenuItem:
```apl
      name ⎕WC 'MenuItem' 'Cu&t'('Event' 'Select' '⍎gridname.GridCut')
```

In addition to the ability to copy blocks of cells through the clipboard, the user may also drag a block of cells from one part of the [Grid](../objects/grid.md) to another.

When the user places the mouse pointer over any of the four edges of a selected block of cells, the cursor changes from a cross to an arrow pointer. The user may now drag the border of the selected block to a new location. If the Ctrl key is pressed at the same time, the contents of the selected cells are *copied* to the new location. If not, the operation is a *move* and the original block of cells is cleared (emptied). In either case, the contents of the original block replace the contents of the target block (marked by the dragging rectangle) and the target block becomes selected. You may only move or copy a *single* block of cells in this way.

These operations generate a [GridDropSel](../methodorevents/griddropsel.md) event. You may prevent the user from moving and copying blocks of cells by disabling this event (by setting its event action code to `¯1`) or you may control these operations selectively with a callback function. Note that although the operation of *inserting* cells (using Ctrl+Shift) has not been implemented, you may provide this facility yourself with the information provided by the event message.

You may also move or copy a block of cells (which need not necessarily be selected) under program control by calling [GridDropSel](../methodorevents/griddropsel.md) event as a method.

**Application**

Objects: [Grid](../objects/grid.md)
