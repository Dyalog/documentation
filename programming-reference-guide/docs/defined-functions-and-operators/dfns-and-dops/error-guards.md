<h1 class="heading"><span class="name">Error-Guards</span></h1>

An **error-guard** is (an expression that evaluates to) a vector of error numbers (see [APL Error Messages](../../error-messages/apl-errors.md)), followed by the digraph: `::`, followed by an expression, the *body* of the guard, to be evaluated as the result of the function. For example:
```apl
      11 5 :: ⍵×0 ⍝ Trap DOMAIN and LENGTH errors.
```

In common with `:Trap` and `⎕TRAP`, error numbers 0 and 1000 are catch-alls for synchronous errors and interrupts respectively.

When an error is generated, the system searches dynamically through the calling functions for an error-guard that matches the error. If one is found, the execution environment is unwound to its state immediately *prior* to the error-guard's execution and the body of the error-guard is evaluated as the result of the function. This means that, during evaluation of the body, the guard is no longer in effect and so the danger of a hang caused by an infinite "trap loop", is avoided.

Notice that you can provide "cascading" error trapping in the following way:
```apl

      0::try_2nd
      0::try_1st
      expr
```

In this case, if `expr` generates an error, its immediately preceding: `0::` catches it and evaluates `try_1st` leaving the remaining error-guard in scope. If `try_1st` fails, the environment is unwound once again and `try_2nd` is evaluated, this time with no error-guards in scope.

See also [Guards](guards.md).

<h2 class="example">Examples</h2>

`Open` returns a handle for a component file. If the exclusive tie fails, it attempts a share-tie and if this fails, it creates a new file. Finally, if all else fails, a handle of 0 is returned.
```apl
open←{                 ⍝ Handle for component file ⍵.
    0::0               ⍝ Fails:: return 0 handle.
    22::⍵ ⎕FCREATE 0   ⍝ FILE NAME:: create new one.
    24 25::⍵ ⎕FSTIE 0  ⍝ FILE TIED:: try share tie.
           ⍵ ⎕FTIE 0   ⍝ Attempt to open file.
}
```

An error in `div` causes it to be called recursively with *improved* arguments.
```apl
div←{                  ⍝ Tolerant division:: ⍺÷0 → ⍺.
    ⍺←1                ⍝ default numerator.
    5::↑∇/↓↑⍺ ⍵        ⍝ LENGTH:: stretch to fit.
    11::⍺ ∇ ⍵+⍵=0      ⍝ DOMAIN:: increase divisor.
    ⍺÷⍵                ⍝ attempt division.
}
```

Notice that some arguments may cause `div` to recur twice:
```apl
       6 4 2 div 3 2
→      6 4 2 div 3 2 0
→      6 4 2 div 3 2 1
→      2 2 2
```

The final example shows the unwinding of the local environment before the error-guard's body is evaluated. Local name `trap` is set to describe the domain of its following error-guard. When an error occurs, the environment is unwound to expose `trap`'s statically correct value.
```apl
      add←{
          trap←'domain' ⋄ 11::trap
          trap←'length' ⋄  5::trap
          ⍺+⍵
      }
 
      2 add 3         ⍝ Addition succeeds 
5
 
      2 add 'three'   ⍝ DOMAIN ERROR generated.
domain
 
      2 3 add 4 5 6   ⍝ LENGTH ERROR generated.
length
```

## Note

Following the setting of an error-guard, subsequent function calls will disable tail call optimisation:
```apl
    {
        22::'Oops!'     ⍝ this error-guard means that ...
        tie←⍵ ⎕FTIE 0
        subfn tie       ⍝ ... tail call not optimised
    }
```

One way to maintain the tail call optimisation in the presence of an error-guard is to isolate it within an inner function:
```apl
    {
        tie←{
            22::0        ⍝ error-guard local to inner fn
            ⍵ ⎕FTIE 0
        }⍵
        tie=0:'Oops!'
        subfn tie        ⍝ ... so this is a tail call 
    }
```
