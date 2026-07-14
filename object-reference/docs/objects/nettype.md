# <span>NetType</span> <span>Object</span>

[Parents](../parentlists/nettype.md), [Children](../childlists/nettype.md), [Properties](../proplists/nettype.md), [Methods](../methodlists/nettype.md), [Events](../eventlists/nettype.md)

**Purpose:** The NetType object is used to export a namespace as a Microsoft.NET class.

**Description**

The NetType object allows you to export an APL namespace as a .NET class that can be accessed by any conforming .NET client application.

The BaseClass property specifies the name of the .NET class from which the specified NetType object inherits. The default is System.Object.

When you create a NetType object, the name of its parent namespace specifies the name of  the corresponding Microsoft .NET Namespace to which the NetType class belongs. If the NetType is created as a child of root, the corresponding Microsoft .NET Namespace is unnamed.
