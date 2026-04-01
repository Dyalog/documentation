---
search:
  boost: 2
---

<!-- Hidden search keywords -->
<div style="display: none;">
  400⌶
</div>

<h1 class="heading"><span class="name">Compiler Control</span> <span class="command">R←{X}(400⌶)Y</span></h1>




Controls the actions of the Compiler (for more information on the Compiler, see the [_Compiler User Guide_](../../../../compiler-user-guide/)).

The optional left-argument `X` must be one of the following:

- `0` – Set automatic compilation options (default)
- `1` – Determine whether the function/operator `Y` has been successfully compiled
- `2` – Compile the function/operator `Y`
- `3` – Uncompile the function/operator `Y`
- `4` – Show bytecode for the compiled function/operator `Y`
- A namespace – Compile the function/operator `Y` using callbacks to provide information about global names

`Y` and `R` depend on the value of `X`.

## X = 0 : Control Automatic Compilation (Default)

`R←0(400⌶)Y  ⍝ control automatic compilation of fns`

`Y` must be one of the following values:

- `0` – Disable automatic compilation (initial setting)
- `1` – Compile functions when they are fixed (with [`⎕FX`](../../system-functions/fx.md) or from the function editor)
- `2` – Compile operators the first time they are executed
- `3` – Compile functions when they are fixed (with `⎕FX` or from the function editor) and compile operators the first time they are executed

The result `R` is the previous value of `Y`.

The automatic compilation setting is maintained within the workspace, and is saved and loaded with the workspace.

## X = 1 : Query Compilation State

`R←1(400⌶)Y  ⍝ query compilation of function/operator Y`

`Y` must be a character vector, matrix, or vector of vectors specifying the name of a function or operator or a list of such names.

The result `R` is a Boolean scalar or vector, with a value of `1` if the function/operator has been successfully compiled and a value of `0` if it has not.

## X = 2 : Compile

`R←2(400⌶)Y  ⍝ compile function/operator(s) Y`

`Y` must be a character vector, matrix, or vector of vectors specifying the name of a function or operator or a list of such names that should be compiled.

The result `R` is a matrix of diagnostic information or, if `Y` was either a matrix or a vector of vectors, a vector of such matrices. Each row of the matrix describes a problem that caused the compilation to fail, with four columns corresponding to:  

- `[;1]` – the APL error number  
- `[;2]` – the line number in the function/operator  
- `[;3]` – the column number (currently always `0`)  
- `[;4]` – the error message  

If the matrix `R` has zero rows then the compilation was successful.

If this mechanism is used to compile operators, then the compiled bytecode will assume that the operator's operands are functions rather than arrays. At run time, the operands will be checked – if they are functions then the compiled bytecode will be used, otherwise the operator will be interpreted.

## X = 3 : Discard Compiled Form

`R←3(400⌶)Y  ⍝ uncompile function/operator(s) Y`

If `Y` is empty, then discard any compiled bytecode for all functions and operators in the workspace.

If `Y` is a character vector, matrix, or vector of vectors specifying the name of a function or operator or a list of such names, then discard any compiled bytecode for them.

`R` is always 0.

## X = 4 : Show Bytecode

`R←4(400⌶)Y  ⍝ show bytecode for function/operator(s) Y`

`Y` must be a character vector, matrix, or vector of vectors specifying the name of a function or operator or a list of such names.

The result `R` is a multi-line string (that is, a character vector with embedded newlines) or, if `Y` was either a matrix or a vector of vectors, a vector of such strings. Each string is a human-readable representation of the bytecode of a compiled function or operator.

!!! Info "Information"
    This functionality is provided for information and diagnostic purposes only. The human-readable form of the bytecode is subject to change at any time.

## X is a Namespace : Compile with Callbacks

`R←N(400⌶)Y  ⍝ compile function/operator(s) Y`

`Y` must be a character vector, matrix, or vector of vectors specifying the name of a function or operator or a list of such names. The specified functions or operators are compiled in the same way as when  [`X` = `2`](#x-2-compile)) except that the compiler uses the namespace `N` to obtain information about global names.

The namespace `N` can contain any or all of following callback functions:

- `N.quadNC` – analogous to the system function [`⎕NC`](../../system-functions/nc.md). When applied monadically to an enclosed character vector it returns the detailed nameclass of that name. For example, given the name of a global dfn it returns the value `3.2`.
- `N.quadAT` – analogous to the system function [`⎕AT`](../../system-functions/at.md). When applied monadically to an enclosed character vector it returns a 1 by 4 matrix whose first item is a vector of 3 integers describing (respectively) the result, function valence, and operator valence of the name.
- `N.getValue` – used to obtain the name of a global constant. When applied monadically to a character vector that is a global constant it returns the enclose of the constant value, otherwise it returns `⍬`.

Each of these callback functions returns information about names that should be guaranteed to exist when the compiled functions are executed. The compiler assumes that the information returned by the callbacks is correct, and generates bytecode accordingly. In the case of `quadNC` and `quadAT`, if the information returned by the callbacks turns out not to be correct when the compiled function is executed, then a runtime error is generated.

The result `R` is a matrix of diagnostic information or, if `Y` was either a matrix or a vector of vectors, a vector of such matrices. Each row of the matrix describes a problem that caused the compilation to fail, with four columns corresponding to:
  
- `[;1]` – the APL error number  
- `[;2]` – the line number in the function/operator  
- `[;3]` – the column number (currently always `0`)  
- `[;4]` – the error message   

If the matrix has zero rows then the compilation was successful.
