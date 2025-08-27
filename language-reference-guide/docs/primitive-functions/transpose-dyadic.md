<div style="display: none;">
  ⍉
</div>






<h1 class="heading"><span class="name">Transpose (Dyadic)</span> <span class="command">R←X⍉Y</span></h1>



`Y` may be any array.  `X` must be a simple scalar or vector whose elements are included in the set `⍳⍴⍴Y`.  Integer values in `X` may be repeated but all integers in the set `⍳⌈/X` must be included.  The length of `X` must equal the rank of `Y`.


`R` is an array formed by the transposition of the axes of `Y` as specified by `X`.  The `I`<sup>th</sup> element of `X` gives the new position for the `I`<sup>th</sup> axis of `Y`.  If `X` repositions two or more axes of `Y` to the same axis, the elements used to fill this axis are those whose indices on the relevant axes of `Y` are equal.


`⎕IO` is an implicit argument of Dyadic Transpose.


<h2 class="example">Examples</h2>
```apl
      A
 1  2  3  4
 5  6  7  8
 9 10 11 12
 
13 14 15 16
17 18 19 20
21 22 23 24
```
```apl

 
      2 1 3⍉A
 1  2  3  4
13 14 15 16
 
 5  6  7  8
17 18 19 20
 
 9 10 11 12
21 22 23 24
 
      1 1 1⍉A
1 18
 
      1 1 2⍉A
 1  2  3  4
17 18 19 20
```


## Alternative Explanation


Assign a distinct letter for each unique integer in `X` :
```apl
0 1 2 3 …
i j k l
```


If `R←X⍉Y`, then `R[i;j;k;…]` equals `Y` indexed by the letters corresponding to elements of `X` .


## For example
```apl
      ⎕IO←0

      Y← ? 5 13 19 17 11 ⍴ 100

      X← 2 1 2 0 1
      ⍝  k j k i j
```
```apl
      R←X⍉Y
```
```apl
      i←?17 ⋄ j←?11 ⋄ k←?5
      R[i;j;k] = Y[k;j;k;i;j]
1
      R[i;j;k]=Y[⊂⍎¨'ijk'[X]]
1
```


From the above it can be seen that:

- the rank of `R` is `0⌈1+⌈/X`
- the shape of R is `(⍴Y)⌊.+(⌈/⍴Y)×X∘.≠⍳0⌈1+⌈/X`


