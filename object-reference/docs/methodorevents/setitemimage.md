# <span>SetItemImage</span> <span>Method 315</span>

**Applies To:** [TreeView](../objects/treeview.md)

**Description**

This method is used to allocate a picture icon to a particular item in a [TreeView](../objects/treeview.md) object.

The argument to SetItemImage is a 2-element array as follows:

|-----|-------------|--------|
|`[1]`|Item number  |Integer.|
|`[2]`|Picture index|Integer.|

*Item number* is the index of the item concerned.

*Picture index* is an index into the array of bitmapped images in the corresponding ImageList object which is referenced via the ImageListObj property.
