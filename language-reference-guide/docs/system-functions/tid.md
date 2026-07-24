---
search:
  boost: 2
---

# <span>Current Thread Identity</span> `R←⎕TID`{{key}}

`R` is a simple integer scalar whose value is the number of the current thread.

<h2 class="example">Examples</h2>
```apl
      ⎕TID     ⍝ Base thread number
0
 
      ⍎&'⎕TID' ⍝ Thread number of async ⍎.
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TID TID
</div>
