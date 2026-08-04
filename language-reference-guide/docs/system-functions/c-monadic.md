---
search:
  boost: 2
---

# <span>Case Fold</span> `R←⎕C Y`{{key}}

`Y` is any array. `R` is a copy of `Y` with character arrays folded, for case-less comparison.

For a discussion of case folding and case conversion (mapping), see [Character Properties, Case Mappings & Names FAQ](https://unicode.org/faq/casemap_charprop.html).

<h2 class="example">Examples</h2>
```apl

      ⎕C 42 'Pete' 'Πέτρος'
42  pete  πέτροσ 
      (⊂'pete'){⍺≡⎕C ⍵}¨'PETE' 'Pete' 'pEte'
1 1 1

```

Greek has two forms of lowercase Sigma, namely "σ" and "ς", but a single uppercase Sigma "Σ". Each lowercase form remains unchanged when mapped to lowercase, but both fold to "σ", while "Σ" is mapped to lowercase "σ".
```apl
      ⎕C 'ίσως'
ίσωσ
```

!!! note
    Refs in `Y` are not followed but just returned unchanged.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕C
</div>
