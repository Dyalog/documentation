---
search:
  exclude: true
---

# <span>Quote Quad</span> `⍞`

`⍞` communicates between an APL expression and the Session or terminal. Referencing it reads characters from there; assigning to it displays characters there.

## Character Input

[`R←⍞`](quotequad-input.md) requests input from standard input and returns the response as a character vector:

```apl
      R←⍞
INPUT
      R
INPUT
```

## Message Output

[`⍞←X`](quotequad-output.md) displays characters on standard error without a trailing new-line, so successive assignments build one line:

```apl
      ⍞←'2+2' ⋄ ⍞←'=' ⋄ ⍞←4
2+2=4
```
