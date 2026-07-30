---
search:
  boost: 2
---

# <span>Convert Unicode Code Point</span> `R←⎕UCS Y`{{key}}

`⎕UCS` converts (Unicode) characters into integers and vice versa.

`Y` is a simple character or integer array, and the result `R` is a simple integer or character array with the same rank and shape as `Y`.

Monadic `⎕UCS` converts any character array to a numeric array of the same shape, or any numeric array to a character array of the same shape. When doing this, characters are converted to Unicode code points and Unicode code points are converted to characters.

```apl

      ⎕UCS 'Hello World'
72 101 108 108 111 32 87 111 114 108 100

      ⎕UCS 2 11⍴72 101 108 108 111 32 87 111 114 108 100
Hello World
Hello World
```

The code points for the Greek alphabet are situated in the 900's:
```apl

      ⎕UCS 'καλημέρα'
954 945 955 951 956 941 961 945

```

Unicode also contains the APL character set. For example:
```apl

      ⎕UCS 123 40 43 47 9077 41 247 9076 9077 125
{(+/⍵)÷⍴⍵}

```

## Translation Error

`⎕UCS` will generate a `DOMAIN ERROR` if the argument cannot be converted. Additionally, in the Classic Edition, a `TRANSLATION ERROR` is generated if the result is not in `⎕AV` or the numeric argument is not in `⎕AVU`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕UCS UCS
</div>
