<div style="display: none;">
  ⌺
</div>

<h1 class="heading"><span class="name">Stencil</span> <span class="command">R←(f⌺g)Y</span></h1>

!!! note "Classic Edition"
    The symbol `⌺` is not available in Classic Edition, and the Stencil operator is instead represented by `⎕U233A`.

Stencil is used in image processing, artificial neural networks, computational fluid dynamics, cellular automata, and many other fields of application. The computation is sometimes referred to as tessellation, moving window, or [stencil code](https://en.wikipedia.org/wiki/Stencil_code). This operator applies the left operand function `f` to a series of (possibly overlapping) rectangles in the array `Y`.



In general, the right operand `g` is a 2- row matrix of positive non-zero integers with up to `⍴⍴Y` columns. The first row contains the rectangle sizes, the second row the *movements* that is, how much to move the rectangle in each step. If `g` is a scalar or vector it specifies the rectangle size and the movement defaults to 1.


The predominant case uses a rectangle size which is odd and a movement of 1.


Rectangles are *centred* on successive elements of `Y` and (unless the rectangle size is 1), padded with fill elements.


The first rectangle is centred on the first element of `Y` preceded by the appropriate number of fill elements. Subsequent rectangles are centred on subsequent elements of `Y` according to the size of the movement, and padded before or after as appropriate. When the movement is 1, each element of `Y` in its turn is the middle of a rectangle.


`f` is invoked dyadically with a vector left argument indicating for each axis the number of fill elements and on what side; positive values mean that the padding precedes the array values,
negative values mean that the padding follows the array values.

<h2 class="example">Example</h2>
```apl
      {⊂⍺ ⍵}⌺3 3⊢3 3⍴⍳12
┌────────────┬────────────┬─────────────┐
│┌───┬─────┐ │┌───┬─────┐ │┌────┬─────┐ │
││1 1│0 0 0│ ││1 0│0 0 0│ ││1 ¯1│0 0 0│ │
││   │0 1 2│ ││   │1 2 3│ ││    │2 3 0│ │
││   │0 4 5│ ││   │4 5 6│ ││    │5 6 0│ │
│└───┴─────┘ │└───┴─────┘ │└────┴─────┘ │
├────────────┼────────────┼─────────────┤
│┌───┬─────┐ │┌───┬─────┐ │┌────┬─────┐ │
││0 1│0 1 2│ ││0 0│1 2 3│ ││0 ¯1│2 3 0│ │
││   │0 4 5│ ││   │4 5 6│ ││    │5 6 0│ │
││   │0 7 8│ ││   │7 8 9│ ││    │8 9 0│ │
│└───┴─────┘ │└───┴─────┘ │└────┴─────┘ │
├────────────┼────────────┼─────────────┤
│┌────┬─────┐│┌────┬─────┐│┌─────┬─────┐│
││¯1 1│0 4 5│││¯1 0│4 5 6│││¯1 ¯1│5 6 0││
││    │0 7 8│││    │7 8 9│││     │8 9 0││
││    │0 0 0│││    │0 0 0│││     │0 0 0││
│└────┴─────┘│└────┴─────┘│└─────┴─────┘│
└────────────┴────────────┴─────────────┘

```
```apl
      
      {+/,⍵}⌺3 3⊢3 3⍴⍳12
12 21 16
27 45 33
24 39 28

```


In the first expression above, the left operand function `{⊂⍺ ⍵}` simply displays its left and right arguments to illustrate the mechanics of the operation. The right operand `(3 3)` specifies that each rectangle contains 3 rows and 3 columns, and the movement is 1.


In order for the first element of `Y` (1) to be centred, the first rectangle is padded with a row above and a column to the left, as indicated by the left argument `(1 1)` to the function.


Another way to think about the way Stencil operates is that it portions the array into sections or neighbourhoods in which elements can be analysed with respect to their immediate neighbours. Stencil  has uses in image processing applications.

<h2 class="example">Examples</h2>
```apl
      {⊂⍺ ⍵}⌺(3 3,[.5]2)⊢3 3⍴⍳12
┌────────────┬─────────────┐
│┌───┬─────┐ │┌────┬─────┐ │
││1 1│0 0 0│ ││1 ¯1│0 0 0│ │
││   │0 1 2│ ││    │2 3 0│ │
││   │0 4 5│ ││    │5 6 0│ │
│└───┴─────┘ │└────┴─────┘ │
├────────────┼─────────────┤
│┌────┬─────┐│┌─────┬─────┐│
││¯1 1│0 4 5│││¯1 ¯1│5 6 0││
││    │0 7 8│││     │8 9 0││
││    │0 0 0│││     │0 0 0││
│└────┴─────┘│└─────┴─────┘│
└────────────┴─────────────┘
       {⊂⍺ ⍵}⌺(3 3,[.5]3)⊢3 3⍴⍳12
┌───────────┐
│┌───┬─────┐│
││1 1│0 0 0││
││   │0 1 2││
││   │0 4 5││
│└───┴─────┘│
└───────────┘

```
```apl
      ⊢ A←5 5⍴0 0 1 0 0, 0 1 2 1 0, 1 2 3 2 1, 0 1 2 1 0
0 0 1 0 0
0 1 2 1 0
1 2 3 2 1
0 1 2 1 0
0 0 1 0 0

```
```apl
      ⊢ y←1=?10 10⍴4
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 1 0 0 0 0
1 0 0 0 1 1 0 0 0 1
1 1 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
1 0 1 0 0 1 1 0 0 1
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0 0
1 0 0 0 1 1 0 1 1 0

```
```apl
      {+/,A×⍵}⌺(⍴A) ⊢y
0 0 1 0 0 1 0 1 2 3
1 1 2 1 2 3 1 0 1 3
4 4 3 4 6 6 3 1 1 3
6 6 5 4 7 7 4 2 2 3
8 6 5 3 5 6 2 0 1 3
6 5 4 3 5 6 5 2 1 3
5 5 4 4 6 7 8 7 4 3
3 2 2 1 4 7 8 7 5 3
3 1 1 1 3 5 6 6 4 2
3 2 2 3 5 6 7 7 5 3

```


You can see that the result identifies where there are clusters in `y`.

## Examples (odd rectangle, movement not 1)


If the movement is greater than one, corresponding portions are skipped as shown below.
```apl
      {⊂⍵}⌺(⍪3 2) ⍳8
┌─────┬─────┬─────┬─────┐
│0 1 2│2 3 4│4 5 6│6 7 8│
└─────┴─────┴─────┴─────┘
      {(¯2↑⍕⍺),' f ',⍕⍵}⌺(⍪3 2) ⍳8
 1 f 0 1 2
 0 f 2 3 4
 0 f 4 5 6
 0 f 6 7 8
⍝      ↑ middle

```
```apl
      {⊂⍵}⌺(⍪5 2) ⍳9
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│0 0 1 2 3│1 2 3 4 5│3 4 5 6 7│5 6 7 8 9│7 8 9 0 0│
└─────────┴─────────┴─────────┴─────────┴─────────┘
      {(¯2↑⍕⍺),' f ',⍕⍵}⌺(⍪5 2) ⍳9
 2 f 0 0 1 2 3
 0 f 1 2 3 4 5
 0 f 3 4 5 6 7
 0 f 5 6 7 8 9
¯2 f 7 8 9 0 0
⍝        ↑ middle

```

## Even Rectangle Size


For even rectangle sizes, the "middle" consists of two elements which are moved according to the movement parameter (equal to 1 in these examples).

<h2 class="example">Examples</h2>
```apl
      ⎕←s←{⊂⍵}⌺ 2 ⍳8
┌───┬───┬───┬───┬───┬───┬───┐
│1 2│2 3│3 4│4 5│5 6│6 7│7 8│
└───┴───┴───┴───┴───┴───┴───┘
```
```apl
      {(¯2↑⍕⍺),' f ',⍕⍵}⌺ 2⍳8
 0 f 1 2
 0 f 2 3
 0 f 3 4
 0 f 4 5
 0 f 5 6
 0 f 6 7
 0 f 7 8
⍝    ↑ ↑ middle
```
```apl
      ⎕←s←{⊂⍵}⌺ 4⍳8
┌───────┬───────┬───────┬───────┬───────┬───────┬───────┐
│0 1 2 3│1 2 3 4│2 3 4 5│3 4 5 6│4 5 6 7│5 6 7 8│6 7 8 0│
└───────┴───────┴───────┴───────┴───────┴───────┴───────┘
      ⍴s
7
      {(¯2↑⍕⍺),' f ',⍕⍵}⌺ 4⍳8
 1 f 0 1 2 3
 0 f 1 2 3 4
 0 f 2 3 4 5
 0 f 3 4 5 6
 0 f 4 5 6 7
 0 f 5 6 7 8
¯1 f 6 7 8 0
⍝      ↑ ↑ middle

```

## Examples (even rectangle, movement not 1)
```apl
      {⊂⍵}⌺(⍪4 2) ⍳8
┌───────┬───────┬───────┬───────┐
│0 1 2 3│2 3 4 5│4 5 6 7│6 7 8 0│
└───────┴───────┴───────┴───────┘
      {(¯2↑⍕⍺),' f ',⍕⍵}⌺(⍪4 2) ⍳8
 1 f 0 1 2 3
 0 f 2 3 4 5
 0 f 4 5 6 7
¯1 f 6 7 8 0
⍝      ↑ ↑ middle

```
```apl
      {⊂⍵}⌺(⍪6 2) ⍳8
┌───────────┬───────────┬───────────┬───────────┐
│0 0 1 2 3 4│1 2 3 4 5 6│3 4 5 6 7 8│5 6 7 8 0 0│
└───────────┴───────────┴───────────┴───────────┘
      {(⍕⍺),' f ',⍕⍵}⌺(⍪6 2) ⍳8
2 f 0 0 1 2 3 4 
0 f 1 2 3 4 5 6 
0 f 3 4 5 6 7 8 
¯2 f 5 6 7 8 0 0
⍝        ↑ ↑ middle

```


