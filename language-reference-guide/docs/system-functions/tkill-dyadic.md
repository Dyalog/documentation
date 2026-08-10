---
search:
  boost: 2
---

# <span>Kill Threads and Descendants</span> `{R}←X ⎕TKILL Y`{{key}}

`Y` must be a simple array of integers representing thread numbers to be terminated. `X` is a Boolean single that indicates whether all descendant threads should also be terminated.

To kill only the named threads, use [monadic `⎕TKILL`](tkill-monadic.md).

The shy result `R` is a vector of the numbers of all threads that have been terminated.

The **base thread** 0 is always excluded from the cull.

<h2 class="example">Examples</h2>
```apl
      1 ⎕TKILL ⎕TID       ⍝ Kill self and descendants.
 
      0 ⎕TKILL ⎕TID       ⍝ Kill self only.
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TKILL TKILL
</div>
