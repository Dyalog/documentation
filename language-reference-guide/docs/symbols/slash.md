---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Slash</span> <span class="command">/</span></h1>

# Used as a Function

Monadic Slash is not defined

Dyadic Slash means
[Replicate](../primitive-functions/replicate.md)
```apl
      3 1 ¯2 2 / 6 7 8 9
6 6 6 7 0 0 9 9

      1 0 1 0 1 / 'Heart'
Hat
```

# Used as an Operator

Slash is a monadic operator with a dyadic operand

Operator Slash means
[Reduce](../primitive-operators/reduce/index.md), [N-Wise Reduce](../primitive-operators/reduce/reduce-n-wise.md)
```apl
      +/ 1 2 3 4 5
15
      2 +/ 1 2 3 4 5   ⍝ pair-wise sum
3 5 7 9

      cube    ⍝ 3D array
 1  2  3  4
 5  6  7  8
 9 10 11 12
           
13 14 15 16
17 18 19 20
21 22 23 24

      +/ cube
10 26 42
58 74 90

      +/[1] cube    ⍝ sum of planes
14 16 18 20
22 24 26 28
30 32 34 36

      +/[2] cube    ⍝ column sums
15 18 21 24
51 54 57 60

```
[Language Elements](../glyphs.md)


