---
search:
  boost: 2
---

# <span>Print Precision</span> `⎕PP`

`⎕PP` is the number of significant digits in the display of numeric output. `⎕PP` may be assigned any integer value in the range 1 to 34. `⎕PP` has Namespace scope.

`⎕PP` is used to format numbers displayed directly. It is an implicit argument of monadic function Format (`⍕`), monadic `⎕FMT` and for display of numbers via `⎕` and `⍞` output. `⎕PP` is ignored for the display of integers.

<h2 class="example">Examples</h2>
```apl

      ⎕PP←10
 
      ÷3 6
0.3333333333 0.1666666667
 
      ⎕PP←3
 
      ÷3 6
0.333 0.167
```

If `⎕PP` is set to a value `≥17` (when `⎕FR` is 645) or 34 (when `⎕FR` is 1287), floating-point numbers may be converted between binary and character representation without loss of precision. Then, if  `⎕CT` is 0 (to ensure exact comparison), for any floating-point number `N` the expression `N=⍎⍕N` is true.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PP PP
</div>
