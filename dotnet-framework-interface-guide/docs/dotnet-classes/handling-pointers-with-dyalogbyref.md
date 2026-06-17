<h1 class="heading"><span class="name">Handling Pointers with Dyalog.ByRef</span></h1>

Certain .NET methods take parameters that are pointers, for example, the <code class="language-nonAPL">DivRem</code> method that is provided by the <code class="language-nonAPL">System.Math</code> class. This method performs an integer division, returning the quotient as its result, and the remainder in an address specified as a pointer by the calling program.

APL does not have a mechanism for dealing with pointers, so Dyalog provides a .NET class for this purpose. This is the <code class="language-nonAPL">Dyalog.ByRef</code> class, which is provided by an Assembly that is automatically loaded by Dyalog).

To gain access to the Dyalog .NET namespace, it must be specified by `⎕USING`. The assembly (DLL) from which it is obtained (the **Dyalog.Net.Bridge.dll** file) does not need to be specified as it is automatically loaded when Dyalog starts:
```apl
      ⎕USING←'System' 'Dyalog'
```

The <code class="language-nonAPL">Dyalog.ByRef</code> class represents a pointer to an object of type <code class="language-nonAPL">System.Object</code>. It has a number of constructors, some of which are used internally by Dyalog. Only two of these are of particular interest – the one that takes no parameters, and the one that takes a single parameter of type <code class="language-nonAPL">System.Object</code>. The former is used to create an empty pointer; the latter to create a pointer to an object or some data.

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

The <code class="language-nonAPL">ByRef</code> class has a single property called <code class="language-nonAPL">Value</code>:
```apl
      ptr2.Value
0

      ptr3.Value
1 2 3 4 5 6 7 8 9 10

      ptr4.Value
30/04/2000 00:00:00
```

If the <code class="language-nonAPL">Value</code> property is referenced without first setting it, a `VALUE ERROR` is returned:
```apl
      ptr1.Value
VALUE ERROR
      ptr1.Value
     ^
```

Returning to the example, the <code class="language-nonAPL">DivRem</code> method takes 3 parameters:

1. the numerator
2. the denominator
3. a pointer to an address into which the method will write the remainder after performing the division
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

Sometimes a .NET method can take a parameter that is an array, and the method expects to populate the array with appropriate values. In APL there is no syntax to allow a parameter to a function to be modified in this way. However, the <code class="language-nonAPL">Dyalog.ByRef</code> class can be used to call this method. For example, the <code class="language-nonAPL">System.IO.FileStream</code> class contains a <code class="language-nonAPL">Read</code> method that populates its first argument with the bytes in the file:
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
