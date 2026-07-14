# <span>Picture</span> <span>Property</span>

[**Applies To**](../propertyapplies/picture.md)

**Description**

The Picture property specifies a bitmap, icon, or other image for an object.

For [Button](../objects/button.md), [Form](../objects/form.md), [Group](../objects/group.md), [MDIClient](../objects/mdiclient.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [SM](../objects/sm.md), [TabBar](../objects/tabbar.md) or [ToolBar](../objects/toolbar.md), this property specifies the name of, or ref to, a [Bitmap](../objects/bitmap.md), [Icon](../objects/icon.md), or [Metafile](../objects/metafile.md) which is drawn as a *background* on the object. Other controls and graphical objects are drawn on top of this background.

When it refers to a [Metafile](../objects/metafile.md), the Picture property specifies the name of, or ref to, the [Metafile](../objects/metafile.md) to be drawn in the object. When it refers to a [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md), the value of the Picture property is a 2-element vector whose elements specify the name of, or ref to, the [Bitmap](../objects/bitmap.md), or [Icon](../objects/icon.md), and the manner in which it is displayed. This is specified as an integer as follows:

|---|---|
|0|The [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md) is drawn in        the top left corner of the object.|
|1|The [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md) is tiled (replicated) to fill the object.|
|2|The [Bitmap](../objects/bitmap.md) is scaled (up or down) to fit exactly in the object. This setting does not apply to an [Icon](../objects/icon.md) whose size is fixed.|
|3|The [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md) is drawn in the centre of the object. This is the default. Note that the centre of the [Bitmap](../objects/bitmap.md) is positioned over the centre of the object, so that you see the middle portion of a [Bitmap](../objects/bitmap.md) that is larger than the object in which it is displayed.|

For example, the following statements produce a [Form](../objects/form.md) filled with the CARS bitmap.
```apl
      'CARS' ⎕WC 'Bitmap' 'C:\WINDOWS\CARS'
      'f1' ⎕WC 'Form' ('Picture' 'CARS' 1)
```

An easy way to provide a customised pushbutton is to create a [Button](../objects/button.md) whose Picture property specifies the name of, or ref to, a [Bitmap](../objects/bitmap.md) or [Icon](../objects/icon.md), using drawmode 3 (the default). This causes the corresponding bitmap or icon to be drawn in the centre of the [Button](../objects/button.md). So long as the [Button](../objects/button.md) is larger than the bitmap or icon, its borders (which give it its 3-dimensional appearance and "pushbutton" behaviour) will be unaffected.

Note that if Picture is set on a [Button](../objects/button.md) whose [Style](style.md) is `'Radio'` or `'Check'`, the Button assumes pushbutton appearance, although its radio/check behaviour is preserved.

For an [Image](../objects/image.md) object, the Picture property specifies the name of, or ref to, a [Bitmap](../objects/bitmap.md), [Icon](../objects/icon.md) or [Metafile](../objects/metafile.md) object to be drawn, or a vector of names or refs. The [Image](../objects/image.md) is a graphical object and is drawn *on top of* the background. It does not support the drawmode options provided by the objects in which Picture specifies the background.

For the [Clipboard](../objects/clipboard.md) object, Picture is a "set-only" property that allows you to place a specified [Bitmap](../objects/bitmap.md) object into the Windows clipboard. To place a [Metafile](../objects/metafile.md) object into the clipboard, use its [Metafile](../objects/metafile.md) property.
