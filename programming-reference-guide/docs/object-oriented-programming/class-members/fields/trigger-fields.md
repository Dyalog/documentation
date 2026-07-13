# Trigger Fields

A field may act as a [Trigger](../../../triggers/triggers.md) so that a function may be invoked whenever the value of the Field is changed.

As an example, it is often useful for the Display Form of an Instance to reflect the value of a certain Field. Naturally, when the Field changes, it is desirable to change the Display Form. This can be achieved by making the Field a Trigger as illustrated by the following example.

Notice that the Trigger function is invoked both by assignments made within the Class (as in the assignment in `ctor`) and those made from outside the Instance.

```apl
:Class MyClass
    :Field Public Name
    :Field Public Country←'England'
    ∇ ctor nm
      :Access Public
      :Implements Constructor
      Name←nm
    ∇
    ∇ format
      :Implements Trigger Name,Country
      ⎕DF'My name is ',Name,' and I live in ',Country
    ∇
:EndClass ⍝ MyClass
 
      me←⎕NEW MyClass 'Pete'
      me  
My name is Pete and I live in England
 
      me.Country←'Greece'
      me
My name is Pete and I live in Greece
 
      me.Name←'Kostas'
      me
My name is Kostas and I live in Greece
```
