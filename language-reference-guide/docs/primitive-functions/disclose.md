<div style="display: none;">
  ↑
</div>






<h1 class="heading"><span class="name">Disclose</span> <span class="command">(⎕ML) R←⊃Y or R←↑Y</span></h1>



The symbol chosen to represent Disclose depends on the current Migration Level.


If  `⎕ML<2`, Disclose is represented by the symbol: `⊃`.


If  `⎕ML≥2`, Disclose is represented by the symbol: `↑`.


`Y` may be any array.  `R` is an array.  If `Y` is non-empty, `R` is the value of the first item of `Y` taken in ravel order.  If `Y` is empty, `R` is the prototype of `Y`.


Disclose is the inverse of Enclose.  The identity `R←→⊃⊂R` holds for all `R`.  Disclose is also referred to as First.


<h2 class="example">Examples</h2>
```apl
      ⊃1
1
 
      ⊃2 4 6
2
 
      ⊃'MONDAY' 'TUESDAY'
MONDAY
 
      ⊃(1 (2 3))(4 (5 6))
1  2 3
 
      ⊃⍳0
0
 
      ' '=⊃''
1
 
      ⊃1↓⊂1,⊂2 3
0  0 0
```


