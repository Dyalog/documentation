# <span>MDIClient</span> <span>Object</span>

**Purpose:** Implements Multiple Document Interface (MDI) behaviour.

**Description**

The multiple-document interface (MDI) is a document-oriented interface that is commonly used by word-processors, spreadsheets and other applications that deal with *documents*. An MDI application allows the user to display multiple documents at the same time, with each document displayed in its own window.

The MDIClient object is a container object that effectively specifies the client area within the parent [Form](form.md) in which the [SubForm](subform.md) are displayed. The MDIClient object also imposes special MDI behaviour which is quite different from that where a [SubForm](subform.md) is simply the child of another [Form](form.md).

By default, the MDIClient occupies the entire client area within its parent [Form](form.md). This is the area within the [Form](form.md) that is not occupied by [CoolBar](coolbar.md)s, [MenuBar](menubar.md)s, [ToolBar](toolbar.md)s, [ToolControl](toolcontrol.md)s, [TabBar](tabbar.md)s, [TabControls](tabcontrol.md) and [StatusBar](statusbar.md)s. In most applications it is therefore not necessary to specify the position and size of the MDIClient object, although you may do so if you want to reserve additional space in the parent [Form](form.md) for other objects.

Each of the four sides of an MDIClient object is automatically *attached* to the corresponding side of its parent [Form](form.md) and maintains its position when the parent [Form](form.md) is resized. This means that a default MDIClient always occupies the entire client area of its parent [Form](form.md), regardless of how the parent is resized.

The appearance of the MDIClient may be changed using its [Border](../properties/border.md), [BCol](../properties/bcol.md) and [Picture](../properties/picture.md) properties. The [EdgeStyle](../properties/edgestyle.md) property has no direct effect and is provided only to pass on a value to its child [Form](form.md)s.

The [MDIActive](../properties/mdiactive.md) and [MDIActiveObject](../properties/mdiactiveobject.md) properties contain the name of and a ref to the [SubForm](subform.md) that currently has the focus. You may set these properties as well as query them.

You can call methods which cause the MDIClient to organise its child [SubForm](subform.md)s in some way. These methods are as follows:

|---------------------------------------------|----------------------------------------------------------------------------------------------------------|
|[MDICascade](../methodorevents/mdicascade.md)|Causes the MDIClient to organise its child Forms in an overlapping manner.                                |
|[MDITile](../methodorevents/mditile.md)      |Causes the MDIClient to arrange its child Forms as a row or column.                                       |
|[MDIArrange](../methodorevents/mdiarrange.md)|Causes the MDIClient to arrange the icons associated with any minimised child Forms in an orderly fashion.|

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [SubForm](../objects/subform.md)

Children: [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [SubForm](../objects/subform.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [Attach](../properties/attach.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [Handle](../properties/handle.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [IconObj](../properties/iconobj.md), [KeepOnClose](../properties/keeponclose.md), [MDIActive](../properties/mdiactive.md), [MDIActiveObject](../properties/mdiactiveobject.md), [MethodList](../properties/methodlist.md), [Picture](../properties/picture.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [Size](../properties/size.md), [TabIndex](../properties/tabindex.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [XRange](../properties/xrange.md), [YRange](../properties/yrange.md)

Methods: [Animate](../methodorevents/animate.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md), [MDIArrange](../methodorevents/mdiarrange.md), [MDICascade](../methodorevents/mdicascade.md), [MDITile](../methodorevents/mditile.md)

Events: [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
