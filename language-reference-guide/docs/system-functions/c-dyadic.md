---
search:
  boost: 2
---

# <span>Case Map</span> `R←X ⎕C Y`{{key}}

`Y` is any array. `R` is an identical array except that character arrays within it are either folded for case-less comparison, or mapped to upper- or lowercase.

For a discussion of case folding and case conversion (mapping), see [Character Properties, Case Mappings & Names FAQ](https://unicode.org/faq/casemap_charprop.html).

The following cases are supported:

|X|Description|
|---|---|
|`1`|`R` is a copy of `Y` with character arrays mapped to uppercase.|
|`¯1`|`R` is a copy of `Y` with character arrays mapped to lowercase.|
|`¯3`|`R` is a copy of `Y` with character arrays folded, for case-less comparison (this is equivalent to monadic [`⎕C`](c-monadic.md)).|

<h2 class="example">Examples</h2>
```apl

      1 ⎕C 42 'Pete' 'Πέτρος'
42  PETE  ΠΈΤΡΟΣ 
      ¯1 ⎕C 42 'Pete' 'Πέτρος'
42  pete  πέτρος

```

Greek has two forms of lowercase Sigma, namely "σ" and "ς", but a single uppercase Sigma "Σ". Each lowercase form remains unchanged when mapped to lowercase, but both map to uppercase "Σ".
```apl
      1 ⎕C 'ίσως'
ΊΣΩΣ
      ¯1⎕C 1 ⎕C 'ίσως'
ίσως

```

!!! note
    Refs in `Y` are not followed but just returned unchanged.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕C
</div>
