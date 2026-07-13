# Triggers

*Triggers* provide the ability to have a function called automatically whenever a variable or a Field is assigned. Triggers are actioned by all forms of assignment (`←`), but only by assignment.

Triggers are designed to allow a class to perform some action when a field is modified – without having to turn the field into a property and use the property setter function to achieve this. Avoiding the use of a property allows the full use of the APL language to manipulate data in a field, without having to copy field data in and out of the class through get and set functions.

Triggers *can* also be applied to variables outside a class, and there will be situations where this is very useful. However, dynamically attaching and detaching a trigger from a variable is a little tricky at present.

The function that is called when a variable or Field changes is referred to as the *Trigger Function*. The name of a variable or Field which has an associated Trigger Function is termed a *Trigger*.

A function is declared as a Trigger function by including the statement:
```apl
      :Implements Trigger Name1,Name2,Name3, ...
```

where `Name1`, `Name2` etc. are the Triggers.

When a Trigger function is invoked, it is passed an Instance of the internal Class `TriggerArguments`. This Class has 3 Fields:

|Member    |Description                                                                                                                     |
|----------|--------------------------------------------------------------------------------------------------------------------------------|
|`Name`    |Name of the Trigger whose change in value has caused the Trigger Function to be invoked.                                        |
|`NewValue`|The newly assigned value of the Trigger                                                                                         |
|`OldValue`|The previous value of the Trigger. If the Trigger was not previously defined, a reference to this Field causes a `VALUE ERROR` .|

A Trigger Function is called *as soon as possible* after the value of a Trigger was assigned; typically by the end of the currently executing line of APL code. The precise timing is not guaranteed and may not be consistent because internal workspace management operations can occur at any time.

If the value of a Trigger is changed more than once by a line of code, the Trigger Function will be called at least once, but the number of times is not guaranteed.

A Trigger Function is not called when the Trigger is expunged.

Expunging a Trigger disconnects the name from the Trigger Function and the Trigger Function will not be invoked when the Trigger is reassigned. The connection may be re-established by re-fixing the Trigger Function.

A Trigger may have only a single Trigger Function. If the Trigger is named in more than one Trigger Function, the Trigger Function that was last fixed will apply.

In general, it is inadvisable for a Trigger function to modify its own Trigger, as this will potentially cause the Trigger to be invoked repeatedly and forever.

To associate a Trigger function with a *local* name, it is necessary to dynamically fix the Trigger function in the function in which the Trigger is localised; for example:
```apl
     ∇ TRIG arg
[1]    :Implements Trigger A
[2]    ...
 
     ∇ TEST;A
[1]    ⎕FX ⎕OR'TRIG'
[2]    A←10
```
