# Standard Error Action

The standard system action in the event of an error or interrupt whilst executing an expression is to suspend execution and display an error report.  If necessary, the state indicator is cut back to a statement such that there is no halted locked function visible in the state indicator.

The error report consists of up to three lines

1. The error message, preceded by the symbol `⍎` if the error occurred while evaluating the Execute function.
2. The statement in which the error occurred (or expression being evaluated by the Execute function), preceded by the name of the function and line number where execution is suspended unless the state indicator has been cut back to immediate execution mode.  If the state indicator has been cut back because of a locked function in execution, the displayed statement is that from which the locked function was invoked.
3. The symbol `^` under the last referenced symbol or name when the error occurred.  All code to the right of the `^` symbol in the expression will have been evaluated.

<h2 class="example">Examples</h2>
```apl
      X PLUS U
VALUE ERROR
      X PLUS U
             ^
      FOO
INDEX ERROR
FOO[2] X←X+A[I]
           ^
      CALC
⍎DOMAIN ERROR
CALC[5] ÷0
        ^

```
