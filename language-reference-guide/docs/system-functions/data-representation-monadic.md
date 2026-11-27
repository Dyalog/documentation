---
search:
  boost: 2
---

# <span>Data Representation (Monadic)</span> `R←⎕DR Y`{{key}}

Monadic `⎕DR` returns the type of its argument `Y`.  The result `R` is an integer scalar containing one of the following values. The internal representation and data types for character data differ between the Unicode and Classic Editions.

Table: Unicode Edition

|Value|Data Type                                |
|-----|-----------------------------------------|
|11   |1 bit Boolean                            |
|80   |8 bits character                         |
|83   |8 bits signed integer                    |
|160  |16 bits character                        |
|163  |16 bits signed integer                   |
|320  |32 bits character                        |
|323  |32 bits signed  integer                  |
|326  |Pointer (32-bit or 64-bit as appropriate)|
|645  |64 bits Floating                         |
|1287 |128 bits Decimal                         |
|1289 |128 bits Complex                         |

Table: Classic Edition

|Value|Data Type                                 |
|-----|------------------------------------------|
|11   |1 bit Boolean                             |
|82   |8 bits character                          |
|83   |8 bits signed integer                     |
|163  |16 bits signed integer                    |
|323  |32 bits signed integer                    |
|326  |Pointer  (32-bit or 64-bit as appropriate)|
|645  |64 bits Floating                          |
|1287 |128 bits Decimal                          |
|1289 |128 bits Complex                          |

Before it reports the type, `⎕DR` squeezes `Y` into a smaller internal representation if it can do so without changing the values. The exception is data converted by [dyadic `⎕DR`](data-representation-dyadic.md), which keeps the internal representation it was converted to until a function that changes it is applied. [`181⌶`](../primitive-operators/i-beam/unsqueezed-type.md) reports the type in which `Y` is stored, without squeezing it.

<h2 class="example">Example</h2>
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
