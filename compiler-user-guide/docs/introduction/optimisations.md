# Optimisations

In addition to reducing interpreter overhead, the compiler can also perform certain optimisations on the APL code. These include:

- constant folding (see xxx)
- eliminating local names (see xxx)
- flexible idiom recognition (see xxx)

## Constant Folding

When a primitive function is applied to constant arguments, the compiler attempts to evaluate the entire expression at compile time, thereby saving time when the function is executed. For example:
```apl
encode←{(⎕A,⎕D)⍳⍵}   ⍝ ⎕A,⎕D is evaluated at compile time
```

However, the compiler cannot always successfully evaluate every expression. For example, the compiler cannot evaluate primitive functions that depend on system variables:
```apl
numbers←{⍳7} ⍝ compiler cannot evaluate ⍳7 as it does not
             ⍝ know what value ⎕IO will have
```

Constants will only be retained if they are reasonably small. The limit is typically around 1,000 items for a simple array.

## Eliminating Local Names

Every assignment to a local name incurs a measurable overhead, especially within a dfn. The compiler discards all local names as part of its normal operation, so this overhead is eliminated in compiled code.

## Flexible Idiom Recognition

The Dyalog interpreter recognises idioms as specific sequences of characters, for example, `0=⍴⍴x`. The compiler recognises the same idioms but in a more flexible way, enabling it to cope with syntactic variations. This means that expressions can be identified as idioms (and processed as such) even if:

- parts of the expression are named (as long as there are no other uses of the same name), for example, `s←⍴x ⋄ 0=⍴s`
- redundant parentheses are added, for example, `0=(⍴⍴x)`
- the arguments to commutative functions are swapped, for example, `(⍴⍴x)=0`

In these situations, the compiler's optimisations transform the expression into one that matches an idiom. For example, `(≢⍬)=⍴⍴x` is recognised as being the same as the idiom `0=⍴⍴x` because the expression `≢⍬` is evaluated to `0` at compile time.
