---
search:
  boost: 2
---

# <span>Convert Unicode Code Point</span> `R←⎕UCS Y`{{key}}

This function converts characters to their Unicode code points, and code points to characters. [Dyadic `⎕UCS`](ucs-dyadic.md) converts between characters and their UTF-8, UTF-16, or UTF-32 encodings.

<h2 class="example">Examples</h2>

```apl
      ⎕UCS 'Hello World'
72 101 108 108 111 32 87 111 114 108 100
      ⎕UCS [72 101 108 108 111
            87 111 114 108 100]
Hello
World
```

The code points of the Greek alphabet are in the 900s:

```apl
      ⎕UCS 'καλημέρα'
954 945 955 951 956 941 961 945
```

Unicode also contains the APL characters:

```apl
      ⎕UCS 123 40 43 47 9077 41 247 9076 9077 125
{(+/⍵)÷⍴⍵}
```

## Right Argument

`Y` is a simple array of characters, or of integers from `0` to `1114111`, which is the range of Unicode code points. An array that contains both characters and numbers signals `DOMAIN ERROR`, as does a number that is not a code point.

## Result

`R` has the shape of `Y`. If `Y` is characters, `R` is their code points. If `Y` is code points, `R` is their characters. An empty `Y` gives an empty `R` of the other type.

!!! Info "Information"
    In the Classic Edition, characters are limited to those in [`⎕AV`](av.md). Converting to a character that is not in `⎕AV` signals `TRANSLATION ERROR`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕UCS UCS
</div>
