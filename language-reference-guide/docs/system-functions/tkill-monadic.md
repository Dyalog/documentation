---
search:
  boost: 2
---

# <span>Kill Threads</span> `{R}←⎕TKILL Y`{{key}}

`Y` must be a simple array of integers representing thread numbers to be terminated. All descendant threads are also terminated.

The shy result `R` is a vector of the numbers of all threads that have been terminated.

The **base thread** 0 is always excluded from the cull.

<h2 class="example">Examples</h2>
```apl
      ⎕TKILL 0            ⍝ Kill background threads.
 
      ⎕TKILL ⎕TID         ⍝ Kill self and descendants.
 
      ⎕TKILL ⎕TCNUMS ⎕TID ⍝ Kill descendants.
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TKILL TKILL
</div>
