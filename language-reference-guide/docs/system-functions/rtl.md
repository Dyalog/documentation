---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕RTL RTL
</div>






# <span>Response Time Limit</span> `⎕RTL`



A non-zero value in `⎕RTL` places a time limit, in seconds, for input requested via `⍞`, `⎕ARBIN`, and `⎕SR`.  `⎕RTL` may be assigned any integer in the range 0 to 32767.  The value in a clear workspace is 0. `⎕RTL` has Namespace scope.

<h2 class="example">Example</h2>
```apl
      ⎕RTL←5 ⋄ ⍞←'FUEL QUANTITY?' ⋄ R←⍞
FUEL QUANTITY?
TIMEOUT
      ⎕RTL←5 ⋄ ⍞←'FUEL QUANTITY?' ⋄ R←⍞
```



