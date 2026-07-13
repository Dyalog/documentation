# <span>ImageListObj</span> <span>Property</span>

[**Applies To**](../propertyapplies/imagelistobj.md)

**Description**

The ImageListObj property is a simple character vector or a ref, or a vector of character vectors or refs that specifies [ImageList](../objects/imagelist.md) objects that are associated with an object.

For a [ComboEx](../objects/comboex.md) or [TreeView](../objects/treeview.md) object, the ImageListObj property specifies the name of, or ref to, a single [ImageList](../objects/imagelist.md) object that contains a set of images to be displayed alongside its Items. The image(s) displayed by a particular item in its normal (unselected) and selected states are specified by the corresponding element of the [ImageIndex](imageindex.md) and [SelImageIndex](selimageindex.md) properties respectively.

For [CoolBar](../objects/coolbar.md), [Menu](../objects/menu.md), and [TabControl](../objects/tabcontrol.md) objects, the ImageListObj property specifies the name of, or ref to, a single [ImageList](../objects/imagelist.md) object that contains a set of images for its [CoolBand](../objects/coolband.md), [MenuItem](../objects/menuitem.md), and [TabButton](../objects/tabbutton.md) children respectively.

For a [ToolControl](../objects/toolcontrol.md), ImageListObj may specify up to three [ImageList](../objects/imagelist.md) objects that correspond to the three different states, normal, highlighted (hot) and inactive, of its [ToolButton](../objects/toolbutton.md) children.

In all these cases, individual images are mapped to the child objects by their [ImageIndex](imageindex.md) property.

For a [ListView](../objects/listview.md) either one or two [ImageList](../objects/imagelist.md) objects may be specified. The first [ImageList](../objects/imagelist.md) contains the *large icon* set of images. the second contains the *small icon* set. The set that is used is determined by the value of the [View](view.md) property. The mapping between the set of images in the [ImageList](../objects/imagelist.md) and items in the object is determined by the [ImageIndex](imageindex.md) property.
