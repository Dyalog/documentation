---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TRACE TRACE
</div>






<h1 class="heading"><span class="name">Set Trace</span> <span class="command">{R}←X ⎕TRACE Y</span></h1>



`Y` must be a simple character scalar or vector which is taken to be the name of a visible defined function or operator.  `X` must be a simple non-negative integer scalar or vector.


`X` identifies the numbers of lines in the function or operator named by `Y` on which a trace control is to be placed.  Numbers outside the range of line numbers in the function or operator (other than 0) are ignored.  The number 0 indicates that a trace control is to be placed immediately prior to exit from the function or operator.  The value of `X` is independent of `⎕IO`.


`R` is a simple integer vector of non-negative elements indicating the lines in the function or operator on which a trace control has been placed.


<h2 class="example">Example</h2>
```apl
      +(0,⍳10) ⎕TRACE'FOO'
0 1
```


Existing trace controls in the function or operator named by `Y` are cancelled before new trace controls are set:
```apl
      + 1 ⎕TRACE'FOO'
1
```


All trace controls may be cancelled by giving `X` an empty vector:
```apl
      ⍴⍬ ⎕TRACE 'FOO'
0
```


Attempts to set trace controls in a locked function or operator are ignored.
```apl
      ⎕LOCK 'FOO'
      +1 ⎕TRACE 'FOO'
```


The effect of trace controls when a function or operator is invoked is to display the result of each complete expression for lines with trace controls as they are executed, and the result of the function if trace control 0 is set.  If a line contains expressions separated by `⋄`, the result of each complete expression is displayed for that line after execution.



The result of a complete expression is displayed even where the result would normally be suppressed.  In particular:

- the result of a branch statement is displayed;
- the result (*pass-through value*) of assignment is displayed;
- the result of a function whose result would normally be suppressed is displayed;




For each traced line, the output from `⎕TRACE` is displayed as a two element vector, the first element of which contains the function or operator name and line number, and the second element of which takes one of two forms.

- The result of the line, displayed as in standard output.
- `→` followed by a line number.


<h2 class="example">Example</h2>
```apl
      ⎕VR 'DSL'
     ∇ R←DSL SKIP;A;B;C;D
[1]    A←2×3+4
[2]    B←(2 3⍴'ABCDEF')A
[3]    →NEXT×⍳SKIP
[4]    'SKIPPED LINE'
[5]   NEXT:C←'one' ⋄ D←'two'
[6]   END:R←C D
     ∇
 
      (0,⍳6) ⎕TRACE 'DSL'
 
      DSL 1
 DSL[1]  14
 DSL[2]   ABC   14
          DEF
 DSL[3]  →5
 DSL[5]  one
 DSL[5]  two
 DSL[6]   one   two
 DSL[0]   one   two
 one  two
```


