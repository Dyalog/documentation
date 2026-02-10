# Writing .NET Classes

Dyalog allows you to build new .NET classes, components and controls:

- A component is a class with emphasis on clean-up and containment, and implements specific interfaces.

- A control is a component with user interface capabilities.

.NET classes created by Dyalog can be hosted by any application or programming language that supports .NET.

With one exception, every .NET class inherits from exactly one base class. This means that it begins with all of the behaviour of the base class, in terms of the base class properties, methods and events. You can add functionality by defining new properties, methods and events on top of those inherited from the base class, or by overriding base class methods with those of your own.
