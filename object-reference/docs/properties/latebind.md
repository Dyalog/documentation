# <span>LateBind</span> <span>Property</span>

**Applies To:** [OLEClient](../objects/oleclient.md), [OLEServer](../objects/oleserver.md)

**Description**

LateBind is a Boolean property that determines whether or not the Type Information is read when an [OLEClient](../objects/oleclient.md) object is instantiated, or when an [OLEServer](../objects/oleserver.md) references a COM object. It must be set when the [OLEClient](../objects/oleclient.md) or [OLEServer](../objects/oleserver.md) object is created and cannot subsequently be changed.

If LateBind is 0 (the default) the Type information is obtained, in its entirety, when the [OLEClient](../objects/oleclient.md) object is instantiated or when an [OLEServer](../objects/oleserver.md) processes a reference to an external COM object.

If LateBind is 1, APL postpones the calls to obtain Type Information until a particular property, method or event of the COM object is referenced; and then only for that particular member.
