---
search:
  exclude: true
---

# <span>Class</span> `⎕CLASS`

`⎕CLASS` relates an instance or class to the classes and interfaces it derives from. The presence of a left argument chooses which of the two it does.

## Class Hierarchy

[Monadic `⎕CLASS`](class-monadic.md) reports that hierarchy:

```apl
      ⎕CLASS Polly←⎕NEW Parrot
┌──────────┬────────┬──────────┐
│ #.Parrot │ #.Bird │ #.Animal │
└──────────┴────────┴──────────┘
```

## Get Class/Interface Implementation

[Dyadic `⎕CLASS`](class-dyadic.md) casts an instance to one class or interface in that hierarchy, reaching the members it implements:

```apl
      (Bird ⎕CLASS Polly).Speak
Tweet, tweet!
```
