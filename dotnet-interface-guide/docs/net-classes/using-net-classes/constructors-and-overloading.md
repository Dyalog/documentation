# Constructors and Overloading

Each .NET class has one or more constructor methods. These are called to initialise an instance of the class. Typically, a class will support several constructor methods, each with a different set of parameters. For example, System.DateTime supports a constructor that takes three Int32 parameters (year, month, day), another that takes six Int32 parameters (year, month, day, hour, minute, second), and various other constructors. These different constructor methods are not distinguished by having different names but by the different sets of parameters that they accept.

This concept, which is known as overloading, may seem somewhat alien to the APL programmer, who will be accustomed to defining functions that accept an arbitrary array. However, type checking, which is fundamental to .NET, requires that a method is called with the correct number of parameters, and that each parameter is of a predefined type. Overloading solves this issue.

When creating an instance of a class in C#, the `new` operator is used. At compile time, this is mapped to the appropriate constructor overload by matching the user-supplied parameters to the various forms of the constructor. A similar mechanism is implemented in Dyalog by the `⎕NEW` system function.
