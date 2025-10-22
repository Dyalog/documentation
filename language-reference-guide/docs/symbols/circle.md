---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Circle</span> <span class="command">○</span></h1>

Monadic Circle means
[Pi Times](../primitive-functions/pi-times.md)
```apl
      ○ 0 1 2
0 3.14159 6.28319
```
Dyadic Circle means
[Circular Functions](../primitive-functions/circular-functions.md)
```apl
          Note: Angles are in radians 
                radians ← ○ degrees ÷ 180

      1 ○ 0 1.5707963 3.1415927
0 1 ¯4.64102E¯8

 ⍺   ⍺ ○ ⍵         ⍺   ⍺ ○ ⍵    
                   0   (1-⍵*2)*0.5
¯1   Arcsin ⍵      1   Sine ⍵
¯2   Arccos ⍵      2   Cosine ⍵
¯3   Arctan ⍵      3   Tangent ⍵
¯4   (¯1+⍵*2)*0.5  4   (1+⍵*2)*0.5
¯5   Arcsinh ⍵     5   Sinh ⍵
¯6   Arccosh ⍵     6   Cosh ⍵
¯7   Arctanh ⍵     7   Tanh ⍵
¯8   -8○⍵          8   (-1+⍵*2)*0.5
¯9   ⍵             9   real part of ⍵
¯10  +⍵           10   |⍵
¯11  ⍵×0J1        11   imaginary part of ⍵
¯12  *⍵×0J1       12   phase of ⍵

```
[Language Elements](../glyphs.md)


