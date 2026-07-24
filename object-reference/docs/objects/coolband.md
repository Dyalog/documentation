# <span>CoolBand</span> <span>Object</span>

**Purpose:** The CoolBand object represents an area in a CoolBar that contains a         child window.

**Description**

The CoolBand object is a container object that represents a band in a [CoolBar](coolbar.md).

A CoolBand can have any combination of a gripper bar, a bitmap, a text label,
and a single child object.

A CoolBand may not contain more than one child object, but that child object
may itself be a container such as a [ToolControl](toolcontrol.md) or a [SubForm](subform.md).

The [Caption](../properties/caption.md) property specifies a text
string to be displayed to the left of the CoolBand. The colour of the text is
specified by the [FCol](../properties/fcol.md) property.

The [ImageIndex](../properties/imageindex.md) property specifies an
optional picture which is to be displayed alongside the [Caption](../properties/caption.md).
If specified, [ImageIndex](../properties/imageindex.md) is an index
into an [ImageList](imagelist.md) whose name is referenced
via the [ImageListObj](../properties/imagelistobj.md) property of the
parent [CoolBar](coolbar.md).

The background in a CoolBand may be specified using its [BCol](../properties/bcol.md) or [Picture](../properties/picture.md) properties. Although typically,
the visible background area is small, it is visible through a [transparent](../properties/transparent.md) [ToolControl](toolcontrol.md).

The [ChildEdge](../properties/childedge.md) property specifies
whether or not the CoolBand leaves space above and below its child window.

The [GripperMode](../properties/grippermode.md) property specifies
whether or not the CoolBand has a gripper bar which is used to reposition and
resize the CoolBand within its parent [CoolBar](coolbar.md).
[GripperMode](../properties/grippermode.md) may be '`Always'`(the default), `'Never'` or `'Auto'`.

The position of a Cool Band within a [CoolBar](coolbar.md) is determined by its [Index](../properties/index-property.md) and [NewLine](../properties/newline.md) properties, and by the position and size of preceding CoolBand objects in the
same [CoolBar](coolbar.md). For a CoolBand, [Posn](../properties/posn.md) is a read-only property that reports its position but [Posn](../properties/posn.md) may not be used to set it.

The [Index](../properties/index-property.md) property specifies the position
of a CoolBand within its parent [CoolBar](coolbar.md),
relative to other CoolBands and is `⎕IO` dependent. Initially, the value of [Index](../properties/index-property.md) is
determined by the order in which the CoolBands are created. You may re-order the
CoolBands within a [CoolBar](coolbar.md), under program
control, by changing [Index](../properties/index-property.md) with `⎕WS`.

The [NewLine](../properties/newline.md) property specifies whether
or not the CoolBand occupies the same row as an existing CoolBand, or is
displayed on a new line within its [CoolBar](coolbar.md) parent. The value of [NewLine](../properties/newline.md) in the first
CoolBand in a [CoolBar](coolbar.md) is always 1, even if
you specify it to be 0. You may move a CoolBand to the previous or next row by
changing its [NewLine](../properties/newline.md) property (using `⎕WS`) from 1 to 0, or from 0 to 1 respectively.

The 2<sup>nd</sup> element of the [Size](../properties/size.md) property determines the width of the CoolBand; the value of the 1<sup>st</sup> element is read-only.

[Size](../properties/size.md) may **only** be specified by `⎕WC`.
However, when you create a CoolBand, it will automatically occupy all the
available space in the current row, to the right of any preceding CoolBands.
Only when you create *another* CoolBand in the *same* row, will the [Size](../properties/size.md) of the first CoolBand be honoured. The rightmost CoolBand will always extend to
the right edge of the CoolBar, whatever its [Size](../properties/size.md).

If you create two or more CoolBands in the same row and you do not specify [Size](../properties/size.md),
the first CoolBand will be maximised, and the others minimised.

When the user drags a CoolBand to a different row its [Index](../properties/index-property.md) and [NewLine](../properties/newline.md) properties may change, as may
the [Index](../properties/index-property.md) and [NewLine](../properties/newline.md) properties of any another CoolBand that is affected by the operation.

If you wish to remember the user's chosen layout when your application
terminates, you must store the values of [Index](../properties/index-property.md), [Size](../properties/size.md) and [NewLine](../properties/newline.md) for each of the CoolBands. When your application is next started, you must
re-create the CoolBands with the same values of these properties.

**Application**

Parents: [CoolBar](../objects/coolbar.md)

Children: [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [Clipboard](../objects/clipboard.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [Cursor](../objects/cursor.md), [Edit](../objects/edit.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Icon](../objects/icon.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Menu](../objects/menu.md), [Metafile](../objects/metafile.md), [MsgBox](../objects/msgbox.md), [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabControl](../objects/tabcontrol.md), [TCPSocket](../objects/tcpsocket.md), [Timer](../objects/timer.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)

Properties: [BCol](../properties/bcol.md), [Caption](../properties/caption.md), [ChildEdge](../properties/childedge.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [Dockable](../properties/dockable.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [GripperMode](../properties/grippermode.md), [ImageIndex](../properties/imageindex.md), [Index](../properties/index-property.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [NewLine](../properties/newline.md), [Picture](../properties/picture.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Size](../properties/size.md), [Type](../properties/type.md), [UndocksToRoot](../properties/undockstoroot.md), [Visible](../properties/visible.md)

Methods: [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [DockAccept](../methodorevents/dockaccept.md), [DockCancel](../methodorevents/dockcancel.md), [DockEnd](../methodorevents/dockend.md), [DockMove](../methodorevents/dockmove.md), [DockRequest](../methodorevents/dockrequest.md), [DockStart](../methodorevents/dockstart.md)
