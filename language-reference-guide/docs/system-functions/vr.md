---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕VR VR
</div>






<h1 class="heading"><span class="name">Vector Representation</span> <span class="command">R←⎕VR Y</span></h1>



`Y` must be a simple character scalar or vector which represents the name of a function or defined operator.


If `Y` is the name of a defined function or defined operator, `R` is a simple character vector containing a character representation of the function or operator with each line except the last terminated by the newline character (`⎕UCS ⎕AVU[4]`).




Its display form is as follows:

1. the header line starts at column 8 with the `∇` symbol in column 6,
2. the line number for each line of the function starts in column 1,
3. the statement contained in each line starts at column 8 except for labelled lines or lines beginning with `⍝` which start at column 7,
4. the header line and statements contain no redundant blanks beyond column 7 except that the `⋄` separator is surrounded by single blanks, control structure indentation is preserved and comments retain embedded blanks as originally defined,
5. the last line shows only the `∇` character in column 6.



If `Y` is the name of a variable, a locked function or operator, an external function, or is undefined, `R` is an empty vector.

<h2 class="example">Example</h2>
```apl

      ⍴V←⎕VR'PLUS'
128

      V
     ∇ R←{A}PLUS B
[1]   ⍝ MONADIC OR DYADIC +
[2]    →DYADIC⍴⍨2=⎕NC'A' ⋄ R←B ⋄ →END
[3]   DYADIC:R←A+B ⋄ →END
[4]   END:
     ∇
```


The definition of `⎕VR` has been extended to names assigned to functions by specification (`←`), and to local names of functions used as operands to defined operators. In these cases, the result of `⎕VR` is identical to that of `⎕CR` except that the representation of defined functions and operators is as described above.

<h2 class="example">Example</h2>
```apl

      AVG←MEAN∘,

      +F←⎕VR'AVG'
      ∇ R←MEAN X    ⍝ Arithmetic mean
[1]     R←(+/X)÷⍴X
     ∇ ∘,

      ⍴F
3

      ]display F
┌→───────────────────────────────────────────┐
│ ┌→───────────────────────────────────┐     │
│ │     ∇ R←MEAN X    ⍝ Arithmetic mean│ ∘ , │
│ │[1]    R←(+/X)÷⍴X                   │ - - │
│ │     ∇                              │     │
│ └────────────────────────────────────┘     │
└∊───────────────────────────────────────────┘
```


