# Basic Usage

Theoretically (although there are some [restrictions](restrictions.md)), every defined function in a workspace can have a compiled bytecode form. This bytecode is saved and loaded as part of the workspace, and will be copied along with the function on [`⎕CY`](../../language-reference-guide/system-functions/cy) or [`)COPY`](../../language-reference-guide/system-commands/copy) or the [`⎕OR`](../../language-reference-guide/system-functions/or) of a compiled function.

To query whether a function `foo` has been successfully compiled, enter:
```apl
      1(400⌶)'foo'
```

This returns a Boolean value of 1 if the compilation has been performed.

To compile a function foo, enter:
```apl
      2(400⌶)'foo'
```

This returns a matrix of diagnostic information. If the matrix has zero rows then the function was compiled successfully. Otherwise, each row of the matrix describes a problem that prevented the compiler from compiling the function.

When a function is executed, Dyalog automatically executes any compiled code for the function. If none is available, then the function is executed using the traditional APL parser.

In summary:
```apl
      ⎕FX'r←foo y' ... ⍝ define foo
```
```apl
      foo 99           ⍝ execute the uncompiled code
```
```apl
      2(400⌶)'foo'     ⍝ compile it
```
```apl
      foo 99           ⍝ execute the compiled code
```

For full details on the syntax of `400⌶`, see [Compiler Control I-beam](../../language-reference-guide/primitive-operators/i-beam/compiler-control).
