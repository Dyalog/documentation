# <span>SetItemState</span> <span>Method 307</span>

**Applies To:** [ListView](../objects/listview.md), [TreeView](../objects/treeview.md)

**Description**

This method is used to set the status of a particular item in a [ListView](../objects/listview.md) or [TreeView](../objects/treeview.md) object.

The argument to SetItemState is a 2-element array as follows:

|-----|-----------|-----------------------------------------|
|`[1]`|Item number|Integer. The index of the item concerned.|
|`[2]`|Status     |Integer                                  |

The status of an item is calculated as the sum of one or more of the following state codes:

|----|----------------------------------------------------------------|
|`¯1`|Error (most likely the Item number is invalid)                  |
|1   |Item has the focus                                              |
|2   |Item is selected                                                |
|8   |Item is highlighted for dropping                                |
|16  |Item is displayed in bold text                                  |
|32  |Item is expanded                                                |
|64  |Item is or has been expanded                                    |
|4096|Item is checked. See [CheckBoxes](../properties/checkboxes.md)  |
