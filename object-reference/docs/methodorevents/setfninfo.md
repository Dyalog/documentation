# <span>SetFnInfo</span> <span>Method 545</span>

**Applies To:** [ActiveXControl](../objects/activexcontrol.md), [OLEServer](../objects/oleserver.md)

**Description**

This method is used to describe an APL function that is to be exported as a method, a Property Get Function, or a Property Put Function of an [ActiveXControl](../objects/activexcontrol.md) or [OLEServer](../objects/oleserver.md) object.

An exported function must be a niladic or monadic defined function (dfns and derived functions are not allowed) and may optionally return a result. Ambivalent functions (functions with optional left argument) are allowed, but will be called monadically by the host application.

COM syntax differs from APL syntax in many ways and the SetFnInfo method is required to declare an APL function to COM in terms that COM understands. In particular, although monadic APL functions take just one argument, COM functions may take several parameters, and some may be optional.

A function exported by SetFnInfo will be called by a host application with the number of parameters that SetFnInfo has described. The argument received when the function is called by a host application, will be a nested vector of this length.

The argument to SetFnInfo is a 2, 3, 4, 5 or 6-element array as follows:

|-----|-------------|---------------------------------------------------------------|
|`[1]`|Function name|character vector                                               |
|`[2]`|Function info|nested array (see below)                                       |
|`[3]`|Help ID      |integer                                                        |
|`[4]`|Function type|integer                                                        |
|`[5]`|Property name|character vector                                               |
|`[6]`|DISPID       |integer. See [DISPID (Dispatch ID)](../miscellaneous/dispid.md)|

## Function info

This specifies an optional help string which describes what the function does, the data type of the result (if any) and the names and data types of its arguments.

If the function syntax is fully described, each element of *Function Info* is a 2-element vector of character vectors. The first element contains the help string and the [COM data type](../miscellaneous/com-data-types.md) of the function's result. Subsequent elements contain the name and [COM data type](../miscellaneous/com-data-types.md) of each parameter.

However, both the help string and the names of the parameters are optional and may be omitted. If so, one or more elements of *Function Info* may be a simple character vector.

Consider a very basic function `ADD` in an [ActiveXControl](../objects/activexcontrol.md) called `F.dbase`, that is designed to add a record to a personnel database. The database consists only of a list of names, ages and addresses.

Function `ADD` expects to be called with a name (character string), age (number) and address (character string), and returns a result 0 or 1 (Boolean) according to whether the record was successfully added. This function could be declared as follows:
```apl
      HELP←'Adds a new record to the personnel database'
      SPEC←⊂(HELP 'VT_BOOL')      ⍝ Result is Boolean     
      SPEC,←⊂('Name' 'VT_BSTR')   ⍝ 1st param called 'Name' is a string   
      SPEC,←⊂('Age' 'VT_I4')      ⍝ 2nd param called 'Age' is an integer  
      SPEC,←⊂('Address' 'VT_BSTR')⍝ 3rd param called 'Address' is a string

      F.dbase.SetFnInfo 'ADD' SPEC
```

Alternatively, but much less helpfully, the function could be declared to take a single unnamed nested argument, leaving it to the host application programmer to guess at its structure :
```apl
      SPEC←⊂('' 'VT_BOOL')              ⍝ No help string, result is Boolean
      SPEC,←⊂('' 'VT_ARRAY OF VT_VARIANT') ⍝ Param is a nested array
      F.dbase.SetFnInfo 'ADD'SPEC
```

## Help ID

This is an integer value that identifies the help context id within the help file associated with the HelpFile property of the [ActiveXControl](../objects/activexcontrol.md) object. The value `¯1` means that no help is provided. APL stores this information in the registry from where it may be retrieved by the host application.

## Function type

This specifies the type of function being exported. This is an integer with one of the following values:

|---|-----------------------------------|
|1  |Function is a method               |
|2  |Function is a property get function|
|4  |Function is a property put function|

In both these last two cases, the name of the property, which is totally independent of the name of the APL function, is given as *Property name*.

If omitted, the function type is *method*.
