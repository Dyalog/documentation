---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MONITOR MONITOR
</div>






<h1 class="heading"><span class="name">Set Monitor</span> <span class="command">{R}←X ⎕MONITOR Y</span></h1>



`Y` must be a simple character scalar or vector which is taken to be the name of a visible defined function or operator.


Note that `⎕MONITOR` does not apply to  dfns or dops.


`X` must be a simple non-negative integer scalar or vector.  `R` is a simple integer vector of non-negative elements.


`X` identifies the numbers of lines in the function or operator named by `Y` on which a monitor is to be placed.  Numbers outside the range of line numbers in the function or operator (other than `0`) are ignored.  The number `0` indicates that a monitor is to be placed on the function or operator as a whole.  The value of `X` is independent of `⎕IO`.


`R` is a vector of numbers on which a monitor has been placed in ascending order.  The result is suppressed unless it is explicitly used or assigned. `R` will be empty for dfns and dops.


The effect of `⎕MONITOR` is to accumulate timing statistics for the lines for which the monitor has been set.  See [Query Monitor](query-monitor.md) for details.



<h2 class="example">Examples</h2>
```apl
      +(0,⍳10) ⎕MONITOR 'FOO'
0 1 2 3 4 5
```


Existing monitors are cancelled before new ones are set:
```apl
      +1 ⎕MONITOR 'FOO'
1
```


All monitors may be cancelled by supplying an empty vector:
```apl
      ⍬ ⎕MONITOR 'FOO'
```


Monitors may be set on a locked function or operator, but no information will be reported.  Monitors are saved with the workspace.



