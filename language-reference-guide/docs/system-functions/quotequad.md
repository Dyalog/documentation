---
search:
  exclude: true
---

# <span>Quote Quad</span> `⍞`

`⍞` communicates between an APL expression and the Session or terminal. Referencing it reads characters from there; assigning to it displays characters there.

## [Character Input](quotequad-input.md)

Referencing `⍞` requests input from standard input and returns the response as a character vector:

```apl
      R←⍞
INPUT
      R
INPUT
```

## [Message Output](quotequad-output.md)

Assigning to `⍞` displays characters on standard error without a trailing new-line, so successive assignments build one line:

```apl
      ⍞←'2+2' ⋄ ⍞←'=' ⋄ ⍞←4
2+2=4
```
