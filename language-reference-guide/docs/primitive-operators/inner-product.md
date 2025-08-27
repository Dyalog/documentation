<div style="display: none;">
  .
</div>






<h1 class="heading"><span class="name">Inner Product</span> <span class="command">R←Xf.gY</span></h1>



`f` and `g` are dyadic functions. The last axis of `X` must have the same length as the first axis of `Y`, or one of `X` and `Y` is single (`^/1=⍴X` or `^/1=⍴Y`).


The result of the derived function has shape `(¯1↓⍴X),1↓⍴Y`; each item is `f/x g¨y` where `x` and `y` are vectors taken from all the combinations of vectors along the last axis of `X` and the first axis of `Y`.


!!! note
    - `g` must return a result.
    - `f` must return a result with the possible exception of the case when `1=⍴x g¨y`.
    - The expression `f/x g¨y` applies even when `R` or `x g¨y` or `X` or `Y` is empty. When `X` or `Y` is empty, the vector `x` is `X` reshaped to the appropriate length (`y` is `Y` reshaped to appropriate length).
    - `x` is just `X` itself if `X` is a scalar. Likewise `y` and `Y`.

<h2 class="example">Examples</h2>
```apl
      1 2 3+.×10 12 14
76
      +/1 2 3×10 12 14
76
 
      NAMES
HENRY
WILLIAM
JAMES
SEBASTIAN
 
      NAMES^.='WILLIAM  '
0 1 0 0
```


