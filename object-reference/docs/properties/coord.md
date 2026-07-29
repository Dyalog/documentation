# <span>Coord</span> <span>Property</span>

**Description**

This property defines an object's co-ordinate system. It is a character
string with one of the following values; `'Inherit'`,
`'Prop'`, `'Pixel'`,
`'RealPixel'`, `'ScaledPixel'`, `'User'` or `'Cell'` (graphics children of a [Grid](../objects/grid.md) only).

If Coord is `'Inherit'`, the co-ordinate
system for the object is **inherited** from its parent. Note that the default
value of Coord for the system object `'.'` is `'Prop'`, so by default all objects
created by [`⎕WC`](../../../language-reference-guide/system-functions/wc) inherit `'Prop'`.

If Coord is `'Prop'`, the origin of the
object's parent is deemed to be at its top left interior corner, and the scale
along its x- and y-axes is 100. The object's position and size ([Posn](./posn.md) and [Size](./size.md) properties) are therefore specified
and reported as a percentage of the dimensions of the parent object, or, for a [Form](../objects/form.md),
of the screen.

If Coord is `'RealPixel'`, the origin of the
object's parent is deemed to be at its top left interior corner, and the scale
along its x- and y-axes is measured in physical pixel units. The object's position
and size ([Posn](posn.md) and [Size](size.md) properties) are therefore reported and set in physical pixel units. If you set
Coord on the system object to `'Pixel'`, the
value of its [Size](size.md) property gives you the
resolution of your screen. Note that pixels are numbered from 0
to (Size -1).

If Coord is `'ScaledPixel'`  the number of pixels specified for [Posn](posn.md), [Size](size.md),  and other such properties will be automatically scaled by Dyalog APL according to the user's chosen display scaling factor. So if you specify an Edit object to be 80 pixels wide and 20 pixels high, and the user's scaling factor is 150%, Dyalog will automatically draw it 120 pixels wide and 30 pixels high. Dyalog will also de-scale coordinate values reported by `⎕WG` and  event messages.

If Coord is `'Pixel'`, it is interpreted as either `'RealPixel'` or `'ScaledPixel'` according to the value of the **Dyalog_Pixel_Type** parameter, which is either ScaledPixel or RealPixel. See [Dyalog_Pixel_Type](../../../windows-installation-and-configuration-guide/configuration-parameters/dyalog-pixel-type).

**If this parameter is not specified, the default is RealPixel. So by default, when you set Coord to Pixel, it will be treated as RealPixel.**

If Coord is `'User'`, the origin and
scale of the co-ordinate system are defined by the values of the [YRange](yrange.md) and [XRange](xrange.md) properties **of the parent
object**. Each of these is a 2-element numeric vector whose elements define
the co-ordinates of top left and bottom right interior corners of the (parent)
object respectively.

Note that if Coord is `'User'` and you
change the values of [YRange](yrange.md) and/or [XRange](xrange.md) of the parent, the object (and all its siblings with Coord `'User'`)
are redrawn (and clipped) according to the new origin and scale defined for the
parent. The values of their [Posn](posn.md), [Size](size.md) and [Points](points.md) properties are unaffected.
Changing [YRange](range.md) and/or [XRange](range.md) therefore provides a convenient and efficient means to "**pan and zoom**".

The Coord property for graphic objects created as  children of a Grid may
also be set to Cell. Apart from being easier to compute, a graphic drawn using
cell coordinates will expand and contract when the grid rows and columns are
resized.

<h2 class="example">Example</h2>

This statement creates a button 10 pixels high, 20 pixels wide, and 5 pixels
down and along from the top-left corner of the parent [Form](../objects/form.md) T.
```apl
      'T.B1'⎕WC'Button' 'OK'(5 5)(10 20)('Coord' 'Pixel')
```

If you set Coord to `'RealPixel'` in the [Root](../objects/root.md) object `'.'`, then query its [Size](size.md),
you get the dimensions of the screen in pixels, that is:
```apl
      '.' ⎕WS 'Coord' 'RealPixel'
      '.' ⎕WG 'Size'
480 640
```

If you set Coord to `'ScaledPixel'` in the [Root](../objects/root.md) object `'.'`, then query its [Size](size.md),
you get the virtual resolution of the screen, that is:
```apl
      '.'⎕WS 'Coord' 'ScaledPixel'
      '.'⎕WG'Size'
1080 1920

```

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Image](../objects/image.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Menu](../objects/menu.md), [Metafile](../objects/metafile.md), [Poly](../objects/poly.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [Text](../objects/text.md), [ToolBar](../objects/toolbar.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
