# <span>EndEditLabel</span> <span>Event 301</span>

**Applies To:** [ListView](../objects/listview.md), [TreeView](../objects/treeview.md)

**Description**

If enabled, this event is reported when the user signals completion of an edit operation in a [ListView](../objects/listview.md) or [TreeView](../objects/treeview.md) object. This occurs when the item being edited loses the focus or when the user presses the Enter key. The default processing for the event is to update the item label (string) with the edited text in the pop-up edit box.

You may disable the update operation by setting the action code for the event to `¯1`. You may also prevent the update from occurring by returning 0 from a callback function. You may specify the text used to update the item by returning the event message (containing the desired text) from a callback function. Finally, you may change the text of any item dynamically by calling EndEditLabel as a method.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :

|-----|-----------|----------------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                           |
|`[2]`|Event      |`'EndEditLabel'` or 301                                                           |
|`[3]`|Item number|Integer. The index of the item.                                                   |
|`[4]`|Text       |character vector containing the text that will be used to update the item's label.|
