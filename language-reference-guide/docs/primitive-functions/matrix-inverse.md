<div style="display: none;">
  ⌹
</div>






<h1 class="heading"><span class="name">Matrix Inverse</span> <span class="command">R←⌹Y</span></h1>



`Y` must be a simple array of rank 2 or less.  `Y` must be non-singular.  If `Y` is a scalar, it is treated as a one-element matrix.  If `Y` is a vector, it is treated as a single-column matrix.  `Y` must have at least the same number of rows as columns.


`R` is the inverse of `Y` if `Y` is a square matrix, or the left inverse of `Y` if `Y` is not a square matrix.  That is, `R+.×Y` is an identity matrix.


The shape of `R` is `⌽⍴Y`.


<h2 class="example">Examples</h2>
```apl
      M
2 ¯3
4 10
 
      +A←⌹M
 0.3125 0.09375
¯0.125  0.0625
```


Within calculation accuracy, `A+.×M` is the identity matrix.
```apl
      A+.×M
1 0
0 1
 
 
      j←{⍺←0 ⋄ ⍺+0J1×⍵}
      x←j⌿¯50+?2 5 5⍴100
      x
¯37J¯41  25J015  ¯5J¯09   3J020 ¯29J041
¯46J026  17J¯24  17J¯46  43J023 ¯12J¯18
  1J013  33J025 ¯47J049 ¯45J¯14   2J¯26
 17J048 ¯50J022 ¯12J025 ¯44J015  ¯9J¯43
 18J013   8J038  43J¯23  34J¯07   2J026
      ⍴x
5 5
      id←{∘.=⍨⍳⍵}  ⍝ identity matrix of order ⍵
      ⌈/,| (id 1↑⍴x) - x+.×⌹x
3.66384E¯16
```


