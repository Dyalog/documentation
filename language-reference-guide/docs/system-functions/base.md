---
search:
  boost: 2
---

# <span>Base Class</span> `R←⎕BASE.Y`{{key}}

`⎕BASE.Y` refers to the member `Y` as the base class of the current class implements it.

<h2 class="example">Example</h2>

`DomesticParrot` derives from `Parrot` and supersedes its `Speak` method. The `Speak` of `DomesticParrot` calls the one of `Parrot` through `⎕BASE`:

```apl
      :Class Parrot
          ∇ R←Speak
            :Access Public
            R←'Squark!'
          ∇
      :EndClass
      :Class DomesticParrot: Parrot
          ∇ R←Speak
            :Access Public
            R←⎕BASE.Speak,' Who''s a pretty boy, then!'
          ∇
      :EndClass
      Maccaw←⎕NEW Parrot
      Maccaw.Speak
Squark!
      Polly←⎕NEW DomesticParrot
      Polly.Speak
Squark! Who's a pretty boy, then!
```

## Member

`Y` is the name of a public member of the base class: a method, a field, or a property. A name that is not a public member of the base class signals `VALUE ERROR`.

`⎕BASE.Y` is mostly used to call a method that the current class supersedes, as in the example above. [Dyadic `⎕CLASS`](class-dyadic.md) reaches a superseded member from outside the class.

<h3 class="example">Example</h3>

`Bird` has a field `Legs` of its own, as does its base class `Animal`:

```apl
      :Class Animal
          :Field Public Legs←4
      :EndClass
      :Class Bird: Animal
          :Field Public Legs←2
          ∇ R←BothLegs
            :Access Public
            R←⎕BASE.Legs,Legs
          ∇
      :EndClass
      (⎕NEW Bird).BothLegs
4 2
```

## Result

`R` is the value of the member: the result of a method, or the value of a field or property.

## Context

`⎕BASE.Y` is special syntax, which works where the current namespace is a class or an instance of one, for example, inside its methods. Where the current namespace is not a class or an instance, it signals `DOMAIN ERROR`, and in a class that has no base class, it signals `VALUE ERROR`. `⎕BASE` on its own signals `SYNTAX ERROR`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕BASE BASE
</div>
