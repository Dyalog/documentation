---
search:
  exclude: true
---

# <span>Implements Statement</span> `:Implements`

The `:Implements` statement identifies the function to be one of the following types.
```apl
:Implements Constructor <[:Base expr]>
:Implements Destructor
:Implements Method <InterfaceName.MethodName>
:Implements Trigger <name1><,name2,name3,...>
:Implements Trigger *
			
```

|Element|Description|
|---|---|
|`Constructor`|Specifies that the function is a [Class Constructor](../../../object-oriented-programming/constructors/constructors.md) .|
|`:Base expr`|Specifies that the [Base Constructor](../../../object-oriented-programming/constructors/base-constructors.md) be called with the result of the expression expr as its argument.|
|`Destructor`|Specifies that the function is a [Class Destructor](../../../object-oriented-programming/constructors/destructors.md) .|
|`Method`|Specifies that the function implements the Method MethodName whose syntax is specified by [Interface InterfaceName](../../../object-oriented-programming/interfaces/interfaces.md) .|
|`Trigger`|Identifies the function as a [Trigger Function](../../../triggers/triggers.md) which is activated by changes to variable name1, name2, and so forth. Trigger * specifies a [Global Trigger](../../../triggers/global-triggers.md) that is activated by the assignment of any global variable in the same namespace.|
