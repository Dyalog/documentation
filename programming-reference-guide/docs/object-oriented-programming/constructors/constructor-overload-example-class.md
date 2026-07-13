---
search:
  exclude: true
---

# Clover Class Example

```apl
:Class Clover ⍝ Constructor Overload Example
    :Field Public Con
    ∇ Make0
      :Access Public
      :Implements Constructor
      make 0
    ∇
    ∇ Make1(arg)
      :Access Public
      :Implements Constructor
      make arg
    ∇
    ∇ Make2(arg1 arg2)
      :Access Public
      :Implements Constructor
      make arg1 arg2
    ∇
    ∇ Make3(arg1 arg2 arg3)
      :Access Public
      :Implements Constructor
      make arg1 arg2 arg3
    ∇
    ∇ MakeAny args
      :Access Public
      :Implements Constructor
      make args
    ∇
    ∇ make args
      Con←(⍴args)(2⊃⎕SI)args
    ∇
:EndClass ⍝ Clover
```
