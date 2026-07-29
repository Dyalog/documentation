# Methods

## Calling Methods

A method is similar to a function in that it may or may not take an argument, perform some action, and return a result.

Examples are the Print, NewPage, Setup and Abort methods, all of which cause a Printer object to take a particular action.

If the system variable `⎕WX` is 1, you may invoke an object's method using exactly the same syntax as you would use to call a function in that object.

For example, to execute the IDNToDate method of a Calendar object named `F.CAL`, you can use the expression:
```apl
      F.CAL.IDNToDate 36525
2000 1 1 5
```

When you call a method in this way, the method name is case-sensitive and if you spell it incorrectly, you will get a  `VALUE ERROR`.
```apl
      F.CAL.idntodate 36525
VALUE ERROR
      F.C.idntodate 36525
     ^
```

## Invoking Methods with `⎕NQ`

Methods may also be called using `⎕NQ` with a left argument of 2, indeed if `⎕WX` is 0, this is the only way to call a method.

The result of the method is returned by `⎕NQ`. Note however that the result is *shy*.

For example, for a TreeView object you can obtain status information about a particular item in the object using the GetItemState method:
```apl
      ⎕←2 ⎕NQ 'f.tv' 'GetItemState' 6
96
 
```

Or you can call the IDNToDate method of a Calendar object `F.C` as follows:
```apl
     ⎕←2 ⎕NQ 'F.CAL' 'IDNToDate' 36525
2000 1 1 5
```

When you call a method using `2 ⎕NQ`, the method name is **not** case-sensitive.
```apl
     ⎕←2 ⎕NQ 'F.CAL' 'idntodate' 36525
2000 1 1 5
```

## Events as Methods

Methods and events are closely related and most events can be invoked as methods.

For example, you can reposition and resize a Form in one step by calling its Configure event as a method. The argument you supply is the same as the event message associated with the event, but with the first two items (Object and Event code) omitted.
```apl
      F.Configure 10 10 30 20
```

Or, using `2 ⎕NQ`
```apl
     2 ⎕NQ 'F' 'Configure' 10 10 30 20
```

Notice that when you call an event as a method, you are executing the *default processing* associated with the event. The setting for the Event property is ignored and, in particular, any callback associated with the event is not executed.
