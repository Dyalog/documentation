<div style="display: none;">
  @
</div>

<h1 class="heading"><span class="name">At</span> <span class="command">R←{X}(f@g)Y</span></h1>

This operator substitutes selected items in `Y` with new values or applies a function to modify selected items in `Y`.

The right operand `g`  identifies which items of array `Y` are to be substituted or modified. It is either:

- an array that specifies a set of indices in `Y`. If `g` is a simple scalar or vector, it selects major cells in `Y`. If nested, it specifies indices for Choose or Reach indexing.
- or a function that when applied to `Y` returns a Boolean array of the same shape as `Y` (a *mask*) in which a 1 indicates that the corresponding item of `Y` is to be substituted or modified. Note that the *ravel* of the mask selects from the *ravel* of the right argument's index array.

The left operand `f` is either:

- an array that contains values to replace those items in `Y` identified by `g`
- or a function to be applied to those items, the result of which is used to replace them. If this function is dyadic, its left argument is the array `X`. Note that the function is applied to the sub-array of `Y` selected by `g` *as a whole* and not to each item separately.

The result `R` is the same as `Y` but with the items specified by `g` substituted or modified by `f`.

## Examples (array @ array)

Replace the 2nd and 4th items of `⍳5`:
```apl
      (10 20@2 4)⍳5   ⍝ [^1]
1 10 3 20 5

      10 20@2 4⍳5
1 10 3 20 5
```

Replace the 2nd and 4th items  of nested vector with `⍬`:
```apl
      (⊂⍬)@2 4 ⍳¨⍳5
┌─┬┬─────┬┬─────────┐
│1││1 2 3││1 2 3 4 5│
└─┴┴─────┴┴─────────┘
```

Replace the 2nd and 4th rows (major cells) of a matrix:
```apl
      (2 3⍴10 20)(@2 4)4 3⍴⍳12
 1  2  3
10 20 10
 7  8  9
20 10 20
```

Replace first and last elements with 0 using Choose Indexing:
```apl
      (0@(1 1)(4 3))4 3⍴⍳12
 0  2 3
 4  5 6
 7  8 9
10 11 0
```
Replace nested items using Reach Indexing:
```apl
       G
┌───────┬───────┬───────┐
│┌───┬─┐│┌───┬─┐│┌───┬─┐│
││ABC│1│││DEF│2│││GHI│3││
│└───┴─┘│└───┴─┘│└───┴─┘│
├───────┼───────┼───────┤
│┌───┬─┐│┌───┬─┐│┌───┬─┐│
││JKL│4│││MNO│5│││PQR│6││
│└───┴─┘│└───┴─┘│└───┴─┘│
└───────┴───────┴───────┘
       G[((1 2)1)((2 3)2)]
┌───┬─┐
│DEF│6│
└───┴─┘
       ('' '*' @((1 2)1)((2 3)2)) G
┌───────┬───────┬───────┐
│┌───┬─┐│┌┬─┐   │┌───┬─┐│
││ABC│1││││2│   ││GHI│3││
│└───┴─┘│└┴─┘   │└───┴─┘│
├───────┼───────┼───────┤
│┌───┬─┐│┌───┬─┐│┌───┬─┐│
││JKL│4│││MNO│5│││PQR│*││
│└───┴─┘│└───┴─┘│└───┴─┘│
└───────┴───────┴───────┘
```

## Examples (function @ array)

Replace the 2nd and 4th items of `⍳5` with their reciprocals:
```apl
      ÷@2 4 ⍳5
1 0.5 3 0.25 5

```

Replace the 2nd and 4th items of `⍳5` with their reversal:
```apl
      ⌽@2 4 ⍳5
1 4 3 2 5
```

Multiply the 2nd and 4th items of `⍳5` by 10:
```apl
      10×@2 4⍳5
1 20 3 40 5
```

Replace the 2nd and 4th items by their totals:
```apl
       +/¨@2 4 ⍳¨⍳5
┌─┬─┬─────┬──┬─────────┐
│1│3│1 2 3│10│1 2 3 4 5│
└─┴─┴─────┴──┴─────────┘
```

Replace the 2nd and 4th rows (major cells) of a matrix with their accumulatives:
```apl
      (+\@2 4)4 3⍴⍳12
 1  2  3
 4  9 15
 7  8  9
10 21 33
```

## Examples (array @ function)

Replace odd elements with 0:
```apl
      0@(2∘|)⍳5
0 2 0 4 0
```

Replace multiples of 3 (note that masked items are substituted in ravel order):
```apl
      'abcde'@{0=3|⍵} 4 4⍴⍳16
 1  2  a  4
 5  b  7  8
 c 10 11  d
13 14  e 16

      'abcde'@(0=3|⊢) 4 4⍴⍳16 ⍝ or using a train
 1  2  a  4
 5  b  7  8
 c 10 11  d
13 14  e 16
```

## Examples (function @ function)

Replace odd elements with their reciprocals:
```apl
      ÷@(2∘|)⍳5
1 2 0.3333333333 4 0.2
```

Replace odd items of `⍳5` with themselves reversed:
```apl
      ⌽@(2∘|)⍳5
5 2 3 4 1

```

[^1]: Note that the expression does not require parentheses because without them, the array 2 4 binds anyway to the @ operator rather than to the ⍳ function.
