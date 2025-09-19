<div style="display: none;">
  ⍕
</div>






<h1 class="heading"><span class="name">Format by Specification</span> <span class="command">R←X⍕Y</span></h1>



`Y` must be a simple real (non-complex) numeric array. `X` must be a simple integer scalar or vector.  `R` is a character array displaying the array `Y` according to the specification `X`. `R` has rank `1⌈⍴⍴Y` and `¯1↓⍴R` is `¯1↓⍴Y`. If any element of `Y` is complex, dyadic `⍕` reports a `DOMAIN ERROR`.


Conformability requires that if `X` has more than two elements, then `⍴X` must be `2×¯1↑⍴Y`. If `X` contains one element, it is extended to `(2×¯1↑⍴Y)⍴0,X`.  If `X` contains 2 elements, it is extended to `(2×¯1↑⍴Y)⍴X`.


`X` specifies two numbers (possibly after extension) for each column in `Y`.  For this purpose, scalar `Y` is treated as a one-element vector.  Each pair of numbers in `X` identifies a format width (`W`) and a format precision (`P`).


If `P` is 0, the column is to be formatted as integers.


<h2 class="example">Examples</h2>
```apl
      5 0 ⍕ 2 3⍴⍳6
    1    2    3
    4    5    6
 
      4 0⍕1.1 2 ¯4 2.547
   1   2  ¯4   3
```

<h2 class="example">Example</h2>


If `P` is positive, the format is floating point with `P` significant digits to be displayed after the decimal point.
```apl
      4 1⍕1.1 2 ¯4 2.547
 1.1 2.0¯4.0 2.5
```

<h2 class="example">Example</h2>


If `P` is negative, scaled format is used with `|P` digits in the mantissa.
```apl
      7 ¯3⍕5 15 155 1555
5.00E0 1.50E1 1.55E2 1.56E3
```

<h2 class="example">Example</h2>


If `W` is 0 or absent, then the width of the corresponding columns of `R` are determined by the maximum width required by any element in the corresponding columns of `Y`, plus one separating space.
```apl
      3⍕2 3⍴10 15.2346 ¯17.1 2 3 4
 10.000 15.235 ¯17.100
  2.000  3.000   4.000
```

<h2 class="example">Example</h2>


If a formatted element exceeds its specified field width when `W>`0, the field width for that element is filled with asterisks.
```apl
      3 0 6 2 ⍕ 3 2⍴10.1 15 1001 22.357 101 1110.1
 10 15.00
*** 22.36
101******
```

<h2 class="example">Example</h2>


If the format precision exceeds the internal precision, low order digits are replaced by the symbol '`_`'.
```apl
      26⍕2*100
1267650600228229_______________.__________________________
 
      ⍴26⍕2*100
59
 
      0 20⍕÷3
 0.3333333333333333____
 
      0 ¯20⍕÷3
 3.333333333333333____E¯1
```



The shape of `R` is the same as the shape of `Y` except that the last dimension of `R` is the sum of the field widths specified in `X` or deduced by the function.  If `Y` is a scalar, the shape of `R` is the field width.
```apl
      ⍴5 2 ⍕ 2 3 4⍴⍳24
2 3 20
```



