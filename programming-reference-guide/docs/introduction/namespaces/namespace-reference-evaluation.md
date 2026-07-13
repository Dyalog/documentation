# Namespace Reference Evaluation

When the interpreter encounters a namespace reference, it:

1. Switches to the namespace.
2. Evaluates the name.
3. Switches back to the original namespace.

If for example, in the following, the current namespace is `#.W`, the interpreter evaluates the line:
```apl
      A ← X.Y.DUP MAT
```

in the following way:

1. Evaluate array `MAT` in current namespace `W` to produce argument for function.
2. Switch to namespace `X.Y` within `W`.
3. Evaluate function `DUP` in namespace `W.X.Y` with argument.
4. Switch back to namespace `W`.
5. Assign variable `A` in namespace `W`.
