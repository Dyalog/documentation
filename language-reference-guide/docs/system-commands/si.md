




<h1 class="heading"><span class="name">State Indicator</span> <span class="command">)SI {n} {-tid=tn}</span></h1>



This command displays the contents of the state indicator in the active workspace.  The state indicator identifies those operations which are suspended or pendent for each suspension.


The optional parameter `n` specifies that only the first `n` or last `¯n` lines of the output should be displayed.


The optional parameter `-tid=tn` specifies that the state indicator is to be displayed only for thread number `tn`.




The list consists of a line for each suspended or pendent operation beginning with the most recently suspended function or operator.  Each line may be:

- The name of a defined function or operator, followed by the line number at which the operation is halted, and followed by the `*` symbol if the operation is suspended. The name of the function or operator is its full pathname relative to the root namespace `#`. For example, `#.UTIL.PRINT`. In addition, the display of a function or operator which has dynamically changed space away from its origin is prefixed with its current space. For example, `[⎕SE] TRAV`.
- A primitive operator symbol.
- The Execute function symbol (`⍎`).
- The Evaluated Input symbol (`⎕`).
- The System Function `⎕DQ` or `⎕SR` (occurs when executing a callback function).



<h2 class="example">Examples</h2>
```apl
      )SI
#.PLUS[2]*
.
#.MATDIV[4]
#.FOO[1]*
⍎
```


This example indicates that at some point function `FOO` was executed and suspended on line 1. Subsequently, function `MATDIV` was invoked, with a function derived from the Inner Product or Outer Product operator (`.`) having defined function `PLUS` as an operand.




In the following, function `foo` in namespace `x` has called `goo` in namespace `y`. Function `goo` has then changed space (`⎕CS`) to namespace `z` where it has been suspended:
```apl
      )SI
[z] y.goo[2]*
x.foo[1]
```



## Threads


In a multi-threading application, where parent threads spawn child threads, the state indicator assumes the structure of a branching tree. Branches of the tree are represented by indenting lines belonging to child threads. For example:
```apl
      )SI
·   #.Calc[1]
&5
·   ·   #.DivSub[1]
·   &7
·   ·   #.DivSub[1]
·   &6
·   #.Div[2]*
&4
#.Sub[3]
#.Main[4]
```



Here, `Main` has called `Sub`, which has spawned threads `4` and `5` with functions: `Div` and `Calc`. Function `Div`, after spawning `DivSub` in each of threads `6` and `7`, has been suspended at line [2].


The state indicator for a particular thread `tn` may be displayed by specifying the parameter `-tid=tn`.
```apl
       ⎕←foo&¨10 10 10 10
┌→─────────┐
│9 10 11 12│
└~─────────┘
       )SI
·   #.foo[1]
&9
·   #.foo[1]
&10
·   #.foo[1]
&11
·   #.foo[1]
&12
      )SI -tid=11
#.foo[1]

```


