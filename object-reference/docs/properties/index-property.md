# <span>Index</span> <span>Property</span>

**Description**

For a [List](../objects/list.md) and a [Combo](../objects/combo.md) with [Style](style.md) `'Simple'`, this property specifies the position of the data in the list box as a positive integer value. If Index has the value "n", it means that the "nth" item in [Items](items.md) is displayed on the top line in the list box. The value of Index is dependent upon the value of `⎕IO`. Note that Index for a [Combo](../objects/combo.md) or [List](../objects/list.md) cannot be set using [`⎕WC`](../../../language-reference-guide/system-functions/wc). The value of Index in a [Combo](../objects/combo.md) with a drop-down list box ([Style](style.md) `'Drop'` or `'DropEdit'`) is always equal to `⎕IO`.

For a [Grid](../objects/grid.md), Index is a 2-element vector that specifies the row and column number of the cell that is currently in the top left corner of the [Grid](../objects/grid.md).

For a [TreeView](../objects/treeview.md), Index is a positive integer value that specifies which item appears at the top of the [TreeView](../objects/treeview.md) window.

For a [FileBox](../objects/filebox.md), the Index property determines which of the [Filters](filters.md) is initially selected.

For a [CoolBand](../objects/coolband.md), the Index property specifies the position of the [CoolBand](../objects/coolband.md) within its parent [CoolBar](../objects/coolbar.md), relative to the other [CoolBands](../objects/coolband.md) in the [CoolBar](../objects/coolbar.md).

The value of Index is dependent on `⎕IO`, and its default value is equal to `⎕IO`.

**Application**

Objects: [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBand](../objects/coolband.md), [FileBox](../objects/filebox.md), [Grid](../objects/grid.md), [List](../objects/list.md), [TreeView](../objects/treeview.md)
