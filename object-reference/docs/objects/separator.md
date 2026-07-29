# <span>Separator</span> <span>Object</span>

**Purpose:** A horizontal or vertical line used to separate items in a menu.

**Description**

This object provides a vertical or horizontal line to separate items in a [Menu](menu.md). It may also be used to split a [MenuBar](menubar.md) over more than one line.

The orientation of the Separator is determined by its [Style](../properties/style.md) property, which may be `'Horz'` (horizontal) or `'Vert'` (vertical). The default is `'Horz'`.

If you want to provide a menu with a 3-Dimensional (pushbutton) appearance, you should also set the [EdgeStyle](../properties/edgestyle.md) property on any Separator objects in it. Alternatively, you can achieve the same effect by setting the background colour ([BCol](../properties/bcol.md)) for the Separators to grey (192 192 192).

The [Posn](../properties/posn.md) property is a single integer number which specifies the positional index of the Separator relative to the other objects in the [Menu](menu.md). A Separator does not generate any events.

Like other components of a menu, the position of a Separator is normally determined by the order in which it is created in relation to other objects with the same parent. However, you can use the [Posn](../properties/posn.md) property to **insert** a Separator into an existing structure. For example, having defined three [MenuItem](menuitem.md) objects as children of a [Menu](menu.md), you can insert a Separator between the first and the second by specifying its [Posn](../properties/posn.md) to be 2. Note that the value of [Posn](../properties/posn.md) for the [MenuItem](menuitem.md)s that were previously second and third will then be reset to third and fourth respectively.

If you put a Separator (either [Style](../properties/style.md)) into a [MenuBar](menubar.md), it has the effect of adding another line to it. Any items added after the Separator will appear in the new line.

**Application**

Parents: [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md)

Children: [Timer](../objects/timer.md)

Properties: [BCol](../properties/bcol.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Style](../properties/style.md), [Translate](../properties/translate.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md)
