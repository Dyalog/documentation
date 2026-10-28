---
search:
  boost: 2
---

# <span>Underscored Uppercase Alphabet</span> `R←⎕Á`{{key}}

!!! Legacy "Legacy"
    `⎕Á` is retained for backwards compatibility purposes. Dyalog Ltd strongly recommends moving away from `⎕Á` and from the underscored alphabet itself, which is the only remaining non-standard use of characters in Dyalog applications.

This is a system constant: a simple character vector of 26 consecutive characters of the [atomic vector](av.md), `⎕AV[97+⍳26]`. The name stems from legacy functionality; `⎕Á` does not contain the uppercase underscored alphabet, which Dyalog APL maps to Unicode's circled uppercase alphabet, `⎕UCS 9397+⍳26`. APL fonts such as _APL385 Unicode_ render these as underscored letters <u>`A`</u> to <u>`Z`</u>, while most other fonts render them as Ⓐ to Ⓩ.

<h2 class="example">Examples</h2>

```apl
      ⎕Á
ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛÝþãìðòõ
      ⎕UCS 9397+⍳26
ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕Á Á ⎕Ⓐ Ⓐ
</div>
