---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕C
</div>

<h1 class="heading"><span class="name">Case Convert</span> <span class="command">R←{X}⎕C Y</span></h1>

`Y` is any array. `R` is an identical array except that character arrays within it are either folded for case-less comparison, or mapped to upper or lower case.

For a discussion of case folding and case conversion (mapping), see [Character Properties, Case Mappings & Names FAQ](https://unicode.org/faq/casemap_charprop.html).

If the optional left-argument `X` is omitted, `R` is a copy of `Y` with character arrays folded, for case-less comparison.

If `X` is specified, the following cases are supported:

|X   |Description                                                                                                     |
|----|----------------------------------------------------------------------------------------------------------------|
|`1` |`R` is a copy of `Y` with character arrays mapped to upper case.                                                |
|`¯1`|`R` is a copy of `Y` with character arrays mapped to lower case.                                                |
|`¯3`|`R` is a copy of `Y` with character arrays folded, for case-less comparison (this is equivalent to monadic use).|

<h2 class="example">Examples</h2>
```apl

      ⎕C 42 'Pete' 'Πέτρος'
42  pete  πέτροσ 
      1 ⎕C 42 'Pete' 'Πέτρος'
42  PETE  ΠΈΤΡΟΣ 
      ¯1 ⎕C 42 'Pete' 'Πέτρος'
42  pete  πέτρος

      (⊂'pete'){⍺≡⎕C ⍵}¨'PETE' 'Pete' 'pEte'
1 1 1

```

<h2 class="example">Example</h2>


Greek has two forms of lower-case Sigma, namely "σ" and "ς" but a single upper-case Sigma "Σ". Each lower-case form remains unchanged when mapped to lower-case, but both fold to "σ", while "Σ" is mapped to lower-case "σ" .
```apl
      ⎕C 'ίσως'
ίσωσ
      1 ⎕C 'ίσως'
ΊΣΩΣ
      ¯1⎕C 1 ⎕C 'ίσως'
ίσωσ

```

!!! note
    Refs in `Y` are not followed but just returned unchanged.


