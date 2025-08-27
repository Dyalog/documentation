<div style="display: none;">
  |
</div>






<h1 class="heading"><span class="name">Residue</span> <span class="command">R←X|Y</span></h1>



`Y` may be any numeric array.  `X` may be any numeric array.


For positive arguments, `R` is the remainder when `Y` is divided by `X`. If `X=0`, `R` is `Y`.


For other argument values, `R` is given by the expression `Y-X×⌊Y÷X+0=X`. This expression also applies when `X` and/or `Y` are complex if the simple `⌊` is replaced by the `CpxFloor` function. See [Complex Floor](floor.md).


`⎕CT` and `⎕DCT` are  implicit arguments of Residue.


<h2 class="example">Examples</h2>
```apl
      3 3 ¯3 ¯3|¯5 5 ¯4 4
1 2 ¯1 ¯2
 
      0.5|3.12 ¯1 ¯0.6
0.12 0 0.4
 
      ¯1 0 1|¯5.25 0 2.41
¯0.25 0 0.41
 
      1j2|2j3 3j4 5j6
1J1 ¯1J1 0J1
```


Note that the ASCII Broken Bar (`⎕UCS 166`, U+00A6) is not interpreted as Residue.


