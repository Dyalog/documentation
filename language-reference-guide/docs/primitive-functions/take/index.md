<div style="display: none;">
  ↑
</div>






<h1 class="heading"><span class="name">Take</span> <span class="command">R←X↑Y</span></h1>



`Y` may be any array.  `X` must be a simple integer scalar or vector.


If `Y` is a scalar, it is treated as a one-element array of shape `(⍴,X)⍴1`.  The length of `X` must be the same as or less than the rank of `Y`. If the length of `X` is less than the rank of `Y`, the missing elements of `X` default to the length of the corresponding axis of `Y`.


`R` is an array of the same rank as `Y` (after possible extension), and of shape `|X`.  If `X[I]` (an element of `X`) is positive, then `X[I]` sub-arrays are taken from the beginning of the `I`<sup>th</sup> axis of `Y`.  If `X[I]` is negative, then `X[I]` sub-arrays are taken from the end of the `I`<sup>th</sup> axis of `Y`.


If more elements are taken than exist on axis `I`, the extra positions in `R` are filled with the fill element of `Y` (`⊂∊⊃Y` with `⎕ML←0`).


<h2 class="example">Examples</h2>
```apl
      5↑'ABCDEF'
ABCDE
 
      5↑1 2 3
1 2 3 0 0
 
      ¯5↑1 2 3
0 0 1 2 3
 
      5↑(⍳3) (⍳4) (⍳5)
 1 2 3  1 2 3 4  1 2 3 4 5  0 0 0  0 0 0
 
```
```apl
      M
1 2 3 4
5 6 7 8
 
      2 3↑M
1 2 3
5 6 7
 
      ¯1 ¯2↑M
7 8
      M3←2 3 4⍴⎕A
      1↑M3
ABCD
EFGH
IJKL
      ¯1↑M3
MNOP
QRST
UVWX
```


