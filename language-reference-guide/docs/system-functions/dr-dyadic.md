---
search:
  boost: 2
---

# <span>Transform Data Representation</span> `R←X ⎕DR Y`{{key}}

This function converts an array to another internal data type, either by reinterpreting its bits or by converting its values. [Monadic `⎕DR`](dr-monadic.md) reports the data type of an array.

<h2 class="example">Example</h2>

```apl
      bits←0 1 0 0 1 0 0 0,0 1 0 0 1 0 1 1
      80 ⎕DR bits
HK
```

## Left Argument

`X` is one of:

- a single data type, to [reinterpret the bits](#reinterpreting-bits) of `Y`
- a 2-item vector of data types, to [convert the values](#converting-values) of `Y`
- in the Classic Edition only, a 3-item vector, to [represent 16-bit integers as characters](#classic-edition-16-bit-integers-as-characters)

A data type is one of the codes listed for [monadic `⎕DR`](dr-monadic.md#data-types), except `326` (pointer). In the Unicode Edition, `82` is not permitted either.

## Right Argument

`Y` is a simple array.

## Result

`R` depends on the form of `X`, as described in the following sections.

The data in `R` keeps the internal representation that `X` specifies until a function that changes it is applied. Normally, workspace compaction squeezes numeric arrays and (in the Unicode Edition) character arrays into smaller internal representations wherever it can do so without changing their values, and [monadic `⎕DR`](dr-monadic.md#squeezing) squeezes its argument in the same way before it reports the data type; the data in `R` is exempt from both. A function that returns its argument unchanged leaves the exemption in place, and assignment (including indexed assignment) has no effect on it. [`181⌶`](../primitive-operators/i-beam/unsqueezed-type.md) reports the internal representation of an array without squeezing it.

## Reinterpreting Bits

If `X` is a single data type, the bits of `Y` are interpreted as the items of an array of that type. The shape of `R` differs from that of `Y` along the last axis. For example, a character vector interpreted as Boolean has 8 times as many items. The number of bits along the last axis of `Y` must be a multiple of the size of the data type, otherwise `LENGTH ERROR` is signalled.

The result depends on the byte order of the computer system.

<h3 class="example">Examples</h3>

`bits`, defined in the example at the top of this page, holds 16 bits:

```apl
      83 ⎕DR bits
72 75
      163 ⎕DR bits
19272
      11 ⎕DR 'HK'
0 1 0 0 1 0 0 0 0 1 0 0 1 0 1 1
```

## Converting Values

If `X` is a 2-item vector, the values of `Y` are converted from one data type to another:

|Item |Content|
|-----|-------|
|`1⊃X`|`0`, or the data type as which the bits of `Y` are interpreted before they are converted|
|`2⊃X`|The data type to which the values are converted|

If `1⊃X` is `0`, the values of `Y` are converted as they are. The conversion preserves each value without loss of precision; a value that cannot be represented in the target type is not converted. A scalar `Y` is treated as a 1-item vector.

`R` is a 2-item vector:

|Item |Content|
|-----|-------|
|`1⊃R`|The converted values, with a fill item (`0` or a space) in place of each value that could not be converted|
|`2⊃R`|A Boolean array of the same shape, in which `1` indicates a value that was converted|

<h3 class="example">Examples</h3>

```apl
      0 645 ⎕DR 72 75
┌─────┬───┐
│72 75│1 1│
└─────┴───┘
      163 645 ⎕DR 72 75
┌─────┬─┐
│19272│1│
└─────┴─┘
```

Only `1` and `¯7` can be represented as 8-bit signed integers:

```apl
      0 83 ⎕DR 1 300 2.5 ¯7
┌────────┬───────┐
│1 0 0 ¯7│1 0 0 1│
└────────┴───────┘
```

## Classic Edition: 16-bit Integers as Characters

In the Classic Edition, `X` can be a 3-item vector in which `1⊃X` is a data type and `1↓X` is `163 82`. The bits of `Y` are interpreted as an array of type `1⊃X`, and are then converted to the character representation of the corresponding 16-bit integers. This form is provided primarily for compatibility with APL\*PLUS; new applications can use the conversion code of [`⎕NAPPEND`](nappend.md) and [`⎕NREPLACE`](nreplace.md) instead. In the Unicode Edition, a 3-item `X` signals `DOMAIN ERROR`.

In the Classic Edition, conversion to and from character data (data type `82`) uses the translate vector given by [`⎕NXLATE 0`](nxlate.md). By default, this is the mapping defined by the current output translate table (usually `WIN.DOT`).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DR DR
</div>
