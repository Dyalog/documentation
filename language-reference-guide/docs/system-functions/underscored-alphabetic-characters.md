---
search:
  boost: 2
---

# <span>Underscored Uppercase Alphabet</span> `R←⎕Á`{{key}}

!!! Legacy "Legacy"
    `⎕Á` is retained for backwards compatibility purposes. Dyalog Ltd strongly recommends moving away from `⎕Á` and from the underscored alphabet itself, which is the only remaining non-standard use of characters in Dyalog applications.

This is a system constant: a simple character vector of the 26 characters at the positions in the [atomic vector](av.md) that held the underscored letters `Ⓐ` to `Ⓩ` before version 11.0. A function that refers to `⎕Á`, therefore, gets characters with the same indices in `⎕AV` as before. Despite the name, they are not all uppercase letters: the last six are lowercase.

<h2 class="example">Example</h2>

```apl
      ⎕Á
ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛÝþãìðòõ
```

Before version 11.0, the name was displayed as `⎕Ⓐ`, and its value as `ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ`, or as the characters above if the Dyalog Alt font was in use. In Unicode editions, `⎕Ⓐ` is not a valid name and gives `SYNTAX ERROR`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕Á ⎕Ⓐ Á Ⓐ
</div>
