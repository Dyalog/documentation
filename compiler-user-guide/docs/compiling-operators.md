# Compiling Operators

When compiling a defined function or operator, the compiler needs to know the nameclass of every name that is used. This presents a problem for defined operators, because the nameclass of the operands is not known:
```apl
op←{
    ⍺⍺ / ⍵ 	  ⍝ ⍺⍺ could be an array or a function
}
```

When an operator is compiled using `2(400⌶)Y` (see [xxx](xxx)), the compiler assumes that the operands are functions. If the compiled operator is subsequently called with an array operand, then the compiled version is not used and the interpreter uses the parser instead.

To work around this, the compiler can be run in a mode where it will attempt to compile a defined operator the first time it is applied to some arguments; at this point the compiler can see exactly what the operands are. If the compilation is successful, then the compiler will record the nameclass of the operands along with the compiled bytecode. When the operator is applied again, the compiled bytecode will only be executed if the operands still have the same nameclass as they did the first time the operator was applied (if the nameclass of an operand has changed, then the compiled bytecode will not be used and the operator will be interpreted).

Continuing the example:
```apl
      400⌶2       ⍝ enable auto compilation of operators
```
```apl
      +op 1 2 3 4 ⍝ op is compiled assuming fn operand
10
```
```apl
      400⌶0       ⍝ disable auto compilation
      ×op 1 2 3 4 ⍝ execute compiled bytecode again
24
```
```apl
      1 2 3 4 op 1 2 3 4 ⍝ operand is array; revert to interpreter
1 2 2 3 3 3 4 4 4 4
```
