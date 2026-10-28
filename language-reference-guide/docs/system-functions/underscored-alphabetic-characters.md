---
search:
  boost: 2
---

# <span>Underscored Uppercase Alphabet</span> `R←⎕Á`{{key}}

!!! Legacy "Legacy"
    `⎕Á` is retained for backwards compatibility purposes. The _Dyalog Box_, _Dyalog Std_, and _Dyalog Std TT_ fonts render it as `⎕Ⓐ` and its content as the underscored uppercase alphabet. Dyalog Ltd strongly recommends moving away from `⎕Á`.

This is a system constant: a simple character vector of 26 consecutive characters of the [atomic vector](av.md), `⎕AV[97+⍳26]`.

Dyalog APL maps the uppercase underscored alphabet to Unicode's circled uppercase alphabet, `⎕UCS 9397+⍳26`. APL fonts such as _APL385 Unicode_ render these as underscored letters <u>`A`</u> to <u>`Z`</u>, while most other fonts render them as <span style="display:inline-block;width:1.6em;height:1.6em;line-height:1.6em;text-align:center;border:0.08em solid currentColor;border-radius:50%">`A`</span> to <span style="display:inline-block;width:1.6em;height:1.6em;line-height:1.6em;text-align:center;border:0.08em solid currentColor;border-radius:50%">`Z`</span>.

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
