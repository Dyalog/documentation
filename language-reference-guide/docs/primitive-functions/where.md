<div style="display: none;">
  ⍸
</div>






<h1 class="heading"><span class="name">Where</span> <span class="command">R←⍸Y</span></h1>



**Classic Edition:**  the symbol `⍸` (Iota Underbar) is not available in Classic Edition, and Where is instead represented by `⎕U2378`.


`Y` must be a simple Boolean or numeric array of non-negative integers.


The model for Where can be expressed as `{(,⍵)/,⍳⍴⍵}`.


If `Y` is Boolean, `R` is a vector of the indices of all the 1s in `Y`. If `Y` is all zeros, `R` is an empty vector.


`⎕IO` is an implicit argument of Where.


<h2 class="example">Examples</h2>
```apl
      ⎕IO
1
      ⍸ 1 0 1 0 0 0 0 1 0
1 3 8

      ⍸'e'='Pete'
2 4

      3 4⍴0 1 1
0 1 1 0
1 1 0 1
1 0 1 1

      ⍸ 3 4⍴0 1 1
┌───┬───┬───┬───┬───┬───┬───┬───┐
│1 2│1 3│2 1│2 2│2 4│3 1│3 3│3 4│
└───┴───┴───┴───┴───┴───┴───┴───┘

      ⍸2 3 4⍴0 0 0 0 1
┌─────┬─────┬─────┬─────┐
│1 2 1│1 3 2│2 1 3│2 2 4│
└─────┴─────┴─────┴─────┘

      ⍸ 0 1 0 2
2 4 4

      {⍵/⍥,⍳⍴⍵} 0 1 0 2
2 4 4
      ⍸2 2⍴0 1 2 3
┌───┬───┬───┬───┬───┬───┐
│1 2│2 1│2 1│2 2│2 2│2 2│
└───┴───┴───┴───┴───┴───┘

```


