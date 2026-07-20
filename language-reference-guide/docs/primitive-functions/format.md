---
search:
  boost: 2
---

# <span>Format</span> `R←⍕Y`{{key}}

`Y` may be any array. `R` is a simple character array which will display identically to the display produced by `Y`. The result is independent of `⎕PW`.  If `Y` is a simple character array, then `R` is `Y`.

<h2 class="example">Example</h2>
```apl
      +B←⍕A←2 6⍴'HELLO PEOPLE'
HELLO
PEOPLE
 
      B ≡ A
1
```

If `Y` is a simple numeric scalar, then `R` is a vector containing the formatted number without any spaces.  A floating point number is formatted according to the system variable `⎕PP`.  `⎕PP` is ignored when formatting integers.

<h2 class="example">Examples</h2>
```apl
      ⎕PP←5
 
      ⍴C←⍕⍳0
0
 
      ⍴C←⍕10
2
 
      C
10
 
      ⍴C←⍕12.34
5
 
      C
12.34
 
      ⍕123456789
123456789
 
      ⍕123.456789
123.46
```

Scaled notation is used if the magnitude of the non-integer number is too large to represent with `⎕PP` significant digits or if the number requires more than five leading zeroes after the decimal point.

<h2 class="example">Examples</h2>
```apl
      ⍕123456.7
1.2346E5
 
      ⍕0.0000001234
1.234E¯7
```

If `Y` is a simple numeric vector, then `R` is a character vector in which each element of `Y` is independently formatted with a single separating space between formatted elements.

<h2 class="example">Example</h2>
```apl
      ⍴C←⍕¯123456 1 22.5 ¯0.000000667 5.00001
27
 
      C
¯1.2346E5 1 22.5 ¯6.67E¯7 5
```

If `Y` is a simple numeric array rank higher than one, `R` is a character array with the same shape as `Y` except that the last dimension of `Y` is determined by the length of the formatted data.  The format width is determined independently for each column of `Y`, such that:

1. the decimal points for floating point or scaled formats are aligned.
2. the `E` characters for scaled formats are aligned, with trailing zeros added to the mantissae if necessary.
3. integer formats are aligned to the left of the decimal point column, if any, or right-adjusted in the field otherwise.
4. each formatted column is separated from its neighbours by a single blank column.
5. the exponent values in scaled formats are left-adjusted to remove any blanks.

<h2 class="example">Examples</h2>
```apl
      C←22 ¯0.000000123 2.34 ¯212 123456 6.00002 0
 
      ⍴C←⍕2 2 3⍴C
2 2 29
 
      C
  22    ¯1.2300E¯7  2.3400E0
¯212     1.2346E5   6.0000E0
 
   0     2.2000E1  ¯1.2300E¯7
   2.34 ¯2.1200E2   1.2346E5
```

If `Y` is non-simple, and all items of `Y` at any depth are scalars or vectors, then `R` is a vector.

<h2 class="example">Examples</h2>
```apl
      B←⍕A←'ABC' 100 (1 2 (3 4 5)) 10
 
      ⍴A
4
      ≡A
¯3
 
      ⍴B
26
      ≡B
1
 
      A
 ABC  100  1 2  3 4 5   10
 
      B
 ABC  100  1 2  3 4 5   10
```

By replacing spaces with `^`, it is clearer to see how the result of `⍕` is formed:
```apl
^ABC^^100^^1^2^^3^4^5^^^10
```

If `Y` is non-simple, and all items of `Y` at any depth are not scalars, then `R` is a matrix.

<h2 class="example">Example</h2>
```apl
      D←⍕C←1 'AB' (2 2⍴1+⍳4) (2 2 3⍴'CDEFGHIJKLMN')
 
      C
1  AB  2 3  CDE
       4 5  FGH
 
            IJK
            LMN
 
      ⍴C
4
 
      ≡C
¯2
 
      D
1  AB  2 3  CDE
       4 5  FGH
 
            IJK
            LMN
 
      ⍴D
5 16
 
      ≡D
1
```

By replacing spaces with `^`, it is clearer to see how the result of `⍕` is formed:
```apl
1^^AB^^2^3^^CDE^
^^^^^^^4^5^^FGH^
^^^^^^^^^^^^^^^^
^^^^^^^^^^^^IJK^
^^^^^^^^^^^^LMN^
```

`⎕PP` is an implicit argument of Format.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍕ format
</div>
