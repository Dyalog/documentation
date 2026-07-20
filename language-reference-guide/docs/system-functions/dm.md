---
search:
  boost: 2
---

# <span>Diagnostic Message</span> `R←⎕DM`{{key}}

This niladic function returns the last reported APL error as a three-element vector, giving error message, line in error and position of caret pointer.

<h2 class="example">Example</h2>
```apl

      2÷0
DOMAIN ERROR
      2÷0
     ^

      ⎕DM
 DOMAIN ERROR        2÷0       ^
```

Note: `⎕SIGNAL` can be used to reset the value of this system constant.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DM DM
</div>
