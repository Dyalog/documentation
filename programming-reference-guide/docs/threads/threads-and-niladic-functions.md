#  Threads & Niladic Functions

In common with other operators, the spawn operator `&` may accept monadic or dyadic functions as operands, but not niladic functions. This means that, using spawn, you cannot start a thread that consists only of a niladic function

If you wish to invoke a niladic function asynchronously, you have the following choices:

- Turn your niladic function into a monadic function by giving it a dummy argument which it ignores.
- Call your niladic function with a dfn to which you give an argument that is implicitly ignored. For example, if the function `NIL` is niladic, you can call it asynchronously using the expression:  `{NIL}& 0`
- Call your function via a dummy monadic function, for example
    ```apl

        ∇ NIL_M DUMMY
    [1]   NIL
        ∇
        NIL_M& '' 
    ```

- Use `execute`, for example
    ```apl
    ⍎& 'NIL'
    ```

Note that niladic functions *can* be invoked asynchronously as callback functions. For example, the statement:
```apl
      ⎕WS'Event' 'Select' 'NIL&'
```

will execute correctly as a thread, even though `NIL` is niladic. This is because callback functions are invoked directly by `⎕DQ` rather than as an operand to the spawn operator.
