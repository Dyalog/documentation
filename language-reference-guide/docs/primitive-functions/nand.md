<div style="display: none;">
  ⍲
</div>






<h1 class="heading"><span class="name">NAND</span> <span class="command">R←X⍲Y</span></h1>



`Y` must be a Boolean array. `X` must be a Boolean array. `R` is Boolean. The value of `R` is the truth value of the proposition "not both `X` and `Y`", and is determined as follows:
```apl
             X   Y     R
      
             0   0     1
             0   1     1
             1   0     1
             1   1     0
```

<h2 class="example">Example</h2>
```apl
      (0 1)(1 0) ⍲ (0 0)(1 1)
 1 1  0 1
```



