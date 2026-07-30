---
search:
  boost: 2
---

# <span>Get Class/Interface Implementation</span> `R←X⎕CLASS Y`{{key}}

`Y` must be a reference to an Instance of a Class and `X` is a reference to an Interface that is supported by Instance `Y` or to a Class upon which Instance `Y` is based.

In this case, `R` is a reference to the implementation of Interface `X` by Instance `Y`, or to the implementation of (Base) Class `X` by Instance `Y`, and is used as a *cast* in order to access members of `Y` that correspond to members of Interface of (Base) Class `X`.

## Example 1

Once again, the Penguin Class example (see[Programmer's Guide: "Penguin Class Example"](../../../programming-reference-guide/object-oriented-programming/interfaces/interface-example)) is used to illustrate the use of Interfaces.
```apl
      Pingo←⎕NEW Penguin
      ⎕CLASS Pingo
  #.Penguin  #.FishBehaviour  #.BirdBehaviour    #.Animal
 
      (FishBehaviour ⎕CLASS Pingo).Swim
I can dive and swim like a fish
      (BirdBehaviour ⎕CLASS Pingo).Fly
Although I am a bird, I cannot fly
      (BirdBehaviour ⎕CLASS Pingo).Lay
I lay one egg every year          
      (BirdBehaviour ⎕CLASS Pingo).Sing
Croak, Croak!           
```

## Example 2

This example illustrates the use of dyadic `⎕CLASS` to cast an Instance to a lower Class and thereby access a member in the lower Class that has been superseded by another Class higher in the tree.
```apl
      Polly←⎕NEW DomesticParrot
      Polly.Speak
Squark! Who's a pretty boy, then!
 
```

Note that the `Speak` method invoked above is the `Speak` method defined by Class `DomesticParrot`, which supersedes the `Speak` methods of sub-classes `Parrot` and `Bird`.

You may use a cast to access the (superseded) `Speak` method in the sub-classes `Parrot` and `Bird`.
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
