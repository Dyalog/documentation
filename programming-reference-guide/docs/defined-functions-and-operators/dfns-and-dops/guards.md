# Guards

A Guard is a Boolean-single valued expression followed on the right by a `':'`. For example:
```apl
      0≡≡⍵:         ⍝ Right arg simple scalar
      ⍺<0:          ⍝ Left arg negative
```

The guard is followed by a single APL expression: the result of the function.
```apl
      ⍵≥0: ⍵*0.5    ⍝ Square root if non-negative.
```

A dfn may contain any number of guarded expressions each on a separate line (or collected on the same line separated by diamonds). Guards are evaluated in turn until one of them yields a 1. The corresponding expression to the right of the guard is then evaluated as the result of the function.

If an expression occurs without a guard, it is evaluated immediately as the default result of the function. For example:
```apl
      sign←{   
          ⍵>0: '+ve'      ⍝ Positive
          ⍵=0: 'zero'     ⍝ zero
               '-ve'      ⍝ Negative (Default)
      }
```

Local definitions and guards can be interleaved in any order.

Note again that any code following the first unguarded expression (which terminates the function) could never be executed and would therefore be redundant.

See also [Error-Guards](error-guards.md).
