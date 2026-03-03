# Compiling With Global Names

When compiling a defined function or operator, the compiler needs to know the nameclass of every name that is used. It is useful to distinguish between local names (those that are defined in the function or operator being compiled) and non-local or global names (everything else).
```apl
foo←{
    n←⍵×2            ⍝ define local name n
    bar n            ⍝ use global name bar and local name n
}
```

If this fuction is compiled with [`2(400⌶)Y` ](compiler-control-ibeam.md#x-2-compile)`'foo'` , the compiler will determine the nameclass of global names by looking at the names that are currently defined in the workspace:

- If `bar` is undefined, then the compiler will not compile `foo`.
- If `bar` is defined, then the compiler will use its nameclass to determine whether it is an array, function or operator, and parse the body of `foo` accordingly.

In the latter case, the nameclass of `bar` is recorded in the compiled form of `foo` as a checked assumption; when `foo` is executed, if `bar` no longer exists or has a different nameclass, an error will be reported.

In more complex applications there could be a requirement to restrict the set of global functions and variables that compiled code can refer to, or it might be known in advance exactly which global variables and functions will exist when the application is run. In these situations, the application can be compiled with `N(400⌶)`, where `N` is a namespace containing callback functions that the compiler can use to determine the nameclass of any global names it encounters.

For example, to mimic the behaviour of `2(400⌶)`, the following callback functions can be defined in `#` (the root namespace):
```apl
      quadNC←⎕NC ⋄ quadAT←⎕AT     ⍝ define callback fns in #
      #(400⌶)'foo'                ⍝ pass in # as the namespace
```

More complicated definitions of the callback functions grant finer control over exactly which global names a compiled function is allowed to refer to.
