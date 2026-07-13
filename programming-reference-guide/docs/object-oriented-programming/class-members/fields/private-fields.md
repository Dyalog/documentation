# Private Fields

A Private Field may only be referenced by code running inside the Class or an Instance of the Class. Furthermore, Private Fields are not inherited.

The [ComponentFile Class ](../properties/component-file-class-example.md) has a Private Instance Field named `tie` that is used to store the file tie number in each Instance of the Class.
```apl
:Class ComponentFile
    :Field Private Instance tie    
    
    ∇ Open filename
      :Implements Constructor
      :Access Public Instance
      :Trap 0
          tie←filename ⎕FTIE 0
      :Else
          tie←filename ⎕FCREATE 0
      :EndTrap
      ⎕DF filename,'(Component File)'
    ∇
```

As the field is declared to be Private, it is not accessible from outside an Instance of the Class, but is only visible to code running inside.
```apl
      F1←⎕NEW ComponentFile 'test1'
      F1.tie
VALUE ERROR
      F1.tie
     ^
```
