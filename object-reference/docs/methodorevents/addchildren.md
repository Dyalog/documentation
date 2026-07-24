# <span>AddChildren</span> <span>Method 310</span>

**Description**

This method is used to add child items to an item in a [TreeView](../objects/treeview.md) object

The argument to AddChildren is a 3, 4 or 5 element array as follows:

|-----|-----------------------|----------------------------|
|`[1]`|Item number            |Integer.                    |
|`[2]`|New items              |Vector of character vectors.|
|`[3]`|Depth vector           |Integer vector.             |
|`[4]`|Picture vector         |Integer vector.             |
|`[5]`|Selected picture vector|Integer vector.             |

*Item number* specifies the index of the item to which the child items are to be added.

*New items* is a vector of character vectors containing the labels for the new child items.

*Depth vector* is an integer vector specifying the depth of each of the new items relative to the parent item to which they are being added. The first element of this array must be 0.

*Picture vector* and *Selected picture vector* are optional and specify values of [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) respectively for each of the new items.

The result is the index at which the first new item has been inserted.

**Application**

Objects: [TreeView](../objects/treeview.md)
