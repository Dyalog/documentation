<div style="display: none;">
  .
</div>






<h1 class="heading"><span class="name">Outer Product</span> <span class="command">{R}←X∘.gY</span></h1>



`g` may be any dyadic function.  The left operand of the operator is the symbol `∘`.  `X` and `Y` may be any arrays whose elements are appropriate to the function `g`.


Function `g` is applied to all combinations of the elements of `X` and `Y`.  If function `g` returns a result, the shape of `R` is `(⍴X),⍴Y`.  Each element of `R` is the item returned by function `g` when applied to the particular combination of elements of `X` and `Y`.



If `X` or `Y` is empty, the result `R` is a conformable empty array, and the operand function is applied *once* between the first items of `X` and `Y` to determine the prototype of `R`.

<h2 class="example">Examples</h2>
```apl
      1 2 3∘.×10 20 30 40
10 20 30  40
20 40 60  80
30 60 90 120
 
      1 2 3∘.⍴'AB'
 A    B
 AA   BB
 AAA  BBB
 
      1 2∘.,1 2 3
 1 1  1 2  1 3
 2 1  2 2  2 3
 
      (⍳3)∘.=⍳3
1 0 0
0 1 0
0 0 1
```


