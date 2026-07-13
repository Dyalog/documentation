# <span>DropObjects</span> <span>Event 455</span>

[**Applies To**](../methodoreventapplies/dropobjects.md)

**Description**


If enabled, this event is reported when the user drags an object icon or a set of object icons from the *Explorer Tool* or *Find Objects Tool* (which are part of the Dyalog APL Session) and drops them onto the object. The system takes no action other than to report the event. You can use this event to extend drag-drop functionality in your Session. For example, you could perform an operation by drag-dropping an APL object icon onto a Button in the Session toolbar.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'DropObjects'` or 455|
|`[3]`|Objects|Vector of character vectors containing the object names.|
|`[4]`|Item number|Integer. The index of the item within the object onto which the file(s) was dropped. Applies only to objects that have an [Items](../properties/items.md) property such as List, [ListView](../objects/listview.md) and [TreeView](../objects/treeview.md) . Otherwise this value is -1.|
|`[5]`|Shift state|Integer. Sum of 1=Shift key, 2=Ctrl key, 4=Alt key|



