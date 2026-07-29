# Using OLE Objects without Type Information

Even if an OLE Object fails to provide Type Information, either using early or late binding, you will still be able to access its methods and properties using a secondary form of late binding  or SetMethodInfo and SetPropertyInfo as follows.

## Secondary Late Binding[^1]

If you refer to a name inside the OLEClient namespace that would otherwise generate a `VALUE ERROR`, and there is no Type information available for that name, APL asks the COM object if it has a member (method or property) of that name.

The mechanism permits APL to determine only that the member is exported; it says nothing about its type (method or property) nor its syntax. If the response from the COM object is positive, APL therefore makes the most general assumption possible, namely:

- That the member is a method
- That it may take up to 16 optional arguments
- That each argument is input/output (that is, specified via a pointer)
- That the method returns a result.

This means that if you know, from its documentation or another source, that a COM object provides a certain Method or Property, you may therefore access that member by simply calling a function of that name in the OLEClient namespace. Note that any parameters you pass will be returned in the result, because APL assumes that all parameters are input/output. Furthermore, APL will be unable to check the validity of the parameters you specify because it does not know what data types are expected.

## SetMethodInfo and SetPropertyInfo

The SetMethodInfo and SetPropertyInfo methods provide a mechanism for you to precisely specify the missing Type Information for the methods and properties that you wish to use. See *Object Reference* for further details.

Note that whether you use late binding or SetMethodInfo/SetPropertyInfo, any sub-object namespaces that you create by invoking the methods and properties in the top-level object, will also have no visible methods and properties. Therefore, if the Type Information is missing, Late Binding or SetMethodInfo and SetPropertyInfo must be used to access all the methods and properties that you wish to use, wherever they occur in the object hierarchy.

## Events

When type library information is available, Dyalog APL automatically connects the appropriate event sinks and establishes the EventList property for the object when it is created. However, if the COM object does not declare its event sinks in a type library, or if the LateBind property were set to 1, it is necessary to connect to them manually. To support these cases, the following methods are used. These apply to top-level COM objects and to the namespaces associated with any other COM objects exposed by them.

|Method|Description|
|---|---|
|`OLEListEventSinks`|Returns the names of any event sinks currently attached to an object. An event sink is a set of events grouped (for convenience) by a COM object.|
|`OLEAddEventSink`|Attaches the namespace associated with an object to a specific event sink that it supports. If successful, new event names will appear in the EventList property of the namespace. This is the only way to access events from an event sink that is not described in the object's Type Information.|
|`OLEDeleteEventSink`|Removes the events associated with a particular event sink from the EventList property of the namespace associated with an object.|

[^1]: Prior to Version 14.0, this was the only form of late binding provided by Dyalog APL.
