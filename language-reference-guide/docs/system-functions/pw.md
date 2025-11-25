---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PW PW
</div>






<h1 class="heading"><span class="name">Print Width</span> <span class="command">⎕PW</span></h1>



`⎕PW` is the maximum number of output characters per line before folding the display.


`⎕PW` may be assigned any integer value in the range 42 to 32767. Note that in versions of Dyalog APL prior to 13.0 `⎕PW` had a minimum value of 30; this was increased to support 128-bit decimal values. `⎕PW` has Session scope.


If an attempt is made to display a line wider than `⎕PW`, then the display will be folded at or before the `⎕PW` width and the folded portions indented 6 spaces.  The display of a simple numeric array may be folded at a width less than `⎕PW` so that individual numbers are not split.


`⎕PW` only affects output, either direct or through `⎕` output.  It does not affect the result of the function Format (`⍕`), of the system function `⎕FMT`, or output through the system functions `⎕ARBOUT` and `⎕ARBIN`, or output through `⍞`.


Note that if the Auto_PW parameter (*Options/Configure/Session/Auto PW*) is set to 1, `⎕PW` is automatically adjusted whenever the Session window is resized. In these circumstances, a value assigned to `⎕PW` will only apply until the Session window is next resized.

<h2 class="example">Examples</h2>
```apl
      ⎕PW←42
 
      ⎕←3⍴÷3
0.3333333333 0.3333333333 0.3333333333
      0.3333333333
```



