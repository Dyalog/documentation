<h1 class="heading"><span class="name">Introduction</span></h1>

.NET classes are implemented as part of the Common Type System. The Type System provides the rules by which different languages can interact with one another. *Types* include interfaces, value types and classes. The .NET Framework provides built-in primitive types plus higher-level types that are useful in building applications.

A *Class* is a kind of Type (as distinct from interfaces and value types) that encapsulates a particular set of methods, events and properties. The word *object* is usually used to refer to an *instance* of a class. An object is typically created by calling the system function `⎕NEW`, with the class as the first element of the argument.

Classes support inheritance in the sense that every class (but one) is based upon another so-called *Base Class*.

An assembly is a file that contains all of the code and metadata for one or more classes. Assemblies can be dynamic (created in memory on-the-fly) or static (files on disk). For the purposes of this document, the term Assembly refers to a file (usually with a .DLL extension) on disk.
