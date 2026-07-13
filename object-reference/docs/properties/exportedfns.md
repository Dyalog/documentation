# <span>ExportedFns</span> <span>Property</span>

**Applies To:** [OLEServer](../objects/oleserver.md)

**Description**

This property specifies the functions to be exposed as methods by an [OLEServer](../objects/oleserver.md) object.

ExportedFns may be set to 0 (none), 1 (all), or a vector of character vectors containing the names of the functions to be exported.

There are certain important restrictions concerning the type of function that you can export as a method.

Firstly, only top-level defined functions within the [OLEServer](../objects/oleserver.md) may be exported; you cannot export functions in other namespaces including sub-namespaces.

Furthermore, you may not export defined operators, dfns, external functions, or functions created by function assignment.

Finally, OLE does not support the concept of a dyadic function, so your exported functions must be niladic, monadic, or take an optional left argument; they may not be explicitly dyadic.

If you wish to export a new function from your [OLEServer](../objects/oleserver.md), and ExportedFns is not 1, you must explicitly reset the value of the ExportedFns property before you re-save the workspace.
