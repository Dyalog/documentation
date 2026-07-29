# Tail Calls

A novel feature of the implementation of dfns is the way in which tail calls are optimised.

When a dfn calls a sub-function, the result of the call may or may not be modified by the calling function before being returned. A call where the result is passed back immediately without modification is termed a tail call.

For example in the following, the first call on function `fact` is a tail call because the result of  `fact` is the result of the whole expression, whereas the second call isn't because the result is subsequently multiplied by `⍵`.
```apl
      (⍺×⍵)fact ⍵-1       ⍝ Tail call on fact.
      ⍵×fact ⍵-1          ⍝ Embedded call on fact.
```

Tail calls occur frequently in dfns, and the interpreter optimises them by re-using the current stack frame instead of creating a new one. This gives a significant saving in both time and workspace usage. It is easy to check whether a call is a tail call by tracing it. An embedded call will pop up a new trace window for the called function, whereas a tail call will re-use the current one.

Using tail calls can improve code performance considerably, although at first the technique might appear obscure. A simple way to think of a tail call is as a **branch with arguments**. The tail call, in effect, branches to the first line of the function after installing new values for `⍵` and `⍺`.

**Iterative algorithms can almost always be coded using tail calls.**

In general, when coding a loop, we use the following steps; possibly in a different order depending on whether we want to test at the "top" or the "bottom" of the loop.

1. Initialise loop control variable(s). `⍝ init`
2. Test loop control variable. `⍝ test`
3. Process body of loop. `⍝ proc`
4. Modify loop control variable for next iteration. `⍝ mod`
5. Branch to step 2. `⍝ jump`

For example, in classical APL you might find the following:
```apl
        ∇ value←limit loop value  ⍝ init
    [1]  top:→(⎕CT>value-limit)/0 ⍝ test
    [2]   value←Next value        ⍝ proc, mod
    [3]   →top                    ⍝ jump
        ∇
```

Control structures help us to package these steps:
```apl
        ∇ value←limit loop value ⍝ init
    [1]   :While ⎕CT<value-limit ⍝ test
    [2]       value←Next value   ⍝ proc, mod
    [3]   :EndWhile              ⍝ jump
        ∇
```

Using tail calls:
```apl
    loop←{⍝ init
        ⎕CT>⍺-⍵:⍵    ⍝ test
        ⍺ ∇ Next ⍵   ⍝ proc, mod, jump
    }
```
