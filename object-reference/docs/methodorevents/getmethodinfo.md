# <span>GetMethodInfo</span> <span>Method 552</span>

**Description**

This method is used to obtain information about a particular method or set of methods supported by a COM object.

For each method supported by a COM object the author will have registered a help message or description of the method (this is in fact optional), the data type of its result (if it has a result), and the name and data type of each of the parameters that must be supplied when you invoke it. The GetMethodInfo method returns this information.

The argument to GetMethodInfo is a single item as follows:

|-----|--------------|---------|
|`[1]`|Method name(s)|see below|

*Method name(s)* is a simple character vector or a vector of character vectors specifying one or more names of methods supported by the object.

The result is a nested vector with one element per method name. Each element of this vector is itself a vector of 2-element character vectors. For each method, the first item describes the help message or description (if any) registered for the method and the data type of its result. Note that if the event does not produce a result, the data type of the result is reported as `'VT_VOID'`. Each of the remaining elements contains a parameter name and its corresponding data type.

<h2 class="example">Example</h2>
```apl
      CLNAME←'Microsoft Multimedia Control, Version 6.0'
      'MM' ⎕WC 'OCXClass' CLNAME
      MM.MethodList
 AboutBox  Refresh  OLEDrag

      DISPLAY ↑ MM.GetMethodInfo 'AboutBox'
┌→──────────────┐
↓ ┌⊖┐ ┌→──────┐ │
│ │ │ │VT_VOID│ │
│ └─┘ └───────┘ │
└∊──────────────┘
```

**Application**

Objects: [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)
