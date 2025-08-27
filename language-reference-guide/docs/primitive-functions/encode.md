<div style="display: none;">
  ⊤
</div>






<h1 class="heading"><span class="name">Encode</span> <span class="command">R←X⊤Y</span></h1>



`Y` must be a simple numeric array.  `X` must be a simple numeric array.  `R` is the numeric array which results from the representation of `Y` in the number system defined by `X`.


The shape of `R` is `(⍴X),⍴Y` (the catenation of the shapes of `X` and `Y`).


If `X` is a vector or a scalar, the result for each element of `Y` is the value of the element expressed in the number system defined by radix `X`.  If `Y` is greater than can be expressed in the number system, the result is equal to the representation of the residue `(×/X)|Y`.  If the first element of `X` is 0, the value will be fully represented.


This function is also known as Representation.


<h2 class="example">Examples</h2>
```apl
      10⊤5 15 125
5 5 5
 
      0 10⊤5 15 125
0 1 12
5 5  5
```


If `X` is a higher-rank array, each of the vectors along the first axis of `X` is used as the radix vector for each element of `Y`.

<h2 class="example">Examples</h2>
```apl
      A
2 0  0
2 0  0
2 0  0
2 0  0
2 8  0
2 8  0
2 8 16
2 8 16
 

```


This example shows binary, octal and hexadecimal representations of the decimal number 75.
```apl
      A⊤75
0 0  0
1 0  0
0 0  0
0 0  0
1 0  0
0 1  0
1 1  4
1 3 11
```

<h2 class="example">Examples</h2>
```apl
      0 1⊤1.25 10.5
1    10
0.25  0.5
 
      4 13⊤13?52
 3 1 0  2 3 2 0 1  3 1 2 3 1
12 2 4 12 1 7 6 3 10 1 0 3 8
```


`⎕IO` is not an implicit argument of encode.


