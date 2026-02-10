# Displaying a .NET Object

When you display a reference to a .NET object, APL calls the object's ToString method and displays the result. All objects provide a ToString method because all objects ultimately inherit from the .NET class System.Object, which provides a default implementation. Many .NET classes provide their own ToString that overrides the one inherited from System.Object and returns a useful representation of the object in question. ToString usually supports a range of calling parameters, but APL always calls the version of ToString that is defined to take no calling parameters. The monadic format function (`⍕`) and monadic `⎕FMT` have been extended to provide the same result and provide a shorthand method to call ToString. The default ToString supplied by System.Object returns the name of the object's Type. For a particular object in the namespace, this can be changed using the system function `⎕DF`.

Example
```apl
      ⎕USING←'System'
      z←⎕NEW DateTime ⎕TS
      z.(⎕DF(⍕DayOfWeek),,'G< 99:99>'⎕FMT 100⊥Hour Minute)
      z
Saturday 09:17

```

The type of an object can be obtained using the GetType method, which is supported by all .NET objects:
```apl
      z.GetType
System.DateTime
```
