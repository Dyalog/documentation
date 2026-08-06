---
search:
  exclude: true
---

# <span>Class</span> `⎕CLASS`

## Monadic `⎕CLASS` means

[Class Hierarchy](class-monadic.md)
```apl
      :Class base
      :EndClass
      :Interface iface
      :EndInterface
      :Class derived : base, iface
      :EndClass
      ⎕CLASS derived
┌────────────────────┬────────┐
│ #.derived  #.iface │ #.base │
└────────────────────┴────────┘
```

## Dyadic `⎕CLASS` means

[Get Class/Interface Implementation](class-dyadic.md)
```apl
      :Class Animal
          ∇ r←Speak
            :Access public
            r←'Some generic noise'
          ∇
      :EndClass
      :Class Dog : Animal
          ∇ r←Speak
            :Access public
            r←'Woof'
          ∇
      :EndClass
      rex←⎕NEW Dog
      rex.Speak
Woof
      (Animal ⎕CLASS rex).Speak
Some generic noise
```
