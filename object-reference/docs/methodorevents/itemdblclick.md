# <span>ItemDblClick</span> <span>Event 342</span>

**Applies To:** [ListView](../objects/listview.md), [TreeView](../objects/treeview.md)

**Description**

If enabled, this event is reported when the user double-clicks a mouse button when the mouse pointer is over an item in a [ListView](../objects/listview.md) or  [TreeView](../objects/treeview.md) object. This event is reported for information only and may not be controlled in any way using a callback function. Generating the event with `⎕NQ`, or calling it as a method, has no effect.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`[1]`|Object      |ref or character vector                                                                                                                                              |
|`[2]`|Event       |`'ItemDblClick'` or 342                                                                                                                                              |
|`[3]`|Item number |Integer. The index of the item.                                                                                                                                      |
|`[4]`|Mouse button|Integer.                                                                                                                                                             |
|`[5]`|Shift state |Integer. Sum of 1=shift key, 2=Ctrl key, 4=Alt key                                                                                                                   |
|`[6]`|Position    |Integer. Indicates the position of the mouse-pointer within the item. It is either 2 (over the icon), 4 (over the label), 8 (over the line), or 16 (over the symbol).|
