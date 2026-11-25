---
search:
  boost: 2
---

# <span>Case Convert</span> `R←{X}⎕C Y`{{key}}

`⎕C` maps the characters in `Y` to upper case or lower case, or folds them for case-insensitive comparison.

<h2 class="example">Examples</h2>

```apl
      ⎕C 42 'Pete' 'Πέτρος'
┌──┬────┬──────┐
│42│pete│πέτροσ│
└──┴────┴──────┘
      1 ⎕C 42 'Pete' 'Πέτρος'
┌──┬────┬──────┐
│42│PETE│ΠΈΤΡΟΣ│
└──┴────┴──────┘
      ¯1 ⎕C 42 'Pete' 'Πέτρος'
┌──┬────┬──────┐
│42│pete│πέτρος│
└──┴────┴──────┘
```

## Left Argument

`X` is optional, and is one of:

- `1` – characters are mapped to upper case.
- `¯1` – characters are mapped to lower case.
- `¯3` – characters are [folded](#folding) for case-insensitive comparison (default).

Any other value signals `DOMAIN ERROR`.

## Right Argument

`Y` is any array. The characters in it are converted at any depth of nesting, and its numbers are unchanged. A reference is returned unchanged, without converting anything in the namespace that it refers to.

<h3 class="example">Example</h3>

```apl
      ns←()
      ns.Name←'Pete'
      r←⎕C ns
      r≡ns
1
      ns.Name
Pete
```

## Result

`R` has the same structure and shape as `Y`. Unicode defines both simple case conversions, which convert one character to exactly one character, and full ones, which can convert one character to several, and can depend on the characters around it. `⎕C` uses only the simple conversions. For example, the full upper case of `ß` is `SS`, but `ß` has no simple upper case, so `⎕C` leaves it as it is.

<h3 class="example">Example</h3>

```apl
      1 ⎕C 'Straße'
STRAßE
```

## Folding

Folding converts characters to a form in which they can be compared without regard to case. For most characters, it is the same as mapping them to lower case, but it also converts characters that differ only in how they are written to the same character. The [Unicode FAQ on case mappings](https://unicode.org/faq/casemap_charprop.html) explains the difference between case folding and case mapping.

<h3 class="example">Examples</h3>

Greek has two forms of lower-case sigma, `σ` and `ς` (used at the end of a word), but only one upper-case form, `Σ`. Mapping to lower case leaves each lower-case form as it is, while folding converts both to `σ`. Mapping `Σ` to lower case gives `σ`, even at the end of a word:

```apl
      ⎕C 'ίσως'
ίσωσ
      ¯1 ⎕C 'ίσως'
ίσως
      1 ⎕C 'ίσως'
ΊΣΩΣ
      ¯1 ⎕C 1 ⎕C 'ίσως'
ίσωσ
```

Folding both sides of a comparison makes it case-insensitive:

```apl
      (⊂⎕C 'pete')≡¨⎕C 'PETE' 'Pete' 'pEte'
1 1 1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕C
</div>
