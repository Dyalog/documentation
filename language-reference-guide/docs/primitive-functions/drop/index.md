<div style="display: none;">
  ↓
</div>






<h1 class="heading"><span class="name">Drop</span> <span class="command">R←X↓Y</span></h1>



`Y` may be any array.  `X` must be a simple scalar or vector of integers. If `X` is a scalar, it is treated as a one-element vector.  If `Y` is a scalar, it is treated as an array whose shape is `(⍴X)⍴1`. After any scalar extensions, the shape of `X` must be less than or equal to the rank of `Y`. Any missing trailing items in `X` default to 0.


`R` is an array with the same rank as `Y` but with elements removed from the vectors along each of the axes of `Y`. For the `I`th axis:

- if `X[I]` is positive, all but the first `X[I]` elements of the vectors result
- if `X[I]` is negative, all but the last `X[I]` elements of the vectors result


If the magnitude of `X[I]` exceeds the length of the `I`th axis, the result is an empty array with zero length along that axis.


<h2 class="example">Examples</h2>
```apl
      4↓'OVERBOARD'
BOARD
 
      ¯5↓'OVERBOARD'
OVER
 
      ⍴10↓'OVERBOARD'
0
 
      M
ONE
FAT
FLY
      0 ¯2↓M
O
F
F
 
      ¯2 ¯1↓M
ON
      1↓M
FAT
FLY
      M3←2 3 4⍴⎕A
 
      1 1↓M3
QRST
UVWX
      ¯1 ¯1↓M3
ABCD
EFGH
```


