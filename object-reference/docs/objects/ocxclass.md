# <span>OCXClass</span> <span>Object</span>

[Parents](../parentlists/ocxclass.md), [Properties](../proplists/ocxclass.md), [Methods](../methodlists/ocxclass.md), [Events](../eventlists/ocxclass.md)

**Purpose:** This object provides access to OLE (ActiveX) Controls.

**Description**

This object loads an OLE Control into memory and defines a new class of object associated with it. The name of the new class is the name specified by the left argument of `⎕WC`  You may create an instance of the newly defined class using the name you assigned to the OCXClass object as the Type property.

Note that you may not create an instance of OCXClass using `⎕NEW`.

Once you have defined a new OCXClass, the properties, events and methods it supports may be obtained from its [PropList](../properties/proplist.md), [EventList](../properties/eventlist.md) and [MethodList](../properties/methodlist.md) properties. These are the properties, events and methods defined for the OLE control by its author.

The [QueueEvents](../properties/queueevents.md) property determines how events reported by the ActiveX control are handled.

To find out how to use the OLE control, you must consult the appropriate documentation. However, a great deal of information about it can be obtained using the [GetPropertyInfo](../methodorevents/getpropertyinfo.md), [GetEventInfo](../methodorevents/geteventinfo.md), and [GetMethodInfo](../methodorevents/getmethodinfo.md) methods.
