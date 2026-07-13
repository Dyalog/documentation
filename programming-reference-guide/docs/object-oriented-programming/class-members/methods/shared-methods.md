# Shared Methods

A Shared method runs in the Class namespace and may be called via an Instance or via the Class. However, a Shared method that is called via an Instance does not have direct access to the Fields and Properties of that Instance.

Class `Parrot` has a `Speak` method that does not require any information about the current Instance, so may be declared as Shared.
```apl
:Class Parrot:Bird
    
    ∇ R←Speak times
      :Access Public Shared
      R←⍕times⍴⊂'Squark!'
    ∇
    
:EndClass ⍝ Parrot
 
      wild←⎕NEW Parrot
      wild.Speak 2
 Squark!  Squark! 
```

Note that `Parrot.Speak` may be executed directly from the Class and does not in fact require an Instance.
```apl
      Parrot.Speak 3
 Squark!  Squark!  Squark!
```
