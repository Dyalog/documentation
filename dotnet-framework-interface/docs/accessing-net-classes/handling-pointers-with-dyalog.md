<h1 class="heading"><span class="name">Handling Pointers with Dyalog.ByRef</span></h1>

Certain .NET methods take parameters that are pointers.

An example is the `DivRem` method that is provided by the `System.Math` class. This method performs an integer division, returning the quotient as its result, and the remainder in an address specified as a pointer by the calling program.

APL does not have a mechanism for dealing with pointers, so Dyalog provides a .NET class for this purpose. This is the `Dyalog.ByRef` class, which is a provided by an Assembly that is loaded automatically by the Dyalog program.

Firstly, to gain access to the Dyalog .NET Namespace, it must be specified by `⎕USING`. Note that you need not specify the Assembly (DLL) from which it is obtained (the  Bridge DLL), because (like `mscorlib.dll`) it is automatically loaded by when APL starts.
```apl
      ⎕USING←'System' 'Dyalog'
```

The `Dyalog.ByRef` class represents a pointer to an object of type `System.Object`. It has a number of constructors, some of which are used internally by APL itself. You only need to be concerned about two of them; the one that takes no parameters, and the one that takes a single parameter of type `System.Object`. The former is used to create an empty pointer; the latter to create a pointer to an object or some data.

For example, to create an empty pointer:
```apl
      ptr1←⎕NEW ByRef
```

Or, to create pointers to specific values,
```apl
      ptr2←⎕NEW ByRef 0
      ptr3←⎕NEW ByRef (⊂⍳10)
      ptr4←⎕NEW ByRef (⎕NEW DateTime (2000 4 30))
```

Notice that a single parameter is required, so you must enclose it if it is an array with several elements. Alternatively, the parameter may be a .NET object.

The ByRef class has a single property called `Value`.
```apl
      ptr2.Value
0
      ptr3.Value
1 2 3 4 5 6 7 8 9 10
      ptr4.Value
30/04/2000 00:00:00
```

Note that if you reference the Value property without first setting it, you get a `VALUE ERROR`.
```apl
      ptr1.Value
VALUE ERROR
      ptr1.Value
     ^
```

Returning to the example, we recall that the `DivRem` method takes 3 parameters:

1. the numerator
2. the denominator
3. a pointer to an address into which the method will write the remainder after performing the division.
```apl
      remptr←⎕NEW ByRef
      remptr.Value
VALUE ERROR
      remptr.Value
      ^
      Math.DivRem 311 99 remptr
3
      remptr.Value
14
```

In some cases a .NET method may take a parameter that is an Array and the method expects to fill in the array with appropriate values. In APL there is no syntax to allow a parameter to a function to be modified in this way. However, we can use the `Dyalog.ByRef` class to call this method. For example, the `System.IO.FileStream` class contains a `Read` method that populates its first argument with the bytes in the file.
```apl
      ⎕USING←'System.IO' 'Dyalog' 'System'
      fs←⎕NEW FileStream ('c:\tmp\jd.txt' FileMode.Open) 
      fs.Length
25
      fs.Read(arg←⎕NEW ByRef,⊂⊂25⍴0)0 25
25
      arg.Value
104 101 108 108 111 32 102 114 111 109 32 106 111 104 110 32 100 97 105 110 116 114 101 101 10
```
