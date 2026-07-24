# <span>Size</span> <span>Property</span>

**Description**

This is a 2-element numeric vector specifying the height and width of the object.

For the [Bitmap](../objects/bitmap.md) object, Size is set and reported in pixels. Setting the Size of a [Bitmap](../objects/bitmap.md) causes it to be scaled (up or down).

For all other objects, Size is reported and set in units defined by the [Coord](coord.md) property and, if [Coord](coord.md) is `'User'`, the [XRange](xrange.md) and [YRange](yrange.md) properties of the object's parent.

For the [Root](../objects/root.md) object, if [Coord](coord.md) is `'Prop'` the value of Size is (100,100). If [Coord](coord.md) is `'Pixel'` the value of Size reports the number of pixels on the screen.

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md), the Size property defines the area within the object, and excludes its title bar, menu bar and border if these are present.

For a [Combo](../objects/combo.md) object with a "drop-down" list, the first element of Size (height) is ignored. The height of the edit field is determined by the height of the font, while the size of the list box is determined by the [Rows](rows.md) property.

Otherwise the Size property defines the total size of the object, including borders, edges etc.

When specifying Size, you can set the height or width to a default value (`⎕WC`) or leave it unchanged (`⎕WS`) by giving the corresponding element a value of `⍬`.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Icon](../objects/icon.md), [Image](../objects/image.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Metafile](../objects/metafile.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [TabButton](../objects/tabbutton.md), [TabControl](../objects/tabcontrol.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
