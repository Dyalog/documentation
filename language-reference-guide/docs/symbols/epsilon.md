---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Epsilon</span> <span class="command">∊</span></h1>

Monadic Epsilon means

If `⎕ML=0` [Type Of](../primitive-functions/type.md)
```apl
      ∊ 3 3⍴1 'abc' 
   0         0
        0
   0         0
```
If `⎕ML≥1` [Enlist](../primitive-functions/enlist.md)
```apl
      mat
1 2 3
4 5 6
      ∊ 0 mat (7 8) 9
0 1 2 3 4 5 6 7 8 9

      ∊ 2 3⍴1 'abc'
1 abc 1 abc 1 abc

```

Dyadic Epsilon means
[Member Of](../primitive-functions/membership.md)
```apl
      'abc' 4 ∊ 4 'ab' 'abcd'
0 1
      mat ∊ 6 2 7 4
0 1 0
1 0 1
```
[Language Elements](../glyphs.md)


