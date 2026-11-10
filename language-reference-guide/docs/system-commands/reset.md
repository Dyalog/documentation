# <span>Reset State Indicator</span> `)RESET {n}`

This command cancels all suspensions recorded in the state indicator and discards any unprocessed events in the event queue.

The optional parameter `n` specifies that only the top `n` levels of the state indicator are to be cleared, leaving execution suspended at the level below them. A suspension that spans several levels can, therefore, be cleared in part, whereas [abort](../other-syntax/abort.md) (`→`) clears the whole of the most recent suspension.

`)RESET` also performs an internal re-organisation of the workspace and process memory. See [Workspace Available](../system-functions/wa.md)  for details.

<h2 class="example">Examples</h2>
```apl
      )SI
#.FOO[1]*
⍎
#.FOO[1]*
 
      )RESET
 
      )SI
```

In `Calculate`, the dfn `outer` calls the dfn `inner`, which divides by zero:

```apl
     ∇ Calculate;outer
[1]    outer←{
[2]        inner←{
[3]            ÷0
[4]        }
[5]        1+inner ⍬
[6]    }
[7]    1+outer ⍬
     ∇
```

The suspension spans three levels of the state indicator. `)RESET 1` clears only the top level, leaving `outer` suspended:

```apl
      Calculate
DOMAIN ERROR: Divide by zero
outer[2] ÷0
         ∧
      )SI
#.inner[2]*
#.outer[4]
#.Calculate[7]
      )RESET 1
      )SI
#.outer[4]*
#.Calculate[7]
```
