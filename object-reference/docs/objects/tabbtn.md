# <span>TabBtn</span> <span>Object</span>

**Purpose:** To tab a [SubForm](subform.md) .

**Description**

TabBtn objects are associated with [SubForm](subform.md)s which are positioned on top of one another. When the user clicks on a TabBtn, the corresponding [SubForm](subform.md) is brought to the top and given the focus.

[TabBar](tabbar.md) and TabBtn objects were implemented before Windows provided direct support for tabbed dialogs, and have been superceded by [TabControl](tabcontrol.md) and [TabButton](tabbutton.md) objects. Please use these instead.

The appearance of a TabBtn is determined by its [EdgeStyle](../properties/edgestyle.md), [Border](../properties/border.md) and [Caption](../properties/caption.md) properties. These take their defaults from the [SubForm](subform.md) with which the TabBtn is associated. Thus there is generally no need to specify them. [BCol](../properties/bcol.md) also defaults to that of its associated [SubForm](subform.md).

The position of a TabBtn is normally determined by its parent [TabBar](tabbar.md) and its default size is fixed (22 x 80 pixels), and not related to the size of its [Caption](../properties/caption.md). These defaults can be overridden using the [Posn](../properties/posn.md) and [Size](../properties/size.md) properties.

A [SubForm](subform.md) is associated with a TabBtn by setting the [TabObj](../properties/tabobj.md) property of the [*SubForm*](subform.md) to the name of, or ref to, the TabBtn. The [TabObj](../properties/tabobj.md) property of the TabBtn is a read-only property that contains the name of, or ref to, the associated [SubForm](subform.md).

**Application**

Parents: [TabBar](../objects/tabbar.md)

Children: [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [Active](../properties/active.md), [Align](../properties/align.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Size](../properties/size.md), [TabObj](../properties/tabobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md)

Methods: [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [DropObjects](../methodorevents/dropobjects.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [Select](../methodorevents/select.md)
