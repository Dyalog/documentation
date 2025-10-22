---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Quad Colon</span> <span class="command">⍠</span></h1>

The Variant operator specifies the value of an option to be used by its left operand function.

<h2 class="example">Examples</h2>
```apl
      ('a' ⎕R 'x') 'ABC'           ⍝ 'a' replaced with 'x'
ABC

      ('a' ⎕R 'x' ⍠ 'IC' 1) 'ABC'  ⍝ .. Ignoring Case
xBC

      IgnCase ← ⍠ 'IC' 1
      
      'a' ⎕R 'x' IgnCase 'ABC'
xBC 
```

The following derived function returns the location of the word `'variant'` within its right argument using default values for all the options.
```apl
      f1 ← 'variant' ⎕S 0
      f1 'The variant Variant operator'
4
```

It may be modified to perform a case-insensitive search:
```apl
      (f1 ⍠ 1) 'The variant Variant operator'
4 12
```

This modified function may be named:
```apl
      f2 ← f1 ⍠ 1
      f2 'The variant Variant operator'
4 12
```

The modified function may itself be modified, in this case to revert to a case sensitive search:
```apl
      f3 ← f2 ⍠ 0
      f3 'The variant Variant operator'
4
```


This is equivalent to:
```apl
      (f1 ⍠ 1 ⍠ 0) 'The variant Variant operator'
4
```
[Language Elements](../glyphs.md)


