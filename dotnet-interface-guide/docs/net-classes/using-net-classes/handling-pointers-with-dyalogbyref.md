# Handling Pointers with Dyalog.ByRef

Certain .NET methods take parameters that are pointers, for example, the DivRem method that is provided by the System.Math class. This method performs an integer division, returning the quotient as its result, and the remainder in an address specified as a pointer by the calling program.

APL does not have a mechanism for dealing with pointers, so Dyalog provides a .NET class for this purpose. This is the Dyalog.ByRef class, which is provided in **Dyalog.Net.Core.Bridge.dll** (which is automatically loaded by Dyalog).

To gain access to the Dyalog .NET namespace, it must be specified by `⎕USING`. The assembly (DLL) from which it is obtained (the **Dyalog.Net.Bridge.dll** file) does not need to be specified as it is automatically loaded when Dyalog starts:
```apl
      ⎕USING←'System.IO,System.IO.FileSystem' 'Dyalog'
```

The Dyalog.ByRef class represents a pointer to an object of type System.Object. It has a number of constructors, some of which are used internally by Dyalog. Only two of these are of particular interest – the one that takes no parameters, and the one that takes a single parameter of type System.Object. The former is used to create an empty pointer; the latter to create a pointer to an object or some data.

For example, to create an empty pointer:
```apl
      ptr1←⎕NEW ByRef
```

or, to create pointers to specific values:
```apl
      ptr2←⎕NEW ByRef 0
      ptr3←⎕NEW ByRef (⊂⍳10)
      ptr4←⎕NEW ByRef (⎕NEW DateTime (2000 4 30))
```

As a single parameter is required, it must be enclosed if it is an array with several elements. Alternatively, the parameter can be a .NET object.

The ByRef class has a single property called Value:
```apl
      ptr2.Value
0
```
```apl

      ptr3.Value
1 2 3 4 5 6 7 8 9 10
```
```apl
      ptr4.Value
30/04/2000 00:00:00
```

If the Value property is referenced without first setting it, a `VALUE ERROR` is returned:
```apl
      ptr1.Value
VALUE ERROR
      ptr1.Value
     ^
```

Returning to the example, the DivRem method takes 3 parameters:

1. the numerator
2. the denominator
3. a pointer to an address into which the method will write the remainder after performing the division
```apl
      remptr←⎕NEW ByRef
      remptr.Value
VALUE ERROR
      remptr.Value
     ^
```
```apl

      Math.DivRem 311 99 remptr
3
      remptr.Value
14
```

Sometimes a .NET method can take a parameter that is an array and the method expects to fill in the array with appropriate values. In APL there is no syntax to allow a parameter to a function to be modified in this way. However, the Dyalog.ByRef class can be used to call this method. For example, the System.IO.FileStream class contains a Read method that populates its first argument with the bytes in the file:
```apl
      ⎕USING←'System.IO' 'Dyalog' 'System'
      fs←⎕NEW FileStream ('c:\tmp\jd.txt' FileMode.Open) 
      fs.Length
25
```
```apl

      fs.Read(arg←⎕NEW ByRef,(⊂25⍴0))0 25
25
```
```apl
      arg.Value
104 101 108 108 111 32 102 114 111 109 32 106 111 104 110 32 100 97 105 110 116 114 101 101 10
```
