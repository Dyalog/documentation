<div style="display: none;">
  ⍤
</div>

<h1 class="heading"><span class="name">Rank</span> <span class="command">R←{X}(f⍤B)Y</span></h1>

!!! note "Classic Edition"
    The symbol `⍤` is not available in Classic Edition, and the Rank operator is instead represented by `⎕U2364`.

The Rank operator `⍤` applies monadic function `f` successively to sub-arrays of `Y`, or dyadic function `f` between sub-arrays of `X` and `Y`. Sub-arrays are selected by right operand `B`.

`B` is a numeric scalar or vector of up to three items, specifying the ranks of the cells to which `f` should be applied. The most general form is a three item vector `p q r`, where:

- `p` specifies the rank of the argument cells when `f` is applied monadically
- `q` specifies the rank of the left argument cells when `f` is applied dyadically
- `r` specifies the rank of the right argument cells when `f` is applied dyadically

If `B` is a two item vector `q r`, it is implicitly extended to `r q r`. If  `B` has a single item `r`, it is implicitly extended to `r r r`.

If an item `k` of `B` is zero or positive it selects k-cells of the corresponding argument. If it is negative, it selects (r+k)-cells where `r` is the rank of the corresponding argument. A value of `¯1` selects major cells.  For further information, see [Cells and Sub-arrays](../../../programming-reference-guide/introduction/arrays/cells-and-subarrays).

If `X` is omitted, `f` may be any monadic function that returns a result. `Y` may be any array. The Rank operator `⍤` applies function `f` successively to the sub-arrays in `Y` specified by `p` (that is, the first item of `B`, as specified or implicitly extended).

If `X` is specified, it may be any array and `f` may be any dyadic function that returns a result. `Y` may be any array. In this case, the Rank operator applies function `f` successively between the sub-arrays in `X` specified by `q` and the sub-arrays in `Y` specified by `r`.

The sub-arrays of `R` are the results of the individual applications of `f`. If these results differ in rank or shape, they are extended to a common rank and shape in the manner of Mix. See [Mix](../primitive-functions/mix.md).

Notice that it is necessary to prevent the right operand `k` binding to the right argument. This can be done using parentheses, for example, `(f⍤1)Y`. The same can be achieved using  `⊢`, for example, `f⍤1⊢Y` because `⍤` binds tighter to its right operand than `⊢` does to its left argument, and `⊢` therefore resolves to Identity.

## Monadic Examples

Using enclose (`⊂`) as the left operand elucidates the workings of the rank operator.
```apl
      Y
36 99 20  5
63 50 26 10
64 90 68 98
           
66 72 27 74
44  1 46 62
48  9 81 22
      ⍴Y
2 3 4
```
```apl
      ⊂⍤2 ⊢Y
┌───────────┬───────────┐
│36 99 20  5│66 72 27 74│
│63 50 26 10│44  1 46 62│
│64 90 68 98│48  9 81 22│
└───────────┴───────────┘
```
```apl
      ⊂⍤1 ⊢Y
┌───────────┬───────────┬───────────┐
│36 99 20 5 │63 50 26 10│64 90 68 98│
├───────────┼───────────┼───────────┤
│66 72 27 74│44 1 46 62 │48 9 81 22 │
└───────────┴───────────┴───────────┘
```

The function `{(⊂⍋⍵)⌷⍵}` sorts a vector.
```apl
      {(⊂⍋⍵)⌷⍵} 3 1 4 1 5 9 2 6 5
1 1 2 3 4 5 5 6 9
```

The rank operator can be used to apply the function to sub-arrays; in this case to sort the 1-cells (rows) of a 3-dimensional array.
```apl
      Y
36 99 20  5
63 50 26 10
64 90 68 98
           
66 72 27 74
44  1 46 62
48  9 81 22
```
```apl
      ({(⊂⍋⍵)⌷⍵}⍤1)Y
 5 20 36 99
10 26 50 63
64 68 90 98
           
27 66 72 74
 1 44 46 62
 9 22 48 81
```

## Dyadic Examples
```apl

      10 20 30 (+⍤0 1)3 4⍴⍳12
10 11 12 13
24 25 26 27
38 39 40 41
```

Using the function `{⍺ ⍵}`  as the left operand demonstrates how the dyadic case of the rank operator works.
```apl

      10 20 30 ({⍺ ⍵}⍤0 1)3 4⍴⍳12
┌──┬─────────┐
│10│0 1 2 3  │
├──┼─────────┤
│20│4 5 6 7  │
├──┼─────────┤
│30│8 9 10 11│
└──┴─────────┘
```

Note that a right operand of `¯1` applies the function between the major cells (in this case *elements*) of the left argument, and the major cells (in this case *rows*) of the right argument.
```apl

      10 20 30 ({⍺ ⍵}⍤¯1)3 4⍴⍳12
┌──┬─────────┐
│10│0 1 2 3  │
├──┼─────────┤
│20│4 5 6 7  │
├──┼─────────┤
│30│8 9 10 11│
└──┴─────────┘
```
