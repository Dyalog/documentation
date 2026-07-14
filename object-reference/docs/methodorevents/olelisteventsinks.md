# <span>OLEListEventSinks</span> <span>Method 542</span>

**Applies To:** [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)

**Description**

This method returns the names of *event sinks* that are currently connected to a COM object.

The list contains the names of all the event sinks that were connected automatically when the object was created, together with any that you have added subsequently using [OLEAddEventSink](./oleaddeventsink.md).

The OLEListEventSinks method is niladic.

The result is a vector of character vectors containing the names of the event sinks connected to the object.
