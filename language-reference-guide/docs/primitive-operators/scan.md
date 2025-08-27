<div style="display: none;">
  \
</div>






<h1 class="heading"><span class="name">Scan</span> <span class="command">R←f\[K]Y</span></h1>



`f` may be any dyadic function that returns a result.  `Y` may be any array whose items in the sub-arrays along the `K`th axis are appropriate to the function `f`.


The axis specification is optional.  If present, `K` must identify an axis of `Y`.  If absent, the last axis of `Y` is implied.  The form `R←f⍀Y` implies the first axis of `Y`.


`R` is an array formed by successive reductions along the `K`th axis of `Y`.  If `V` is a typical vector taken from the `K`th axis of `Y`, then the `I`<sup>th</sup> element of the result is determined as `f/I↑V`.


The shape of `R` is the same as the shape of `Y`.  If `Y` is an empty array, then `R` is the same empty array.


<h2 class="example">Examples</h2>
```apl
      ∨\0 0 1 0 0 1 0
0 0 1 1 1 1 1
 
      ^\1 1 1 0 1 1 1
1 1 1 0 0 0 0
 
      +\1 2 3 4 5
1 3 6 10 15
 
      +\(1 2 3)(4 5 6)(7 8 9)
 1 2 3  5 7 9  12 15 18
```
```apl

      M
1 2 3
4 5 6
 
      +\M
1 3  6
4 9 15
 
      +⍀M
1 2 3
5 7 9
 
      +\[1]M
1 2 3
5 7 9
 
      ,\'ABC'
A AB  ABC
 
      T←'ONE(TWO) BOOK(S)'
 
      ≠\T∊'()'
0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0
 
      ((T∊'()')⍱≠\T∊'()')/T
ONE BOOK
 
```


