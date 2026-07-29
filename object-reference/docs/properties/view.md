# <span>View</span> <span>Property</span>

**Description**

The View property specifies how the items in a [ListView](../objects/listview.md) object are displayed. It is a character vector which may have one of the following values; `'Icon'` (the default), `'SmallIcon'`, `'List'` or `'Report'`.

When View is `'Icon'` or `'SmallIcon'`, the items are arranged *row-wise* with large or small icons as appropriate. When View is set to `'List'`, the items are arranged *column-wise* using small icons. When View is set to `'Report'`, the items are displayed in a single column using small icons but with the matrix specified by [ReportInfo](reportinfo.md) displayed alongside. In this format, the ListView also provides column headings which are specified by the ColTitles property. The alignment of these titles (and of the data in the columns beneath them) is defined by the [ColTitleAlign](coltitlealign.md) property. Examples of different views are illustrated below.

![](../img/listview-icon.png)

![](../img/listview-list.png)

![](../img/listview-report.png)

**Application**

Objects: [ListView](../objects/listview.md)
