# Introduction

When the APL interpreter executes a user-defined function, it spends most of its time performing two separate actions:

- Parsing the APL syntax ("interpreter overhead")
- Executing individual primitive functions

The compiler is designed to reduce the time spent on the first of these two actions – the interpreter overhead – by converting the APL source code into a bytecode form that is more efficient to execute.

The biggest performance gains are achieved when the compiler is used on functions that are applied to simple scalars or small array arguments. If the arguments are large arrays, then the interpreter spends most of its time executing the primitive functions; this means that the benefit of reducing the interpreter overhead is less significant.

!!! Info "Information"
    Dyalog Ltd is continually researching performance improvement mechanisms; advances in other areas mean that the compiler is unlikely to be developed further as efforts are now being directed elsewhere.
