# Trigger Example

The following function displays information when the value of variables `A` or `B` changes.
```apl
     ∇ TRIG arg
[1]    :Implements Trigger A,B
[2]    arg.Name'is now 'arg.NewValue
[3]    :Trap 6 ⍝ VALUE ERROR
[4]        arg.Name'was    'arg.OldValue
[5]    :Else
[6]        arg.Name' was     [undefined]'
[7]    :EndTrap
     ∇
```

Note that on the very first assignment to `A`, when the variable was previously undefined, `arg.OldValue` is a `VALUE ERROR`.
```apl
      A←10
 A  is now   10
 A   was     [undefined] 
 
      A+←10
 A  is now   20
 A  was      10
 
      A←'Hello World'
 A  is now   Hello World 
 A  was      20
 
      A[1]←⊂2 3⍴⍳6
 A  is now    1 2 3 ello World 
              4 5 6            
 A  was      Hello World 
 
      B←⌽¨A
 B  is now    3 2 1 ello World 
              6 5 4            
 B   was     [undefined] 
 
      A←⎕NEW MyClass
 A  is now   #.[Instance of MyClass] 
 A  was       1 2 3 ello World 
              4 5 6            
 
      'F'⎕WC'Form'
      A←F
 A  is now   #.F 
 A  was      #.[Instance of MyClass] 
```

Note that Trigger functions are actioned only by assignment, so changing `A` to a Form using `⎕WC` does not invoke `TRIG`.
```apl
      'A'⎕WC'FORM' ⍝ Note that Trigger Function is not invoked
```

However, the connection (between `A` and `TRIG`) remains and the Trigger Function will be invoked if and when the Trigger is re-assigned.
```apl
      A←99
 A  is now   99
 A  was      #.A
```

See [Trigger Fields](../object-oriented-programming/class-members/fields/trigger-fields.md) for information on how a Field (in a Class) may be used as a Trigger.
