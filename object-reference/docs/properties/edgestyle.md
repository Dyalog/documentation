# <span>EdgeStyle</span> <span>Property</span>

[**Applies To**](../propertyapplies/edgestyle.md)

**Description**

This property is used to give a 3-dimensional appearance to screen objects.

This is achieved by drawing the object with a grey or white background colour
and by drawing a border around it using various combinations of black, white and
dark grey lines. Note that this border is drawn *outside* a control but *inside* a [Form](../objects/form.md) or [SubForm](../objects/subform.md).

**Note that EdgeStyle is not honoured for objects which have a natural
		built-in 3-dimensional appearance.**

The value of the EdgeStyle property is a character vector chosen from the
following :

|---|---|
|`'None'`|Object is drawn with no 3-dimensional effects and the EdgeStyle       properties of its children are ignored (treated as `None` ).|
|`'Plinth'`|Object is drawn with a light shadow along its top and left edges and a       dark shadow along its bottom and right edges. This gives the illusion of a       raised effect.|
|`'Recess'`|Object is drawn with a dark shadow along its top and left edges and a       light shadow along its bottom and right edges. This gives the illusion of       a sunken effect.|
|`'Groove'`|Object is drawn with a border that has the appearance of a groove.|
|`'Ridge'`|Object is drawn with a border that has the appearance of a ridge.|
|`'Shadow'`|Object is drawn with a dark border line along its top and left edges.|
|`'Default'`|Object itself is drawn with no 3-dimensional border, but the values of       the EdgeStyle properties of its children are observed.|
|`'Dialog'`|Used in conjunction with ( `'Border' 2` ),       this gives a Form the appearance of a standard 3-dimensional dialog box.       This setting applies **only** to a [Form](../objects/form.md) or a [SubForm](../objects/subform.md)|

For the [Root](../objects/root.md) object, the EdgeStyle property
may be `'None'` or `'Default'`.
If EdgeStyle is `'None'`, screen objects are
drawn without 3-dimensional effects of any kind and the value of their EdgeStyle
property is ignored. If EdgeStyle is `'Default'`,
all controls are drawn using their default EdgeStyle properties.

Note that [MsgBox](../objects/msgbox.md), [FileBox](../objects/filebox.md) and the set-up dialog box associated with the [Printer](../objects/printer.md) object are all drawn with 3-dimensional effects regardless of the value of
EdgeStyle on [Root](../objects/root.md). These objects do not have
their own EdgeStyle properties.

If you set EdgeStyle to `'None'` on the [Root](../objects/root.md) object, all your objects will (by default) be drawn without 3-dimensional
effects.
