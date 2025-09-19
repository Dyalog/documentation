<div style="display: none;">
  &
</div>






<h1 class="heading"><span class="name">Spawn</span> <span class="command">{R}←{X}f&Y</span></h1>



`&` is a monadic operator with an ambivalent derived function. `&` spawns a new thread in which `f` is applied to its argument `Y` (monadic case) or between its arguments `X` and `Y` (dyadic case). The shy result of this application is the number of the newly created thread.


When function f terminates, its result (if any), the **thread result**, is returned. If the thread number is the subject of an active `⎕TSYNC`, the thread result appears as the result of `⎕TSYNC`. If no `⎕TSYNC` is in effect, the thread result is displayed in the session in the normal fashion.


Note that `&` can be used in conjunction with the **each** operator `¨` to launch many threads in parallel.


<h2 class="example">Examples</h2>
```apl
      ÷&4         ⍝ Reciprocal in background
0.25
 
      ⎕←÷&4       ⍝ Show thread number
1
0.25
 
      FOO&88      ⍝ Spawn monadic function.
 
      2 FOO&3     ⍝ dyadic
 
      {NIL}&0     ⍝ niladic
 
      ⍎&'NIL'     ⍝ ..
 
      X.GOO&99    ⍝ thread in remote space.
 
      ⍎&'⎕DL 2'   ⍝ Execute async expression.
 
      'NS'⍎&'FOO' ⍝ .. remote .. .. .. 
 
      PRT&¨↓⎕NL 9 ⍝ PRT spaces in parallel.
```


