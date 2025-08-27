<div style="display: none;">
  ⌽
</div>






<h1 class="heading"><span class="name">Rotate</span> <span class="command">R←X⌽[K]Y</span></h1>



`Y` may be any array.  `X` must be a simple integer array.  The axis specification is optional.  If present, `K` must be a simple integer scalar or one-element vector.


The value of `K` must be an axis of `Y`.  If absent, the last axis of `Y` is implied.  The form `R←X⊖Y` implies the first axis.


`X` must have the same shape as `Y`, excluding `Y`'s `K`th axis. Otherwise, if `X` is a one-element array, it will be extended to conform.


`R` is an array with the same shape as `Y`, with the elements of each of the vectors along the `K`th axis of `Y` rotated by the value of the corresponding element of `X`.  If the value is positive, the rotation is in the sense of right to left.  If the value is negative, the rotation is in the sense of left to right.


<h2 class="example">Examples</h2>
```apl
      3 ⌽ 1 2 3 4 5 6 7
4 5 6 7 1 2 3
      ¯2 ⌽ 1 2 3 4 5
4 5 1 2 3
 
      M
 1  2  3  4
 5  6  7  8
 
 9 10 11 12
13 14 15 16
 
      I
0 1 ¯1 0
0 3  2 1

      I⌽[2]M
 1  6  7  4
 5  2  3  8
 
 9 14 11 16
13 10 15 12

```
```apl
 
      J
2 ¯3
3 ¯2
      J⌽M
 3  4  1  2
 6  7  8  5
 
12  9 10 11
15 16 13 14
 
```


