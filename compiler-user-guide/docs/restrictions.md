# Restrictions

There are several restrictions when using the compiler, some of which might be removed in later versions.

## Restriction 1

__A function that uses semi-global names cannot be compiled.__

To compile a function, the compiler needs to be able to determine the nameclass of every name used in that function so that it knows whether it refers to an array, a function or an operator.

For local names, the compiler can identify the nameclass because it can see the definition of the name:
```apl
sum←{
    f←+         ⍝ compiler sees this definition...
    f/⍵         ⍝ ... so knows that f is a function here
}
```

For global names, [callbacks from `400⌶`](compiler-control-ibeam.md#x-is-a-namespace-compile-with-callbacks)) enable the compiler to identify the nameclass.

However, for semi-global names (that is, names that are local to the function that calls the function to be compiled) the compiler cannot determine the nameclass:
```apl
∇ r←sum y       ⍝ if f is defined in sum's caller, then...
  r←f/y         ⍝ ...this could be +/y, or 2/y, etc.
∇
```

## Restriction 2

__A function that calls system functions which refer to values by name or create new named values cannot be compiled.__

Compiled functions can use local names but, as part of the compilation process, the compiler discards these names, so they do not appear in the compiled bytecode. For this reason, system functions that refer to values by name, or create new named values, are prohibited:
```apl
foo←{
    a←⍺+⍵       ⍝ local name 'a' is discarded by compiler
    r←⎕NL 2     ⍝ ⎕NL is prohibited as it needs to see 'a'
    'a'⎕NS''    ⍝ ⎕NS is prohibited as it redefines 'a'
}
```

## Restriction 3

__A function that uses the dot syntax for namespace references cannot be compiled.__

The compiler cannot determine the nameclass of a name when the dot syntax is used to refer to names inside arbitrary namespaces:
```apl
sum←{
    ⍺.f / ⍵         ⍝ ⍺.f could be an array or a function
}
```
```apl
prod←{
    #.util.prod ⍵   ⍝ nameclass of util and prod unknown
}
```

## Restriction 4

__A function that includes certain control structures cannot be compiled.__

The following control structures prevent a function from being compiled:

- [`:Trap`](../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/trap)

- [`:Hold`](../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/hold)

- [`:With`](../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/with)

- [`:Disposable`](../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/disposable)

## Restriction 5

__A function cannot be compiled if it includes certain language features.__

The following language features prevent a function from being compiled:

- dfn error guards
- localised [`⎕TRAP`](../../language-reference-guide/system-functions/trap)
- function trains

## Restriction 6

__A function that includes the Execute function (`⍎`) cannot be compiled.__

The compiler prohibits the use of _execute_ ([`⍎`](../../language-reference-guide/docs/primitive-functions/execute)) because it could have arbitrary side effects unknown to the compiler.

## Summary

A function cannot be compiled if it:

- uses semi-global names.
- calls a system function that refers to values by name or creates new named values.
- uses the dot syntax between user-defined names.
- includes the control structures `:Trap`, `:Hold`, `:With` or `:Disposable`
- includes dfn error guards or localises `⎕TRAP`
- includes function trains
- includes the _execute_ function (`⍎`)
