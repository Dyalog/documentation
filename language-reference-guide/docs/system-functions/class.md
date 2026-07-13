---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS
</div>






# <span>Class</span> `R←{X}⎕CLASS Y`{{key}}


## Monadic Case


Monadic `⎕CLASS` returns a list of references to Classes and Interfaces that specifies the class hierarchy for the Class or Instance specified by `Y`.


`Y` must be a reference to a Class or to an Instance of a Class.


`R` is a vector of vectors whose items represent nodes in the Class hierarchy of `Y`. Each item of `R` is a vector whose first item is a Class reference and whose subsequent items (if any) are references to the Interfaces supported by that Class.



## Example 1


This example illustrates a simple inheritance tree or Class hierarchy. There are 3 Classes, namely:
```apl
Animal
    Bird (derived from Animal)
        Parrot (derived from Bird)

:Class Animal
...
:EndClass ⍝ Animal
 
:Class Bird: Animal
...
:EndClass ⍝ Bird
 
:Class Parrot: Bird
...
:EndClass ⍝ Parrot

```
```apl
       ⎕CLASS Eeyore←⎕NEW Animal
  #.Animal  
       ⎕CLASS Robin←⎕NEW Bird
  #.Bird    #.Animal  
       ⎕CLASS Polly←⎕NEW Parrot
  #.Parrot    #.Bird    #.Animal
 
      ⎕CLASS¨ Parrot Animal
   #.Parrot    #.Bird    #.Animal      #.Animal
```



### Example 2


The Penguin Class example (see[Programmer's Guide: "Penguin Class Example"](../../../programming-reference-guide/object-oriented-programming/interfaces/interface-example)) illustrates the use of Interfaces.


In this case, the `Penguin` Class derives from `Animal` (as above) but additionally supports the `BirdBehaviour` and `FishBehaviour` Interfaces, thereby inheriting members from both.
```apl
      Pingo←⎕NEW Penguin
      ⎕CLASS Pingo
  #.Penguin  #.FishBehaviour  #.BirdBehaviour    #.Animal
```



## Dyadic Case


If `X` is specified, `Y` must be a reference to an Instance of a Class and `X` is a reference to an Interface that is supported by Instance `Y` or to a Class upon which Instance `Y` is based.


In this case, `R` is a reference to the implementation of Interface `X` by Instance `Y`, or to the implementation of (Base) Class `X` by Instance `Y`, and is used as a *cast* in order to access members of `Y` that correspond to members of Interface of (Base) Class `X`.



#### Example 1


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



#### Example 2


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



