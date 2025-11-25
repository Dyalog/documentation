---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TKILL TKILL
</div>






<h1 class="heading"><span class="name">Kill Thread</span> <span class="command">{R}←{X}⎕TKILL Y</span></h1>



`Y` must be a simple array of integers representing thread numbers to be terminated. `X` is a Boolean single, defaulting to 1, which indicates that all descendant threads should also be terminated.


The shy result `R` is a vector of the numbers of all threads that have been terminated.


The **base thread** 0 is always excluded from the cull.


<h2 class="example">Examples</h2>
```apl
      ⎕TKILL 0            ⍝ Kill background threads.
 
      ⎕TKILL ⎕TID         ⍝ Kill self and descendants.
 
      0 ⎕TKILL ⎕TID       ⍝ Kill self only.
 
      ⎕TKILL ⎕TCNUMS ⎕TID ⍝ Kill descendants.
```


