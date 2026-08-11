# Default Left Argument

The special  syntax: `⍺←expr` is used to give a default value to the left argument if a dfn is called monadically. For example:
```apl
      root←{      ⍝ ⍺th root
          ⍺←2     ⍝ default to sqrt
          ⍵*÷⍺
      }
```

The expression to the right of  `⍺←` is evaluated *only* if its dfn is called with no left argument.

Note that the syntax must be exactly `⍺←`, that is, it cannot contain parentheses, and so on.

`⍺←` must be the first tokens at the beginning of an expression. That expression can appear anywhere in the body, not only on the first line, but `⍺` has no value until it is evaluated.

**Ambivalence**

The assignment `⍺←⊢` allows an ambivalent function to call an ambivalent sub-function. For example in:
```apl
      foo←{
         ⍺←⊢
         ⍺ goo ⍵
      }
```

If `foo` is given a left argument, this is passed to `goo`. Otherwise, `⍺` is assigned `⊢` and the last line is `⊢ goo ⍵`, which is a monadic call on `goo` followed by the `⊢` (Right) of the result of `goo`, which is the same value.

The assignment `⍺←⍣0` allows an ambivalent operator to skip the application of an operand to a missing argument. For example in:
```apl
      over←{
         ⍺←⍣0
         (⍺⍺ ⍺)⍵⍵(⍺⍺ ⍵)
      }
```

If the function derived from *over* is given a left argument, this argument is preprocessed by the left operand `⍺⍺` and the result is passed to the right operand `⍵⍵`. Otherwise, `⍺` is assigned `⍣0` and the last line is `(⍺⍺⍣0)⍵⍵(⍺⍺ ⍵)`, which is a monadic call on `⍵⍵` followed by not applying `⍺⍺` to the result of `⍵⍵`, returning it unmodified.

The assignment `⍺←⍵` allows a function to act as if the *commute* operator (`⍨`) was applied to it twice:
```apl
      sort←{
         ⍺←⍵
         ⍵[⍋⍺]
      }
```

If sort is given a left argument, the right argument is sorted according to the left argument. Otherwise, `⍺` is assigned `⍵` and the last line is `⍵[⍋⍵]`, which has the right argument sorted according to itself. This is, therefore, equivalent to `sort←{⍵[⍋⍺]}⍨⍨` or `sort←{⍺[⍋⍵]}⍨`.
