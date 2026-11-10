---
search:
  boost: 2
---

# <span>Get Class/Interface Implementation</span> `R←X ⎕CLASS Y`{{key}}

This function casts an instance to one of the classes or interfaces it derives from, reaching the members that one implements. To report the whole hierarchy instead, see [Class Hierarchy](class-monadic.md).

<h2 class="example">Example</h2>

```apl
      (Bird ⎕CLASS Polly).Speak
Tweet, tweet!
```

## Right Argument

`Y` is a reference to an instance of a class.

## Left Argument

`X` is a reference to an interface that instance `Y` supports, or to a base class that `Y` is derived from. Both are reported by [monadic `⎕CLASS`](class-monadic.md).

## Result

`R` is a reference to the implementation of interface `X`, or of base class `X`, by instance `Y`. It is used as a *cast*, to reach the members of `Y` that correspond to the members of `X`.

<h2 class="example">Example</h2>

A cast reaches an interface implementation. In the [Penguin Class example](../../programming-reference-guide/object-oriented-programming/interfaces/interface-example.md), `Penguin` supports the `BirdBehaviour` and `FishBehaviour` interfaces, and implements each of their members under a name of its own:

```apl
      ⎕CLASS Pingo←⎕NEW Penguin
┌─────────────────────────────────────────────┬──────────┐
│ #.Penguin  #.FishBehaviour  #.BirdBehaviour │ #.Animal │
└─────────────────────────────────────────────┴──────────┘

      (FishBehaviour ⎕CLASS Pingo).Swim
I can dive and swim like a fish
      (BirdBehaviour ⎕CLASS Pingo).Fly
Although I am a bird, I cannot fly
      (BirdBehaviour ⎕CLASS Pingo).Lay
I lay one egg every year
      (BirdBehaviour ⎕CLASS Pingo).Sing
Croak, Croak!
```

<h2 class="example">Example</h2>

A cast also reaches a member that a base class defines and a derived class supersedes. `DomesticParrot` derives from `Parrot`, which derives from `Bird`, and each defines its own `Speak`. The instance runs the one nearest to it:

```apl
      Pol←⎕NEW DomesticParrot
      Pol.Speak
Squark! Who's a pretty boy, then!
```

Casting to `Parrot` or `Bird` runs the superseded one:

```apl
      (Parrot ⎕CLASS Pol).Speak
Squark!
      (Bird ⎕CLASS Pol).Speak
Tweet, tweet!
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS cast interface implementation
</div>
