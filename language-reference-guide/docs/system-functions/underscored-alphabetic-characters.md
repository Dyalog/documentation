---
search:
  boost: 2
---

# <span>Underscored Uppercase Alphabet</span> `R←⎕Á`{{key}}

!!! Legacy "Legacy"
    `⎕Á` is deprecated but retained for backwards compatibility. The _Dyalog Box_, _Dyalog Std_, and _Dyalog Std TT_ fonts render it as `⎕Ⓐ` and its content as the underscored uppercase alphabet.

This is a system constant: a simple character vector of 26 consecutive characters of the [atomic vector](av.md), `⎕AV[97+⍳26]`.

Dyalog APL maps the uppercase underscored alphabet to Unicode's circled uppercase alphabet, `⎕UCS 9397+⍳26`. APL fonts such as _APL385 Unicode_ render these as underscored letters <code style="text-decoration:underline;">A</code> to <code style="text-decoration:underline;">Z</code>, while most other fonts render them as <code style="display:inline-block;width:1.4em;height:1.4em;text-align:center;border-radius:50%;outline: 0.1em solid currentColor;outline-offset:-0.3em;margin: -0.2em;">A</code> to <code style="display:inline-block;width:1.4em;height:1.4em;text-align:center;border-radius:50%;outline: 0.1em solid currentColor;outline-offset:-0.3em;margin: -0.2em;">Z</code>.

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
