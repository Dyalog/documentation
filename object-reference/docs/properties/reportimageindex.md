# <span>ReportImageIndex</span> <span>Property</span>

**Description**

The ReportImageIndex property is an integer scalar or matrix  that specifies the images to be displayed alongside each item  in a [ListView](../objects/listview.md) object in Report View.

If it is a matrix, its first column specifies the indices of the icons to be displayed against the [Items](items.md) of the [ListView](../objects/listview.md), overriding the icons specified by [ImageIndex](imageindex.md), and its subsequent columns specify the indices of the icons to be displayed against the elements of [ReportInfo](reportinfo.md).

That is, if non-scalar, `(⍴ReportImageIndex)←→(0 1+⍴ReportInfo)`

Each  element of ReportImageIndex specifies an index into the [ImageList](../objects/imagelist.md) object specified by the [ImageListObj](imagelistobj.md) property.

**Application**

Objects: [ListView](../objects/listview.md)
