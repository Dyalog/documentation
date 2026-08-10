---
search:
  boost: 2
---

# <span>Class Hierarchy</span> `R←⎕CLASS Y`{{key}}

Monadic `⎕CLASS` returns a list of references to classes and interfaces that specifies the class hierarchy for the class or instance specified by `Y`.

To instead access the lower level implementations of a class, use [dyadic `⎕CLASS`](class-dyadic.md).

`Y` must be a reference to a class or to an instance of a class.

`R` is a vector of vectors whose items represent nodes in the class hierarchy of `Y`. Each item of `R` is a vector whose first item is a class reference and whose subsequent items (if any) are references to the interfaces supported by that class.

<h2 class="example">Examples</h2>

This example illustrates a simple inheritance tree or class hierarchy. There are 3 classes, namely:
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

The [Penguin class example](../../../programming-reference-guide/object-oriented-programming/interfaces/interface-example) illustrates the use of interfaces.

In this case, the `Penguin` class derives from `Animal` (as above) but additionally supports the `BirdBehaviour` and `FishBehaviour` interfaces, thereby inheriting members from both.
```apl
      Pingo←⎕NEW Penguin
      ⎕CLASS Pingo
  #.Penguin  #.FishBehaviour  #.BirdBehaviour    #.Animal
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS
</div>
