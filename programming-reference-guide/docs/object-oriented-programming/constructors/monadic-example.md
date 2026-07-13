# Monadic Example

In the following example, `DomesticParrot` is derived from `Parrot` which is derived from `Bird`. They all share the Field `Species` (inherited from `Bird`) but only a `DomesticParrot` has a Field `Name`. Each of the 3 Classes has its own Constructor called `egg`.
```apl
:Class Bird
    :Field Public Species
    ∇ egg spec
      :Access Public Instance
      :Implements Constructor
      Species←spec
    ∇
    ...
:EndClass ⍝ Bird
 
:Class Parrot: Bird
    ∇ egg species
      :Access Public Instance
      :Implements Constructor :Base 'Parrot: ',species
    ∇
    ...
:EndClass ⍝ Parrot
 
:Class DomesticParrot: Parrot
    :Field Public Name
    ∇ egg(name species)
      :Access Public Instance
      :Implements Constructor :Base species
      ⎕DF Name←name
    ∇
    ...
:EndClass ⍝ DomesticParrot
 
```

```apl

      pol←⎕NEW DomesticParrot('Polly' 'Scarlet Macaw')
      pol.Name
Polly
      pol.Species
Parrot: Scarlet Macaw
```

## Explanation

`⎕NEW` creates the new instance and runs the Constructor `DomesticParrot.egg`. The `egg` header splits the argument into two items `name` and `species`. As soon as the line:
```apl
:Implements Constructor :Base species
```

is encountered, `⎕NEW` calls the Base Class constructor `Parrot.egg`, passing it the result of the expression to the right, which in this case is simply the value in `species`.

`Parrot.egg` starts to execute and as soon as the line:
```apl
:Implements Constructor :Base 'Parrot: ',species
```

is encountered, `⎕NEW` calls *its* Base Class constructor `Bird.egg`, passing it the result of the expression to the right, which in this case is the character vector `'Parrot: '` catenated with the value in `species`.

`Bird.egg` assigns its argument to the Public Field `Species`.

At this point, the state indicator would be:
```apl
       )SI
[#.[Instance of DomesticParrot]] #.Bird.egg[3]*
[constructor]
:base
[#.[Instance of DomesticParrot]] #.Parrot.egg[2]
[constructor]
:base
[#.[Instance of DomesticParrot]] #.DomesticParrot.egg[2]
[constructor]
```

`Bird.egg` then returns to `Parrot.egg` which returns to `DomesticParrot.egg`.

Finally, `DomesticParrot.egg[3]` is executed, which establishes Field `Name` and the Display Format (`⎕DF`) for the instance.
