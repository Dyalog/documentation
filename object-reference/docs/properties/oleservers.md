# <span>OLEServers</span> <span>Property</span>

**Applies To:** [Root](../objects/root.md)

**Description**

The OLEServers property is a read-only property that reports the names and CLSIDs of all the OLE Automation servers installed on your computer. This information comes from the Windows registry.

Its value is a nested vector with one element per OLE Server.

Each element is a vector of 2-element character vectors. The first is the name of the OLE Server; the second is its class identifier or CLSID which is a type of [GUID](../miscellaneous/globally-unique-identifier-guid.md).
