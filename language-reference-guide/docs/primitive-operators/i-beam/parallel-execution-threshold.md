
<!-- Hidden search keywords -->
<div style="display: none;">
  1112⌶
</div>






<h1 class="heading"><span class="name">Parallel Execution Threshold</span> <span class="command">R←1112⌶Y</span></h1>



`Y` is an integer that specifies the array size threshold at which parallel execution takes place. If a parallel-enabled function is invoked on an array whose number of elements is equal to or greater than this threshold, execution takes place in parallel. If not, it doesn't.


Prior to this call, the default value of the threshold is specified by an environment variable named `APL_MIN_PARALLEL`. If this variable is not set, the default is 32768.


`R` is the previous value.


See [Parallel Execution](../../../../programming-reference-guide/introduction/parallel-execution) and [Number of Threads](number-of-threads.md).



