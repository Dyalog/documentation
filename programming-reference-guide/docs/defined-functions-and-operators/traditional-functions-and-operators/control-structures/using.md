# :Using Statement

```apl
:Using <NameSpace[,Assembly]>
```

This statement specifies a .NET namespace that is to be searched to resolve unqualified names of .NET types referenced by expressions in the Class.

|Element|Description|
|---|---|
|`NameSpace`|Specifies a .NET namespace.|
|`Assembly`|Specifies the Assembly in which NameSpace is located. If the Assembly is located in the Microsoft.NET installation directory, you need only specify its name. If not, you must specify a full or relative pathname.|

If the Microsoft .NET Framework is installed, the System namespace in`mscorlib.dll` is automatically loaded when Dyalog APL starts. To access this namespace, it is not necessary to specify the name of the Assembly.

When the class is fixed, `⎕USING` is inherited from the surrounding space. Each `:Using` statement appends an element to `⎕USING`, with the exception of `:Using` with no argument:

If you omit `<Namespace>`, this is equivalent to clearing `⎕USING`, which means that no .NET namespaces will be searched (unless you follow this statement with additional `:Using` statements, each of which will append to `⎕USING`).

To set `⎕USING`, to a single empty character vector, which only allows references to fully qualified names of classes in `mscorlib.dll`, you must write:

`:Using ,` (note the presence of the comma)

or

`:Using ,mscorlib.dll`

that is, specify an empty namespace name followed by no assembly, or followed by the default assembly, which is always loaded.
