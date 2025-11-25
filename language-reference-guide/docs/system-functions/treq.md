---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TREQ TREQ
</div>






<h1 class="heading"><span class="name">Token Requests</span> <span class="command">R←⎕TREQ Y</span></h1>



`Y` is a simple scalar or vector of thread numbers.


`R` is a vector containing the concatenated token requests for all the threads specified in `Y`. This is effectively the result of catenating all of the right arguments together for all threads in `Y` that are currently executing `⎕TGET`.

<h2 class="example">Example</h2>
```apl
    ⎕TREQ ⎕TNUMS    ⍝ tokens required by all threads.
```



