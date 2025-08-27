<div style="display: none;">
  ⌈
</div>






<h1 class="heading"><span class="name">Ceiling</span> <span class="command">R←⌈Y</span></h1>



Ceiling is defined in terms of Floor as `⌈Y←→-⌊-Y`


`Y` must be numeric.


If an element of `Y` is real, the corresponding element of `R` is the least integer greater than or equal to the value of `Y`.


If an element of `Y` is complex, the corresponding element of `R` depends on the relationship between the real and imaginary parts of the numbers in `Y`.

<h2 class="example">Examples</h2>
```apl
      ⌈¯2.3  0.1  100  3.3
¯2 1 100 4
 
      ⌈1.2j2.5 1.2j¯2.5
1J3 1J¯2
```


For further explanation, see [Floor](floor.md).


`⎕CT` is an implied argument of Ceiling.



