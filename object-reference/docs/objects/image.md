# <span>Image</span> <span>Object</span>

**Purpose:** Positions bitmaps and icons within an object.

**Description**

The [Points](../properties/points.md) property specifies the co-ordinates of one or more points at which the specified graphical objects are to be drawn.

The [Picture](../properties/picture.md) property specifies the name(s) of [Bitmap](bitmap.md), [Icon](icon.md) or [Metafile](metafile.md) object(s) that are to be drawn. It may be a simple character vector or a vector of vectors.

To draw a single graphic picture, the [Picture](../properties/picture.md) property is a simple character vector specifying the name of a [Bitmap](bitmap.md), [Icon](icon.md) or [Metafile](metafile.md) object. [Points](../properties/points.md) is either a 2-element vector or a 1-row, 2-column matrix whose elements specify the y-coordinate and x-coordinate respectively at which the object is to be drawn.

To draw the same picture at several different positions, the [Picture](../properties/picture.md) property is a simple character vector specifying the name of the [Bitmap](bitmap.md), [Icon](icon.md) or [Metafile](metafile.md) object. [Points](../properties/points.md) is either a 2-column matrix of y-coordinates and x-coordinates, or a nested vector whose first element contains the y-coordinates and whose second element contains the x-coordinates.

To draw several different pictures, the [Picture](../properties/picture.md) property is a vector of character vectors specifying the names of several [Bitmap](bitmap.md), [Icon](icon.md) and/or [Metafile](metafile.md) objects. [Points](../properties/points.md) is a 2-column matrix or 2-element nested vector as described above.

Setting the [EdgeStyle](../properties/edgestyle.md) property causes the picture to be surrounded by the appropriate border. For example, setting [EdgeStyle](../properties/edgestyle.md) to `'Plinth'` produces a button-like appearance.

Setting the [Size](../properties/size.md) property causes the picture to be scaled to fit within the specified rectangle. It is only necessary to specify [Size](../properties/size.md) when an Image is used to draw a [Metafile](metafile.md) object. For a [Bitmap](bitmap.md) or [Icon](icon.md), [Size](../properties/size.md) defaults to the size of the object being drawn.

The [Dragable](../properties/dragable.md) property specifies whether or not the Image can be dragged and dropped using the mouse.

<h2 class="example">Examples</h2>

First make a [Form](form.md)
```apl
      'F' ⎕WC 'Form'
```

Then make two [Bitmap](bitmap.md)s :
```apl
      'YES' ⎕WC 'Bitmap' 'C:\WDYALOG\WS\YES'
      'NO'  ⎕WC 'Bitmap' 'C:\WDYALOG\WS\NO'
```

Display the "YES" [Bitmap](bitmap.md) at (20,10)
```apl
      'F.I' ⎕WC 'Image' (20 10)('Picture' 'YES')
```

Display the "YES" [Bitmap](bitmap.md) at (20,10) and (20,50)
```apl
      'F.I' ⎕WC 'Image' (20(10 50))('Picture' 'YES')
```

Display the "YES" [Bitmap](bitmap.md) at (20,10) and the "NO" [Bitmap](bitmap.md) at (20,50)
```apl
      'F.I' ⎕WC'Image'(20(10 50))('Picture' 'YES' 'NO')
```

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Bitmap](../objects/bitmap.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Metafile](../objects/metafile.md), [Printer](../objects/printer.md), [PropertyPage](../objects/propertypage.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [AutoConf](../properties/autoconf.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [OnTop](../properties/ontop.md), [Picture](../properties/picture.md), [Points](../properties/points.md), [PropList](../properties/proplist.md), [Size](../properties/size.md), [Type](../properties/type.md), [Visible](../properties/visible.md)

Methods: [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [Help](../methodorevents/help.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [Select](../methodorevents/select.md)
