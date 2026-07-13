# <span>InstanceMode</span> <span>Property</span>



**Applies To:** [OLEClient](../objects/oleclient.md)

**Description**


The InstanceMode property specifies how APL attempts to connect the [OLEClient](../objects/oleclient.md) to an OLE Server.


InstanceMode is a character vector that may be `'ExistingFirst'` (the default), `'ExistingOnly'` or `'New'`. Its value is effective only when the object is created with `⎕WC`. Changing InstanceMode with `⎕WS` has no effect.


If InstanceMode is `'ExistingFirst'`, APL attempts first to connect to a running instance of the OLE Server. If there is no running instance, it starts the OLE server to obtain a new object.


If InstanceMode is `'ExistingOnly'`, APL attempts to connect to a running instance of the object. If there is no running instance, it fails with a `DOMAIN ERROR`.


Note that in either case, if there is more than one instance running, there is no way to predict to which instance APL will be connected.


If InstanceMode is `'New'`, APL attempts to start the OLE Server to obtain a new object, whether or not the OLE Server is already running. However, if the OLE Server has registered itself as a single instance object and is already running, APL will be connected to it, and a second instance of the Server will not in fact be started.


