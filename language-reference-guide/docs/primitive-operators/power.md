<div style="display: none;">
  ⍣
</div>






<h1 class="heading"><span class="name">Power</span> <span class="command">{R}←{X}(f⍣g)Y</span></h1>



If right operand `g` is a numeric integer scalar, power applies its left operand function `f` cumulatively `g` times to its argument. In particular, `g` may be Boolean 0 or 1 for conditional function application.


If right operand `g` is a scalar-returning dyadic *function*, then left operand function `f` is applied repeatedly **until** `((f Y) g Y)` or until a strong interrupt occurs. Notice that power calls its dyadic right operand `g` with the next `(f Y)` and current `(Y)` values of the iteration as left and right arguments. In particular, if `g` is `=` or `≡`, the result is sometimes termed a *fixpoint* of `f`.


If a left argument `X` is present, it is bound as left argument to left operand function `f`:
```apl
      X (f ⍣ g) Y → (X∘f ⍣ g) Y
```

A *negative* right operand `g` applies the *inverse* of the operand function `f`, `(|g)`times. In this case, `f` may be a primitive function or an expression of primitive functions combined with primitive operators:

|----|-------------|
|`∘` |compose      |
|`¨` |each         |
|`∘.`|outer product|
|`⍨` |commute      |
|`\` |scan         |
|`[]`|axis         |
|`⍣` |power        |

If the function does not have an inverse, a negative argument `g` generates `DOMAIN ERROR`.

!!! Tip "Hints and Recommendations"
    Dyalog Ltd recommends that the use of inverses in production code is limited to `⊥`, `⍸`, `+\`, `≠\`, `+⍀`, and `≠⍀`, and functions derived from these, for example, `2∘⊥` and `≠\[1]`.

<h2 class="example">Examples</h2>
```apl
 
    (,∘⊂∘,⍣(1=≡,vec))vec    ⍝ ravel-enclose if simple.
 
    a b c←1 0 1{(⊂⍣⍺)⍵}¨abc ⍝ enclose first and last.
 
    cap←{(⍺⍺⍣⍺)⍵}           ⍝ conditional application.
 
    a b c←1 0 1⊂cap¨abc     ⍝ enclose first and last.
```
```apl
    succ←1∘+                ⍝ successor function.
 
    (succ⍣4)10              ⍝ fourth successor of 10. 
14
    (succ⍣¯3)10             ⍝ third predecessor of 10.
7
    1+∘÷⍣=1                 ⍝ fixpoint: golden mean.
1.618033989
 
    f←(32∘+)∘(×∘1.8)        ⍝ Fahrenheit from Celsius.
    f 0 100
32 212
 
    c←f⍣¯1                  ⍝ c is Inverse of f.
    c 32 212                ⍝ Celsius from Fahrenheit.
0 100
 
    invs←{(⍺⍺⍣¯1)⍵}         ⍝ inverse operator.
 
    +\invs 1 3 6 10         ⍝ scan inverse.
1 2 3 4
 
    2∘⊥invs 9               ⍝ decode inverse.
1 0 0 1
 
    dual←{⍵⍵⍣¯1 ⍺⍺ ⍵⍵ ⍵}    ⍝ dual operator.
 
    mean←{(+/⍵)÷⍴⍵}         ⍝ mean function.
 
    mean dual⍟ 1 2 3 4 5    ⍝ geometric mean.
2.605171085
 
    +/dual÷ 1 2 3 4 5       ⍝ parallel resistance.
0.4379562044
 
    mean dual(×⍨)1 2 3 4 5  ⍝ root-mean-square.
3.31662479
 
    ⍉dual↑ 'hello' 'world'  ⍝ vector transpose.
 hw  eo  lr  ll  od
```

!!! warning
    Some expressions, such as the following, will cause an infinite internal loop and APL will appear to hang. In most cases this can be resolved by issuing a hard INTERRUPT.
    ```apl
      !⍣-1
      !⍣-2
    ```

One can ensure that weak interrupts and `⎕TKILL` can interrupt by packaging the `⍣` within the dop `{⍺←⊢ ⋄ ⍺ (⍺⍺{⍺←⊢ ⋄ ⍺ ⍺⍺ ⍵}⍣⍵⍵) ⍵}`.

<h2 class="example">Example</h2>
```apl
      PowOp←{⍺←⊢ ⋄ ⍺ (⍺⍺{⍺←⊢ ⋄ ⍺ ⍺⍺ ⍵}⍣⍵⍵) ⍵}
      tnum←!PowOp-&1 ⍝ using naked ⍣ will freeze APL

      ⎕TKILL tnum
```


