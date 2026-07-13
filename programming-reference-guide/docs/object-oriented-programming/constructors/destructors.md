# Destructors

A *Destructor* is a function that is called just before an Instance of a Class ceases to exist and is typically used to close files or release external resources associated with an Instance.

An Instance of a Class is destroyed when:

- The Instance is expunged using `⎕EX` or `)ERASE`.
- A function, in which the Instance is localised, exits.

But be aware that a destructor will also be called if:

- The Instance is re-assigned (see below)
- The result of `⎕NEW` is not assigned (the instance gets created then immediately destroyed).
- APL creates (and then destroys) a new Instance as a result of a reference to a member of an [empty Instance](empty-arrays-of-instances-how.md). The destructor is called after APL has obtained the appropriate value from the instance and no longer needs it.
- The constructor function fails. Note that the Instance is actually created before the constructor is run (inside it), and if the constructor fails, the fledgling Instance is discarded. Note too that this means a destructor *may* need to deal with a partially constructed instance, so the code may need to check that resources were actually acquired, before releasing them.
- On the execution of `)CLEAR`, `)LOAD`, `⎕LOAD`, `)OFF` or `⎕OFF`.

!!! warning 
    A destructor may be executed on **any** thread.

Note that an Instance of a Class only disappears when the *last reference* to it disappears. For example, the sequence:
```apl
      I1←⎕NEW MyClass
      I2←I1
      )ERASE I1
```

will not cause the Instance of `MyClass` to disappear because it is still referenced by `I2`.

A Destructor is identified by the statement `:Implements Destructor` which must appear immediately after the function header in the Class script.
```apl
:Class Parrot
    ...
    ∇ kill
      :Implements Destructor
      'This Parrot is dead'
    ∇
    ...
:EndClass ⍝ Parrot
```
```apl
       pol←⎕NEW Parrot 'Scarlet Macaw'
      )ERASE pol
This Parrot is dead
```

Note that reassignment to `pol` causes the Instance referenced by `pol` to be destroyed and the Destructor invoked:
```apl
      pol←⎕NEW Parrot 'Scarlet Macaw'
      pol←⎕NEW Parrot 'Scarlet Macaw'
This Parrot is dead
```

If a Class inherits from another Class, the Destructor in its Base Class is automatically called after the Destructor in the Class itself.

So, if we have a Class structure: `DomesticParrot => Parrot => Bird` containing the following Destructors:
```apl
:Class DomesticParrot: Parrot
    ...
    ∇ kill
      :Implements Destructor
      'This ',(⍕⎕THIS),' is dead'
    ∇
     ...
:EndClass ⍝ DomesticParrot

 
:Class Parrot: Bird
    ...
    ∇ kill
      :Implements Destructor
      'This Parrot is dead'
    ∇
    ...
:EndClass ⍝ Parrot

```
```apl

 
:Class Bird
    ...
    ∇ kill
      :Implements Destructor
      'This Bird is dead'
    ∇
    ...
:EndClass ⍝ Bird
```

Destroying an Instance of `DomesticParrot` will run the Destructors in `DomesticParrot`, `Parrot` and `Bird` and in that order.
```apl
      pol←⎕NEW DomesticParrot

      )CLEAR
This Polly is dead
This Parrot is dead
This Bird is dead
clear ws
```
