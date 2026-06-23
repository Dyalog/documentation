---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CR CR
</div>






<h1 class="heading"><span class="name">Canonical Representation</span> <span class="command">R←⎕CR Y</span></h1>



`Y` must be a simple character scalar or vector which represents the name of a defined function or operator.


If `Y` is a name of a defined function or operator, `R` is a simple character matrix.  The first row of `R` is the function or operator header.  Subsequent rows are lines of the function or operator.  `R` contains no unnecessary blanks, except for leading indentation of control structures, trailing blanks that pad each row, and the blanks in comments.  If `Y` is the name of a variable, a locked function or operator, an external function, or is undefined, `R` is an empty matrix whose shape is `0 0`.


<h2 class="example">Example</h2>
```apl
      ∇R←MEAN X    ⍝ Arithmetic mean
[1]  R←(+/X)÷⍴X
[2]  ∇
      +F←⎕CR'MEAN'
R←MEAN X    ⍝ Arithmetic mean
R←(+/X)÷⍴X
 
      ⍴F
2 30
```


The definition of `⎕CR` has been extended to names assigned to functions by specification (`←`), and to local names of functions used as operands to defined operators.


If `Y` is a name assigned to a primitive function, `R` is a one-element vector containing the corresponding function symbol.  If `Y` is a name assigned to a system function, `R` is a one element nested array containing the name of the system function.

<h2 class="example">Examples</h2>
```apl
      PLUS←+
      +F←⎕CR'PLUS'
+
      ⍴F
1
      C←⎕CR
      C'C'
 ⎕CR
      ⍴C'C'
1
```
```apl

      ∇R←CONDITION (FN1 ELSE FN2) X
[1]   →CONDITION/L1
[2]   R←FN2 X ⋄ →0
[3]  L1:R←FN1 X
[4]   ∇
 
      2 ⎕STOP 'ELSE'
      (X≥0) ⌊ ELSE ⌈ X←¯2.5
 
ELSE[2]
       X
¯2.5
       ⎕CR'FN2'
⌈
       →⎕LC
¯2
```


If `Y` is a name assigned to a derived function, `R` is a vector whose elements represent the arrays, functions, and operators from which `Y` was constructed.  Constituent functions are represented by their own `⎕CR`s, so in this respect the definition of `⎕CR` is recursive.  Primitive operators are treated like primitive functions, and are represented by their corresponding symbols.  Arrays are represented by themselves.

<h2 class="example">Example</h2>
```apl
      BOX←2 2∘⍴
      +F←⎕CR'BOX'
 2 2 ∘⍴
      ⍴F
3
      ]Display F
.→----------.
| .→--.     |
| |2 2| ∘ ⍴ |
| '~--' - - |
'∊----------'
```


If `Y` is a name assigned to a defined function, `R` is the `⎕CR` of the defined function.  In particular, the name that appears in the function header is the name of the original defined function, not the assigned name `Y`.

<h2 class="example">Example</h2>
```apl
      AVERAGE←MEAN
      ⎕CR'AVERAGE'
R←MEAN X    ⍝ Arithmetic mean
R←(+/X)÷⍴X
```


