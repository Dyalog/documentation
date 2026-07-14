# <span>ClassID</span> <span>Property</span>

**Applies To:** [ActiveXControl](../objects/activexcontrol.md), [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md), [OLEServer](../objects/oleserver.md)

**Description**

The ClassID property specifies the class identifier (usually abbreviated to CLSID) of an APL object that is used to represent a COM object. The CLSID is a globally unique identifier ([GUID](../miscellaneous/globally-unique-identifier-guid.md)) that uniquely identifies the object.

When you create or recreate an ActiveXControl or [OLEServer](../objects/oleserver.md) using `⎕WC`, you may specify ClassID. This allows you to re-use a value that was previously allocated to that control by the system. However, you should not specify any other value because that value could be allocated now or in the future to another object *on any other computer in the world*. Otherwise, a new ClassID is automatically allocated by the system.

Note that the CLSID is not actually recorded on your computer (in the registry) until you register it using `)SAVE` or *Make OCX*, or by executing the [OLERegister](../methodorevents/oleregister.md) method.
