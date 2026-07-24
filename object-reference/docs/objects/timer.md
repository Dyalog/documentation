# <span>Timer</span> <span>Object</span>

**Purpose:** To generate an action at regular intervals.

**Description**

The Timer object is used to generate an event at regular intervals. It can be used to produce animation and to implement "repeaters" such as spin buttons.

The [Interval](../properties/interval.md) property specifies how often the Timer generates events and is defined in milliseconds. Its default value is 1000.

The [Active](../properties/active.md) property determines whether or not the Timer generates events and can be used to switch the Timer off and on as required.

The [FireOnce](../properties/fireonce.md) property may be used to implement a once-off Timer event and has the value 0, 1 or 2.

Note that if you create a Timer object whose [Timer](../methodorevents/timer.md) event generates an error (for example by attaching it to a non-existent callback) it may be very difficult or even impossible to type into the Session, because the error will be displayed over and over again. Care is therefore recommended.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [Clipboard](../objects/clipboard.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Cursor](../objects/cursor.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Icon](../objects/icon.md), [Image](../objects/image.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [MenuItem](../objects/menuitem.md), [Metafile](../objects/metafile.md), [MsgBox](../objects/msgbox.md), [NetClient](../objects/netclient.md), [NetType](../objects/nettype.md), [OLEClient](../objects/oleclient.md), [OLEServer](../objects/oleserver.md), [Poly](../objects/poly.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [Separator](../objects/separator.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [SysTrayItem](../objects/systrayitem.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [TabButton](../objects/tabbutton.md), [TabControl](../objects/tabcontrol.md), [TCPSocket](../objects/tcpsocket.md), [Text](../objects/text.md), [Timer](../objects/timer.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)

Children: [Timer](../objects/timer.md)

Properties: [Active](../properties/active.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FireOnce](../properties/fireonce.md), [Interval](../properties/interval.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md), [Wait](../methodorevents/wait.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [Timer](../methodorevents/timer.md)
