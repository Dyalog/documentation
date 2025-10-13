<h1 class="heading"><span class="name">Global Triggers</span></h1>

A global Trigger is a function that triggers on any assignment to a global variable in the same namespace. Global Triggers may be disabled and re-enabled using `2007⌶`. See [Disable Global Triggers](../../../language-reference-guide/primitive-operators/i-beam/disable-global-triggers).

This is implemented by the function declaration statement:

```apl
    :Implements Trigger *
```

The argument to the trigger function is an instance of the internal class `TriggerArguments` which contains the following members:

|Member|Description|
|---|---|
|`Name`|The name of the global variable that is about to be changed.|
|`Indexers`|If the assignment is some form of indexed assignment, `Indexers` is an array with the same shape as the sub-array that was assigned and contains the ravel-order, `⎕IO` -sensitive, indices of the changed elements. Otherwise, `Indexers` is undefined.|

<h2 class="example">Example</h2>
```apl
     ∇ foo args
[1]    :Implements Trigger *
[2]    args.Name'has changed'
[3]    :If 2=args.⎕NC'Indexers'
[4]        '⍴Indexers'(⍴args.Indexers)
[5]        'Indexers'(,args.Indexers)
[6]    :EndIf
     ∇

```
```apl
      vec←⍳5
 vec  has changed

      a b←10 'Pete'
 a  has changed 
 b  has changed 
 
      vec[2 4]←99
 vec  has changed 
 ⍴Indexers  2 
 Indexers  2 4 
```
```apl

      array←2 3 4⍴⍳12
 array  has changed 

```
```apl

      (2 1 3↑array)←42
 array  has changed 
 ⍴Indexers  2 1 3 
 Indexers  1 2 3 13 14 15 

```

!!! note
     - like other Triggers, only the most recently fixed global trigger function will apply and be called on assignment to a global variable. 
     - global triggers do not apply to local names nor to semi-globals (names which are localised further up the stack).
     - an assignment to a global variable will fire both its specific trigger (if defined) and the global trigger. However, the order of execution is undefined.
     - do not use an argument name for your trigger function that may conflict with a global variable name in the namespace.

## Further Example

A potential use for a global trigger is to detect the unintended creation of global variables due to localisation omissions. Note however that the timing of the activation of the Trigger is unpredictable. In this example, the trigger for the assignment to `b` activates after function `hoo` has exited. When Threads are involved, timing becomes even less predictable.
```apl
     ∇ CatchGlobals arg
[1]    ⍝ Displays a warning when a global is assigned
[2]    :Implements Trigger *
[3]    '*** assignment to global variable: ',
        arg.Name,' from ',1↓⎕SI
     ∇
     ∇ foo
[1]    goo
     ∇
     ∇ goo
[1]    hoo
     ∇
     ∇ hoo
[1]    a←10
[2]    b←a
     ∇
      foo              
*** assignment to global variable: a from  hoo  goo  foo 
*** assignment to global variable: b from  goo  foo 
```
