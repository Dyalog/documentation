# Initialising Fields

A Field may be assigned an initial value. This can be specified by an arbitrary expression that is executed when the Class is fixed by the Editor or by `⎕FIX`.

```apl
:Class DomesticParrot: Parrot
    :Field Public Name
        :Field Public Talks←1
 
    ∇ egg nm
      :Access Public
      :Implements Constructor
      Name←nm
    ∇
    ...
:EndClass ⍝ DomesticParrot
```

Field `Talks` will be initialised to `1` in every instance of the Class.
```apl
      pet←⎕NEW DomesticParrot 'Dicky'
 
      pet.Talks
1
      pet.Name
Dicky
```

Note that if a Field is ReadOnly, this is the only way that it may be assigned a value.

See also: [Shared Fields.](shared-fields.md)
