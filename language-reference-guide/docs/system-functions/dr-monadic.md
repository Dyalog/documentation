---
search:
  boost: 2
---

# <span>Query Data Representation</span> `R←⎕DR Y`{{key}}

This function returns the internal data type of an array. [Dyadic `⎕DR`](dr-dyadic.md) converts an array to another data type.

<h2 class="example">Example</h2>

```apl
      ⎕DR 1 0 1
11
      ⎕DR 1000
163
      ⎕DR 'abc'
80
```

## Right Argument

`Y` is any array.

## Result

`R` is an integer scalar containing the code of the data type in which `Y` is stored, as listed in [](#data-types). A nested array has the data type `326`.

A data type code is the number of bits per item followed by a digit for the kind of data:

- `0`: Unicode character
- `1`: Boolean
- `2`: Classic character
- `3`: signed integer
- `5`: binary floating-point
- `6`: pointer
- `7`: decimal floating-point
- `9`: complex

For example, `163` is a 16-bit signed integer. The exception is `326`, which identifies a pointer whether the interpreter uses 32-bit or 64-bit pointers.

The internal representation of character data differs between the Unicode and Classic editions, so some data types exist in only one of them.

Table: Data types { #data-types }

|Code |Data type                                       |Edition|
|-----|------------------------------------------------|-------|
|`11` |1-bit Boolean                                   |Both   |
|`80` |8-bit character                                 |Unicode|
|`82` |8-bit character                                 |Classic|
|`83` |8-bit signed integer                            |Both   |
|`160`|16-bit character                                |Unicode|
|`163`|16-bit signed integer                           |Both   |
|`320`|32-bit character                                |Unicode|
|`323`|32-bit signed integer                           |Both   |
|`326`|Pointer (32-bit or 64-bit, as appropriate)      |Both   |
|`645`|64-bit binary floating-point                    |Both   |
|`1287`|128-bit decimal floating-point                 |Both   |
|`1289`|128-bit complex                                |Both   |

## Squeezing

Before it reports the data type, `⎕DR` squeezes `Y` into a smaller internal representation if it can do so without changing the values. The exception is data converted by [dyadic `⎕DR`](dr-dyadic.md), which keeps the internal representation it was converted to until a function that changes it is applied. [`181⌶`](../primitive-operators/i-beam/unsqueezed-type.md) reports the data type in which `Y` is stored, without squeezing it.

<h3 class="example">Example</h3>

```apl
      v←645 ⎕DR 64⍴0
      ⎕DR v
645
      ⎕DR ⍪v
83
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DR DR
</div>
