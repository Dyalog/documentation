
<!-- Hidden search keywords -->
<div style="display: none;">
  85⌶
</div>






<h1 class="heading"><span class="name">Execute Expression</span> <span class="command">R←X(85⌶)Y</span></h1>



Executes an expression.


`Y` is a character vector containing an APL expression.


The function executes the expression in `Y` exactly as it would be executed by the monadic Execute primitive function `⍎`, but handles shy results  of the execution rather differently.


The left argument `X` determines how a shy result from the execution of `Y` is treated and is either 0 or 1.


If `X` is 1, and the expression in `Y` returns an explicit result, `R` is that result. If the expression in `Y` returns no result or returns a shy result, the function signals `ERROR 85`. Effectively, a shy result is discarded.


If `X` is 0, and the expression in `Y` returns an explicit result or a shy result, `R` is that result (but is no longer shy). If the expression in `Y` returns no result, the function signals `ERROR 85`.

<h2 class="example">Examples</h2>

```apl
      ⍎'a←42'
      ⎕← ⍎'a←42'     ⍝ shy result
42
      0 (85⌶) 'a←42' ⍝ not shy
42
      1 (85⌶) 'a←42'
ERROR 85
      1(85⌶)'a←42'
     ∧

```


