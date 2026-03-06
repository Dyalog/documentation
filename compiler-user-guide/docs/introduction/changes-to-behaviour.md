# Changes to Behaviour of Functions when Compiled

The same run-time engine is used by both compiled functions and interpreted functions when executing primitive functions. However, a small number of behavioural changes occur when functions are compiled.

## Thread Switching

Thread switching will not occur between lines of code after a function has been compiled. However, it can still occur at the start of the function before the first line is executed.

## Error Trapping

Compiled functions cannot be suspended. Errors occurring within compiled functions are signalled back to the calling environment (in the same way as if [`⎕SIGNAL`](../../../language-reference-guide/system-functions/signal) had been used inside the function).

Similarly, when an error in a compiled function is handled by an Execute trap, the APL expression specified in the trap will be executed in the calling environment and will not be able to see any of the compiled function's local names.

## Visible Names

When a user-defined operator is compiled, its local names are eliminated. As a result, the names are no longer visible to any sub‑functions that it calls.
