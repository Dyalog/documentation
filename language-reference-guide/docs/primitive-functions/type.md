<div style="display: none;">
  ∊
</div>

<h1 class="heading"><span class="name">Type</span> <span class="command">(⎕ML<1) R←∊Y</span></h1>

Migration level must be such that `⎕ML<1` (otherwise `∊` means Enlist. See [Enlist](enlist.md)).

`Y` may be any array.  `R` is an array with the same shape and structure as `Y` in which a numeric value is replaced by 0 and a character value is replaced by `' '`.

<h2 class="example">Examples</h2>
```apl
      ∊(2 3⍴⍳6)(1 4⍴'TEXT')
 0 0 0
 0 0 0
 
      ' '=∊'X'
1
```



