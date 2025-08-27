<div style="display: none;">
  ⍳
</div>






<h1 class="heading"><span class="name">Index Generator</span> <span class="command">R←⍳Y</span></h1>



`Y` must be a simple scalar or vector array of non-negative numbers. `R` is a numeric array composed of the set of all possible coordinates of an array of shape `Y`. The shape of `R` is `Y` and each element of `R` occurs in its self-indexing position in `R`. In particular, the following identity holds:
```apl
      ⍳Y ←→ (⍳Y)[⍳Y]
```


`⎕IO` is an implicit argument of Index Generator. This function is also known as Interval.


<h2 class="example">Examples</h2>
```apl
      ⎕IO
1
      ⍴⍳0
0
      ⍳5
1 2 3 4 5
 
      ⍳2 3
 1 1  1 2  1 3
 2 1  2 2  2 3
 
      ⊢A←2 4⍴'MAINEXIT'
MAIN
EXIT
      A[⍳⍴A]
MAIN
EXIT
      
```
```apl
      ⎕IO←0
      ⍳5
0 1 2 3 4
 
      ⍳2 3
 0 0  0 1  0 2
 1 0  1 1  1 2
 
      A[⍳⍴A]
MAIN
EXIT
```


