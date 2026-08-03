---
search:
  boost: 2
---

# <span>Get Class/Interface Implementation</span> `R←X ⎕CLASS Y`{{key}}

Dyadic `⎕CLASS` returns a reference to the implementation of interface `X` by instance `Y`, or to the implementation of (base) class `X` by instance `Y`, and is used as a _cast_ in order to access members of `Y` that correspond to members of interface or (base) class `X`.

`Y` must be a reference to an instance of a class and `X` is a reference to an interface that is supported by instance `Y` or to a class upon which instance `Y` is based.

<h2 class="example">Examples</h2>

The [Penguin class example](../../../programming-reference-guide/object-oriented-programming/interfaces/interface-example) is used to illustrate the use of interfaces.

```apl
      Pingo←⎕NEW Penguin
      (FishBehaviour ⎕CLASS Pingo).Swim
I can dive and swim like a fish
      (BirdBehaviour ⎕CLASS Pingo).Fly
Although I am a bird, I cannot fly
      (BirdBehaviour ⎕CLASS Pingo).Lay
I lay one egg every year         
      (BirdBehaviour ⎕CLASS Pingo).Sing
Croak, Croak!          
```

The next example illustrates the use of dyadic `⎕CLASS` to cast an instance to a lower class and thereby access a member in the lower class that has been superseded by another class higher in the tree.

```apl
      Polly←⎕NEW DomesticParrot
      Polly.Speak
Squark! Who's a pretty boy, then!
```

Note that the `Speak` method invoked above is the `Speak` method defined by class `DomesticParrot`, which supersedes the `Speak` methods of sub-classes `Parrot` and `Bird`.

You can use a cast to access the (superseded) `Speak` method in the sub-classes `Parrot` and `Bird`.

```apl
      (Parrot ⎕CLASS Polly).Speak
Squark!
      (Bird ⎕CLASS Polly).Speak
Tweet, tweet!
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS
</div>
