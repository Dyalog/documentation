# <span>Menu</span> <span>Object</span>

**Purpose:** This is a pop-up object which allows the user to initiate an action or         to select an option using a "menu".

**Description**

For a Menu that is owned by a [MenuBar](menubar.md) or
another Menu, the [Caption](../properties/caption.md) property
determines the text string that is displayed as the "choice". The Menu
is then popped up by the user clicking on this text. It is automatically popped
down when the user chooses an option (by selecting a [MenuItem](menuitem.md))
or cancels the operation (by clicking elsewhere).

If a Menu belongs to a [Form](form.md), [SubForm](subform.md) or is a top-level object, it must be popped up by the application. This is
commonly done in response to a [MouseDown](../methodorevents/mousedown.md) event. A Menu is popped-up by calling [`⎕DQ`](../../../language-reference-guide/system-functions/dq) with only the name of the Menu as its argument. The user may therefore not
interact with any other object until a selection is made or until the operation
is cancelled. When either occurs, the Menu is automatically popped down and
de-activated, and its [`⎕DQ`](../../../language-reference-guide/system-functions/dq) terminates.

The Menu object does not have a [Size](../properties/size.md) property. Instead, its size is determined automatically by its contents.

If a Menu is owned by a [MenuBar](menubar.md) or by
another Menu, its position within its parent is also calculated automatically,
dependent on the order in which other related objects are established. The [Posn](../properties/posn.md) property may however be used to **insert** a new Menu into an existing
structure. For example, having defined three Menu objects as children of a [MenuBar](menubar.md),
you can insert a fourth one between the first and the second by specifying its [Posn](../properties/posn.md) to be 2. Note that the value of [Posn](../properties/posn.md) for the
Menus that were previously second and third will then be reset to 3 and 4
respectively.

If a Menu is a child of a [MenuBar](menubar.md) which is
itself a child of a [Form](form.md) or [SubForm](subform.md),
the Align property can be set to `'Right'`.
This is used to position a single Menu (or [MenuItem](menuitem.md))
at the rightmost end of a [MenuBar](menubar.md). This does
not apply if the [MenuBar](menubar.md) is owned by a [ToolControl](toolcontrol.md).

The [BtnPix](../properties/btnpix.md) property is used to display a
picture in a Menu. [BtnPix](../properties/btnpix.md) specifies the
names of, or refs to, three [Bitmap](bitmap.md) objects.
The first [Bitmap](bitmap.md) is displayed when the Menu
does not have the focus (normal), the second when it does have the focus
(highlighted). The third [Bitmap](bitmap.md) is displayed
when the Menu is made inactive ([Active](../properties/active.md) property is 0). If [Caption](../properties/caption.md) is also defined,
it is displayed **on top of** the bitmaps.

If the Menu is a submenu (owned by a Menu), you may set its [EdgeStyle](../properties/edgestyle.md) property to `'Plinth'`. This causes the Menu
to take on an appearance that is similar to a pushbutton and be raised when not
selected and recessed when selected. Note that to enable 3-dimensional
appearance, you must set [EdgeStyle](../properties/edgestyle.md) to
something other than `'None'` for all the
objects above the Menu in the tree.

[EdgeStyle](../properties/edgestyle.md), [BtnPix](../properties/btnpix.md),
[Font](font.md), [FCol](../properties/fcol.md) and
[BCol](../properties/bcol.md) do not affect the appearance of a Menu if
it is the direct child of a [MenuBar](menubar.md). However,
the [EdgeStyle](../properties/edgestyle.md) property **must** be set
to something other than `'None'` if you want
its children Menu and [MenuItem](menuitem.md) objects to
have a 3-dimensional appearance.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Calendar](../objects/calendar.md), [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [OLEServer](../objects/oleserver.md), [Root](../objects/root.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [SysTrayItem](../objects/systrayitem.md), [TCPSocket](../objects/tcpsocket.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Bitmap](../objects/bitmap.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [Separator](../objects/separator.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [Active](../properties/active.md), [Align](../properties/align.md), [BCol](../properties/bcol.md), [BtnPix](../properties/btnpix.md), [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [Data](../properties/data.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [ImageIndex](../properties/imageindex.md), [ImageListObj](../properties/imagelistobj.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Translate](../properties/translate.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md), [Wait](../methodorevents/wait.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [DropDown](../methodorevents/dropdown.md), [Select](../methodorevents/select.md)
