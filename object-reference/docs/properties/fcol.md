# <span>FCol</span> <span>Property</span>

**Description**

This property defines the foreground colour(s) of an object.

For
non-graphical objects, FCol specifies a single colour. For graphical objects
with more than one constituent part, it may specify a set of background colours,
one for each part. A single colour is represented by a single number which
refers to a standard colour, or by a 3-element vector which defines a colour
explicitly in terms of its red, green and blue intensities.

If FCol is 0 (which is the default) the foreground colour is defined by your
current colour scheme for the object in question. For example, if you select red
as your MS-Windows "Button Text" colour, you will by default get red
writing on all your [Button](../objects/button.md) objects, simply by
not specifying FCol or by setting it to 0.

A negative value of FCol refers to a standard MS-Windows colour as described
below. Positive values are reserved for a possible future extension.

|FCol |Colour Element       |FCol |Colour Element         |
|-----|---------------------|-----|-----------------------|
|`0`  |Default              |`¯11`|Active Border          |
|`¯1` |Scroll Bars          |`¯12`|Inactive Border        |
|`¯2` |Desktop              |`¯13`|Application Workspace  |
|`¯3` |Active Title Bar     |`¯14`|Highlight              |
|`¯4` |Inactive Title Bar   |`¯15`|Highlighted Text       |
|`¯5` |Menu Bar             |`¯16`|Button Face            |
|`¯6` |Window Background    |`¯17`|Button Shadow          |
|`¯7` |Window Frame         |`¯18`|Disabled Text          |
|`¯8` |Menu Text            |`¯19`|Button Text            |
|`¯9` |Window Text          |`¯20`|Inactive Title Bar Text|
|`¯10`|Active Title Bar Text|`¯21`|Button Highlight       |

If instead, FCol contains a 3-element vector, it specifies the intensity of
the red, green and blue components of the colour as values in the range 0-255.
For example, (255 0 0) is red and (255 255 0) is yellow.

Note that if the colour specified by FCol would normally be rendered as a
dithered colour, it is instead converted to the nearest pure colour available on
the device. The actual colour realised also depends upon the capabilities of the
display adapter and driver, and the current Windows colour map.

For a [Button](../objects/button.md), [Combo](../objects/combo.md),
[Edit](../objects/edit.md), [Label](../objects/label.md), [List](../objects/list.md),
[Menu](../objects/menu.md) and [MenuItem](../objects/menuitem.md),
FCol refers to the colour of the **text** in the object. [Border](border.md)s
around these objects (where applicable) are drawn using the standard Windows
colour. For a [Static](../objects/static.md) object however, FCol
specifies the colour of its border.

For the [Ellipse](../objects/ellipse.md), [Poly](../objects/poly.md) and [Rect](../objects/rect.md) objects, FCol specifies the colour of
the line drawn around the perimeter of the object. If a dashed or dotted line is
used ([LStyle](lstyle.md) 1-4) the "gaps" in
the line are drawn using the colour specified by [BCol](bcol.md),
or are left undrawn if [BCol](bcol.md) is not specified.
For the [Marker](../objects/marker.md) object, FCol specifies the
colour in which the markers are drawn. For the graphics objects [Ellipse](../objects/ellipse.md),
[Poly](../objects/poly.md), [Rect](../objects/rect.md) and [Text](../objects/text.md),
FCol may be a vector of 3-element vectors specifying a set of colours for the
constituent parts of the object. For example, a [Poly](../objects/poly.md) object consisting of four polygons, may have a FCol property of four 3-element
vectors. In addition, for graphics objects, FCol is used in place of [FillCol](fillcol.md) if the latter is not specified.

**Application**

Objects: [ActiveXContainer](../objects/activexcontainer.md), [ActiveXControl](../objects/activexcontrol.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Circle](../objects/circle.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Marker](../objects/marker.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Separator](../objects/separator.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [TabBtn](../objects/tabbtn.md), [Text](../objects/text.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
