# <span>NetClient</span> <span>Object</span>

[Parents](../parentlists/netclient.md), [Children](../childlists/netclient.md)

**Purpose:** The NetClient object represents an instance of a Microsoft .NET class.

**Description**

The NetClient object represents an instance of a .NET class.

Normally, you create a NetClient object using the `New` method. For example:
```apl
      ⎕USING ←'System'
      DT1←DateTime.New 2002 4 30
      DT1.Type
NetClient
```

If, for any reason, you are unable to use the `New` method, you may create a NetClient object using  `⎕WC`. In this case, the ClassName property specifies the *full* name of the .NET class, and the ConstructorArgs property specifies the arguments for the constructor function if required.
```apl
      ⎕USING ←'System'
      'DT2'⎕WC'NetClient' 'System.DateTime'(1949 4 30)
      DT2.(Type ClassName ConstructorArgs)
 NetClient  System.DateTime  1949 4 30
```
