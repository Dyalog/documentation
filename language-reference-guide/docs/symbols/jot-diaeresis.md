---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Jot Diaeresis</span> <span class="command">⍤</span></h1>

Jot Diaeresis is a dyadic operator with an ambivalent left operand

Operator Jot Diaeresis means
[Atop](../primitive-operators/atop.md)
```apl
      -⍤÷ 4
¯0.25
      12 -⍤÷ 4
¯3
      3 1 4 1 5 ~⍤∊ 1 2 3
0 0 1 0 1
      3 1 4 1 5 (~⍤∊ ⊢⍤/ ⊣) ⍳3  ⍝ ⊢⍤/ is always a function
4 5
```
[Rank ](../primitive-operators/rank.md)
```apl
      cube    ⍝ 3D array
 1  2  3
 4  5  6
        
 7  8  9
10 11 12

      (,⍤2) cube
1 2 3  4  5  6
7 8 9 10 11 12

      cmat    ⍝ character matrix
abc
zxy 
      (⍋⍤1) cmat    ⍝ grade-up by row  
1 2 3 
2 3 1 
      nmat     ⍝ numeric matrix
1  2  3  4
5  6  7  8
9 10 11 12
 
      10 20 30 (+⍤0 1) nmat  ⍝ scalars plus vectors
11 12 13 14 
25 26 27 28 
39 40 41 42
```
[Language Elements](../glyphs.md)


