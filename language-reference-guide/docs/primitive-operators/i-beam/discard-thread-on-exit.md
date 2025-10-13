
<!-- Hidden search keywords -->
<div style="display: none;">
  2501⌶
</div>

<h1 class="heading"><span class="name">Discard Thread on Exit</span> <span class="command">R←2501⌶Y</span></h1>

APL threads that Dyalog creates to serve incoming .NET requests are not terminated when their work is done. They persist so that if another call comes in on the same .NET thread the same APL thread can handle it. In effect the thread is *parked* until it is needed again. If the thread is not required, there is a small performance cost in maintaining it in this state.

`(2501⌶0)` must be called from WITHIN one of these threads and tells the interpreter NOT to park the thread on termination, but to discard the thread completely.



