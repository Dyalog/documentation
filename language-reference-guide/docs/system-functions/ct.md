---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CT CT
</div>






<h1 class="heading"><span class="name">Comparison Tolerance</span> <span class="command">⎕CT</span></h1>



The value of `⎕CT` determines the precision with which two numbers are judged to be equal.  Two numbers, `X` and `Y`, are judged to be equal if `(|X-Y)≤⎕CT×(|X)⌈|Y`where `≤` is applied without tolerance.


Thus `⎕CT` is not used as an absolute value in comparisons, but rather specifies a relative value that is dependent on the magnitude of the number with the greater magnitude. It then follows that `⎕CT` has no effect when either of the numbers is zero.


`⎕CT` may be assigned any value in the range from `0` to  `2*¯32`  (about `2.3E¯10`). A value of `0` ensures exact comparison.  The value in a clear workspace is `1E¯14`. `⎕CT` has Namespace scope.


If [`⎕FR`](fr.md) is 1287, the system uses `⎕DCT`. See [Decimal Comparison Tolerance ](dct.md).


`⎕CT` and `⎕DCT` are implicit arguments of the monadic primitive functions Ceiling (`⌈`), Floor (`⌊`) and Unique (`∪`), and of the dyadic functions Equal (`=`), Excluding (`~`), Find (`⍷`), Greater (`>`), Greater or Equal (`≥`), Greatest Common Divisor (`∨`), Index of (`⍳`), Intersection (`∩`), Less (`<`), Less or Equal (`≤`), Lowest Common Multiple (`∧`), Match (`≡`), Membership (`∊`), Not Match (`≢`), Not Equal (`≠`), Residue (`|`) and Union (`∪`), as well as `⎕FMT` O-format.

<h2 class="example">Examples</h2>
```apl
      ⎕CT←1E¯10
      1.00000000001 1.0000001 = 1
1 0
```



