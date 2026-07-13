# <span>SubForm</span> <span>Object</span>



[Parents](../parentlists/subform.md), [Children](../childlists/subform.md), [Properties](../proplists/subform.md), [Methods](../methodlists/subform.md), [Events](../eventlists/subform.md)



**Purpose:** This object represents a window that is owned by and constrained         within another [Form](form.md) or an [MDIClient](mdiclient.md) .

**Description**


If the SubForm is the child of a [Form](form.md), it is
by default a simple featureless window that occupies the entire client area
(excluding standard [ToolBar](toolbar.md)s, [StatusBar](statusbar.md)s
and [TabBar](tabbar.md)s) of its parent.



The properties
that control its appearance, including [Sizeable](../properties/sizeable.md),
[Moveable](../properties/moveable.md), [SysMenu](../properties/sysmenu.md),
[Border](../properties/border.md), [MaxButton](../properties/maxbutton.md) and [MinButton](../properties/minbutton.md), all default to 0. The [EdgeStyle](../properties/edgestyle.md) property also defaults to `'None'`, so the
background of the SubForm defaults to the Window Background colour.


If the SubForm is the child of an [MDIClient](mdiclient.md),
its default appearance is the same as for a top-level [Form](form.md).
By default its size is 25% of its parent client area and it is positioned in the
centre of its parent object.


The [Posn](../properties/posn.md) property specifies the location of
the **internal** top-left corner of the SubForm relative to its parent. If
the SubForm has a title bar, border, or a 3-dimensional shadow, you must allow
sufficient space for these components. Similarly, the [Size](../properties/size.md) property specifies the internal size of the SubForm excluding the title bar and
border.


A SubForm is constrained so that it cannot be moved outside its parent. In
all other respects it behaves in a similar manner to a [Form](form.md) object. See [Form](form.md) object and the descriptions of
its properties for further details.


