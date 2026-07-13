# <span>GetPropertyInfo</span> <span>Method 550</span>



**Applies To:** [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)

**Description**


This method is used to obtain information about a particular property or set of properties supported by a COM object.



For each property supported by a COM object, the author will have registered the property name, its data type, and an optional help message or description of the property. GetPropertyInfo returns this information.



The argument to GetPropertyInfo is a single item as follows:


|-----|----------------|---------|
|`[1]`|Property name(s)|see below|


*Property name(s)* is a simple character vector or a vector of character vectors specifying one or more names of properties supported by the object.



The result is a nested vector with one element per property name. Each element of this vector is itself a 2-element vector of character vectors containing the data type and help message for the corresponding property.

<h2 class="example">Example</h2>
```apl
      CLNAME←'Microsoft Multimedia Control, Version 6.0'
      'MM' ⎕WC 'OCXClass' CLNAME
      MM.PropList
 Type  DeviceType  AutoEnable  PrevVisible ...

      DISPLAY ↑MM.GetPropertyInfo 'PrevVisible'
┌→──────────────────────────────────────────────────────┐
↓ ┌→────────────────────────────────────────┐ ┌→──────┐ │
│ │Determines if the Prev button is visible.│ │VT_VOID│ │
│ └─────────────────────────────────────────┘ └───────┘ │
│ ┌→─┐                                        ┌→──────┐ │
│ │⌈P│                                        │VT_BOOL│ │
│ └──┘                                        └───────┘ │
└∊──────────────────────────────────────────────────────┘
```


If the data type of a property is VT_USERDEFINED, it means that the property may assume one of a set of values defined by a type list. In this case, the name of the type list is returned in place of the string "VT_USERDEFINED". Further information can be obtained using [GetTypeInfo](gettypeinfo.md) with this name as a parameter.


