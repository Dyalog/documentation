---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Tilde Diaeresis</span> <span class="command">⍨</span></h1>

Tilde Diaeresis is a monadic operator with a dyadic operand

Operator Tilde Diaeresis means
[Commute](../primitive-operators/commute.md)
```apl
      2 ⍴ 3     ⍝ ⍺ ⍴ ⍵
3 3
      2 ⍴⍨ 3    ⍝ ⍵ ⍴ ⍺
2 2 2
      ⍴⍨ 3      ⍝ ⍵ ⍴ ⍵
3 3 3
```

[Constant](../primitive-operators/constant.md)
```apl
      'mu'⍨ 'any' ⎕NULL   ⍝ Always returns its operand
mu
      1E100 ('mu'⍨) 1j1
mu
      ¯1⍨¨ ⍳2 3
¯1 ¯1 ¯1
¯1 ¯1 ¯1
```
[Language Elements](../glyphs.md)


