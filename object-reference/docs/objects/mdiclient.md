# <span>MDIClient</span> <span>Object</span>



[Parents](../parentlists/mdiclient.md), [Children](../childlists/mdiclient.md), [Properties](../proplists/mdiclient.md), [Methods](../methodlists/mdiclient.md), [Events](../eventlists/mdiclient.md)



**Purpose:** Implements Multiple Document Interface (MDI) behaviour.

**Description**


The multiple-document interface (MDI) is a document-oriented interface that is commonly used by word-processors, spreadsheets and other applications that deal with *documents*. An MDI application allows the user to display multiple documents at the same time, with each document displayed in its own window.



The MDIClient object is a container object that effectively specifies the client area within the parent [Form](form.md) in which the [SubForm](subform.md) are displayed. The MDIClient object also imposes special MDI behaviour which is quite different from that where a [SubForm](subform.md) is simply the child of another [Form](form.md).


By default, the MDIClient occupies the entire client area within its parent [Form](form.md). This is the area within the [Form](form.md) that is not occupied by [CoolBar](coolbar.md)s, [MenuBar](menubar.md)s, [ToolBar](toolbar.md)s, [ToolControl](toolcontrol.md)s, [TabBar](tabbar.md)s, [TabControls](tabcontrol.md) and [StatusBar](statusbar.md)s. In most applications it is therefore not necessary to specify the position and size of the MDIClient object, although you may do so if you want to reserve additional space in the parent [Form](form.md) for other objects.


Each of the four sides of an MDIClient object is automatically *attached* to the corresponding side of its parent [Form](form.md) and maintains its position when the parent [Form](form.md) is resized. This means that a default MDIClient always occupies the entire client area of its parent [Form](form.md), regardless of how the parent is resized.


The appearance of the MDIClient may be changed using its [Border](../properties/border.md), [BCol](../properties/bcol.md) and [Picture](../properties/picture.md) properties. The [EdgeStyle](../properties/edgestyle.md) property has no direct effect and is provided only to pass on a value to its child [Form](form.md)s.


The [MDIActive](../properties/mdiactive.md) and [MDIActiveObject](../properties/mdiactiveobject.md) properties contain the name of and a ref to the [SubForm](subform.md) that currently has the focus. You may set these properties as well as query them.


You can call methods which cause the MDIClient to organise its child [SubForm](subform.md)s in some way. These methods are as follows:


|---------------------------------------------|----------------------------------------------------------------------------------------------------------|
|[MDICascade](../methodorevents/mdicascade.md)|Causes the MDIClient to organise its child Forms in an overlapping manner.                                |
|[MDITile](../methodorevents/mditile.md)      |Causes the MDIClient to arrange its child Forms as a row or column.                                       |
|[MDIArrange](../methodorevents/mdiarrange.md)|Causes the MDIClient to arrange the icons associated with any minimised child Forms in an orderly fashion.|


