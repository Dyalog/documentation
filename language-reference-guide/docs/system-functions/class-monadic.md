---
search:
  boost: 2
---

# <span>Class Hierarchy</span> `R←⎕CLASS Y`{{key}}

This function reports the classes and interfaces that a class or instance derives from, which [dyadic `⎕CLASS`](class-dyadic.md) can cast an instance to.

<h2 class="example">Example</h2>

`Parrot` derives from `Bird`, which derives from `Animal`:

```apl
      :Class Animal
      :EndClass
      :Class Bird: Animal
      :EndClass
      :Class Parrot: Bird
      :EndClass
      ⎕CLASS Polly←⎕NEW Parrot
┌──────────┬────────┬──────────┐
│ #.Parrot │ #.Bird │ #.Animal │
└──────────┴────────┴──────────┘
```

## Right Argument

`Y` is a reference to a class or to an instance of a class.

## Result

`R` is a vector of vectors whose items represent nodes in the class hierarchy of `Y`, the class of `Y` first and the class it ultimately derives from last. Each item is a vector whose first item is a class reference, and whose subsequent items, if any, are references to the interfaces that class supports.

<h3 class="example">Examples</h3>

Continuing with the classes from the example above, an instance reports its own class and every class that class derives from. A class reports the same for itself:

```apl
      ⎕CLASS Eeyore←⎕NEW Animal
┌──────────┐
│ #.Animal │
└──────────┘
      ⎕CLASS Robin←⎕NEW Bird
┌────────┬──────────┐
│ #.Bird │ #.Animal │
└────────┴──────────┘
      ⎕CLASS¨Parrot Animal
┌────────────────────────────────┬────────────┐
│┌──────────┬────────┬──────────┐│┌──────────┐│
││ #.Parrot │ #.Bird │ #.Animal │││ #.Animal ││
│└──────────┴────────┴──────────┘│└──────────┘│
└────────────────────────────────┴────────────┘
```

Interfaces appear alongside the class that supports them, within the same item of `R`. As in the [Penguin Class example](../../programming-reference-guide/object-oriented-programming/interfaces/interface-example.md), `Penguin` derives from `Animal` but additionally supports the `BirdBehaviour` and `FishBehaviour` interfaces. Its first node, therefore, holds three references, and `#.Animal` remains a node of its own:

```apl
      :Interface BirdBehaviour
      :EndInterface
      :Interface FishBehaviour
      :EndInterface
      :Class Penguin: Animal,BirdBehaviour,FishBehaviour
      :EndClass
      ⎕CLASS Pingo←⎕NEW Penguin
┌─────────────────────────────────────────────┬──────────┐
│ #.Penguin  #.FishBehaviour  #.BirdBehaviour │ #.Animal │
└─────────────────────────────────────────────┴──────────┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS hierarchy inheritance
</div>
