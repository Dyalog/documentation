# <span>ImageList</span> <span>Object</span>

**Purpose:** The ImageList object represents a set of bitmapped images.

**Description**

An ImageList object represents an array of bitmapped images which are used to depict items in a [ListView](listview.md) or [TreeView](treeview.md) object, or the images in a [CoolBar](coolbar.md), [Menu](menu.md), [TabControl](tabcontrol.md) or [ToolControl](toolcontrol.md).

Making an ImageList is a 2-step process. First, you create an (empty) ImageList specifying its [Size](../properties/size.md) and [Masked](../properties/masked.md) properties. The former establishes the size of each of the bitmapped images in the array. The [Masked](../properties/masked.md) property specifies whether the ImageList is to contain opaque or transparent images. Note that these properties must be established when the ImageList is created by `⎕WC` and may not subsequently be changed using `⎕WS`.

Next, you create a series of [Bitmap](bitmap.md) or [Icon](icon.md) objects as *children* of the ImageList. As you make each one, APL adds the corresponding image (or images) to the ImageList object. If the size of each of the [Bitmap](bitmap.md) or [Icon](icon.md) objects is equal to the [Size](../properties/size.md) of the ImageList itself, each child object corresponds to an image in the ImageList. However, if you add an object whose *width* is an exact multiple of the *width* of the ImageList, a corresponding number of images will be added.

For example, if the [Size](../properties/size.md) of the ImageList is 16x16 (the default) and you create a child [Bitmap](bitmap.md) of size 16x48, three images (each of size 16x16) will be added to the ImageList. This is more efficient than building the images one-by-one. In other circumstances (where the size of the [Bitmap](bitmap.md) or [Icon](icon.md) is not equal to [Size](../properties/size.md) of ImageList), the [Bitmap](bitmap.md) or [Icon](icon.md) will be scaled to fit.

Note that when making Bitmaps or Icons as children of an ImageList, it is not necessary to *name* them because they are subsequently referenced only via the [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) properties and not by name. The number of images in an ImageList is given by the read-only property, ImageCount.

The [MapCols](../properties/mapcols.md) property, which must be specified at the time you create the object, specifies whether or not bitmap colours are remapped to reflect the user's colour preferences.

An ImageList is *associated* with a [ListView](listview.md) or [TreeView](treeview.md) object by the [ImageListObj](../properties/imagelistobj.md) property. Each item in the [ListView](listview.md) or [TreeView](treeview.md) is then allocated a specific image in the ImageList by the [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) properties.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [ButtonEdit](../objects/buttonedit.md), [CoolBand](../objects/coolband.md), [CoolBar](../objects/coolbar.md), [Form](../objects/form.md), [Group](../objects/group.md), [ListView](../objects/listview.md), [OLEServer](../objects/oleserver.md), [PropertyPage](../objects/propertypage.md), [Root](../objects/root.md), [SubForm](../objects/subform.md), [TabControl](../objects/tabcontrol.md), [TCPSocket](../objects/tcpsocket.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TreeView](../objects/treeview.md)

Children: [Bitmap](../objects/bitmap.md), [Cursor](../objects/cursor.md), [Icon](../objects/icon.md), [Timer](../objects/timer.md)

Properties: [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [Handle](../properties/handle.md), [ImageCount](../properties/imagecount.md), [KeepOnClose](../properties/keeponclose.md), [MapCols](../properties/mapcols.md), [Masked](../properties/masked.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [Size](../properties/size.md), [Translate](../properties/translate.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md)
