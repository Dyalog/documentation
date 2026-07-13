# <span>RunMode</span> <span>Property</span>



**Applies To:** [OLEServer](../objects/oleserver.md)

**Description**


This property specifies the way in which an [OLEServer](../objects/oleserver.md) object serves multiple clients.



RunMode is a character vector and may be `'MultiUse'` (the default),  `'SingleUse'` or `'RunningObject'`.


If RunMode is `'MultiUse'`, OLE will load a single copy of Dyalog APL and the appropriate workspace into memory. All OLE client processes will communicate with the same Dyalog APL session.


Note that in this case, each OLE client is actually connected to a separate *instance* of the corresponding APL namespace. That is to say, each client will appear to have its own private copy of the namespace. However, the individual functions and variables in the namespace are not physically copied until they are changed. This means that, in general, OLE clients will share APL functions but have private copies of the namespace variables. However, please remember that global objects in the workspace or in other namespaces are not *instanced* and will effectively be shared by all clients although they are not directly accessible to them.


If RunMode is `'SingleUse'`, OLE will load a separate copy of Dyalog and a separate copy of the appropriate workspace into memory for each OLE client. Each OLE client operates directly on the namespace associated with the object and not an *instance* of it.


If RunMode is `'RunningObject'`, OLE will load a single copy of Dyalog and the appropriate workspace into memory. All OLE client processes will communicate with the same Dyalog session and indeed with the same namespace. The namespace is not *instanced* and all objects, including exported variables, are shared by all clients.


