<h1 class="heading"><span class="name">Multi-Line Dfns</span></h1>

The single expression which provides the result of the dfn may be preceded by any number of assignment statements. Each such statement introduces a name which is local to the function.

For example in the following, the expressions `sum←` and `num←` create **local** definitions `sum` and `num`.
```apl

      mean←{          ⍝ Arithmetic mean
          sum←+/⍵     ⍝ Sum of items
          num←⍴⍵      ⍝ Number of items
          sum÷num     ⍝ Mean
       }
```

An assignment to `⍵` is not allowed and will result in an error. For assignment to `⍺`, see [Default Left Argument](default-left-argument.md).

Note that dfns may be commented in the usual way using `⍝`.

When the interpreter encounters a local definition, a new local name is created. The name is shadowed dynamically exactly as if the assignment had been preceded by: `⎕SHADOW` *name* `⋄`.

It is **important** to note the distinction between the two types of statement above. There can be **many** assignment statements, each introducing a new local definition, but only a **single** expression where the result is not assigned. As soon as the interpreter encounters such an expression, it is evaluated and the result returned immediately as the result of the function.

For example, in the following,
```apl

      mean←{          ⍝ Arithmetic mean
          sum←+/⍵     ⍝ Sum of items
          num←⍴⍵      ⍝ Number of items
          sum,num     ⍝ Attempt to show sum,num (wrong)!
          sum÷num     ⍝ ... and return result.
       }
		
```

... as soon as the interpreter encounters the expression `sum,num`, the function terminates with the two item result (`sum,num`) and the following line is not evaluated.

To display arrays to the session from within a dfn, you can use the explicit display forms `⎕←` or `⍞←` as in:
```apl

      mean←{          ⍝ Arithmetic mean
          sum←+/⍵     ⍝ Sum of items
          num←⍴⍵      ⍝ Number of items
          ⎕←sum,num   ⍝ show sum,num.
          sum÷num     ⍝ ... and return result.
       }
```

Note that local definitions can be used to specify local nested dfns:
```apl

      rms←{                ⍝ Root Mean Square
         root←{⍵*0.5}      ⍝ ∇ Square root
         mean←{(+/⍵)÷⍴⍵}   ⍝ ∇ Mean
         square←{⍵×⍵}      ⍝ ∇ Square
         root mean square ⍵
       }
```
