# <span>SubForm</span> <span>Object</span>

**Purpose:** This object represents a window that is owned by and constrained         within another [Form](form.md) or an [MDIClient](mdiclient.md) .

**Description**

If the SubForm is the child of a [Form](form.md), it is
by default a simple featureless window that occupies the entire client area
(excluding standard [ToolBar](toolbar.md)s, [StatusBar](statusbar.md)s
and [TabBar](tabbar.md)s) of its parent.

The properties
that control its appearance, including [Sizeable](../properties/sizeable.md),
[Moveable](../properties/moveable.md), [SysMenu](../properties/sysmenu.md),
[Border](../properties/border.md), [MaxButton](../properties/maxbutton.md) and [MinButton](../properties/minbutton.md), all default to 0. The [EdgeStyle](../properties/edgestyle.md) property also defaults to `'None'`, so the
background of the SubForm defaults to the Window Background colour.

If the SubForm is the child of an [MDIClient](mdiclient.md),
its default appearance is the same as for a top-level [Form](form.md).
By default its size is 25% of its parent client area and it is positioned in the
centre of its parent object.

The [Posn](../properties/posn.md) property specifies the location of
the **internal** top-left corner of the SubForm relative to its parent. If
the SubForm has a title bar, border, or a 3-dimensional shadow, you must allow
sufficient space for these components. Similarly, the [Size](../properties/size.md) property specifies the internal size of the SubForm excluding the title bar and
border.

A SubForm is constrained so that it cannot be moved outside its parent. In
all other respects it behaves in a similar manner to a [Form](form.md) object. See [Form](form.md) object and the descriptions of
its properties for further details.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Group](../objects/group.md), [MDIClient](../objects/mdiclient.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [TabControl](../objects/tabcontrol.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [Cursor](../objects/cursor.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Icon](../objects/icon.md), [Image](../objects/image.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [Metafile](../objects/metafile.md), [MsgBox](../objects/msgbox.md), [OCXClass](../objects/ocxclass.md), [Poly](../objects/poly.md), [ProgressBar](../objects/progressbar.md), [PropertySheet](../objects/propertysheet.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabControl](../objects/tabcontrol.md), [TCPSocket](../objects/tcpsocket.md), [Text](../objects/text.md), [Timer](../objects/timer.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dockable](../properties/dockable.md), [DockChildren](../properties/dockchildren.md), [Docked](../properties/docked.md), [DockShowCaption](../properties/dockshowcaption.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [HelpButton](../properties/helpbutton.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [HScroll](../properties/hscroll.md), [IconObj](../properties/iconobj.md), [KeepOnClose](../properties/keeponclose.md), [MaxButton](../properties/maxbutton.md), [MethodList](../properties/methodlist.md), [MinButton](../properties/minbutton.md), [Moveable](../properties/moveable.md), [OnTop](../properties/ontop.md), [PageSize](../properties/pagesize.md), [Picture](../properties/picture.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Range](../properties/range.md), [Redraw](../properties/redraw.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [State](../properties/state.md), [Step](../properties/step.md), [SysMenu](../properties/sysmenu.md), [TabIndex](../properties/tabindex.md), [TabObj](../properties/tabobj.md), [TextSize](../properties/textsize.md), [Thumb](../properties/thumb.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [UndocksToRoot](../properties/undockstoroot.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md), [XRange](../properties/xrange.md), [YRange](../properties/yrange.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DockAccept](../methodorevents/dockaccept.md), [DockCancel](../methodorevents/dockcancel.md), [DockEnd](../methodorevents/dockend.md), [DockMove](../methodorevents/dockmove.md), [DockRequest](../methodorevents/dockrequest.md), [DockStart](../methodorevents/dockstart.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [FrameContextMenu](../methodorevents/framecontextmenu.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [HScroll](../methodorevents/hscroll.md), [HThumbDrag](../methodorevents/hthumbdrag.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MDIActivate](../methodorevents/mdiactivate.md), [MDIDeactivate](../methodorevents/mdideactivate.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md), [StateChange](../methodorevents/statechange.md), [VScroll](../methodorevents/vscroll.md), [VThumbDrag](../methodorevents/vthumbdrag.md)
