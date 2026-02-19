# Using .NET Classes

To create a Dyalog object as an instance of a .NET class, the `⎕NEW` system function is used. The `⎕NEW` system function is monadic. It takes a 1 or 2-element argument, the first element of which is a class.

If the argument is a scalar or a 1-element vector, an instance of the class is created using the constructor overload that takes no argument.

If the argument is a 2-element vector, an instance of the class is created using the constructor overload  (see [Section 1.0.1](constructors-and-overloading.md)) whose argument matches the disclosed second element.

Example

Creating an instance of the DateTime class requires an argument with two elements: (the class and the constructor argument; in this example the constructor argument is a 3-element vector representing the date). Many classes provide a default constructor that takes no arguments. From Dyalog , the default constructor is called by calling `⎕NEW` with only a reference to the class in the argument.

To create a DateTime object whose value is 30 April 2008:
```apl
      ⎕USING←'System'
      mydt←⎕NEW DateTime (2008 4 30)

```

Alternatively, to use fully-qualified class names, one of the elements of `⎕USING` must be an empty vector:
```apl
      ⎕USING←,⊂''
      mydt←⎕NEW System.DateTime (2008 4 30)
```

In both cases, the result of  `⎕NEW` is a reference to the newly created instance:
```apl
      ⎕NC ⊂'mydt'
9.2
```

When a reference to a .NET object is formatted, APL calls its ToString method to obtain a useful description or identification of the object (this topic is discussed in more detail in [Section 1.0.1](displaying-a-dotnet-object.md)):
```apl
      mydt
30/04/2008 00:00:00
```
