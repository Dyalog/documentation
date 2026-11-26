---
search:
  boost: 2
---

# <span>Nested Representation of Function</span> `R←⎕NR Y`{{key}}

`⎕NR` returns the definition of the function or operator named in `Y` as a vector of character vectors, one per line. [`⎕CR`](cr.md) returns it as a character matrix instead, and [`⎕ATX`](atx.md) can also return it as it was typed.

<h2 class="example">Example</h2>

```apl
      ∇ R←Mean X    ⍝ Arithmetic mean
[1]    R←(+/X)÷≢X
      ∇
      ⎕NR 'Mean'
┌──────────────────────────────┬───────────┐
│ R←Mean X    ⍝ Arithmetic mean│ R←(+/X)÷≢X│
└──────────────────────────────┴───────────┘
```

## Right Argument

`Y` is a character scalar or vector that is the name of a function or operator, optionally with its namespace path. An array of higher rank signals `RANK ERROR`.

## Result

If `Y` is the name of a defined function or operator, `R` is a vector of character vectors. Its first item is the header, and each other item is a line of the definition. The lines are normalised, so that they have no unnecessary blanks other than the blanks in comments and the indentation of control structures. Each line starts with a blank, except a label or a line that is only a comment, which starts in the first column.

[`⎕FX`](fx.md) accepts `R`, to define the function or operator again.

If `Y` is the name of a [locked](lock.md) function or operator, an [external function](na.md), a variable, or a namespace, or if it is not defined, `R` is an empty vector.

<h3 class="example">Example</h3>

```apl
      ∇ R←Sign X
[1]   ⍝ The sign of a number
[2]    :If X>0
[3]        R←1
[4]    :Else
[5]        R←¯1
[6]    :EndIf
      ∇
      ⎕NR 'Sign'
┌─────────┬──────────────────────┬────────┬────────┬──────┬─────────┬───────┐
│ R←Sign X│⍝ The sign of a number│ :If X>0│     R←1│ :Else│     R←¯1│ :EndIf│
└─────────┴──────────────────────┴────────┴────────┴──────┴─────────┴───────┘
```

## Assigned Functions and Operands

If `Y` is a name to which a function was assigned, or the name of an operand inside a defined operator, `R` represents that function:

- For a primitive function, `R` is a 1-item vector of its symbol.
- For a system function, `R` is a 1-item vector of its name, enclosed.
- For a defined function or operator, `R` is its own representation, whose header has its original name rather than `Y`.
- For a derived function or a train, `R` is a vector of the representations of its parts, in which an array is itself and a primitive operator is its symbol.

<h3 class="example">Examples</h3>

Continuing with `Mean` from the example above:

```apl
      Plus←+
      ⎕NR 'Plus'
+
      N←⎕NR
      ⎕NR 'N'
┌───┐
│⎕NR│
└───┘
      Avg←Mean∘,
      ⎕NR 'Avg'
┌────────────────────────────────────────────┬─┬─┐
│┌──────────────────────────────┬───────────┐│∘│,│
││ R←Mean X    ⍝ Arithmetic mean│ R←(+/X)÷≢X││ │ │
│└──────────────────────────────┴───────────┘│ │ │
└────────────────────────────────────────────┴─┴─┘
```

Inside the operator `Show`, `F` is the name of its operand:

```apl
      ∇ R←(F Show) Y
[1]    R←⎕NR 'F'
      ∇
      +Show 0
+
      Mean Show 0
┌──────────────────────────────┬───────────┐
│ R←Mean X    ⍝ Arithmetic mean│ R←(+/X)÷≢X│
└──────────────────────────────┴───────────┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NR NR
</div>
