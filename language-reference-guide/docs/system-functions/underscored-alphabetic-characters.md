---
search:
  boost: 2
---

# <span>Underscored Uppercase Alphabet</span> `R←⎕Á`{{key}}

!!! Legacy "Legacy"
    `⎕Á` is retained for backwards compatibility purposes. Dyalog Ltd strongly recommends moving away from `⎕Á` and from the underscored alphabet itself, which is the only remaining non-standard use of characters in Dyalog applications.

This is a system constant: a simple character vector of 26 consecutive characters of the [atomic vector](av.md), `⎕AV[97+⍳26]` when `⎕IO` is `0`. Despite its name, `⎕Á` is neither underscored nor entirely uppercase.

The underscored uppercase alphabet itself is `⎕UCS 9333+⎕UCS ⎕A`. Dyalog APL [maps the underscored letters](avu.md) to the Unicode circled letters, which APL fonts such as APL385 Unicode display as underscored letters, and most other fonts as `Ⓐ` to `Ⓩ`.

<h2 class="example">Examples</h2>

```apl
      ⎕Á
ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛÝþãìðòõ
      ⎕UCS 9333+⎕UCS ⎕A
ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕Á Á
</div>
