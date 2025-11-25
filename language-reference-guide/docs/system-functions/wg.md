---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WG WG
</div>






<h1 class="heading"><span class="name">Window Get Property</span> <span class="command">R←{X}⎕WG Y</span></h1>



**Windows only.**


This system function returns property values for a GUI object.


`X` is a namespace reference or a character vector containing the name of the object. `Y` is a character vector or a vector of character vectors containing the name(s) of the properties whose values are required. The result `R` contains the current values of the specified properties. If `Y` specifies a single property name, a single property value is returned. If `Y` specifies more than one property, `R` is a vector with one element per name in `Y`.



If `X` refers to a non-existent GUI name, a `VALUE ERROR` is reported. If `Y` refers to a non-existent property, or to a property that is not defined for the type of object `X`, a `DOMAIN ERROR` is reported.


GUI objects are named **relative** to the current namespace. A null value of `X` (referring to the namespace in which the function is being evaluated) may be omitted. The following examples are equivalent:
```apl

      'F1.B1' ⎕WG 'Caption'
      'B1' F1.⎕WG 'Caption'
      '' F1.B1.⎕WG 'Caption'
      F1.B1.⎕WG 'Caption'
```

<h2 class="example">Examples</h2>
```apl

      'F1' ⎕WC 'Form' 'TEST'

      'F1' ⎕WG 'Caption'
TEST

      'F1' ⎕WG 'MaxButton'
1

      'F1' ⎕WG 'Size'
50 50

      ]display 'F1' ⎕WG 'Caption' 'MaxButton' 'Size'
┌→─────────────────┐
│ ┌→───┐   ┌→────┐ │
│ │TEST│ 1 │50 50│ │
│ └────┘   └~────┘ │
└∊─────────────────┘
```


