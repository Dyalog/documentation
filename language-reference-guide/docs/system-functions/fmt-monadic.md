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

`R` is a simple character matrix that appears the same as the [default display](../../programming-reference-guide/introduction/arrays/display-of-arrays.md) of `Y`. Unlike [_format_](../primitive-functions/format.md) (`⍕`), whose result's rank depends on `Y`, `⎕FMT` always returns a matrix.

[`⎕PP`](pp.md) is an implicit argument of `⎕FMT`.

<h3 class="example">Example</h3>

```apl
      ⎕PP←3
      ⎕FMT ÷3
0.333
```

## Control Characters

`⎕FMT` resolves four control characters in the character data of `Y`:

|Character|Effect|
|---------|------|
|`⎕UCS 8` (backspace)|Moves back one position, so that the next character replaces the one there, or, if the two form an APL overstrike symbol, combines with it; at the start of a row, it has no effect|
|`⎕UCS 10` (line feed)|Moves down to a new row, keeping the same position in the row|
|`⎕UCS 13` (carriage return)|Starts a new row|
|`⎕UCS 133` (next line)|Starts a new row|

Other control characters, such as tab (`⎕UCS 9`), are left unchanged in the result.

<h3 class="example">Examples</h3>

```apl
      A←⎕FMT '∩',(⎕UCS 8),'∘'
      ⍴A
1 1
      A
⍝
      ⎕FMT 'ab',(⎕UCS 10),'cd'
ab
  cd
```

The result of [`⎕VR`](vr.md) separates its lines with carriage returns, so `⎕FMT` turns it into a matrix with one row per line:

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
