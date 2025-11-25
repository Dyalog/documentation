---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕STOP STOP
</div>

<h1 class="heading"><span class="name">Set Stop</span> <span class="command">{R}←X ⎕STOP Y</span></h1>

`Y` must be a simple character scalar or vector which is taken to be the name of a visible defined function or operator.  `X` must be a simple non-negative integer scalar or vector.  `R` is a simple integer vector of non-negative elements.  `X` identifies the numbers of lines in the function or operator named by `Y` on which a stop control is to be placed.  Numbers outside the range of line numbers in the function or operator (other than 0) are ignored.  The number 0 indicates that a stop control is to be placed immediately prior to exit from the function or operator.  If `X` is empty, all existing stop controls are cancelled.  The value of `X` is independent of `⎕IO`.


`R` is a vector of the line numbers on which a stop control has been placed in ascending order.  The result is suppressed unless it is explicitly used or assigned.

<h2 class="example">Examples</h2>
```apl
      ⊢(0,⍳10) ⎕STOP 'FOO'
0 1
```

Existing stop controls in the function or operator named by `Y` are cancelled before new stop controls are set:
```apl
      ⊢1 ⎕STOP 'FOO'
1
```

All stop controls may be cancelled by giving `X` an empty vector:
```apl
      ⍴'' ⎕STOP 'FOO'
0
 
      ⍴⍬ ⎕STOP 'FOO'
0
```

Attempts to set stop controls in a locked function or operator are ignored.
```apl
      ⎕LOCK'FOO'
 
      ⊢0 1 ⎕STOP'FOO'
```


The effect of `⎕STOP` when a function or operator is invoked is to suspend execution at the beginning of any line in the function or operator on which a stop control is placed immediately before that line is executed, and immediately before exiting from the function or operator if a stop control of 0 is set.  Execution may be resumed by a branch expression.  A stop control interrupt (1001) may also be trapped - see [Trap Event](trap.md).

<h2 class="example">Example</h2>
```apl
      ⎕FX'R←FOO' 'R←10'
 
      0 1 ⎕STOP'FOO'
 
      FOO
FOO[1]
 
      R
VALUE ERROR
      R
      ^
 
      →1
FOO[0]
 
      R
10
 
      →⎕LC
10
```


