---
search:
  exclude: true
---

# <span>Class</span> `⎕CLASS`

`⎕CLASS` relates an instance or class to the classes and interfaces it derives from.

## Class Hierarchy

[Monadic `⎕CLASS`](class-monadic.md) reports that hierarchy. Here, `Parrot` derives from `Bird`, which derives from `Animal`:

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
      ⎕CLASS Polly←⎕NEW Parrot
┌──────────┬────────┬──────────┐
│ #.Parrot │ #.Bird │ #.Animal │
└──────────┴────────┴──────────┘
```

## Get Class/Interface Implementation

[Dyadic `⎕CLASS`](class-dyadic.md) casts an instance to one class or interface in that hierarchy, reaching the members it implements. Continuing with `Polly` from the example above:

```apl
      (Bird ⎕CLASS Polly).Speak
Tweet, tweet!
```
