<h1 class="heading"><span class="name"> Operators Summarised</span></h1>

[](#MonadicOperators) and [](#DyadicOperators) below summarise the Monadic and Dyadic primitive operators whose detailed descriptions  follow in alphabetical order in this section.

Some operators may include an axis specification (indicated `[]`in the tables). Note that in these case `⎕IO` is an implicit argument of the derived function.

Table: Monadic Primitive Operators {: #MonadicOperators }

|Name                           |Producing Monadic derived function|Producing Dyadic derived function|
|-------------------------------|----------------------------------|---------------------------------|
|Assignment (Modified)          |&nbsp;                            |`Xf←Y`                           |
|Assignment (Indexed Modified)  |&nbsp;                            |`X[I]f←Y`                        |
|Assignment (Selective Modified)|&nbsp;                            |`(EXP X)f←Y`                     |
|Commute                        |`f⍨Y`                             |`Xf⍨Y`                           |
|Each                           |`f¨Y`                             |`Xf¨Y`                           |
|I-Beam                         |`A⌶Y`                             |`X(A⌶)Y`                         |
|Key                            |`f⌸Y`                             |`Xf⌸Y`                           |
|Reduction                      |`f/Y  [ ]`                        |`Xf/Y [ ]`                       |
|Reduction First                |`f⌿Y  [ ]`                        |`Xf⌿Y [ ]`                       |
|Scan                           |`f\Y  [ ]`                        |&nbsp;                           |
|Scan First                     |`f⍀Y  [ ]`                        |&nbsp;                           |
|Spawn                          |`f&Y`                             |`Xf&Y`                           |

Table: Dyadic Primitive Operators {: #DyadicOperators }

| Name         |Producing Monadic derived function| Producing Dyadic derived function |
|--------------|----------------------------------|-----------------------------------|
| At           |`f@gY`                            | `Xf@gY`                           |
| Atop         |`f⍤gY`                            | `Xf⍤gY`                           |
| Axis         |`f[B]Y`                           | `Xf[B]Y`                          |
| Behind       |`f⍛gY`                            | `Xf⍛gY`                           |
| Beside       |`f∘gY`                            | `Xf∘gY`                           |
| Bind         |`A∘gY`                            | &nbsp;                            |
|_            _|`(f∘B)Y`                          | &nbsp;                            |
| Constant     |`(A⍨)Y`                           | `X(A⍨)Y`                          |
| Inner Product |&nbsp;                            | `Xf.gY`                           |
| Outer Product |&nbsp;                            | `X∘.gY`                           |
| Over         |`f⍥gY`                            | `Xf⍥gY`                           |
| Power        |`f⍣gY`                            | `Xf⍣gY`                           |
| Rank         |`f⍤kY`                            | `Xf⍤kY`                           |
| Stencil      |`f⌺gY`                            | &nbsp;                            |
| Variant      |`f⍠gY`                            | `Xf⍠gY`                           |
