---
search:
  exclude: true
---

# <span>Class</span> `⎕CLASS`

`⎕CLASS` relates an Instance or Class to the Classes and Interfaces it derives from. The presence of a left argument chooses which of the two it does.

## Class Hierarchy

[Monadic `⎕CLASS`](class-monadic.md) reports that hierarchy:

```apl
      ⎕CLASS Polly←⎕NEW Parrot
┌──────────┬────────┬──────────┐
│ #.Parrot │ #.Bird │ #.Animal │
└──────────┴────────┴──────────┘
```

## Get Class/Interface Implementation

[Dyadic `⎕CLASS`](class-dyadic.md) casts an Instance to one Class or Interface in that hierarchy, reaching the members it implements:

```apl
      (Bird ⎕CLASS Polly).Speak
Tweet, tweet!
```
