---
search:
  boost: 2
---

# <span>Signal Event with Custom Name</span> `{R}←X ⎕SIGNAL Y`{{key}}

`Y` must be a scalar or vector.

To signal an event without a custom message, use [monadic `⎕SIGNAL`](signal-monadic.md).

If `Y` is a an empty vector nothing is signalled.

If `Y` is a vector of more than one element, all but the first element are ignored.

`R` has the same value as `Y`.

`Y=0` is a special form of `⎕SIGNAL`, the side effect of which is to reset the values of certain system constants. It is described further down this section.

If the first element of `Y` is a simple integer it is taken to be an event number. Permitted values are 0, 1-999 and 1006. `X` is a text message.   If present, `X` must be a simple character scalar or vector, or an object reference. If `X` is empty, the standard event message for the corresponding event number  is assumed. See ["APL Error Messages"](../../../programming-reference-guide/error-messages/apl-errors). If there is no standard message, a message of the form `ERROR NUMBER n` is composed, where `n` is the event number in `Y`. Values outside the permitted range will result in a `DOMAIN ERROR`.

If the first element of `Y` is a 2 column matrix or a vector of 2 element vectors of name/values pairs, then it is considered to be a set of values to be used to override the default values in a new instance of `⎕DMX`. Any other value for the first element of `Y` will result in a `DOMAIN ERROR`.

The names in the error specification must all  appear in a system-generated `⎕DMX`, otherwise a `DOMAIN ERROR` will be issued. For each name specified, the default value in the new instance of `⎕DMX` is replaced with the value specified. `EN` must be one of the names in the error specification. Attempting to specify certain names, including `InternalLocation` and `DM`, will result in a `DOMAIN ERROR`. The value which is to be assigned to a name must be appropriate to the name in question.

Dyalog might enhance `⎕DMX` in future, thus potentially altering the list of valid and/or assignable names.

If the first element of `Y` is an array of name/value pairs then  specifying any value for `X` will result in a `DOMAIN ERROR`.

The effect of the system function is to interrupt execution.  The state indicator is cut back to exit from the function or operator containing the line that invoked `⎕SIGNAL`, or is cut back to exit the Execute (`⍎`) expression that invoked `⎕SIGNAL`. If executed within a nested dfn, the state indicator is cut back to exit from the capsule containing the line that invoked `⎕SIGNAL`. An error is then generated.

An error interrupt can be trapped if the system variable `⎕TRAP` is set to intercept the event.  Otherwise, the standard system action is taken (which might involve cutting back the state indicator further if there are locked functions or operators in the state indicator).  The standard event message is replaced by the text given in `X`, if present.

<h2 class="example">Example</h2>
```apl
      ⎕VR'DIVIDE'
     ∇ R←A DIVIDE B;⎕TRAP
[1]    ⎕TRAP←11 'E' '→ERR'
[2]    R←A÷B ⋄ →0
[3]   ERR:'DIVISION ERROR' ⎕SIGNAL 11
     ∇
 
      2 4 6 DIVIDE 0
DIVISION ERROR
      2 4 6 DIVIDE 0
     ^
```

If you are using the Microsoft .NET Framework, you can use `⎕SIGNAL` to throw an exception by specifying a value of 90 in `Y`. In this case, if you specify the left argument `X`, it must be a reference to a .NET object that is or derives from the Microsoft .NET class System.Exception. The following example illustrates a *constructor* function `CTOR` that expects to be called with a value for `⎕IO` (0 or 1)
```apl
     ∇ CTOR IO;EX
[1]    :If IO∊0 1
[2]        ⎕IO←IO
[3]    :Else
[4]        EX←ArgumentException.New'IO must be 0 or 1'
[5]        EX ⎕SIGNAL 90
[6]    :EndIf
     ∇
```

## `⎕SIGNAL 0`: Reset error-related system constants

If `Y` is a simple integer with the value 0, `⎕SIGNAL` does not interrupt execution, but merely returns the value 0. The side effect of calling `⎕SIGNAL 0` is to reset the values of `⎕DM`, `⎕DMX`, `⎕EN` and `⎕EXCEPTION` to their default values. `⎕SIGNAL 0` is the only form of `⎕SIGNAL` which can be used to reset the aforementioned system constants; including a left argument or using a name/value pair right argument of `⎕SIGNAL` will result in a `DOMAIN ERROR`.

## Further examples

## Example 1
```apl

      'Hello'⎕SIGNAL 200
Hello
      'Hello'⎕SIGNAL 200
     ∧
      ⎕DMX
 EM       Hello 
 Message            

      ⎕DM
 Hello        'Hello'⎕SIGNAL 200       ∧ 

```
```apl


      ⎕DMX
 EM       ERROR 200 
 Message    

      ⎕DM
 ERROR 200        ⎕SIGNAL⊂⊂('EN' 200)       ∧ 

```

## Example 2
```apl
      ⎕DMX
 EM       ERROR 200 
 Message  My error
```
```apl
      ⍪⎕DMX.(EN EM Vendor)
       200 
 ERROR 200 
      Andy 
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIGNAL SIGNAL
</div>
