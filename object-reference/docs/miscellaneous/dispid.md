# DISPID (Dispatch ID)

COM objects created by Dyalog (OLEServer and ActiveXControl objects) export their members (methods, properties and events) using the standard *IDispatch* interface.

Using this interface, a client application may discover the names and parameters of the members supported by an object at run-time, and then access them by name. Alternatively, a client application may compile references to the object's members in advance  using their  *Dispatch IDs* or *DISPIDs*.

Prior to Version 14.1, Dyalog assigned all DISPIDs automatically[^1], making it impractical for them to be compiled into client applications.

From Version 14.1 onwards, the  SetFnInfo, SetPropertyInfo and SetEventInfo methods  allow the Dyalog programmer to assign DISPIDs so that they may be used directly by client applications. The specified DISPID must be a non-zero integer. The special value `¯1` causes Dyalog to assign the DISPID automatically as before.

## Note

Each of the DISPIDs exported by a COM object must be unique.  Furthermore, the behaviour of a COM object with non-unique DISPIDs is undefined. Non-unique DISPIDs may prevent the COM object from being registered (with or without generating an error) or may cause a run-time failure.  If Dyalog assigns all the DISPIDs of an object, they will be unique. If you choose to allocate your own DISPIDs to **any** of the members of a Dyalog COM object, the responsibility to ensure that they are **all** unique is yours. In this case, Dyalog does not guarantee nor check for uniqueness.

[^1]: An automatically assigned DISPID is its index into the list of the names of the object's members in alphabetic order, and may therefore change when this list is altered in any way.
