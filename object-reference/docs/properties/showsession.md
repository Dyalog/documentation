# <span>ShowSession</span> <span>Property</span>

**Applies To:** [OLEServer](../objects/oleserver.md)

**Description**

This property specifies whether or not the APL Session window is displayed when an [OLEServer](../objects/oleserver.md) object is started by an OLE client.

Its default value is 0 (hide Session).

Note that if [RunMode](runmode.md) is `'MultiUse'`, you may not in any way access the *instances* of the object that are being controlled by the client applications, even if only a single client is connected.
