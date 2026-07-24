# <span>TipField</span> <span>Object</span>

**Purpose:** To display pop-up help.

**Description**

The TipField is used to display pop-up help when the user moves the mouse pointer over an object.

Most of the GUI objects supported by Dyalog APL/W have a [Tip](../properties/tip.md) and a [TipObj](../properties/tipobj.md) property. [TipObj](../properties/tipobj.md) specifies the name of, or ref to, a TipField object, and [Tip](../properties/tip.md) specifies a "help" message. The TipField automatically pops-up to display the [Tip](../properties/tip.md) when the user moves the mouse pointer over the object. It disappears when the user moves the mouse pointer away.

The TipField is a simple box with a 1-pixel black border in which the text specified by [Tip](../properties/tip.md) is displayed. [FCol](../properties/fcol.md), [BCol](../properties/bcol.md) and [FontObj](../properties/fontobj.md) can be used to customise the appearance of the text within the box. [FCol](../properties/fcol.md) specifies the colour of the text; [BCol](../properties/bcol.md) specifies the background colour with which the box is filled. The default is black on yellow.

If you wish to display [Tip](../properties/tip.md)s for particular objects in different fonts and colours, you must create a separate TipField for each combination of colour and font you need.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Group](../objects/group.md), [OLEServer](../objects/oleserver.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Root](../objects/root.md), [SubForm](../objects/subform.md), [TCPSocket](../objects/tcpsocket.md)

Children: [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [BCol](../properties/bcol.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [Translate](../properties/translate.md), [Type](../properties/type.md)

Methods: [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md)
