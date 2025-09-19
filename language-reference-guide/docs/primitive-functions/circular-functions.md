<div style="display: none;">
  ○
</div>






<h1 class="heading"><span class="name">Circular Functions</span> <span class="command">R←X○Y</span></h1>



`Y` must be numeric. `X` must be an integer in the range `¯12 ≤ X ≤ 12`. `R` is numeric.


`X` determines which of a family of trigonometric, hyperbolic, Pythagorean, and complex functions to apply to `Y`, from the following table. Note that when `Y` is complex, `a` and  `b` are used to represent its real and imaginary parts, while `θ` represents its phase.


|(-X) ○ Y|X|X ○ Y|
|---|---|---|
|`(1-Y*2)*.5`|`0`|`(1-Y*2)*.5`|
|`Arcsin Y`|`1`|`Sine Y`|
|`Arccos Y`|`2`|`Cosine Y`|
|`Arctan Y`|`3`|`Tangent Y`|
|`Y=¯1:0Y≠¯1:(Y+1)×((Y-1)÷Y+1)*0.5`|`4`|`(1+Y*2)*.5`|
|`Arcsinh Y`|`5`|`Sinh Y`|
|`Arccosh Y`|`6`|`Cosh Y`|
|`Arctanh Y`|`7`|`Tanh Y`|
|`-8○Y`|`8`|`(-1+Y*2)*0.5`|
|`Y`|`9`|`a`|
|`+Y`|`10`|`|Y`|
|`Y×0J1`|`11`|`b`|
|`*Y×0J1`|`12`|`θ`|


<h2 class="example">Examples</h2>
```apl
      0 ¯1 ○ 1
0 1.570796327
 
      1○(PI←○1)÷2 3 4
1 0.8660254038  0.7071067812
 
      2○PI÷3
0.5
```
```apl
 
      9 11○3.5J¯1.2
3.5 ¯1.2

      9 11∘.○3.5J¯1.2 2J3 3J4
 3.5 2 3
¯1.2 3 4

      ¯4○¯1
0
```


