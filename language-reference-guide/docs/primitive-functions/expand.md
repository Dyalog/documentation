<div style="display: none;">
  \
</div>






<h1 class="heading"><span class="name">Expand</span> <span class="command">R←X\[K]Y</span></h1>



`Y` may be any array.  `X` is a simple integer scalar or vector.  The axis specification is optional.  If present, `K` must be a simple integer scalar or 1-element vector.  The value of `K` must be an axis of `Y`.  If absent, the last axis of `Y` is implied.  The form `R←X⍀Y` implies the first axis.  If `Y` is a scalar, it is treated as a one-element vector.


If `Y` has length 1 along the `K`<sup>th</sup> (or implied) axis, it is extended along that axis to match the number of positive elements in `X`. Otherwise, the number of positive elements in `X` must be the length of the `K`<sup>th</sup> (or implied) axis of `Y`.


`R` is composed from the sub-arrays along the `K`<sup>th</sup> axis of `Y`. If `X[I]` (an element of `X`) is the `J`<sup>th</sup> positive element in `X`, then the `J`<sup>th</sup> sub-array along the `K`<sup>th</sup> axis of `Y` is replicated `X[I]` times. If `X[I]` is negative, then a sub-array of fill elements of `Y` is replicated `|X[I]` times and inserted in relative order along the `K`<sup>th</sup> axis of the result. If `X[I]` is zero, it is treated as the value `¯1`. The shape of `R` is the shape of `Y` except that the length of the `K`<sup>th</sup> axis is `+/1⌈|X`.


<h2 class="example">Examples</h2>
```apl
      0\⍳0
0
 
      1 ¯2 3 ¯4 5\'A'
A  AAA    AAAAA
 
      M
1 2 3
4 5 6
 
      1 ¯2 2 0 1\M
1 0 0 2 2 0 3
4 0 0 5 5 0 6
 
      1 0 1⍀M
1 2 3
0 0 0
4 5 6
 
      1 0 1\[1]M
1 2 3
0 0 0
4 5 6
 
      1 ¯2 1\(1 2)(3 4 5)
 1 2  0 0  0 0  3 4 5
```


