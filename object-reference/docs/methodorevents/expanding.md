# <span>Expanding</span> <span>Event 302</span>

**Description**

If enabled, this event is reported by a [Grid](../objects/grid.md) or a [TreeView](../objects/treeview.md) object just before it is about to expand to show additional rows or children of the current item.

In a Grid, this occurs when the user clicks the picture or tree line in the row title.

In a TreeView, this occurs when the user double-clicks the item label or clicks in the button or on the tree line to the left of the item label.

The default processing for the event is to expand the tree at the corresponding point.

You may disable the expand operation by setting the action code for the event to `¯1`. You may also prevent the expand from occurring by returning 0 from a callback function. You may expand an object dynamically under program control by calling Expanding as a method.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 3-element vector as follows :

|-----|-----------|--------------------------------------|
|`[1]`|Object     |ref or character vector               |
|`[2]`|Event      |`'Expanding'` or 302                  |
|`[3]`|Item number|Integer. The index of the row or item.|

**Application**

Objects: [Grid](../objects/grid.md), [TreeView](../objects/treeview.md)
