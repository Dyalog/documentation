# <span>TabButton</span> <span>Object</span>

[Parents](../parentlists/tabbutton.md), [Children](../childlists/tabbutton.md), [Properties](../proplists/tabbutton.md), [Methods](../methodlists/tabbutton.md), [Events](../eventlists/tabbutton.md)

**Purpose:** The TabButton object represents an individual tab or button in a [TabControl](tabcontrol.md)

**Description**

The TabButton object represents an individual tab or button in a [TabControl](tabcontrol.md)

The position and size of a TabButton object are entirely determined by its parent [TabControl](tabcontrol.md) and may not be altered. For this reason, the [Posn](../properties/posn.md) and [Size](../properties/size.md) properties are read-only.

The [Caption](../properties/caption.md) property specifies the text that appears on the button or tab.

A picture is specified by setting the ImageIndex property of the TabButton. This is a number that points to a particular icon or bitmap defined in an [ImageList](imagelist.md) object whose name is specified by the [ImageListObj](../properties/imagelistobj.md) property of the parent [TabControl](tabcontrol.md).

Note that all TabButton objects share the same font which is defined by the [FontObj](../properties/fontobj.md) property of the [TabControl](tabcontrol.md).

The foreground and background colours of the TabButton object are fixed.

When used as a tab, a TabButton is normally attached to a [SubForm](subform.md) by the [TabObj](../properties/tabobj.md) property of the [SubForm](subform.md). The [TabObj](../properties/tabobj.md) property of the TabButton itself, is a read-only property that specifies the name of, or ref to, the [SubForm](subform.md) to which the TabButton is attached.

The [State](../properties/state.md) property reports the (selected) state of a TabButton.
