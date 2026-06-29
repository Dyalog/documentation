---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NR NR
</div>






<h1 class="heading"><span class="name">Nested Representation</span> <span class="command">R←⎕NR Y</span></h1>



`Y` must be a simple character scalar or vector which represents the name of a function or a defined operator.


If `Y` is a name of a defined function or defined operator, `R` is a vector of text vectors.  The first element of `R` contains the text of the function or operator header.  Subsequent elements contain lines of the function or operator.  Elements of `R` contain no unnecessary blanks, except for leading indentation of control structures and the blanks which precede comments.


If `Y` is the name of a variable, a locked function or operator, an external function or a namespace, or is undefined, `R` is an empty vector.


<h2 class="example">Example</h2>
```apl
      ∇R←MEAN X    ⍝ Average
[1]   R←(+/X)÷⍴X
      ∇
 
      +F←⎕NR'MEAN'
  R←MEAN X    ⍝Average   R←(+/X)÷⍴X
 
      ⍴F
2
      ]Display F
.→----------------------------------------.
| .→---------------------.  .→----------. |
| | R←MEAN X    ⍝ Average|  | R←(+/X)÷⍴X| |
| '----------------------'  '-----------' |
'∊----------------------------------------'
```


The definition of `⎕NR` has been extended to names assigned to functions by specification (`←`), and to local names of functions used as operands to defined operators.  In these cases, the result of `⎕NR` is identical to that of `⎕CR` except that the representation of defined functions and operators is as described above.

<h2 class="example">Example</h2>
```apl
      AVG←MEAN∘,
 
      +F←⎕NR'AVG'
   R←MEAN X    ⍝ Average   R←(+/X)÷⍴X  ∘,
 
      ⍴F
3
      ]Display F
.→------------------------------------------------.
| .→----------------------------------------.     |
| | .→---------------------.  .→----------. | ∘ , |
| | | R←MEAN X    ⍝ Average|  | R←(+/X)÷⍴X| | - - |
| | '----------------------'  '-----------' |     |
| '∊----------------------------------------'     |
'∊------------------------------------------------'
```





