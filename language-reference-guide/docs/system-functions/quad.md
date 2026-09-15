---
search:
  exclude: true
---

# <span>Quad</span> `⎕`

`⎕` communicates between an APL expression and the Session or terminal. Referencing it reads a value from there; assigning to it displays a value there.

## [Evaluated Input](quad-input.md)

Referencing `⎕` prompts for an expression, evaluates it, and returns the result:

```apl
      10×⎕+2
⎕:
      ⍳3
30 40 50
```

## [Standard Output](quad-output.md)

Assigning to `⎕` displays the array in the same form as implicit output, on standard output:

```apl
      ⎕←2 4⍴'WINEMART'
WINE
MART
```
