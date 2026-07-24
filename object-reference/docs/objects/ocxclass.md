# <span>OCXClass</span> <span>Object</span>

**Purpose:** This object provides access to OLE (ActiveX) Controls.

**Description**

This object loads an OLE Control into memory and defines a new class of object associated with it. The name of the new class is the name specified by the left argument of `⎕WC`  You may create an instance of the newly defined class using the name you assigned to the OCXClass object as the Type property.

Note that you may not create an instance of OCXClass using `⎕NEW`.

Once you have defined a new OCXClass, the properties, events and methods it supports may be obtained from its [PropList](../properties/proplist.md), [EventList](../properties/eventlist.md) and [MethodList](../properties/methodlist.md) properties. These are the properties, events and methods defined for the OLE control by its author.

The [QueueEvents](../properties/queueevents.md) property determines how events reported by the ActiveX control are handled.

To find out how to use the OLE control, you must consult the appropriate documentation. However, a great deal of information about it can be obtained using the [GetPropertyInfo](../methodorevents/getpropertyinfo.md), [GetEventInfo](../methodorevents/geteventinfo.md), and [GetMethodInfo](../methodorevents/getmethodinfo.md) methods.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [OLEServer](../objects/oleserver.md), [PropertyPage](../objects/propertypage.md), [Root](../objects/root.md), [SubForm](../objects/subform.md), [TCPSocket](../objects/tcpsocket.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [OLEServer](../objects/oleserver.md), [PropertyPage](../objects/propertypage.md), [Root](../objects/root.md), [SubForm](../objects/subform.md), [TCPSocket](../objects/tcpsocket.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Properties: [ChildList](../properties/childlist.md), [ClassID](../properties/classid.md), [ClassName](../properties/classname.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [HelpFile](../properties/helpfile.md), [KeepOnClose](../properties/keeponclose.md), [LicenseKey](../properties/licensekey.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [QueueEvents](../properties/queueevents.md), [ToolboxBitmap](../properties/toolboxbitmap.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [TypeList](../properties/typelist.md)

Methods: [Browse](../methodorevents/browse.md), [Detach](../methodorevents/detach.md), [GetEventInfo](../methodorevents/geteventinfo.md), [GetMethodInfo](../methodorevents/getmethodinfo.md), [GetPropertyInfo](../methodorevents/getpropertyinfo.md), [GetTypeInfo](../methodorevents/gettypeinfo.md), [OLEAddEventSink](../methodorevents/oleaddeventsink.md), [OLEDeleteEventSink](../methodorevents/oledeleteeventsink.md), [OLEListEventSinks](../methodorevents/olelisteventsinks.md), [SetMethodInfo](../methodorevents/setmethodinfo.md), [SetPropertyInfo](../methodorevents/setpropertyinfo.md), [ShowHelp](../methodorevents/showhelp.md), [ShowProperties](../methodorevents/showproperties.md)
