# <span>TreeView</span> <span>Object</span>

[Parents](../parentlists/treeview.md), [Children](../childlists/treeview.md), [Properties](../proplists/treeview.md), [Methods](../methodlists/treeview.md), [Events](../eventlists/treeview.md)

**Purpose:** The TreeView object displays a hierarchical list of items.

**Description**

A TreeView object displays a hierarchical list of items, such as the headings in a document, the entries in an index, or the files and directories on a disk. Each item consists of a label and an optional bitmapped image, and each item can have a list of sub-items associated with it. By clicking an item, the user can expand and collapse the associated list of sub-items.

The contents of a TreeView object are defined by the [Items](../properties/items.md) property; a vector of character vectors that specifies the item labels.

The [ImageListObj](../properties/imagelistobj.md), [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) properties define bitmapped images corresponding to each item. The bitmapped images are drawn to the left of the item labels.

[ImageListObj](../properties/imagelistobj.md) specifies the name of a single [ImageList](imagelist.md) object that contains one or more bitmaps.

[ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) are `⎕IO` sensitive scalars, or vectors with the same length as the number of items in the object. The value in the ith element specifies the image for the ith item and is an index into the corresponding [ImageList](imagelist.md) object. [ImageIndex](../properties/imageindex.md) specifies the image displayed when an item is *not selected*, [SelImageIndex](../properties/selimageindex.md) specifies the image displayed when an item is *selected*.

If [ImageListObj](../properties/imagelistobj.md) is specified, but ImageIndex is empty or not specified, the first bitmap in the [ImageList](imagelist.md) is drawn alongside every item. If an element of [ImageIndex](../properties/imageindex.md) or [SelImageIndex](../properties/selimageindex.md) specifies a value that does not correspond to a bitmap in the [ImageList](imagelist.md), no picture is drawn.

The structure of the items (that is, the parent/child relationships of the items) is defined by the [Depth](../properties/depth.md) property. This is either a scalar 0 (the default) which means that all items are *root* items, or it is a numeric vector of the same length as Items. Non-zero values in [Depth](../properties/depth.md) indicate child items.

The [HasLines](../properties/haslines.md) property is 0, 1 or 2 and determines whether or not lines are drawn that link child items to their corresponding parent item. If [HasLines](../properties/haslines.md) is 0, no lines are drawn. If [HasLines](../properties/haslines.md) is 1, lines are drawn at all except the top level, that is, the object does not link items at the root of the hierarchy. The default value for [HasLines](../properties/haslines.md) is 2 which provides lines at all levels including the root.

The [HasButtons](../properties/hasbuttons.md) property determines whether or not the TreeView object has a button to the left side of each parent item. It is Boolean with a default value of 1. The user can click the button to expand or collapse the child items as an alternative to double-clicking the parent item. Note that by itself, setting [HasButtons](../properties/hasbuttons.md) to 1 does not add buttons to items at the root of the hierarchy. To achieve this you must also set [HasLines](../properties/haslines.md) to 2.

The [CheckBoxes](../properties/checkboxes.md) property specifies whether or not check boxes are displayed alongside items in a TreeView.

The [FullRowSelect](../properties/fullrowselect.md) property specifies whether just the item itself, or the entire row of the TreeView, is highlighted when an item is selected. [FullRowSelect](../properties/fullrowselect.md) should not be used if [HasLines](../properties/haslines.md) is 1 or 2

When the user presses the left mouse button over an item, the object generates an [ItemDown](../methodorevents/itemdown.md) event. This is followed by an [ItemUp](../methodorevents/itemup.md) event when the mouse button is released. The object also generates an [ItemDblClick](../methodorevents/itemdblclick.md) event when the left mouse is double-clicked over an item. If all three events are enabled, they are reported in the order [ItemDown](../methodorevents/itemdown.md), [ItemDblClick](../methodorevents/itemdblclick.md), [ItemUp](../methodorevents/itemup.md).

When a parent item is in its retracted state (its children are not visible) it can be expanded to show its children by the user double-clicking its label or by clicking over its button or tree lines. An [Expanding](../methodorevents/expanding.md) event is reported immediately before the children are shown. Similarly, when a parent item is in its expanded state, it can be retracted to hide its children when a [Retracting](../methodorevents/retracting.md) event is reported. You can use the [Expanding](../methodorevents/expanding.md) event to define new children for the object just before they are shown. You can also control the actions of these events using callback functions.

The [EditLabels](../properties/editlabels.md) is a Boolean property (default 0) that determines whether or not the user may edit the labels which are specified by the Items property.

The [SelItems](../properties/selitems.md) property is a Boolean vector that indicates which of the items is currently selected and has the focus. If more items are visible than can fit within the object, a scrollbar is automatically provided. The [Index](../properties/index-property.md) property is a `⎕IO` sensitive integer that reports the index number of the first item displayed in the object and changes as the items are scrolled.

!!! warning
    Due to the limitations of the Win32 TreeView object, it is necessary to query the state of each item in a TreeView in order to obtain the value of the [SelItems](../properties/selitems.md) property, making it a comparatively slow operation if there are a lot of [Items](../properties/items.md).
