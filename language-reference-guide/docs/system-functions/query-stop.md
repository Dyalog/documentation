---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕STOP STOP
</div>






<h1 class="heading"><span class="name">Query Stop</span> <span class="command">R←⎕STOP Y</span></h1>



`Y` must be a simple character scalar or vector which is taken to be the name of a visible defined function or operator.  `R` is a simple non-negative integer vector of the line numbers of the function or operator named by `Y` on which stop controls are set, shown in ascending order.  The value 0 in `R` indicates that a stop control is set immediately prior to exit from the function or operator.

<h2 class="example">Example</h2>
```apl
      ⎕STOP'FOO'
0 1
```



