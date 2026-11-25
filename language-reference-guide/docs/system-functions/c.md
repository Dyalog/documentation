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

- `1` – characters are [mapped](#mapping) to upper case.
- `¯1` – characters are [mapped](#mapping) to lower case.
- `¯3` – characters are [folded](#folding) for case-insensitive comparison (default).

Any other value signals `DOMAIN ERROR`.

## Right Argument

`Y` is any array. The characters in it are converted at any depth of nesting, and all other data is unchanged. A reference is returned unchanged, without converting anything in the namespace that it refers to.

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

`R` has the same structure and shape as `Y`. Unicode defines both simple case conversions, which convert one character to exactly one character, and full ones, which can convert one character to several, and can depend on the language and on the characters around it. `⎕C` uses only the simple conversions.

## Mapping

Mapping converts characters to upper case or to lower case. A character that has no case, or that is already in that case, is left as it is, and so is a character for which Unicode gives no simple conversion to that case.

<h3 class="example">Examples</h3>

The full upper case of `ß` is `SS`, but `ß` has no simple upper case:

```apl
      1 ⎕C 'Straße'
STRAßE
```

Mapping does not depend on the language. In Turkish, `ı` and `i` are different letters, whose upper cases are `I` and `İ`, but `⎕C` maps both to `I`, and both `I` and `İ` to `i`:

```apl
      1 ⎕C 'ıi'
II
      ¯1 ⎕C 'Iİ'
ii
```

Mapping does not depend on the characters around it either. Greek writes lower-case sigma as `ς` at the end of a word and as `σ` elsewhere, but `⎕C` maps `Σ` to `σ` wherever it is:

```apl
      1 ⎕C 'ίσως'
ΊΣΩΣ
      ¯1 ⎕C 1 ⎕C 'ίσως'
ίσωσ
```

## Folding

Folding converts characters to a form in which they can be compared without regard to case. For most characters, it is the same as mapping them to lower case, but it also converts characters that differ only in how they are written to the same character. The [Unicode FAQ on case mappings](https://unicode.org/faq/casemap_charprop.html) explains the difference between case folding and case mapping.

<h3 class="example">Examples</h3>

Mapping `ίσως` to lower case leaves both of its sigmas as they are, while folding converts both to `σ`:

```apl
      ¯1 ⎕C 'ίσως'
ίσως
      ⎕C 'ίσως'
ίσωσ
```

Applying a function to folded arguments makes it case-insensitive:

```apl
      'pete' 'pete' 'pete' ≡⍥⎕C 'PETE' 'Pete' 'pEte'
1
      'Andy' 'Brian' 'Pete' ⍳⍥⎕C 'ANDY' 'pete'
1 3
      ∪⎕C'Abracadabra'
abrcd
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕C
</div>
