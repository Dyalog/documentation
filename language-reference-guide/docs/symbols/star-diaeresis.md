---
search:
  exclude: true
---
# <span>Star Diaeresis</span> `⍣`

Star Diaeresis is a dyadic operator with an ambivalent left operand and an integer or dyadic right operand

Operator Star Diaeresis means
[Power](../primitive-operators/power.md)
```apl
      cube    ⍝ 3D array
AB
CD
  
EF
GH
      (↓⍣1) cube   ⍝ split once
┌──┬──┐
│AB│CD│
├──┼──┤
│EF│GH│
└──┴──┘
      (↓⍣2) cube   ⍝ split twice
┌───────┬───────┐
│┌──┬──┐│┌──┬──┐│
││AB│CD│││EF│GH││
│└──┴──┘│└──┴──┘│
└───────┴───────┘

      f ← (32∘+)∘(×∘1.8)   ⍝ °F from °C

      f ¯273 ¯40 0 100     ⍝ Fahrenheit
¯459.4 ¯40 32 212

      c ← f⍣¯1             ⍝ Inverse: °C from °F

      c ¯459.4 ¯40 32 212  ⍝ Celsius
¯273 ¯40 0 100

      1 +∘÷⍣= 1            ⍝ fixpoint: golden mean
1.61803
```
[Language Elements](../glyphs.md)
