# Creating a Concrete Version of a Generic Class

The class System.Collections.Generic.List is a generic class with one type parameter, which is the type of the elements of the list.

A concrete version of the List class can be created using `43⌶632`. For example, a list class that contains integers can be created as follows:
```apl
     IntList←System.Collections.Generic.List(43⌶632)System.Int32
     IntList
(System.Collections.Generic.List`1[System.Int32])
```

The shared members of the IntList class can then be accessed, and the class instantiated using `⎕NEW`. It is not necessary to give the constructed class a name.

The operations can also be combined and multiple type argument specified. For example:
```apl
    types←System.Char System.Int32
    ⎕NEW System.Collections.Generic.Dictionary (43⌶632) types
System.Collections.Generic.Dictionary`2[System.Char,System.Int32]

```

Attempting to instantiate a generic class without the expected number of type arguments generates an exception. For example:
```apl
    ⎕USING←''
    ⎕NEW System.Collections.Generic.List
EXCEPTION: Invalid number of generic type arguments applied (expected 1, got 0)
    ⎕NEW System.Collections.Generic.List
    ∧
```
