# Implementing an Object Hierarchy

Despite the close correspondence between the object model and Dyalog APL namespace technology, there is one significant difference. OLE does not support object hierarchies in the sense that one object *contains* or *owns* another.

Instead you must implement object hierarchies using *properties* that refer to other objects and/or *methods* that return objects as results.

It is not possible to pass Dyalog APL namespace hierarchies through OLE because OLE does not support them. If you want to write an OLE Automation Server in APL that implements an object hierarchy, you must follow the OLE conventions for doing so.

You can pass an *instance* of a Dyalog APL OLEServer namespace to an OLE client as a `⎕OR`, which can be the result of a function or the value of a variable. In order to be recognised as an OLE object, the namespace must be of type OLEServer.

In fact, when you export a workspace containing one or more OLEServer objects, any child OLEServer objects that they contain are registered too.

The CFILES Workspace (`samples\ole\cfiles.dws`) illustrates the use of an object hierarchy.
