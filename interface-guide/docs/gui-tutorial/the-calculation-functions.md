# The Calculation Functions

So far we have built the user-interface, and we have written one callback function `QUIT` to terminate the application. We now need to write the two functions `f2c` and `c2f` which will actually perform the conversions. First let's tackle `f2c`.

A callback such as this one performs just one simple action. This does not depend upon the type of event that called it (there is only one), so the function has no need of arguments. Neither does it need to do anything fancy, such as preventing the event from proceeding. It need not therefore return a result. The header line, which includes the local variables we will need, is then...
```apl
   [0]  f2c;F;C
```

The first thing the function must do is to obtain the contents of the Fahrenheit edit field which is called `TEMP.F`. As we have defined the FieldType as `'Numeric'`, this is easily done by querying its Value property...
```apl
   [1]  F ← TEMP.F.Value
```

Next, we need to calculate Centigrade from Fahrenheit...
```apl
   [2]  C ← (F-32) × 5÷9
```

... and finally, display the value in the Centigrade edit field. As we have also defined this as a numeric field, we can just set its Value property using assignment.
```apl
   [3]  TEMP.C.Value←C
```

So our completed `f2c` callback function is...
```apl
      ∇ f2c;F;C
   [1]  F ← TEMP.F.Value
   [2]  C ← (F-32) × 5÷9
   [3]  TEMP.C.Value←C
      ∇
```

which can be simplified to:
```apl
      ∇ f2c
   [1]    TEMP.C.Value←(TEMP.F.Value-32)×5÷9
      ∇
```

The Centigrade to Fahrenheit callback function `c2f` looks very similar:
```apl
      ∇ c2F
   [1]    TEMP.F.Value←32+TEMP.C.Value×9÷5
      ∇
```
