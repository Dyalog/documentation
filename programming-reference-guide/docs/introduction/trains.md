<h1 class="heading"><span class="name">Function Trains</span></h1>

## Introduction

A *Train* is a derived function constructed from a sequence of 2 or 3 functions, or from an array followed by two functions, which bind together to form a function.

Note that the right-most item  of a function train (which is by definition a function) must be isolated from anything to its right, otherwise it will be bound to that rather than to the items to its left. This is done using parentheses.

For example, the following expression  comprises a function train `-,÷` that is separated from its argument 2 by parentheses:
```apl
      (-,÷) 2
¯2 0.5
```

and means:

1. Calculate the reciprocal of 2
2. Calculate the negation of 2
3. Catenate these 2 results together

Whereas, without the parentheses to identify the function train, the expression      means (as it did before):

1. Calculate the reciprocal of 2
2. Ravel the result of step 1
3. Negate the result of step 2
```apl

      -,÷ 2
¯0.5
```

## Forks and Atops

The following trains are currently supported where `f`, `g` and `h` are functions and `A` is an array:
```apl
      f g h
      A g h
        g h
```

The 3-item trains `(f g h)` and `(A g h)` are termed *forks* while the 2-item train `(g h)` is termed an *atop*. To distinguish the two styles of *fork*, we can use the terms *fgh-fork* or *Agh-fork*.

## Trains as Functions

A train is syntactically equivalent to a function and so, in common with any other function, may be:

- named using assignment
- applied to or between arguments
- consumed by operators as an operand
- and so forth.

In particular, trains may be applied to a single array (monadic use) or between 2 arrays (dyadic use), providing  six new constructs.
```apl
    ⍺(f g h)⍵ ←→ (⍺ f ⍵) g (⍺ h ⍵)   ⍝ dyadic (fgh) fork
    ⍺(A g h)⍵ ←→    A    g (⍺ h ⍵)   ⍝ dyadic (Agh) fork
    ⍺(  g h)⍵ ←→         g (⍺ h ⍵)   ⍝ dyadic       atop

     (f g h)⍵ ←→ (  f ⍵) g (  h ⍵)   ⍝ monadic (fgh) fork
     (A g h)⍵ ←→    A    g (  h ⍵)   ⍝ monadic (Agh) fork
     (  g h)⍵ ←→         g (  h ⍵)   ⍝ monadic       atop
```

## Identifying a Train

For a sequence to be interpreted as a train it must be separated from the argument to which it is applied. This can be done using parentheses or by naming the derived function.

## Example - fork: negation of catenated with reciprocal
```apl
      (-,÷)5         
¯5 0.2
```

## Example - named fork
```apl
      negrec←-,÷ 
      negrec 5
 ¯5 0.2
```

Whereas, without these means to identify the sequence as a train, the expression:
```apl
      -,÷ 5         
¯0.2
```

means the negation of the ravel of the reciprocal of 5.

## Idiom Recognition

Function trains lend themselves to idiom recognition, a technique used to optimise the performance of certain expressions.

<h3 class="example">Example</h3>

An expression to find the first position in a random integer vector `X` of a number greater than 999000 is:
```apl
      X←?1e6⍴1e6
      (X≥999000)⍳1
1704
```

A function train is not only more concise, it is faster too.
```apl

      X (⍳∘1 ≥) 999000
1704
```

## Trains of Trains

As a train resolves to a function, a sequences of more than 3 functions represents a train of trains. Function sequences longer than 3 are bound in threes, starting from the right:
```apl
... fu fv fw fx fy fz → ... fu (fv fw (fx fy fz))
```

This means that, in the absence of parentheses, a sequence of an odd number of functions resolves to a 3-train (fork) and an even-numbered sequence resolves to a 2-train (atop):

```apl
e f g h i j k → e f(g h(i j k))     ⍝ fork(fork(fork))
f g h i j k →   f(g h(i j k))       ⍝ atop(fork(fork))
```

<h3 class="example">Examples</h3>
```apl
      6( +,-,×,÷)2     ⍝ fork:(6+2),((6-2),((6×2),(6÷2)))
8 4 12 3

      6(⌽+,-,×,÷)2     ⍝ atop: ⌽ (6+2), ...
3 12 4 8

      ]Boxing on
Was OFF
```
```apl

      +,-,×,÷          ⍝ boxed display of fork
┌─┬─┬─────────────┐
│+│,│┌─┬─┬───────┐│
│ │ ││-│,│┌─┬─┬─┐││
│ │ ││ │ ││×│,│÷│││
│ │ ││ │ │└─┴─┴─┘││
│ │ │└─┴─┴───────┘│
└─┴─┴─────────────┘
      ⌽+,-,×,÷         ⍝ boxed display of atop
┌─┬───────────────────┐
│⌽│┌─┬─┬─────────────┐│
│ ││+│,│┌─┬─┬───────┐││
│ ││ │ ││-│,│┌─┬─┬─┐│││
│ ││ │ ││ │ ││×│,│÷││││
│ ││ │ ││ │ │└─┴─┴─┘│││
│ ││ │ │└─┴─┴───────┘││
│ │└─┴─┴─────────────┘│
└─┴───────────────────┘
```
```apl
      ]Boxing -trains=tree
Was -trains=box
      +,-,×,÷          ⍝ boxed (tree) display of fork
┌─┼───┐      
+ , ┌─┼───┐  
    - , ┌─┼─┐
        × , ÷

```

## Binding Strengths

The binding strength between the items of a train is less than that of operand-operator binding. In other words, operators bind first with their function (or array) operands to form derived functions, which may then participate as items in a train.

<h3 class="example">Example</h3>
```apl
      +⌿ ÷ ≢            ⍝ fork for mean value
┌─────┬─┬─┐
│┌─┬─┐│÷│≢│
││+│⌿││ │ │
│└─┴─┘│ │ │
└─────┴─┴─┘

      ⌊/,⌈/             ⍝ fork for min_max
┌─────┬─┬─────┐
│┌─┬─┐│,│┌─┬─┐│
││⌊│/││ ││⌈│/││
│└─┴─┘│ │└─┴─┘│
└─────┴─┴─────┘
```

This means that any of the four hybrid tokens `/ ⌿ \ ⍀` will not be interpreted as a function if there's a function to its left in the train. In order to fix one of these tokens as a replicate or expand function, it must be isolated from the function to its left:
```apl
      (⍳/⍳)3        ⍝ → ⍳/ atop ⍳3 → RANK ERROR
RANK ERROR

      (⍳{⍺/⍵}⍳)3    ⍝ → (⍳3){⍺/⍵}(⍳3) → (⍳3)/(⍳3)
1 2 2 3 3 3

      (⍳(/∘⊢)⍳)3    ⍝ → (⍳3)/⊢(⍳3)
1 2 2 3 3 3

      (2/⍳)3        ⍝ Agh-fork is OK
1 1 2 2 3 3
```
