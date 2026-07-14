# <span>OLEUnregister</span> <span>Method 531</span>

**Applies To:** [OLEServer](../objects/oleserver.md)

**Description**

This method is used to unregister an [OLEServer](../objects/oleserver.md) object that has previously been saved by Dyalog APL.

The OLEUnregister method is niladic.

This method removes all traces of the object from the Windows registry and erases its Type Library file.

Note that the name of the object removed from the registry is the name of the [OLEServer](../objects/oleserver.md) object prefixed by the string "dyalog."
