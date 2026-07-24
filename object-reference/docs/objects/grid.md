# <span>Grid</span> <span>Object</span>

**Purpose:** Spreadsheet object for displaying and editing data.

**Description**

The [Values](../properties/values.md) property is a matrix whose
elements are displayed in the cells of the Grid. An element (and therefore a
cell) may contain a single number, a single character, a character vector or a
character matrix.

The [CellHeights](../properties/cellheights.md) property specifies
the height of each of the rows of the spreadsheet. It may be a single value
which applies to all rows, or a vector with one element per row. The [CellWidths](../properties/cellwidths.md) property determines the width of each column of the spreadsheet. It too may be a
single value or a vector with one element per column.

The [RowTitles](../properties/rowtitles.md) property is either an
empty character vector (the default) or a vector of character vectors that
specify row titles displayed to the left of the cells in the Grid. If [RowTitles](../properties/rowtitles.md) is not specified, the Grid labels each row with its row number. The [ColTitles](../properties/coltitles.md) property is similar and is used to specify column headings. If [ColTitles](../properties/coltitles.md) is not specified, the Grid displays "standard" spreadsheet column headings
A-Z, then AA-AZ and so forth.

The [TitleHeight](../properties/titleheight.md) property specifies
height of the column headers. If this is set to 0, the column titles will not be
displayed. Similarly, the [TitleWidth](../properties/titlewidth.md) property specifies the width of the row titles and again a value of zero
disables the row titles.

The [CornerTitleBCol](../properties/align.md) property specifies the background colour of the rectangle in the top-left corner of the Grid.

The [FontObj](../properties/fontobj.md) property may be used to
specify the font to be used for the Grid as a whole, including the titles. The [CellFonts](../properties/cellfonts.md) property may be used to specify fonts for individual cells.

The [FCol](../properties/fcol.md) and [BCol](../properties/bcol.md) properties may each specify a single colour for the Grid as a whole, or may
specify a vector of colours whose elements are mapped to individual cells
through the [CellTypes](../properties/celltypes.md) property.

The [CellFonts](../properties/cellfonts.md) property is either a
character vector or a vector of character vectors that specifies the name of a
single font object to be used for all cells in the Grid, or a vector of
character vectors that specifies a set of font objects that are mapped to
individual cells through the [CellTypes](../properties/celltypes.md) property.

The [Input](../properties/input.md) property is a character vector
that specifies the name of an object which is to be associated with every cell
in the Grid, or a vector of names whose elements are mapped to individual cells
through the [CellTypes](../properties/celltypes.md) property. These
objects may be of type [Button](button.md), [ColorButton](colorbutton.md),
[Combo](combo.md), [Edit](edit.md), [Label](label.md),
[Spinner](spinner.md) or [TrackBar](trackbar.md).
In addition, the [Input](../properties/input.md) property may specify
instances of [OCXClass](ocxclass.md) objects (ActiveX
controls) and [NetType](nettype.md) objects (.NET classes).

If the [Input](../properties/input.md) property is empty (the
default) the user may browse the data in the spreadsheet but may not alter it.
Furthermore, no feedback is provided as to which is the current cell. If the [Input](../properties/input.md) property specifies the name of an object that is the child of the Grid itself,
this object *floats* from cell to cell as the user moves around the
spreadsheet, and the current cell is identified by its presence.

If the [Input](../properties/input.md) property specifies the name of an external object (that is, an object that is *not* a child of the Grid), the contents of the current cell are copied into that
object as the user moves around the spreadsheet. In addition, the current cell
is identified by a thick border. In either case, the associated object is used
to impose formatting and validation.

If the [Input](../properties/input.md) property specifies the name
of a [Label](label.md) object, that object is used to
impose formatting, but the data is protected and may not be changed. If the [Label](label.md) is a child of the Grid, it moves from cell to cell, and its characteristics ([Border](../properties/border.md),
[FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FontObj](../properties/fontobj.md)) can be used to identify the
current cell. If the [Label](label.md) is an external one,
no visual feedback is provided; even though the current cell (reflected by the [CurCell](../properties/curcell.md) property) changes as the user moves around the Grid.

If the Input property specifies one or more instances of OCXClass objects
(ActiveX controls) and [NetType](nettype.md) objects (.NET
classes), the [InputProperties](../properties/inputproperties.md) property is used to map the [Values](../properties/values.md) property
of the Grid to specific properties of the external object.

The [CellTypes](../properties/celltypes.md) property is either an
empty numeric matrix (the default) or an integer matrix of the same shape as [Values](../properties/values.md).
If specified, each element of [CellTypes](../properties/celltypes.md) determines the index into various properties, including the [FCol](../properties/fcol.md),
[BCol](../properties/bcol.md), [CellFonts](../properties/cellfonts.md) and [Input](../properties/input.md) properties, to be used for the
corresponding cell. For example, if an element in [CellTypes](../properties/celltypes.md) is 3, the 3rd element of [FCol](../properties/fcol.md) is used for the
foreground colour of the corresponding cell, the 3rd element of [BCol](../properties/bcol.md) specifies the background colour, and so forth.

The [CurCell](../properties/curcell.md) property may be used to set
or query the current cell. The current cell is the cell which the user has
picked by clicking the mouse over it or by using the cursor keys. [CurCell](../properties/curcell.md) is a 2-element vector containing the current cell's row number and column
number respectively and is `⎕IO` dependent. The [Index](../properties/index-property.md) property specifies the
row and column number of the cell in the top-left corner of the Grid. It too is `⎕IO` dependent.

The [AutoExpand](../properties/autoexpand.md) property is a
2-element Boolean vector which specifies whether (1) or not (0) new rows and
columns are added when the user presses the corresponding cursor key when at the
end of the block of cells. Its default value is (0 0).

The Grid object reports a [CellDown](../methodorevents/celldown.md) event
when the user depresses a mouse button over a cell. The event message contains
the row and column address of the cell in question which is `⎕IO` dependent. It also reports a similar [CellUp](../methodorevents/cellup.md) event when the mouse button is released and a [CellDblClick](../methodorevents/celldblclick.md) event when it is double-clicked. The number of the mouse button and the state of
the shift keys are also reported.

When the user moves to another cell, the Grid object reports a [CellMove](../methodorevents/cellmove.md) event. This simply reports the address of the new cell and may be used to take
some appropriate action when a particular cell is picked. If the user alters the
data in a cell and then attempts to move to another, the Grid reports a [CellChange](../methodorevents/cellchange.md) event. This can be used to perform validation.

Alternatively, the Grid may
report a [CellChanged](../methodorevents/cellchanged.md) event which occurs
after the [Values](../properties/values.md) property has been updated
with the new cell contents. This may be used to perform immediate recalculation.

The [AddRow](../methodorevents/addrow.md) event is generated if the current
cell is in the last row of the Grid and the user presses Cursor Down. By
default, this operation adds a new row to the Grid, but you can attach a
callback to the [AddRow](../methodorevents/addrow.md) and selectively disable
this default action if required. The [AddCol](../methodorevents/addcol.md) event works in a similar manner for columns. Although the user has no direct
means of *inserting* a row or column, your application can do this by
calling [AddRow](../methodorevents/addrow.md) or [AddCol](../methodorevents/addcol.md) as a method on the Grid object. Typically this would be done in response to the
user selecting a [MenuItem](menuitem.md) or pressing a [Button](button.md).

The [ColChange](../methodorevents/colchange.md), [RowChange](../methodorevents/rowchange.md),
[DelRow](../methodorevents/delrow.md), [DelCol](../methodorevents/delcol.md) and [Undo](../methodorevents/undo.md) methods allow your application to
perform these corresponding operations.

The Grid object maintains a buffer of the most recent 8 changes made by the
user since the [Values](../properties/values.md) property was last set
by [`⎕WC`](../../../language-reference-guide/system-functions/wc) or [`⎕WS`](../../../language-reference-guide/system-functions/ws).
Your application can restore these changes one by one by calling the [Undo](../methodorevents/undo.md) method. The [Undo](../methodorevents/undo.md) method restores the most recent
change made by the user and removes that change from the undo stack. It is
therefore not possible to "undo an undo".

The Grid supports the selection of a block or blocks of cells using the mouse
and/or the keyboard. The ability to select a range of cells is determined by the
[CellSelect](../properties/cellselect.md) property. When the user
performs a selection, the Grid generates a [GridSelect](../methodorevents/gridselect.md) event. The range of cells currently selected is given by the [SelItems](../properties/selitems.md) property.

If a block of cells has been selected, the user may delete the contents, and
cut or copy the contents of the cells to the clipboard by pressing Delete,
Shift+Delete or Ctrl+Insert respectively. These operations also generate [GridDelete](../methodorevents/griddelete.md),
[GridCut](../methodorevents/gridcut.md) and [GridCopy](../methodorevents/gridcopy.md) events which you can selectively disable using a callback function. You can
also perform these operations under program control by calling them as methods.

If more than one block of cells has been selected, these operations are
honoured only if the blocks begin and end on the same rows or begin and end on
the same columns. If so, the data placed in the clipboard is the result of
joining the blocks horizontally or vertically as appropriate.

The user may paste data from the clipboard into a Grid by pressing
Shift+Insert. Data is pasted into the currently selected block of cells, or, if
there is no selection, data is pasted starting at the current cell (`CurCell`).
The operation also generates a [GridPaste](../methodorevents/gridpaste.md) event, and, if the operation cannot proceed, a [GridPasteError](../methodorevents/gridpasteerror.md) event.

If you move the mouse pointer over any of the four edges of a selected block
of cells, the cursor changes to an arrow. You may now click and drag the border
of the selected cells with the mouse.

If you press the Ctrl key at the same
time, the contents of the selected cells are *copied* to the new location,
replacing the values in the block of cells onto which they are dropped.
Otherwise, the operation is treated as a *move* and the original block of
cells is emptied. This operation also generates a [GridDropSel](../methodorevents/griddropsel.md) event. You may only move or copy a *single* block of cells in this way.

The user may be permitted to resize the rows and/or columns of a Grid. This
is controlled by the [ResizeRows](../properties/resizerows.md) and [ResizeCols](../properties/resizecols.md) properties whose default values are 0. To allow the user to resize, set either
or both to 1. You can also specify a Boolean vector to allow specific
rows/columns to be resized while others are fixed. Two additional properties
named [ResizeRowTitles](../properties/resizerowtitles.md) and [ResizeColTitles](../properties/resizecoltitles.md) determine whether or not the user may alter the width of the row titles and the
height of the column titles.

If resizable, the cursor changes to a double-heads arrow when the user moves
the mouse pointer over the lines between the row and/or column titles. The user
may click and drag with the mouse to the desired size. The user may also
double-click. This causes the row or column to be resized to fit the data. Both
operations generate a [SetColSize](../methodorevents/setcolsize.md), or [SetRowSize](../methodorevents/setrowsize.md) event.

When you edit data in a Grid, the editing behaviour and the action of the
cursor movement keys is determined by the [InputMode](../properties/inputmode.md) and [InputModeKey](../properties/inputmodekey.md) properties.

The [GridFCol](../properties/gridfcol.md) property specifies the
colour of all the grid lines. Alternatively, the [GridLineFCol](../properties/gridlinefcol.md),
[GridLineWidth](../properties/gridlinewidth.md), [RowLineTypes](../properties/rowlinetypes.md) and [ColLineTypes](../properties/collinetypes.md) properties may
specify the appearance for individual grid lines.

The [GridBCol](../properties/gridbcol.md) property specifies the
colour used to fill the area between the end of the last column of data and the
right edge of the Grid and between the bottom row of data and the bottom edge of
the Grid.

The [RowTitleFCol](../properties/rowtitlefcol.md) and [ColTitleFCol](../properties/coltitlefcol.md) properties specify the colours to be used for the row and column titles
respectively.

The [ClipCells](../properties/clipcells.md) property determines
whether or not the Grid displays partial cells. The default is 1. If you set [ClipCells](../properties/clipcells.md) to 0, the Grid displays only complete cells and automatically fills the space
between the last visible cell and the edge of the Grid with the [GridBCol](../properties/gridbcol.md) colour.

The [CellSet](../properties/cellset.md) property is a Boolean array
that marks which cells are *set* (that is, have values) and which are empty.
This allows you to edit large numeric matrices which contain empty cells without
a severe workspace penalty.

The [HScroll](../properties/hscroll.md) and [VScroll](../properties/vscroll.md) properties specify whether or not horizontal and vertical scrollbars are
displayed. Either property may be given the value `¯3` which forces the
corresponding scrollbar to appear always. [VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) may only be set when the object is created and may not subsequently be changed.

The Grid object supports *comments* in a manner that is consistent with
the way that comments are handled by Microsoft Excel. If a comment is
associated with a cell, a small red triangle is displayed in its top right
corner. When the user rests the mouse pointer over a commented cell, the comment
is displayed as a pop-up with an arrow pointing back to the cell to which it
refers. The comment disappears when the mouse pointer is moved away. This is
referred to as *tip* behaviour. Comments may also be associated with row
and column titles.

Grid comments are managed by a set of methods, namely [AddComment](../methodorevents/addcomment.md),
[DelComment](../methodorevents/delcomment.md), [GetComment](../methodorevents/getcomment.md),
[ShowComment](../methodorevents/showcomment.md), [HideComment](../methodorevents/hidecomment.md) and [ClickComment](../methodorevents/clickcomment.md).

You may lock individual rows and columns using the [LockRows](../methodorevents/lockrows.md) and [LockColumns](../methodorevents/lockcolumns.md) methods. This facility is
however not supported in combination with hierarchical rows and/or columns which
are specified by [RowTitleDepth](../properties/rowtitledepth.md) and [ColTitleDepth](../properties/coltitledepth.md).

The Grid can display a *TreeView like* interface on the Row titles. In
this mode, the Grid automatically shows and hides row of data as the end user
expands and contracts nodes of the tree.

The [RowTreeDepth](../properties/rowtreedepth.md) property is used
to specify the depth of rows in the Grid.

The appearance of the tree is determined by the [RowTreeStyle](../properties/rowtreestyle.md) property.

User defined bitmaps can be used instead of the default Images by setting the
[RowTreeImages](../properties/rowtreeimages.md) property.

The Grid generates [Expanding](../methodorevents/expanding.md) and [Retracting](../methodorevents/retracting.md) events when the user interacts with the tree.

The [RowSetVisibleDepth](../methodorevents/rowsetvisibledepth.md) method
can be used to set the visible depth of the tree.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md)

Children: [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [Circle](../objects/circle.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [Cursor](../objects/cursor.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Icon](../objects/icon.md), [Image](../objects/image.md), [Label](../objects/label.md), [Marker](../objects/marker.md), [Menu](../objects/menu.md), [MsgBox](../objects/msgbox.md), [OCXClass](../objects/ocxclass.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Spinner](../objects/spinner.md), [Text](../objects/text.md), [Timer](../objects/timer.md), [TrackBar](../objects/trackbar.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [AlignChar](../properties/alignchar.md), [AlwaysShowBorder](../properties/alwaysshowborder.md), [AlwaysShowSelection](../properties/alwaysshowselection.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [AutoExpand](../properties/autoexpand.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [CellFonts](../properties/cellfonts.md), [CellHeights](../properties/cellheights.md), [CellSelect](../properties/cellselect.md), [CellSet](../properties/cellset.md), [CellTypes](../properties/celltypes.md), [CellWidths](../properties/cellwidths.md), [ChildList](../properties/childlist.md), [ClipCells](../properties/clipcells.md), [ColLineTypes](../properties/collinetypes.md), [ColSortImages](../properties/colsortimages.md), [ColTitleAlign](../properties/coltitlealign.md), [ColTitleBCol](../properties/coltitlebcol.md), [ColTitleDepth](../properties/coltitledepth.md), [ColTitleFCol](../properties/coltitlefcol.md), [ColTitles](../properties/coltitles.md), [Coord](../properties/coord.md), [CornerTitleBCol](../properties/cornertitlebcol.md), [CurCell](../properties/curcell.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [EnterReadOnlyCells](../properties/enterreadonlycells.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [FormatString](../properties/formatstring.md), [GridBCol](../properties/gridbcol.md), [GridFCol](../properties/gridfcol.md), [GridLineFCol](../properties/gridlinefcol.md), [GridLineWidth](../properties/gridlinewidth.md), [Handle](../properties/handle.md), [HighlightHeaders](../properties/highlightheaders.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [HScroll](../properties/hscroll.md), [Index](../properties/index-property.md), [Input](../properties/input.md), [InputMode](../properties/inputmode.md), [InputModeKey](../properties/inputmodekey.md), [InputProperties](../properties/inputproperties.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [OverflowChar](../properties/overflowchar.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [ResizeCols](../properties/resizecols.md), [ResizeColTitles](../properties/resizecoltitles.md), [ResizeRows](../properties/resizerows.md), [ResizeRowTitles](../properties/resizerowtitles.md), [RowHiddenDepth](../properties/rowhiddendepth.md), [RowLineTypes](../properties/rowlinetypes.md), [RowTitleAlign](../properties/rowtitlealign.md), [RowTitleBCol](../properties/rowtitlebcol.md), [RowTitleDepth](../properties/rowtitledepth.md), [RowTitleFCol](../properties/rowtitlefcol.md), [RowTitles](../properties/rowtitles.md), [RowTreeDepth](../properties/rowtreedepth.md), [RowTreeImages](../properties/rowtreeimages.md), [RowTreeStyle](../properties/rowtreestyle.md), [SelectionBorderWidth](../properties/selectionborderwidth.md), [SelectionColor](../properties/selectioncolor.md), [SelectionColorAlpha](../properties/selectioncoloralpha.md), [SelItems](../properties/selitems.md), [ShowInput](../properties/showinput.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [TabIndex](../properties/tabindex.md), [TextSize](../properties/textsize.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [TitleHeight](../properties/titleheight.md), [TitleWidth](../properties/titlewidth.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Values](../properties/values.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md), [XRange](../properties/xrange.md), [YRange](../properties/yrange.md)

Methods: [AddComment](../methodorevents/addcomment.md), [Animate](../methodorevents/animate.md), [CellFromPoint](../methodorevents/cellfrompoint.md), [ChooseFont](../methodorevents/choosefont.md), [ColChange](../methodorevents/colchange.md), [ColSorted](../methodorevents/colsorted.md), [DelCol](../methodorevents/delcol.md), [DelComment](../methodorevents/delcomment.md), [DelRow](../methodorevents/delrow.md), [Detach](../methodorevents/detach.md), [DuplicateColumn](../methodorevents/duplicatecolumn.md), [DuplicateRow](../methodorevents/duplicaterow.md), [GetCellRect](../methodorevents/getcellrect.md), [GetComment](../methodorevents/getcomment.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md), [LockColumns](../methodorevents/lockcolumns.md), [LockRows](../methodorevents/lockrows.md), [RowChange](../methodorevents/rowchange.md), [RowSetVisibleDepth](../methodorevents/rowsetvisibledepth.md), [SetCellSet](../methodorevents/setcellset.md), [SetCellType](../methodorevents/setcelltype.md), [Undo](../methodorevents/undo.md)

Events: [AddCol](../methodorevents/addcol.md), [AddRow](../methodorevents/addrow.md), [CellChange](../methodorevents/cellchange.md), [CellChanged](../methodorevents/cellchanged.md), [CellDblClick](../methodorevents/celldblclick.md), [CellDown](../methodorevents/celldown.md), [CellError](../methodorevents/cellerror.md), [CellMove](../methodorevents/cellmove.md), [CellOver](../methodorevents/cellover.md), [CellUp](../methodorevents/cellup.md), [ClickComment](../methodorevents/clickcomment.md), [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expanding](../methodorevents/expanding.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [GotFocus](../methodorevents/gotfocus.md), [GridCopy](../methodorevents/gridcopy.md), [GridCopyError](../methodorevents/gridcopyerror.md), [GridCut](../methodorevents/gridcut.md), [GridDelete](../methodorevents/griddelete.md), [GridDropSel](../methodorevents/griddropsel.md), [GridKeyPress](../methodorevents/gridkeypress.md), [GridPaste](../methodorevents/gridpaste.md), [GridPasteError](../methodorevents/gridpasteerror.md), [GridSelect](../methodorevents/gridselect.md), [Help](../methodorevents/help.md), [HideComment](../methodorevents/hidecomment.md), [IndexChanged](../methodorevents/indexchanged.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [Retracting](../methodorevents/retracting.md), [Select](../methodorevents/select.md), [SetColSize](../methodorevents/setcolsize.md), [SetRowSize](../methodorevents/setrowsize.md), [ShowComment](../methodorevents/showcomment.md)
