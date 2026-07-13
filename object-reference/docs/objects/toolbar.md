# <span>ToolBar</span> <span>Object</span>



[Parents](../parentlists/toolbar.md), [Children](../childlists/toolbar.md), [Properties](../proplists/toolbar.md), [Methods](../methodlists/toolbar.md), [Events](../eventlists/toolbar.md)



**Purpose:** To manage a group of controls such as [Button](button.md) s.

**Description**


The ToolBar object is used to display and manage a set of controls. It is
typically used to present a set of [Button](button.md)s
which the user can press to perform various actions. However, the ToolBar has
the ability to manage other controls too.



By default, the ToolBar is a raised bar stretched across the top of its
parent form. You can alter its appearance using its [EdgeStyle](../properties/edgestyle.md) property and you can control its alignment with its [Align](../properties/align.md) property. [Align](../properties/align.md) can be set to Top (the
default), Bottom, Left or Right and causes the ToolBar to be attached to the
corresponding edge of the [Form](form.md). A ToolBar
aligned Top or Bottom will automatically stretch or shrink horizontally when its
parent [Form](form.md) is resized, but it will remain fixed
vertically. A ToolBar aligned Left or Right will stretch vertically but will
remain fixed horizontally. By default a ToolBar occupies the entire width or
length of the side of the [Form](form.md) to which it is
attached and is 30 pixels high or wide. You can change these defaults using the [Posn](../properties/posn.md) and [Size](../properties/size.md) properties.


A ToolBar organises its child controls in the order they are created. The way
this is done is governed by the value of the [Align](../properties/align.md) property. If [Align](../properties/align.md) is Top or Bottom, the
ToolBar arranges its controls in rows across the screen. If [Align](../properties/align.md) is Left or Right, the ToolBar arranges controls in columns.


The first control added to a ToolBar is automatically positioned 2 pixels
down and 2 pixels across from its top left corner. The rule for positioning
subsequent controls depends upon the value of the [Align](../properties/align.md) property.


If [Align](../properties/align.md) is `'Top'` or `'Bottom'`, controls are positioned so as
to be horizontally adjacent to one another. Whenever a control is added it is
positioned relative to the one that immediately preceded it so that its top left
corner meets the top right corner of the previous one. The [HScroll](../properties/hscroll.md) property determines what happens when the end of the ToolBar is reached. If [HScroll](../properties/hscroll.md) is 0 (the default) a control that would otherwise extend beyond the width of the
ToolBar is instead positioned immediately below the first control in the
ToolBar, thereby starting a new row. Note however that the ToolBar is not
automatically resized vertically to accommodate a second row. If you want a
multi-row ToolBar you have to set its height explicitly. If [HScroll](../properties/hscroll.md) is `¯1` or `¯2`,
controls continue to be added along the ToolBar even though they extend beyond
its right edge and may be scrolled into view using a mini scrollbar. If [HScroll](../properties/hscroll.md) is `¯1`, the scrollbar is shown whether or
not any controls extend beyond the width of the ToolBar. If [HScroll](../properties/hscroll.md) is `¯2`, the scrollbar appears only if
required and may appear or disappear when the user resizes the parent [Form](form.md).


If [Align](../properties/align.md) is `'Left'` or `'Right'`, controls are positioned so as
to be vertically adjacent to one another. Whenever a control is added, its top
left corner is positioned against the bottom left corner of the previous
control. The [VScroll](../properties/vscroll.md) property determines
what happens when the bottom of the ToolBar is reached. If [VScroll](../properties/vscroll.md) is 0 (the default) a control that would otherwise extend beyond the bottom of
the ToolBar is instead positioned immediately to the right of the first one;
thereby starting a new column. Note however that the ToolBar is not
automatically resized horizontally to accommodate a second column. You must set
the width of the ToolBar explicitly.


If [VScroll](../properties/vscroll.md) is `¯1` or `¯2`,
controls continue to be added down the ToolBar even though they extend beyond
its bottom edge and may be scrolled into view using a mini scrollbar. If [VScroll](../properties/vscroll.md) is `¯1`, the scrollbar is shown whether or
not any controls extend beyond the bottom of the ToolBar. If [VScroll](../properties/vscroll.md) is `¯2`, the scrollbar appears only if
required and may appear or disappear when the user resizes the parent [Form](form.md).


[VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) may only be set when the object is created and may not subsequently be changed.


If you specify a value for its [Posn](../properties/posn.md) property, a control will be placed at the requested position regardless of the
value of [Style](../properties/style.md), [VScroll](../properties/vscroll.md) or [HScroll](../properties/hscroll.md). However, the next control added
will take its default position from the previous one according to the value of
these properties. Thus if you wish to group your controls together with spaces
between the groups, you need only specify the position of the first one in each
group.


The ToolBar object was introduced in Dyalog APL before an appropriate standard Windows control existed. The ToolBar object should be considered as a legacy object and used only in old GUI applications. The [ToolControl](toolcontrol.md) object should be used instead.


