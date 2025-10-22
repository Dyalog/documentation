---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Comma</span> <span class="command">,</span></h1>

Monadic Comma means
[Ravel](../primitive-functions/ravel/index.md)
```apl
      cube    ⍝ 3D array
1 2
3 4
   
5 6
7 8
      , cube
1 2 3 4 5 6 7 8

      ,[2 3] cube    ⍝ Ravel with axes
1 2 3 4
5 6 7 8
```
[Ravel with Axes](../primitive-functions/ravel/ravel-with-axes.md)
```apl
      ,[1.5]'ABC'
A
B
C
```

Dyadic Comma means
[Catenate/Laminate (Join)](../primitive-functions/catenate-laminate.md)
```apl
      1 2 3 , 4 5 6
1 2 3 4 5 6

      cube , 99
1 2 99
3 4 99
      
5 6 99
7 8 99

      1 2 3 ,[0.5] 4 5 6   ⍝ Laminate
1 2 3
4 5 6 
```
[Language Elements](../glyphs.md)


