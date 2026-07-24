# <span>Font</span> <span>Object</span>

**Purpose:** Loads a font resource

**Description**

This object loads a Windows font into memory ready for use by another object.

The characteristics of the font are specified by its properties as follows :

|---|---|
|[PName](../properties/pname.md)|A character vector containing the name of the font face.       The default is `'System'` . Note that       case is ignored when you specify the name, although it will be returned       correctly by [`⎕WG`](../../../language-reference-guide/system-functions/wg) .|
|[Size](../properties/size.md)|An integer that specifies the character height of the font in pixels.|
|[Fixed](../properties/fixed.md)|A Boolean value that specifies whether the font is fixed-width (1) or       proportional (0).|
|[Italic](../properties/italic.md)|A Boolean value that specifies whether the font is italicised (1) or not       (0).|
|[Underline](../properties/underline.md)|A Boolean value that specifies whether the font is underlined (1) or not (0).|
|[Weight](../properties/weight.md)|An integer in the range 0-1000 that specifies how bold or heavy the font is (1000 = most bold).|
|[Rotate](../properties/rotate.md)|A numeric scalar that specifies the angle of rotation of the font in       radians. The angle is measure from the x-axis in a counter-clockwise       direction.|
|[CharSet](../properties/charset.md)|An integer that specifies the character encoding.|

The [Coord](../properties/coord.md) property may be set to  `'Pixel'`, `'ScaledPixel'` or `'RealPixel'` when the object is created, but [Coord](../properties/coord.md) may not subsequently be changed.

If Coord is `'Pixel'`, it is interpreted as either `'RealPixel'` or `'ScaledPixel'` according to the value of the **Dyalog_Pixel_Type** parameter, which is either ScaledPixel or RealPixel. See [Dyalog_Pixel_Type](../../../windows-installation-and-configuration-guide/configuration-parameters/dyalog-pixel-type).

**If this parameter is not specified, the default is RealPixel. So by default, when you set Coord to Pixel, it will be treated as RealPixel.**

If you are using `'ScaledPixel'`, this means that your fonts will also be scaled up automatically, as well as the sizes of the controls in which they are used.

When you ask Windows to allocate a font, you may specify as many or as few of these properties as you wish. Windows actually supplies the font that most closely matches the attributes you have specified. The matching rules it uses are complex, and may be found in the appropriate Windows documentation.

The values of the above properties after [`⎕WC`](../../../language-reference-guide/system-functions/wc) or [`⎕WS`](../../../language-reference-guide/system-functions/ws) reflect the attributes of the font which has been allocated by Windows, and not necessarily the values you have specified. Furthermore, it is possible that changing the value of one property will cause the values of others to be changed.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBand](../objects/coolband.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [Metafile](../objects/metafile.md), [OLEServer](../objects/oleserver.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TCPSocket](../objects/tcpsocket.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)

Children: [Timer](../objects/timer.md)

Properties: [CharSet](../properties/charset.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [Data](../properties/data.md), [EventList](../properties/eventlist.md), [Fixed](../properties/fixed.md), [Handle](../properties/handle.md), [Italic](../properties/italic.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PName](../properties/pname.md), [PropList](../properties/proplist.md), [Rotate](../properties/rotate.md), [Size](../properties/size.md), [Type](../properties/type.md), [Underline](../properties/underline.md), [Weight](../properties/weight.md)

Methods: [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [Select](../methodorevents/select.md)
