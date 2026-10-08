---
search:
  exclude: true
---

# <span>JSON Convert</span> `⎕JSON`

`⎕JSON` converts between APL data and [JavaScript Object Notation](https://www.json.org/json-en.html) (JSON). The left argument chooses the direction.

## Import JSON

[`0 ⎕JSON`](json-import.md) converts a JSON document to APL data:

```apl
      0 ⎕JSON'[1,-2,3]'
1 ¯2 3
```

## Export JSON

[`1 ⎕JSON`](json-export.md) converts APL data to a JSON document:

```apl
      1 ⎕JSON 1 ¯2 3
[1,-2,3]
```

!!! Hint "Hints and Recommendations"
    As a mnemonic, think of the left argument as specifying the desired "JSON-ness": `0` means "no JSON", that is, converting away from JSON; `1` means "yes JSON", that is, converting towards JSON.
