<div style="display: none;">
  /
</div>






<h1 class="heading"><span class="name">Replicate</span> <span class="command">R←X/[K]Y</span></h1>



`Y` may be any array.  `X` is a simple integer vector or scalar.


The axis specification is optional.  If present, `K` must be a simple integer scalar or 1-element vector.  The value of `K` must be an axis of `Y`.  If absent, the last axis of `Y` is implied.  The form `R←X⌿Y` implies the first axis of `Y`.


If `Y` has length 1 along the `K`<sup>th</sup> (or implied) axis, it is extended along that axis to match the length of `X`. Otherwise, the length of `X` must be the length of the `K`<sup>th</sup> (or implied) axis of `Y`. However, if `X` is a scalar or one-element vector, it will be extended to the length of the `K`<sup>th</sup> axis.


`R` is composed from sub-arrays along the `K`th axis of `Y`.  If `X[I]` (an element of `X`) is positive, then the corresponding sub-array is replicated `X[I]` times.  If `X[I]` is zero, then the corresponding sub-array of `Y` is excluded.  If `X[I]` is negative, then the fill element of  `Y` is replicated `|X[I]` times.  Each of the (replicated) sub-arrays and fill items are joined along the `K`th axis in the order of occurrence.  The shape of `R` is the shape of `Y` except that the length of the (implied) `K`th axis is `+/|X` (after possible extension).



This function is sometimes called Compress when `X` is Boolean.

<h2 class="example">Examples</h2>
```apl
      1 0 1 0 1/⍳5
1 3 5
 
      1 ¯2 3 ¯4 5/⍳5
1 0 0 3 3 3 0 0 0 0 5 5 5 5 5
 
      M
1 2 3
4 5 6
 
      2 0 1/M
1 1 3
4 4 6
 
      0 1⌿M
4 5 6
 
      0 1/[1]M
4 5 6
```


If `Y` is a singleton `(1=×/⍴,Y)` its value is notionally extended to the length of `X` along the specified axis.
```apl
      1 0 1/4
4 4
      1 0 1/,3
3 3
      1 0 1/1 1⍴5
5 5
 
 
```


