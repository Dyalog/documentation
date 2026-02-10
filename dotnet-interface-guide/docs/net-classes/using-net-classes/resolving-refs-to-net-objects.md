# Resolving References to .NET Objects

When Dyalog executes an expression such as
```apl
      mydt←⎕NEW DateTime (2008 4 30)
```

the following logic is used to resolve the reference to DateTime correctly.

The first time that Dyalog encounters a reference to a non-existent name (that is, a name that would otherwise generate a `VALUE ERROR`), it searches the .NET namespaces/assemblies specified by `⎕USING` for a .NET class of that name. If found, the name (in this case, System.DateTime) is recorded in the APL symbol table with a name class of 9.6 and is associated with the corresponding .NET Type. If not found, then `VALUE ERROR` is reported as usual. This search ONLY takes place if `⎕USING` has been assigned a non-empty value.

Subsequent references to that symbol (in this case DateTime) are resolved directly and do not involve any assembly searching.

If `⎕NEW` is called with only a class as argument, then Dyalog attempts to call the overload of its constructor that is defined to take no arguments. If no such overload exists, then the call fails with a `LENGTH ERROR`.

If `⎕NEW` is called with a class as argument and a second element, then Dyalog calls the version of the constructor whose parameters match the second element supplied to `⎕NEW`. If no such overload exists, then the call will fail with either a `LENGTH ERROR` or a `DOMAIN ERROR`.
