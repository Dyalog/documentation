# Calling a Generic Method

Generic methods have a display form with a generic type parameter list shown in square brackets. For example:
```apl
    ⎕USING←''
    System.Decimal.CreateChecked
System.Decimal CreateChecked[TOther](TOther)
```

The `CreateChecked` function has one type parameter, shown in square brackets, and one regular parameter, shown in parentheses.

The generic type argument can be applied using  `43⌶632`. When the monadic operator `43⌶632` is run with a .NET method as its left argument, and a scalar type or a vector of .NET types as its right argument, the result is a derived function that calls the specified .NET method with both the generic type arguments and regular arguments applied. For example:
```apl
    fn←System.Decimal.CreateChecked (43⌶632) System.Int32
    fn 123
123
```

Attempting to call a method without specifying the type argument generates an exception. For example:
```apl
    System.Decimal.CreateChecked 123
EXCEPTION: Invalid number of generic type arguments applied (expected 1, got 0)
    System.Decimal.CreateChecked 123
                   ∧
```
