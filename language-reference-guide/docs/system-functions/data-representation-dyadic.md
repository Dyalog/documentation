---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DR DR
</div>

<h1 class="heading"><span class="name">Data Representation (Dyadic)</span> <span class="command">R←X ⎕DR Y</span></h1>

Dyadic `⎕DR` converts the data type of its argument `Y` according to the type specification `X`. See [Data Representation (Monadic)](data-representation-monadic.md) for a list of data types but note that 1287 is not a permitted value in `X`.

## Case 1

`X` is a single integer value. The bits in the right argument are interpreted as elements of an array of type `X`. The shape of the resulting new array will typically be changed along the last axis. For example, a character array interpreted as Boolean will have 8 times as many elements along the last axis.

## Case 2

`X` is a 2-element integer value. `Y` is any array.

`X[1]` is either 0 or a data type. If `X[1]` is 0, `Y` is converted to data type `X[2]`. If `X[1]` is non-zero, the bits in `Y` are first interpreted as being of type `X[1]` before being converted to type `X[2]`. If `Y` is a scalar it is ravelled. Conversion of `Y` from one internal data type to another is performed so as to preserve its values without loss of precision.

The result `R` is a two element nested array comprised of:

1. The converted elements or a fill element (0 or blank) where the conversion failed
2. A Boolean array of the same shape indicating which elements were successfully converted.

<h2 class="example">Examples</h2>

```apl
      bits← 0 1 0 0 1 0 0 0 , 0 1 0 0 1 0 1 1
      80 ⎕DR bits
HK
      83 ⎕DR bits
72 75
      163 ⎕DR bits
19272

      0 645 ⎕DR 72 75
┌─────┬───┐
│72 75│1 1│
└─────┴───┘
      163 645 ⎕DR 72 75
┌─────┬─┐
│19272│1│
└─────┴─┘

```
## Case 3: Classic Edition Only

`X` is a 3-element integer value and `X[2 3]` is `163 82`. The bits in the right argument are interpreted as elements of an array of type `X[1]`. The system then converts them to the character representation of the corresponding 16 bit integers. This case is provided primarily for compatibility with APL*PLUS. For new applications, the use of the [conv] field with `⎕NAPPEND` and `⎕NREPLACE` is recommended.

Conversion to and from character (data type 82) uses the translate vector given by `⎕NXLATE 0`. By default this is the mapping defined by the current output translate table (usually WIN.DOT).

## Notes

- The internal representation of data may be modified during workspace compaction. For example, numeric arrays and (in the Unicode Edition) character arrays will, if possible, be squeezed to occupy the least possible amount of memory. However, the internal representation of the result `R` is guaranteed to remain unmodified until it is re-assigned (or partially re-assigned) with the result of any function.
- The precise operation of dyadic `⎕DR` depends upon the byte-ordering scheme of the computer system.
