# <span>BeginEditLabel</span> <span>Event 300</span>



**Applies To:** [ListView](../objects/listview.md), [TreeView](../objects/treeview.md)

**Description**


If enabled, this event is reported when the user clicks on an item in a [ListView](../objects/listview.md) or [TreeView](../objects/treeview.md) object that has the focus, and signals the start of an edit operation. The default processing for the event is to display a pop-up edit box around the item and to permit the user to change its text.


You may disable the operation by setting the action code for the event to `¯1`. You may prevent a particular item from being edited by returning 0 from a callback function. You may also initiate the edit operation by calling BeginEditLabel as a method.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 3-element vector as follows :


|-----|-----------|-------------------------------|
|`[1]`|Object     |ref or character vector        |
|`[2]`|Event      |`'BeginEditLabel'` or 300      |
|`[3]`|Item number|Integer. The index of the item.|



