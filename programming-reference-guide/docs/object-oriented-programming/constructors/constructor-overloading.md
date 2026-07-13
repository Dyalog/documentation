# Constructor Overloading

NameList header syntax is used to define different versions of a Constructor each with a different number of parameters, referred to as its *signature*. See [Namelists](../../defined-functions-and-operators/traditional-functions-and-operators/namelists.md) for details. The [Clover Class](constructor-overload-example-class.md){: .noprint } illustrates this principle.

In deciding which Constructor to call, APL matches the shape of the Constructor argument with the signature of each of the Constructors that are defined. If a constructor with the same number of arguments exists (remembering that 0 arguments will match a niladic Constructor), it is called. If there is no exact match, and there is a Constructor with a general signature (an un-parenthesised right argument), it is called. If no suitable constructor is found, a `LENGTH ERROR` is reported.

There may be one and only one constructor with a particular signature.

The only way a Constructor function should be invoked is by `⎕NEW`. See [Base Constructors](./base-constructors.md) for further details. If you attempt to call a Constructor function  from outside its Class, it will cause a `SYNTAX ERROR`. A Constructor function should not call another Constructor function within the same Class, although it will not generate an error. This would cause the Base Constructor to be called twice, with unpredictable consequences.

In the [Clover Class](constructor-overload-example-class.md){: .noprint } example Class, the following Constructors are defined:

|Constructor|Implied argument  |
|-----------|------------------|
|`Make1`    |1-item vector     |
|`Make2`    |2-item vector     |
|`Make3`    |3-item vector     |
|`Make0`    |No argument       |
|`MakeAny`  |Any array accepted|

In the following examples, the `Make` function (see [Clover Class](constructor-overload-example-class.md){: .noprint }  for details) displays:
```apl
<shape of argument> <name of Constructor called><argument>
(see function make)
```

Creating a new Instance of Clover with a 1-element vector as the Constructor argument, causes the system to choose the `Make1` Constructor. Note that, although the argument to `Make1` is a 1-element vector, this is disclosed as the list of arguments is unpacked into the (single) variable `arg1`.
```apl
      (⎕NEW Clover(,1)).Con
   Make1  1
```

Creating a new Instance of Clover with a 2- or 3-element vector as the Constructor argument causes the system to choose `Make2`, or `Make3` respectively.
```apl
      (⎕NEW Clover(1 2)).Con
 2  Make2  1 2 
      (⎕NEW Clover(1 2 3)).Con
 3  Make3  1 2 3 
```

Creating an Instance with any other Constructor argument causes the system to choose `MakeAny`.
```apl
      (⎕NEW Clover(⍳10)).Con
 10  MakeAny  1 2 3 4 5 6 7 8 9 10
      (⎕NEW Clover(2 2⍴⍳4)).Con
 2 2  MakeAny  1 2 
               3 4
```

Note that a scalar argument will call `MakeAny` and not `Make1`.
```apl
      (⎕NEW Clover 1).Con
   MakeAny  1
```

and finally, creating an Instance without a Constructor argument causes the system to choose `Make0`.
```apl
      (⎕NEW Clover).Con
   Make0  0
```
