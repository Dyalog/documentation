---
search:
  boost: 2
---

# <span>Get Class/Interface Implementation</span> `R←X ⎕CLASS Y`{{key}}

This function casts an instance to one of the classes or interfaces that [monadic `⎕CLASS`](class-monadic.md) reports for it, reaching the members that one implements.

<h2 class="example">Example</h2>

`Parrot` derives from `Bird`, which derives from `Animal`, and each defines its own `Speak`. Casting an instance of `Parrot` to `Bird` runs the `Speak` of `Bird`:

```apl
      :Class Animal
          ∇ R←Speak
            :Access Public
            R←'...'
          ∇
      :EndClass
      :Class Bird: Animal
          ∇ R←Speak
            :Access Public
            R←'Tweet, tweet!'
          ∇
      :EndClass
      :Class Parrot: Bird
          ∇ R←Speak
            :Access Public
            R←'Squark!'
          ∇
      :EndClass
      Polly←⎕NEW Parrot
      (Bird ⎕CLASS Polly).Speak
Tweet, tweet!
```

## Left Argument

`X` is a reference to an interface that the instance `Y` supports, or to a base class that `Y` derives from. Any other reference signals `DOMAIN ERROR`.

## Right Argument

`Y` is a reference to an instance of a class.

## Result

`R` is a reference to the implementation of the interface or base class `X` by the instance `Y`. It is used as a *cast*, to reach the members of `Y` that correspond to the members of `X`.

<h3 class="example">Examples</h3>

A cast reaches an interface implementation. As in the [Penguin Class example](../../programming-reference-guide/object-oriented-programming/interfaces/interface-example.md), `Penguin` supports the `BirdBehaviour` and `FishBehaviour` interfaces, and implements each of their members under a name of its own. Continuing with `Animal` from the example above:

```apl
      :Interface BirdBehaviour
          ∇ R←Fly
          ∇
      :EndInterface
      :Interface FishBehaviour
          ∇ R←Swim
          ∇
      :EndInterface
      ⎕FIX(
          ':Class Penguin: Animal,BirdBehaviour,FishBehaviour'
          '    ∇ R←NoCanFly'
          '      :Implements Method BirdBehaviour.Fly'
          '      R←''Although I am a bird, I cannot fly'''
          '    ∇'
          '    ∇ R←Dive'
          '      :Implements Method FishBehaviour.Swim'
          '      R←''I can dive and swim like a fish'''
          '    ∇'
          ':EndClass'
      )
      Pingo←⎕NEW Penguin
      (FishBehaviour ⎕CLASS Pingo).Swim
I can dive and swim like a fish
      (BirdBehaviour ⎕CLASS Pingo).Fly
Although I am a bird, I cannot fly
```

A cast also reaches a member that a base class defines and a derived class supersedes. `DomesticParrot` derives from `Parrot` and supersedes its `Speak`, which it calls through [`⎕BASE`](base.md). The instance runs its own `Speak`, while casting it to `Parrot` or `Bird` runs theirs:

```apl
      :Class DomesticParrot: Parrot
          ∇ R←Speak
            :Access Public
            R←⎕BASE.Speak,' Who''s a pretty boy, then!'
          ∇
      :EndClass
      Pol←⎕NEW DomesticParrot
      Pol.Speak
Squark! Who's a pretty boy, then!
      (Parrot ⎕CLASS Pol).Speak
Squark!
      (Bird ⎕CLASS Pol).Speak
Tweet, tweet!
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS cast interface implementation
</div>
