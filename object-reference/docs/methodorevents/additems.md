# <span>AddItems</span> <span>Method 308</span>

**Description**

This method is used to add items to a [TreeView](../objects/treeview.md) object

The argument to AddItems is a 3, 4 or 5-element array as follows:

|-----|-----------------------|----------------------------|
|`[1]`|Item number            |Integer.                    |
|`[2]`|New items              |Vector of character vectors.|
|`[3]`|Depth vector           |Integer vector.             |
|`[4]`|Picture vector         |Integer vector.             |
|`[5]`|Selected picture vector|Integer vector.             |

*Item number* specifies the index of the item to which the child items are to be added.

*New items* is a vector of character vectors containing the labels for the new child items.

*Depth vector* is an integer vector specifying the depth of each of the new items relative to the parent item to which they are being added. The first element of this array must be 0. This element may be omitted. If so, it is assumed to be all 0s.

*Picture vector* and *Selected picture vector* are optional and specify values of [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) respectively for each of the new items.

The new items are inserted with the first one being placed at the same level in the hierarchy as the item specified in element [1].

The result is an integer that reports the index position at which the first of the new items has been inserted.

**Application**

Objects: [TreeView](../objects/treeview.md)
