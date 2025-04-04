<h1 class="heading"><span class="name">Methods</span></h1>

When you create an instance of a COM object, the methods and the properties are directly accessible from the corresponding namespace.

## Calling Methods

You invoke a method in an OLE object as if it were an APL function in your workspace.

If a method takes no parameters, you must invoke it as if it were niladic.

If a method takes parameters, you must call it as if it were monadic. Each element of its argument corresponds to each of the method's parameters.

If a method takes a parameter declared as a string (VT_BSTR) you must call it with an **enclosed** character vector.

**Note:** In previous versions of Dyalog APL, a character vector was automatically enclosed if required. For backwards compatibility you may select old or new behaviour using `⎕WX`. If `⎕WX` is 3 (the default) you **must** enclose a single string argument. IF `⎕WX` is 0 or 1, you **may** supply a simple character vector.

For example, the OpenDatabase method in the DAO.DBEngine OLE server may be called with a single parameter that specifies the name of the database to be opened. You may call it from APL with either of the following two expressions:
```apl
     OpenDatabase 'c:\example.mdb' ⍝only if ⎕WX is 0 or 1
     OpenDatabase ⊂'c:\example.mdb'⍝any value of ⎕WX
 
```

## Arrays and Pointers

Many parameters to OLE methods are specified by pointers. If, for example, the parameter type is VT_BSTR, it means that the calling routine must supply a pointer to (that is, the address of) a character string.

Similarly, if the parameter type is defined to be VT_VARIANT, it means that the parameter is the address of an arbitrary array (the VT_VARIANT data type actually maps nicely onto a Dyalog APL nested array).

The rule is that if a pointer is required, APL will provide it automatically; you do not have to do so. Instead, all you do is supply the value.

## Optional Parameters

Methods are often defined to have optional parameters. For example the parameters defined for the OpenDatabase method provided by the DAO.DBEngine OLE object are:
```apl
 Name         VT_BSTR     
 [Exclusive]  VT_VARIANT  
 [ReadOnly]   VT_VARIANT  
 [Connect]    VT_VARIANT
```

To call the corresponding APL function, you may supply a nested array that contains 1,2, 3or 4 elements corresponding to these parameters.

The parameters to some methods are all optional. This means that the method may be called with or without any parameters. As APL does not support this type of syntax, the special value `⍬` (zilde) is used to mean "0 parameters".

For example, the parameters for the Idle method provided by DAO.DBEngine are defined to be:
```apl
 [Action]  VT_VARIANT
```

This means that the method takes either no arguments or one argument. To call it with no argument, you must use `⍬` (zilde), for example:
```apl
      Idle ⍬
```

Note that you cannot therefore call a function in an *APL* server with a single argument that is an empty numeric vector.

## Output Parameters

You may encounter parameters whose data type is defined explicitly as a pointer to something else, for example VT_PTR to VT_UI4 specifies a pointer to an unsigned 4-byte integer.

In these cases, it usually means that the calling routine is expected to pass an address into which the OLE method will place a value.

When you invoke the method you must use data of the type pointed to.

The result of the method is then a vector containing the result defined for the method, followed by the (new) values of the output parameters. This is similar to the mechanism used by `⎕NA`.

## Named Parameters

Visual Basic syntax allows you to specify parameters by position or by name; rather like `⎕WC` and `⎕WS`. For example the parameters defined for the OpenDatabase method provided by the DAO.DBEngine OLE object are:
```apl
 Name         VT_BSTR     
 [Exclusive]  VT_VARIANT  
 [ReadOnly]   VT_VARIANT  
 [Connect]    VT_VARIANT
```

You could call this method from Visual Basic using the syntax:
```apl
Set Db = OpenDatabase(Name:="c:\example.mdb",_
                      ReadOnly:=True)
```

You may do the same thing from Dyalog APL, using `⎕WS` syntax. For example, the equivalent call from APL would be:
```apl
      OpenDatabase('Name' 'c:\example.mdb')('ReadOnly' 1)
```

Note that you may only use named parameters if they are supported by the method. Many methods do not allow them.

## Methods that return Objects

Object hierarchies in OLE are not static, but are created dynamically by calling methods that return objects as their result.

If the data type of the result of a method is a pre-defined object type, or VT_DISPATCH or VT_COCLASS, or VT_PTR to VT_DISPATCH or VT_PTR to VT_COCLASS, the result returned to APL is a *namespace*. If the result is assigned to a name, the value associated with that name becomes a *namespace reference*. For example, GetMethodInfo tells us that the syntax for the OpenDatabase method provided by the OLE object DAO.DBEngine is as follows:
```apl
      ↑ DB.GetMethodInfo 'OpenDatabase'
 Opens a specified database  VT_DISPATCH 
 Name                        VT_BSTR     
 [Exclusive]                 VT_VARIANT  
 [ReadOnly]                  VT_VARIANT  
 [Connect]                   VT_VARIANT
```

The data-type of the result is VT_DISPATCH, so it returns an object; indeed the help for the method tells us that it returns a Database object. The function could be called from APL as follows:
```apl
      DB←OpenDatabase ⊂'example.mdb'
```

Alternatively, you may simply use the result as an argument to a defined function or as the argument to `⎕CS` or `:With`, thereby switching into the namespace returned by the method. For example:
```apl
      :With OpenDatabase ⊂'example.mdb'

      :EndWith
```

Notice that in both these cases, the namespace associated with the result of the OpenDatabase method is *unnamed*. Assigning the result of OpenDatabase to `DB` does not set the namespace *name* to `DB`, it merely assigns a namespace *reference* to `DB`.

To preserve compatibility with previous versions of Dyalog APL that did not support namespace references, a method that returns an object may be called with the name of the (new) namespace as its left argument. Note that OLE methods do not themselves accept left arguments, so this extension does not conflict with OLE conventions.
```apl
      'DB' OpenDatabase ⊂'example.mdb'
```

This expression creates a new namespace called `DB` associated with a new object in the OLE Server. Note that if you invoke the `OpenDataBase` method in this way, its result is a number that represents the *Dispatch Interface* of the new object. This is done to preserve compatibility with previous versions of Dyalog APL.
