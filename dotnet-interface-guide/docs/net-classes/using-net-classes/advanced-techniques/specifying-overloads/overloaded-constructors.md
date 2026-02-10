# Overloaded Constructors

If a class provides constructor overloads, then a similar mechanism is used to specify which of the constructors is to be used when an instance of the class is created using `⎕NEW`.

For example, if MyClass is a .NET class with an overloaded constructor, and one of its constructors is defined to take two parameters; a double and an int, then the following statement would create an instance of the class by calling that specific constructor overload:
```apl
      (⎕NEW ⍠ (⊂Double Int32)) MyClass (1 1)
```
