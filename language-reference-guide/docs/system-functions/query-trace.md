---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TRACE TRACE
</div>





<h1 class="heading"><span class="name">Query Trace</span> <span class="command">R←⎕TRACE Y</span></h1>



`Y` must be a simple character scalar or vector which is taken to be the name of a visible defined function or operator.  `R` is a simple non-negative integer vector of the line numbers of the function or operator named by `Y` on which trace controls are set, shown in ascending order.  The value 0 in `R` indicates that a trace control is set to display the result of the function or operator immediately prior to exit.

<h2 class="example">Example</h2>

```apl
      ⎕TRACE'DSL'
0 1 2 3 4 5 6
```



