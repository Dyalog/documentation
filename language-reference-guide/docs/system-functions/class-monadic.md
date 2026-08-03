---
search:
  boost: 2
---

# <span>Class Hierarchy</span> `R←⎕CLASS Y`{{key}}

Monadic `⎕CLASS` returns a list of references to Classes and Interfaces that specifies the class hierarchy for the Class or Instance specified by `Y`.

`Y` must be a reference to a Class or to an Instance of a Class.

`R` is a vector of vectors whose items represent nodes in the Class hierarchy of `Y`. Each item of `R` is a vector whose first item is a Class reference and whose subsequent items (if any) are references to the Interfaces supported by that Class.

<h2 class="example">Examples</h2>

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

The [Penguin Class example](../../../programming-reference-guide/object-oriented-programming/interfaces/interface-example) illustrates the use of Interfaces.

In this case, the `Penguin` Class derives from `Animal` (as above) but additionally supports the `BirdBehaviour` and `FishBehaviour` Interfaces, thereby inheriting members from both.
```apl
      Pingo←⎕NEW Penguin
      ⎕CLASS Pingo
  #.Penguin  #.FishBehaviour  #.BirdBehaviour    #.Animal
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS
</div>
