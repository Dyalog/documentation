<div style="display: none;">
  *
</div>






<h1 class="heading"><span class="name">Power</span> <span class="command">R←X*Y</span></h1>



`Y` must be a numeric array.  `X` must be a numeric array.  `R` is numeric.  The value of `R` is `X` raised to the power of `Y`.


If `Y` is zero, `R` is defined to be 1.


If `X` is zero, `Y` must be non-negative.


In general, `X*Y` is defined as `*Y×⍟X`. If `X` is negative, the result `R` is likely to be complex.

<h2 class="example">Examples</h2>
```apl
      2*2 ¯2
4 0.25
 
      9 64*0.5
3 8
 
      ¯27*3 2 1.2 .5
¯19683 729 ¯42.22738244J¯30.67998919 0J5.196152423

      ¯8*÷3
1J1.732050808

```



