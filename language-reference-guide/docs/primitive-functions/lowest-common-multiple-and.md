<div style="display: none;">
  ^
</div>





<h1 class="heading"><span class="name">Lowest Common Multiple/AND</span> <span class="command">R←X∧Y</span></h1>


## Case 1: Lowest Common Multiple – either or both X and Y are numeric (non-Boolean)


`R` is the lowest common multiple of `X` and `Y`. Note that in this case, `⎕CT` and `⎕DCT` are implicit arguments.

<h2 class="example">Example</h2>
```apl
      15 1 2 7 ∧ 35 1 4 0
105 1 4 0
 
      2 3 4 ∧ 0j1 1j2 2j3
0J2 3J6 8J12
 
      2j2 2j4 ∧ 5j5 4j4
10J10 ¯4J12
```

## Case 2: AND – `X` and `Y` are Boolean


`R` is Boolean is determined as follows:
```apl
             X   Y     R
      
             0   0     0
             0   1     0
             1   0     0
             1   1     1
```



Note that the ASCII caret (`^`) will also be interpreted as an APL **And** (`∧`).


<h2 class="example">Example</h2>
```apl
      0 1 0 1 ^ 0 0 1 1
0 0 0 1
```


