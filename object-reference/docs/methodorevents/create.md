# <span>Create</span> <span>Event 34</span>

**Description**

If enabled, this event is reported *after* an object has been created.
You may not nullify or modify the event with a 0-returning callback, nor may you
generate the event using `⎕NQ`, or call it
as a method.

The event message reported as the result of `⎕DQ`,
or supplied as the right argument to your callback function, is a 3-element
vector as follows :

|-----|------|------------------------------------------------------------------------------------|
|`[1]`|Object|ref or character vector                                                             |
|`[2]`|Event |`'Create'` or 34                                                                    |
|`[3]`|Flag  |1 = object was created by `⎕WC` 0 = object was created by `)LOAD` , `)COPY` or `⎕OR`|

This event also applies to the Session object `⎕SE` and may be used to fire a start-up function (in the `⎕SE` namespace) when APL initialises.

**Application**

Objects: [ActiveXContainer](../objects/activexcontainer.md), [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [Clipboard](../objects/clipboard.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Cursor](../objects/cursor.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Icon](../objects/icon.md), [Image](../objects/image.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [MenuItem](../objects/menuitem.md), [Metafile](../objects/metafile.md), [MsgBox](../objects/msgbox.md), [OLEServer](../objects/oleserver.md), [Poly](../objects/poly.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Separator](../objects/separator.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [SysTrayItem](../objects/systrayitem.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [TabButton](../objects/tabbutton.md), [TabControl](../objects/tabcontrol.md), [TCPSocket](../objects/tcpsocket.md), [Text](../objects/text.md), [Timer](../objects/timer.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
