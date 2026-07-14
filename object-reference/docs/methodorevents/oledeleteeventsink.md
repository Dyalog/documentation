# <span>OLEDeleteEventSink</span> <span>Method 541</span>

**Applies To:** [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)

**Description**

This method disconnects a named event sink from a COM object and removes the events defined by that event sink from the [EventList](../properties/eventlist.md) property of the associated namespace.

This method may be used to remove an event sink that was established automatically when the OLE object was created.

The argument to OLEDeleteEventSink is a single item as follows:

|-----|---------------|----------------|
|`[1]`|Event sink name|character vector|
