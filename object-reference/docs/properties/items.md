# <span>Items</span> <span>Property</span>

**Description**

This property specifies the list of items from which the user may choose.

The value of Items is a text array. It is normally specified as a vector of character vectors each of which represents an item. For a [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), or [List](../objects/list.md) or [Spinner](../objects/spinner.md), Items may also be a matrix whose rows specify items. If a character scalar or simple vector is specified, it is treated as a single item.

An empty character vector is treated the same as a vector of blanks, and represents one item.

A zero-length vector of vectors or an empty matrix represents 0 items. The default value for Items is an empty matrix.

`⎕WG 'Items'` returns an array of the same structure as was assigned by [`⎕WC`](../../../language-reference-guide/system-functions/wc) or [`⎕WS`](../../../language-reference-guide/system-functions/ws).

**Application**

Objects: [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Spinner](../objects/spinner.md), [TreeView](../objects/treeview.md)
