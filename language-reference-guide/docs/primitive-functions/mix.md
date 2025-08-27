<div style="display: none;">
  ⊃
</div>

<h1 class="heading"><span class="name">Mix</span> <span class="command">(⎕ML) R←↑[K]Y or R←⊃[K]Y</span></h1>

The symbol chosen to represent Mix depends on the current Migration Level.

If `⎕ML<2`, Mix is represented by the symbol: `↑`.

If `⎕ML≥2`, Mix is represented by the symbol: `⊃`.

`Y` may be any array whose items may be uniform in rank and shape, or differ in rank and shape. If the items of `Y` are non-uniform, they are extended prior to the application of the function as follows:

1. If the items of `Y` have different ranks, each item is extended in rank to that of the greatest rank by padding its shape with leading 1s. 
2. If the items of `Y` have different shapes, each is padded with the corresponding prototype to a shape that represents the greatest length along each axis of all items in `Y`.

For the purposes of the following narrative,  `y` represents the virtual item in `Y` with the greatest rank and shape, with which all other items are extended to conform.

`R` is an array composed from the items of  `Y` assembled into a higher-rank array with one less level of nesting. `⍴R` will be some permutation of `(⍴Y),⍴y`.

`K` is an optional axis specification whose value(s)  indicate where in the result the axes of `y` appear. There are three cases:

1. `K` may be a scalar or 1-element vector whose value is a fractional number indicating the two axes of `Y` between which new axes are to be inserted for `y`.  The shape of `R` is the shape of `Y` with the shape `⍴y` inserted between the `⌊K`th and the `⌈K`th axes of `Y`
2. `K` may be a scalar or 1-element vector integer whose value specifies the position of the first axis of `y` in the result. This case is identical to the fractional case where `K` (in this case) is `⌈K` (in the fractional case).
3. `K` may be an integer vector, with the same length as `⍴y`, each element of which specifies the position in the result of the corresponding axis of the `y`. 

If `K` is absent, the axes of `y` appear as the last axes of the result.

## Simple Vector Examples

In this example, the shape of `Y` is 3, and the shape of  `y` is 2. So the shape of the result will be a permutation of 2 and 3, that is, in this simple example, either `(2 3)` or `(3 2`).

If `K` is omitted, the shape of the result is `(⍴Y),⍴y`.
```apl
      ↑(1 2)(3 4)(5 6)
1 2
3 4
5 6
```

If `K` is between 0 and 1, the shape of the result is `(⍴y),⍴Y` because `(⍴y)` is inserted between the 0<sup>th</sup> and the 1<sup>st</sup> axis of the result, that is, at the beginning.
```apl

      ↑[.5](1 2)(3 4)(5 6)
1 3 5
2 4 6
```

If `K` is between 1 and 2, the shape of the result is `(⍴Y),⍴y` because `(⍴y)` is inserted between the 1<sup>st</sup> and 2<sup>nd</sup> axis of the result, that is, at the end. This is the same as the case when `K` is omitted.
```apl

      ↑[1.5](1 2)(3 4)(5 6)
1 2
3 4
5 6
```

An integer `K` may be used instead. If `⎕ML≥2`,  `⊃` is used instead of `↑`).
```apl
      ⎕ML←3
      ⊃(1 2)(3 4)(5 6)
1 2
3 4
5 6
      ⊃[1](1 2)(3 4)(5 6)
1 3 5
2 4 6
      ⊃[2](1 2)(3 4)(5 6)
1 2
3 4
5 6
```

## Shape Extension

If the items of `Y` are unequal in shape, the shorter ones are extended:
```apl
      ⎕ML←3
      ⊃(1)(3 4)(5)
1 0
3 4
5 0
       ⊃[1](1)(3 4)(5)
1 3 5
0 4 0
```

# More Simple Vector Examples
```apl
      ]box on
Was OFF
       'Andy' 'Geoff' 'Pauline'
┌────┬─────┬───────┐
│Andy│Geoff│Pauline│
└────┴─────┴───────┘
      ↑'Andy' 'Geoff' 'Pauline'
Andy   
Geoff  
Pauline

        ⎕ML←3
        ⊃('andy' 19)('geoff' 37)('pauline' 21)
┌───────┬──┐
│andy   │19│
├───────┼──┤
│geoff  │37│
├───────┼──┤
│pauline│21│
└───────┴──┘
        ⊃[1]('andy' 19)('geoff' 37)('pauline' 21)
┌────┬─────┬───────┐
│andy│geoff│pauline│
├────┼─────┼───────┤
│19  │37   │21     │
└────┴─────┴───────┘
        ⊃('andy' 19)('geoff' 37)(⊂'pauline')
┌───────┬───────┐
│andy   │19     │
├───────┼───────┤
│geoff  │37     │
├───────┼───────┤
│pauline│       │
└───────┴───────┘
```

Notice that in the last statement, the shape of the third item was extended by catenating it with its prototype.

### Example (Matrix of Matrices)

In the following examples, `Y` is a matrix of shape `(5 4)` and each item of `Y` (`y`) is a matrix of shape `(3 2)`. The shape of the result will be some permutation of `(5 4 3 2)`.
```apl
       Y←5 4⍴(⍳20)×⊂3 2⍴1
       Y
┌─────┬─────┬─────┬─────┐
│1 1  │2 2  │3 3  │4 4  │
│1 1  │2 2  │3 3  │4 4  │
│1 1  │2 2  │3 3  │4 4  │
├─────┼─────┼─────┼─────┤
│5 5  │6 6  │7 7  │8 8  │
│5 5  │6 6  │7 7  │8 8  │
│5 5  │6 6  │7 7  │8 8  │
├─────┼─────┼─────┼─────┤
│9 9  │10 10│11 11│12 12│
│9 9  │10 10│11 11│12 12│
│9 9  │10 10│11 11│12 12│
├─────┼─────┼─────┼─────┤
│13 13│14 14│15 15│16 16│
│13 13│14 14│15 15│16 16│
│13 13│14 14│15 15│16 16│
├─────┼─────┼─────┼─────┤
│17 17│18 18│19 19│20 20│
│17 17│18 18│19 19│20 20│
│17 17│18 18│19 19│20 20│
└─────┴─────┴─────┴─────┘
```

By default, the axes of `y` appear in the last position in the shape of the result, but this position is altered by specifying the axis `K`. Notice where the `(3 2)` appears in the following results:
```apl
      ⍴⊃Y
5 4 3 2
      ⍴⊃[1]Y
3 2 5 4
      ⍴⊃[2]Y
5 3 2 4
      ⍴⊃[3]Y
5 4 3 2
      ⍴⊃[4]Y
INDEX ERROR
      ⍴⊃[4]Y
     ∧

```

Note that `⊃[4]Y` generates an `INDEX ERROR` because 4 is greater than the length of the result.

### Example (Vector K)

The axes of `y` do not have to be contiguous in the shape of the result. By specifying a vector `K`, they can be distributed. Notice where the `3` and the `2` appear in the following results:
```apl
      ⍴⊃[1 3]Y
3 5 2 4
      ⍴⊃[1 4]Y
3 5 4 2
      ⍴⊃[2 4]Y
5 3 4 2
      ⍴⊃[4 2]Y
5 2 4 3
```

### Rank Extension

If the items of `Y` are unequal in rank, the lower rank items are extended in rank by prefixing their shapes with 1s. Each additional 1 may then be increased to match the maximum shape of the other items along that axis.
```apl
      ⎕ML←3
      Y←(1)(2 3 4 5)(2 3⍴10×⍳8)
      Y
┌─┬───────┬────────┐
│1│2 3 4 5│10 20 30│
│ │       │40 50 60│
└─┴───────┴────────┘
       ⍴⊃Y
3 2 4
       ⊃Y
 1  0  0 0
 0  0  0 0
          
 2  3  4 5
 0  0  0 0
          
10 20 30 0
40 50 60 0
```

In the above example, the first item (1) becomes (`1 1⍴1`) to conform with the 3rd item which is rank 2. It is then extended in shape to become `(2 4↑1 1⍴1)` to conform with the 2-row 3rd item, and 4-column 2nd item.. Likewise, the 2nd item becomes a 2-row matrix, and the 3rd item gains another column.
