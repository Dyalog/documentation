# <span>Form</span> <span>Object</span>

**Purpose:** This is a top-level window used to contain other objects (controls).

**Description**

The [Posn](../properties/posn.md) property specifies the location of
the **internal** top-left corner of the window relative to the top-left
corner of the screen. If the window has a title bar and/or border, you must
allow sufficient space for them. Similarly, the [Size](../properties/size.md) property specifies the internal size of the window excluding the title bar and
border. The default for [Size](../properties/size.md) is 50% of the
screen height and width. The default for [Posn](../properties/posn.md) places the Form in the middle of the screen.

Normally, a Form has a title bar, a system menu box, a border and maximise
and minimise buttons. To disable the System Menu box, set [SysMenu](../properties/sysmenu.md) to 0. To disable one or both of the maximise/minimise buttons, set [MaxButton](../properties/maxbutton.md) and/or [MinButton](../properties/minbutton.md) to 0.

The [HelpButton](../properties/helpbutton.md) property specifies
that a Question (?) button appears in the title bar of the Form. However, this
does not apply if the Form has a maximise or minimise button which both take
precedence. The user may obtain help by clicking on the Question (?) button and
then on a control in the Form. It is up to you to provide the help by responding
to the [Help](../methodorevents/help.md) event on the control.

By default, a Form may be moved and resized using the mouse. These actions
are achieved by dragging on the title bar and border respectively. It follows
that a Form that is [Moveable ](../properties/moveable.md)**must** have a title bar, and one that is [Sizeable](../properties/sizeable.md) **must** have a border, regardless of the value of other properties. Also, if
you specify any of [SysMenu](../properties/sysmenu.md), [MaxButton](../properties/maxbutton.md) or [MinButton](../properties/minbutton.md), the window must have a
title bar in which to place these controls. A title bar itself requires a
border. To obtain a window without a title bar, you must therefore set [Moveable](../properties/moveable.md),
[SysMenu](../properties/sysmenu.md), [MaxButton](../properties/maxbutton.md) and [MinButton](../properties/minbutton.md) to 0. Note that setting [Caption](../properties/caption.md) does **not** force a title bar on the window.

If [Sizeable](../properties/sizeable.md) is 1, the window will have
a double-line border, regardless of the values of other properties. If [Sizeable](../properties/sizeable.md) is 0, and any one or more of [Moveable](../properties/moveable.md), [SysMenu](../properties/sysmenu.md),
[MaxButton](../properties/maxbutton.md), [MinButton](../properties/minbutton.md) or [Border](../properties/border.md) is 1, the window will have a
1-pixel border. Only if all these properties are 0 will the window be
borderless. To obtain a dialog box that may only be moved or closed, set [Border](../properties/border.md) to 2.

Note that the default value for [Caption](../properties/caption.md) is an empty character vector which results in a blank title.

To obtain a standard dialog box with 3-dimensional appearance, create a Form
with [Border](../properties/border.md) set to 2 and [EdgeStyle](../properties/edgestyle.md) set to `'Dialog'`, for example:
```apl
  'F' ⎕WC 'Form' 'Dialog Box' ('EdgeStyle' 'Dialog')('Border' 2)
```

The [State](../properties/state.md) property has the value 0 if the
window is currently displayed in its "normal" state, 1 if it is
currently displayed as an icon, and 2 if it is currently maximised and displayed
full-screen. This property does not just report the current state, but can be
used to set the state under program control.

The [VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) properties determine whether or not a Form has a vertical and horizontal
scrollbar respectively. These properties are set to `¯1`to obtain a scrollbar. Their default value is 0 (no scrollbar). [VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) may only be set when the object is created and may not subsequently be changed. The [Range](../properties/range.md) property is a 2-element vector that specifies the maximum value for the vertical
and horizontal scrollbars respectively. The [PageSize](../properties/pagesize.md) property is a 2-element vector that specifies the sizes of the thumbs in each scrollbar. The [Step](../properties/step.md) property is a 4-element vector that specifies the sizes of the small and large
change. Its first two elements refer to the vertical scrollbar, elements 3 and 4
refer to the horizontal scrollbar. The [Thumb](../properties/thumb.md) property is a 2-element vector that both reports and sets the position of the
thumb in the vertical and horizontal scrollbars respectively. When the user
attempts to move the thumb in one of the scrollbars, the Form generates a [VScroll](../methodorevents/vscroll.md) or [HScroll](../methodorevents/hscroll.md) event.

[VScroll](../methodorevents/vscroll.md) and [HScroll](../methodorevents/hscroll.md) cannot be changed using [`⎕WS`](../../../language-reference-guide/system-functions/ws).
However, you can make a scrollbar disappear by setting the corresponding element
of [Range](../properties/range.md) to 1, thus allowing you to
dynamically switch the scrollbar off and on. Note however that doing so will
change the size of the Form.

Setting the [FontObj](../properties/fontobj.md) property on a Form
does not affect the text in its title bar. However, the value of [FontObj](../properties/fontobj.md) will (unless over-ridden) be inherited by all of the objects within the Form.

The background of the Form may be coloured using [BCol](../properties/bcol.md).
The default value for [BCol](../properties/bcol.md) is the Windows
Button Face colour unless [EdgeStyle](../properties/edgestyle.md) is
set to `'None'` or `'Default'` in which case it is the Windows background colour. Alternatively, the background
of a Form can be defined using a [Bitmap](bitmap.md) or [Metafile](metafile.md) object whose name is defined by the [Picture](../properties/picture.md) property. A [Metafile](metafile.md) is automatically scaled
to fit the Form. A [Bitmap](bitmap.md) can be tiled *or* scaled. See [Picture](../properties/picture.md) property for details.

The [OnTop](../properties/ontop.md) property is either 0 or 1. If it
is 0, the Form assumes its normal position within the stack of windows on the
screen and is only brought to the front when it receives the input focus. If [OnTop](../properties/ontop.md) is set to 1, the Form is always brought to the front even when it doesn't have
the focus. If more than one Form has [OnTop](../properties/ontop.md) set to 1, the stacking order of this set of Forms is defined by the order in
which they were created.

A Form can be created as a child of another Form. If so, it has the following
characteristics:

- A child Form always appears on top of its parent Form (although it is not
    constrained by it)
- When you minimize a parent Form, its child Forms disappear.
- Making the parent Form invisible or inactive has no effect on a Child
    Form.

Note that the [Posn](../properties/posn.md) and [Size](../properties/size.md) properties of a child Form are expressed in screen coordinates and are not given
relative to its parent.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [OLEClient](../objects/oleclient.md), [OLEServer](../objects/oleserver.md), [Root](../objects/root.md), [SubForm](../objects/subform.md), [TCPSocket](../objects/tcpsocket.md)

Children: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [Clipboard](../objects/clipboard.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [Cursor](../objects/cursor.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Icon](../objects/icon.md), [Image](../objects/image.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [Metafile](../objects/metafile.md), [MsgBox](../objects/msgbox.md), [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md), [OLEServer](../objects/oleserver.md), [Poly](../objects/poly.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertySheet](../objects/propertysheet.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [SysTrayItem](../objects/systrayitem.md), [TabBar](../objects/tabbar.md), [TabControl](../objects/tabcontrol.md), [TCPSocket](../objects/tcpsocket.md), [Text](../objects/text.md), [Timer](../objects/timer.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [AlphaBlend](../properties/alphablend.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dockable](../properties/dockable.md), [DockChildren](../properties/dockchildren.md), [Docked](../properties/docked.md), [DockShowCaption](../properties/dockshowcaption.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [HelpButton](../properties/helpbutton.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [HScroll](../properties/hscroll.md), [IconObj](../properties/iconobj.md), [KeepOnClose](../properties/keeponclose.md), [MaskCol](../properties/maskcol.md), [MaxButton](../properties/maxbutton.md), [MethodList](../properties/methodlist.md), [MinButton](../properties/minbutton.md), [Moveable](../properties/moveable.md), [OKButton](../properties/okbutton.md), [OnTop](../properties/ontop.md), [PageSize](../properties/pagesize.md), [Picture](../properties/picture.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Range](../properties/range.md), [Redraw](../properties/redraw.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [State](../properties/state.md), [Step](../properties/step.md), [SysMenu](../properties/sysmenu.md), [TabIndex](../properties/tabindex.md), [TextSize](../properties/textsize.md), [Thumb](../properties/thumb.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [UndocksToRoot](../properties/undockstoroot.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md), [XRange](../properties/xrange.md), [YRange](../properties/yrange.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md), [Wait](../methodorevents/wait.md)

Events: [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DockAccept](../methodorevents/dockaccept.md), [DockCancel](../methodorevents/dockcancel.md), [DockEnd](../methodorevents/dockend.md), [DockMove](../methodorevents/dockmove.md), [DockRequest](../methodorevents/dockrequest.md), [DockStart](../methodorevents/dockstart.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [DyalogCustomMessage1](../methodorevents/dyalogcustommessage1.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [FrameContextMenu](../methodorevents/framecontextmenu.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [HScroll](../methodorevents/hscroll.md), [HThumbDrag](../methodorevents/hthumbdrag.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md), [StateChange](../methodorevents/statechange.md), [VScroll](../methodorevents/vscroll.md), [VThumbDrag](../methodorevents/vthumbdrag.md)
