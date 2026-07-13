# Niladic Example

In the following example, `DomesticParrot` is derived from `Parrot` which is derived from `Bird`. They all share the Field `Desc` (inherited from `Bird`). Each of the 3 Classes has its own *niladic* Constructor called `egg0`.
```apl

:Class Bird
    :Field Public Desc
    ∇ egg0
      :Access Public
      :Implements Constructor
      Desc←'Bird'
    ∇
:EndClass ⍝ Bird
			
:Class Parrot: Bird
    ∇ egg0
      :Access Public
      :Implements Constructor
      Desc,←'→Parrot'
    ∇
:EndClass ⍝ Parrot

:Class DomesticParrot: Parrot
    ∇ egg0
      :Access Public
      :Implements Constructor
      Desc,←'→DomesticParrot'
    ∇
:EndClass ⍝ DomesticParrot

      (⎕NEW DomesticParrot).Desc
Bird→Parrot→DomesticParrot
```

## Explanation

`⎕NEW` creates the new instance and runs the niladic Constructor `DomesticParrot.egg0`. As soon as the line:
```apl
:Implements Constructor
```

is encountered, `⎕NEW` calls the niladic constructor in the Base Class `Parrot.egg0`

`Parrot.egg0` starts to execute and as soon as the line:
```apl
:Implements Constructor
```

is encountered, `⎕NEW` calls the niladic constructor in the Base Class `Bird.egg0.`

When the line:
```apl
:Implements Constructor
```

is encountered, `⎕NEW` cannot call the niladic constructor in the Base Class (there is none) so the chain of Constructors ends. Then, as the state indicator unwinds ...

|-------------------|--------|--------------------------|
|Bird.egg0          |executes|`Desc←'Bird''`            |
|Parrot.egg0        |executes|`Desc,←'→Parrot''`        |
|DomesticParrot.egg0|execute |`Desc,←'→DomesticParrot''`|
