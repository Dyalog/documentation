# Using an OLE Server

You can access an OLE Automation Server (also known as COM Server) using the OLEClient object. When you create an OLEClient, you specify the name of the Server as the ClassName property for the object.

For example:

```apl
    EX←⎕NEW 'OLEClient' (⊂'ClassName' 'Excel.Application')
```

or, using `⎕WC`

```apl
   'EX'⎕WC'OLEClient' 'Excel.Application'
```

The effect of both statements is to create an object `EX`, which is connected to an instance of the of the Excel.Application Class, an OLE Server. The OLE Server instance may be *in-process* or *out-of-process*. If it is in-process, the code and data associated with the instance are loaded into the same address space as the Dyalog APL process. In the latter case, the instance represents a separate Windows process on your computer or, on an entirely different computer in the network.

When APL connects to an out-of-process OLE Server in this way, you can specify whether you wish to connect to an existing (running) instance of the Server, or start a new copy of the Server. This is done using the InstanceMode property.
