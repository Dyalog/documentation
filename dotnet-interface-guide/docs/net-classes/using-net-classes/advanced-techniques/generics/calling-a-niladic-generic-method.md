# Calling a Niladic Generic Method

.NET methods that only export overloads with zero parameters are exported as niladic functions, which means they cannot be passed as an operand to `43⌶632` without being evaluated.  To accomodate this, `43⌶632` also accepts a character vector as its left argument. In this case, it runs the .NET method with that name, with the generic type arguments applied. For example:
```apl
    r←'System.Array.Empty'(43⌶632)System.Int32
    r≡⍬
1
```

Attempting to evaluate the niladic function without calling `43⌶632`  generates an exception. For example:
```apl
    System.Array.Empty
EXCEPTION: Invalid number of generic type arguments applied (expected 1, got 0)
    System.Array.Empty
    ∧
```
