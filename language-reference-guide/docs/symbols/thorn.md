---
search:
  exclude: true
---





<h1 class="heading"><span class="name">Thorn</span> <span class="command">⍕</span></h1>


Monadic Thorn means


[Format](../primitive-functions/format.md)
```apl

NB: In the following examples space characters
    are represented by small dots: ···

      4 5 6          ⍝ numeric vector
4 5 6
      ⍕ 4 5 6        ⍝ equivalent character vector
4·5·6
      
      mat            ⍝ numeric matrix
1 2 3
4 5 6

      ⍕ mat          ⍝ equivalent character matrix
1·2·3
4·5·6
```


N.B. depends on `⎕PP`

Dyadic Thorn means


[Format By Specification](../primitive-functions/format-by-Specification.md)
```apl

Field-width and number of decimal places:

      6 2 ⍕ 3.125 0.002
··3.13··0.00

      6 2 ⍕ mat
··1.00··2.00··3.00
··4.00··5.00··6.00

      6 2 ⍕ 1234   ⍝ (field not wide enough)
******

```
[Language Elements](../glyphs.md)


