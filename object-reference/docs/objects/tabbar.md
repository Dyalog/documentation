# <span>TabBar</span> <span>Object</span>

[Parents](../parentlists/tabbar.md), [Children](../childlists/tabbar.md), [Properties](../proplists/tabbar.md), [Methods](../methodlists/tabbar.md), [Events](../eventlists/tabbar.md)

**Purpose:** To manage a set of [TabBtn](tabbtn.md) objects.

**Description**

The TabBar object manages a group of [TabBtn](tabbtn.md) objects. These are associated with a set of [SubForm](subform.md) objects which are positioned on top of one another. When the user clicks on a [TabBtn](tabbtn.md),
the corresponding [SubForm](subform.md) is brought to the
top and given the focus.

TabBar and [TabBtn](tabbtn.md) objects were implemented
before Windows provided direct support for tabbed dialogs, and have been
superceded by [TabControl](tabcontrol.md) and [TabButton](tabbutton.md) objects. Please use these instead.

By default, a TabBar is a flat bar stretched across the bottom of its parent
form. You can alter its appearance using its [EdgeStyle](../properties/edgestyle.md) property and you can control its alignment with its [Align](../properties/align.md) property. [Align](../properties/align.md) can be set to Top, Bottom
(the default), Left or Right and causes the TabBar to be attached to the
corresponding edge of the [Form](form.md). A TabBar aligned
Top or Bottom will automatically stretch or shrink horizontally when its parent [Form](form.md) is resized, but it will remain fixed vertically. A TabBar aligned Left or Right
will stretch vertically but will remain fixed horizontally. By default a TabBar
occupies the entire width or length of the side of the [Form](form.md) to which it is attached. Both the [Posn](../properties/posn.md) and [Size](../properties/size.md) properties can be altered.

The alignment of a TabBar also determines the orientation of its [TabBtn](tabbtn.md)s.
TabBars aligned Top or Bottom cause their [TabBtn](tabbtn.md)s
to be drawn left to right with the free edge of the [TabBtn](tabbtn.md)s
facing downwards or upwards respectively. TabBar aligned Left or Right draw
their [TabBtn](tabbtn.md)s downwards with their free edges
facing left or right respectively.

By default, [TabBtn](tabbtn.md) objects are positioned
along the inner edge of the TabBar. This is the edge closest to the [SubForm](subform.md) s they will tab. They are also positioned so that they overlap one another
horizontally or vertically according to the [Align](../properties/align.md) property.

The [HScroll](../properties/hscroll.md) and [VScroll](../properties/vscroll.md) properties determine what happens when the end of the TabBar is reached. If [HScroll](../properties/hscroll.md) or [VScroll](../properties/vscroll.md) is 0 (the default) a [TabBtn](tabbtn.md) that would otherwise extend beyond the TabBar is instead positioned immediately
above, below or alongside the first [TabBtn](tabbtn.md) in
the TabBar, thereby starting a new row or column. Note however that the TabBar
is not automatically resized vertically to accommodate a second row or column.
If you want a multi-flight TabBar you have to set its height or width
explicitly. If [HScroll](../properties/hscroll.md) or [VScroll](../properties/vscroll.md) is `¯1` or `¯2`,
[TabBtn](tabbtn.md)s continue to be added along the TabBar
even though they extend beyond its boundary and may be scrolled into view using
a mini scrollbar. If [HScroll](../properties/hscroll.md) is `¯1`,
the scrollbar is shown whether or not any controls extend beyond the TabBar. If [HScroll](../properties/hscroll.md) is `¯2`, the scrollbar appears only if
required and may appear or disappear when the user resizes the parent [Form](form.md).

[VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) may only be set when the object is created and may not subsequently be changed.

If you specify a value for its [Posn](../properties/posn.md) property, a [TabBtn](tabbtn.md) will be placed at the
requested position regardless of the value of [Style](../properties/style.md),
[HScroll](../properties/hscroll.md) or [VScroll](../properties/vscroll.md).
However, the next control added will take its default position from the previous
one according to the value of these properties. Thus if you wish to group your
controls together with spaces between the groups, you need only specify the
position of the first one in each group.

If you specify a value for its [Posn](../properties/posn.md) property, a [TabBtn](tabbtn.md) will be placed at the
requested position regardless of the value of [Align](../properties/align.md).
However, the next [TabBtn](tabbtn.md) added will take its
default position from the previous one. Thus if you wish to group your [TabBtn](tabbtn.md)s
together with spaces between the groups, you need only specify the position of
the first one in each group.
