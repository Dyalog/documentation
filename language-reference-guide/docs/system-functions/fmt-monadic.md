---
search:
  boost: 2
---

# <span>Resolve Display Format</span> `R←⎕FMT Y`{{key}}

This function returns the display of an array as a character matrix, resolving any control characters. [Dyadic `⎕FMT`](fmt-dyadic.md) formats numbers and text according to a format specification instead.

<h2 class="example">Example</h2>

```apl
      ⍴⎕FMT 2 4⍴⍳8
2 7
```

## Right Argument

`Y` is any array.

## Result

`R` is a simple character matrix that appears the same as the [default display](../../programming-reference-guide/introduction/arrays/display-of-arrays.md) of `Y`. Unlike [_format_](../primitive-functions/format.md) (`⍕`), whose result has the rank of `Y`, or rank 1 if `Y` is a scalar, `⎕FMT` always returns a matrix.

[`⎕PP`](pp.md) is an implicit argument of `⎕FMT`.

<h3 class="example">Example</h3>

```apl
      ⎕PP←3
      ⎕FMT ÷3
0.333
```

## Control Characters

If `Y` contains control characters from [`⎕TC`](tc.md), `⎕FMT` resolves them. After a backspace (`⎕TC[1]`), the next character replaces the one before the backspace, or, if the two form an APL overstrike symbol, combines with it:

```apl
      A←⎕FMT '∩',⎕TC[1],'∘'
      ⍴A
1 1
      A
⍝
```

A line ending starts a new row, so a character vector of several lines, such as the result of [`⎕VR`](vr.md), becomes a matrix with one row per line:

```apl
      ⎕FX 'R←FOO' 'R←10'
      A←⎕VR 'FOO'
      ⍴A
31
      B←⎕FMT A
      B
     ∇ R←FOO
[1]    R←10
     ∇
      ⍴B
3 12
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FMT FMT
</div>
