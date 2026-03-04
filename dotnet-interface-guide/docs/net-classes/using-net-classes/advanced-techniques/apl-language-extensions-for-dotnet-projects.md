# APL Language Extensions for .NET Projects

.NET provides a set of standard operators (methods) that are supported by certain classes, for example, methods to add and subtract .NET objects and methods to compare two .NET objects.

Example 1: DateTime – Adding and subtracting

The `op_Addition` and `op_Subtraction` operators add and subtract `TimeSpan` objects to `DateTime` objects:
```apl
      DT3←System.DateTime.Now
      DT3
15/02/2024 10:35:35
```
```apl
      TS←⎕NEW TimeSpan (1 1 1)
      TS
01:01:01
```
```apl
      DateTime.op_Addition DT3 TS
15/02/2024 11:36:36
```
```apl
      DateTime.op_Subtraction DT3 TS
15/02/2024 09:34:34
```

Example 2: DateTime – Comparing

The `op_Equality` and `op_Inequality` operators  compare two DateTime objects:
```apl
      DT1←⎕NEW DateTime (2024 4 30)
      DT2←⎕NEW DateTime (2024 1 1)

      ⍝ Is DT1 equal to DT2?
      DateTime.op_Equality DT1 DT2
0
```

Some corresponding APL primitive functions have been extended to accept .NET objects as arguments and call these standard .NET methods internally. The methods and the corresponding APL primitives that are currently available are shown in **Table 1-1**.

|.NET Method  |APL Primitive Function|
|-------------|----------------------|
|op_Equality  |`=` and `≡`           |
|op_Inequality|`≠` and `≢`           |

This means that Example 2 becomes:
```apl
      DT1←⎕NEW DateTime (2024 4 30)
      DT2←⎕NEW DateTime (2024 1 1)

      ⍝ Is DT1 equal to DT2?
      DT1 = DT2
0
```

Calculations and comparisons performed by .NET methods are performed independently from the values of APL system variables (such as `⎕FR` and `⎕CT`).
