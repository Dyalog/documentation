# Creating .NET Classes with APL Source Files

New .NET classes can be defined and used within an APL Source file. This section provides a brief introduction to writing classes, aimed specifically at APL Source files – see the Dyalog APL Programming Reference Guide for more information on writing classes in Dyalog.

A class is defined by `:Class` and `:EndClass` statements:

- `:Class Name: Type` declares a new class called `Name`, which is based on the base class `Type`, which can be any valid .NET class.

- `:EndClass` terminates a class definition block.

The methods provided by the class are defined as function bodies enclosed within these statements. You can also define sub-classes or nested classes using nested `:Class` and `:EndClass` statements.

A class specified in this way will automatically support the methods, properties and events that it inherits from its base class, together with any new public methods that are specified. However, the new class only inherits a default constructor (which is called with no parameters) and does not inherit all of the other private constructors from its base class. You can define a method to be a constructor using the `:Implements Constructor` declarative comment. Constructor overloading is supported, and you can define any number of different constructor functions in this way, but they must have unique parameter sets for the system to distinguish between them.

You can create and use instances of a class by using the `⎕NEW` system function in statements elsewhere in the APL Source file.

For more information on creating .NET classes with APL Source files, see:

- [Section ](../dotnet-framework-interface-guide/exporting-functions-as-methods.md)

- [Section ](../dotnet-framework-interface-guide/example-creating-a-dotnet-class-using-an-apl-source-file.md)

- [Section ](../dotnet-framework-interface-guide/defining-properties.md)

- [Section ](../dotnet-framework-interface-guide/indexers.md)
