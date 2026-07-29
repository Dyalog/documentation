---
search:
  boost: 2
---

# <span>Event Number</span> `R←⎕EN`{{key}}

This simple integer scalar reports the identification number for the most recent event which occurred, caused by an APL action or by an interrupt or by the `⎕SIGNAL` system function.  Its value in a clear workspace is `0`.

<h2 class="example">Example</h2>
```apl
      ÷0
DOMAIN ERROR: Divide by zero
      ÷0
     ∧
      ⎕EN
11
```

See [APL Error Messages](../../../programming-reference-guide/error-messages/apl-errors).

!!! note
    `⎕SIGNAL` can be used to reset the value of this system constant.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EN EN
</div>
