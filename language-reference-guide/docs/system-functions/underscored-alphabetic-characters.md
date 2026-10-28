---
search:
  boost: 2
---

# <span>Underscored Uppercase Alphabet</span> `R←⎕Á`{{key}}

!!! Legacy "Legacy"
    `⎕Á` is retained for backwards compatibility purposes. Dyalog Ltd strongly recommends moving away from `⎕Á` and from the underscored alphabet itself, which is the only remaining non-standard use of characters in Dyalog applications.

This is a system constant: a simple character vector of 26 consecutive characters of the [atomic vector](av.md), `⎕AV[97+⍳26]` when `⎕IO` is `0`. Despite the name, they are not all uppercase letters: the last six are lowercase.

<h2 class="example">Example</h2>

```apl
      ⎕Á
ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛÝþãìðòõ
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕Á Á
</div>
