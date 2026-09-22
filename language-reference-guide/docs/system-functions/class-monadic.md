---
search:
  boost: 2
---

# <span>Class Hierarchy</span> `R←⎕CLASS Y`{{key}}

This function reports the Classes and Interfaces that a Class or Instance derives from. To cast an Instance to one of them instead, see [Get Class/Interface Implementation](class-dyadic.md).

<h2 class="example">Example</h2>

```apl
      ⎕CLASS Polly←⎕NEW Parrot
┌──────────┬────────┬──────────┐
│ #.Parrot │ #.Bird │ #.Animal │
└──────────┴────────┴──────────┘
```

## Right Argument

`Y` is a reference to a Class or to an Instance of a Class.

## Result

`R` is a vector of vectors whose items represent nodes in the Class hierarchy of `Y`, the Class of `Y` first and the Class it ultimately derives from last. Each item is a vector whose first item is a Class reference, and whose subsequent items, if any, are references to the Interfaces that Class supports.

<h2 class="example">Example</h2>

This inheritance tree has three Classes, each derived from the one above it:

```apl
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

An Instance reports its own Class and every Class that Class derives from. A Class reports the same for itself:

```apl
      ⎕CLASS Eeyore←⎕NEW Animal
┌──────────┐
│ #.Animal │
└──────────┘
      ⎕CLASS Robin←⎕NEW Bird
┌────────┬──────────┐
│ #.Bird │ #.Animal │
└────────┴──────────┘
      ⎕CLASS Polly←⎕NEW Parrot
┌──────────┬────────┬──────────┐
│ #.Parrot │ #.Bird │ #.Animal │
└──────────┴────────┴──────────┘

      ⎕CLASS¨Parrot Animal
┌────────────────────────────────┬────────────┐
│┌──────────┬────────┬──────────┐│┌──────────┐│
││ #.Parrot │ #.Bird │ #.Animal │││ #.Animal ││
│└──────────┴────────┴──────────┘│└──────────┘│
└────────────────────────────────┴────────────┘
```

<h2 class="example">Example</h2>

Interfaces appear alongside the Class that supports them, within the same item of `R`. In the [Penguin Class example](../../programming-reference-guide/object-oriented-programming/interfaces/interface-example.md), `Penguin` derives from `Animal` but additionally supports the `BirdBehaviour` and `FishBehaviour` Interfaces, inheriting members from both. Its first node therefore holds three references, and `#.Animal` remains a node of its own:

```apl
      ⎕CLASS Pingo←⎕NEW Penguin
┌─────────────────────────────────────────────┬──────────┐
│ #.Penguin  #.FishBehaviour  #.BirdBehaviour │ #.Animal │
└─────────────────────────────────────────────┴──────────┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLASS CLASS hierarchy inheritance
</div>
