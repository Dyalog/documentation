# Results

A function may return a value, known as its *result*. Not every function returns one, and a result that is returned is not always displayed. Every function application produces exactly one of three outcomes:

- an *explicit result*: a value that is returned and, at the Session prompt, displayed unless it is assigned or otherwise used;
- a *shy result*: a value that is returned but not displayed, although it can still be assigned or used; or
- *no result*: no value is returned, so using the application where a value is required signals a [`VALUE ERROR`](../error-messages/value-error.md).

An explicit result that is not consumed by the rest of the expression is displayed in the same form as any other value (see [Display of Arrays](arrays/display-of-arrays.md)).

Assignment is itself an operation that returns a result: the *pass-through* value, that is, the value assigned. This result is shy, so a plain assignment displays nothing, whereas using the assignment within a larger expression makes the value available:
```apl
      a←42
      ⎕←a←42
42
      (a←42)+1
43
```

## Shy Results

A *shy result* is a value that a function returns but which is not displayed when the function application is the whole of an expression evaluated at the Session prompt. The value is still returned: it can be assigned to a name, passed as an argument, or otherwise used, exactly like an explicit result. Assigning or using a shy result makes it no longer shy.

Shy results suit functions whose main purpose is a side effect, such as updating a file or fixing a function, but which still have a useful value to offer a caller that wants it. The system function [`⎕FX`](../../../language-reference-guide/system-functions/fx) is an example: it fixes a function and returns that function's name as a shy result.
```apl
      ⎕FX 'r←f x' 'r←x+1'
      ⎕←⎕FX 'r←g x' 'r←x-1'
g
```

## No Result

A function application produces *no result* when the function returns no value. Using such an application where a value is required, for example as an argument or on the right of an assignment, signals a `VALUE ERROR`.
```apl
      ∇ greet name
[1]     'Hello ',name
      ∇
      greet 'Ada'
Hello Ada
      x←greet 'Ada'
Hello Ada
VALUE ERROR: No result was provided when the context expected one
      x←greet 'Ada'
        ∧
```

## Dynamic Functions and Operators

The result of a [dynamic function](../defined-functions-and-operators/dfns-and-dops/dynamic-functions-and-operators.md) is the value of the first statement it evaluates that is not an assignment; that result is explicit. If every statement it evaluates is an assignment, the value of the last one is returned as a shy result. A dynamic function that evaluates no value-yielding statement, such as the empty function `{}`, returns no result.

The idiomatic way to give a dynamic function a shy result is therefore to assign the result on the final line, guarded so that it is the last statement evaluated (see [Shy Result](../defined-functions-and-operators/dfns-and-dops/shy-result.md)):
```apl
      log←{
          tie←⍺ ⎕FSTIE 0
          cno←⍵ ⎕FAPPEND tie
          tie←⎕FUNTIE tie
          1:r←cno            ⍝ component number, shy result
      }
```
Whether a dynamic function returns a value, and whether that value is shy, can thus depend on the path taken through it.

## Traditional Functions and Operators

A traditional function or operator declares its result in the header. [Model Syntax](../defined-functions-and-operators/traditional-functions-and-operators/model-syntax.md) gives the three forms:

- a header with no result name never returns a value;
- an explicit result name, `R←`, returns the value of `R` when the function exits;
- a braced result name, `{R}←`, returns the value of `R` as a shy result.

If the header names a result but the function exits without assigning it, the application returns no result. A function can therefore have an optional result, returning a value on some paths and none on others.

### Namelists

If the result is declared as a *namelist*, a parenthesised, blank-delimited list of names, the values of those names are stranded together into the result when the function exits (see [Namelists](../defined-functions-and-operators/traditional-functions-and-operators/namelists.md)).

## System Functions

Many system functions return shy results, so that they can be used for their effect without cluttering the Session while still providing a value when one is wanted. Some are shy only in certain cases: [`⎕FX`](../../../language-reference-guide/system-functions/fx) returns a shy result on success but an explicit result, the index of the offending line, on failure, and [`⎕NS`](../../../language-reference-guide/system-functions/ns) returns a shy result only when called dyadically.

## Primitive Operators

A primitive operator applies to one or two operand functions and produces a derived function. The result of that derived function takes the same kind, explicit, shy, or none, as the operand function that produces the final value.
```apl
      {⍵+1}¨1 2 3           ⍝ explicit operand, explicit derived result
2 3 4
      {1:r←⍵+1}¨1 2 3       ⍝ shy operand, shy derived result (not displayed)
```
With [Each (`¨`)](../../../language-reference-guide/primitive-operators/each/each-with-monadic-operand) the derived result matches its operand. With a composition such as [Beside (`∘`)](../../../language-reference-guide/primitive-operators/beside), the outermost function determines the kind: `f∘g` returns whatever kind `f` returns.

A few primitive operators return a shy result of their own, whatever their operand. The [Spawn (`&`)](../../../language-reference-guide/primitive-operators/spawn) operator returns the number of the newly created thread as a shy result.
