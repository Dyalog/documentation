# <span>SetMethodInfo</span> <span>Method 556</span>

**Description**

This method is used to redefine the arguments or data types associated with a method that is exported by a COM object. SetMethodInfo is used to override the information provided by the object's Type Library.

The argument to SetMethodInfo is a 2 or 3-element array as follows:

|-----|------------|-------------------------|
|`[1]`|Method name |character vector         |
|`[2]`|Method info |nested vector (see below)|
|`[3]`|Method index|integer                  |

If you wish to describe the method completely, the structure of *Method info* should be identical to the structure returned by GetMethodInfo, although abbreviated formats are also allowed.

If the object exports the method directly, and not through the standard IDispatch interface, you must also specify *Method Index*, which is the index of the method in the object's virtual table (vtable). This information may be available in printed documentation or in a C-language header file.

For example, the InchesToPoint method exported by *Excel.Application* takes a single argument whose name is *Arg1* and whose data type is VT_R8. The function returns a result of the same data type. The details provided in the *Excel.Application* Type Library are in fact correct, but if you wanted to redefine them, the following statements could be used to describe the InchesToPoints method.
```apl
      'EX' ⎕WC 'OLEClient' 'Excel.Application' ('AutoBrowse' 0)

      methodinfo← ('' 'VT_R8')('Arg1' 'VT_R8')
      EX.SetMethodInfo 'InchesToPoints' methodinfo
```

Note that the structure of variable `methodinfo` is identical to the result of the GetMethodInfo method.
```apl
      DISPLAY methodinfo
┌→───────────────────────────────────┐
│ ┌→────────────┐ ┌→───────────────┐ │
│ │ ┌⊖┐ ┌→────┐ │ │ ┌→───┐ ┌→────┐ │ │
│ │ │ │ │VT_R8│ │ │ │Arg1│ │VT_R8│ │ │
│ │ └─┘ └─────┘ │ │ └────┘ └─────┘ │ │
│ └∊────────────┘ └∊───────────────┘ │
└∊───────────────────────────────────┘

      DISPLAY EX.GetMethodInfo 'InchesToPoints'
┌→───────────────────────────────────┐
│ ┌→────────────┐ ┌→───────────────┐ │
│ │ ┌⊖┐ ┌→────┐ │ │ ┌→───┐ ┌→────┐ │ │
│ │ │ │ │VT_R8│ │ │ │Arg1│ │VT_R8│ │ │
│ │ └─┘ └─────┘ │ │ └────┘ └─────┘ │ │
│ └∊────────────┘ └∊───────────────┘ │
└∊───────────────────────────────────┘
```

Unless you are going to call the method using the names of its arguments, these names are clearly superfluous and may be omitted, for example:
```apl
      methodinfo← 'VT_R8' 'VT_R8'
      EX.SetMethodInfo 'InchesToPoints' methodinfo 
```

**Application**

Objects: [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)
