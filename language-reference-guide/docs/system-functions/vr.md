---
search:
  boost: 2
---

# <span>Vector Representation of Function</span> `R←⎕VR Y`{{key}}

`⎕VR` returns the definition of the function or operator named in `Y` as a single character vector, with line numbers and the lines separated by carriage returns. [`⎕NR`](nr.md) returns it as a vector of lines instead, and [`⎕ATX`](atx.md) can also return it as it was typed.

<h2 class="example">Example</h2>

```apl
      ∇ R←Mean X    ⍝ Arithmetic mean
        R←(+/X)÷≢X
      ∇
      ⎕VR 'Mean'
     ∇ R←Mean X    ⍝ Arithmetic mean
[1]    R←(+/X)÷≢X
     ∇
```

## Right Argument

`Y` is a character scalar or vector that is the name of a function or operator, optionally with its namespace path. An array of higher rank signals `RANK ERROR`.

## Result

If `Y` is the name of a defined function or operator, `R` is a simple character vector of lines, each of which except the last ends with a carriage return (`⎕UCS 13`). The first line is `∇` followed by the header, each line of the definition is normalised and starts with its line number in brackets, and the last line is `∇`.

[`⎕FX`](fx.md) accepts `R`, to define the function or operator again.

If `Y` is the name of a [locked](lock.md) function or operator, an [external function](na.md), a variable, or a namespace, or if it is not defined, `R` is an empty vector.

<h3 class="example">Example</h3>

```apl
      ∇ R←Sign X
        ⍝ The sign of a number
        :If X>0 ⋄ R←1 ⋄ :Else ⋄ R←¯1 ⋄ :EndIf
      ∇
      ⎕VR 'Sign'
     ∇ R←Sign X
[1]   ⍝ The sign of a number
[2]    :If X>0 ⋄ R←1 ⋄ :Else ⋄ R←¯1 ⋄ :EndIf
     ∇
      +/(⎕VR 'Sign')=⎕UCS 13
3
```

## Assigned Functions and Operands

If `Y` is a name to which a function was assigned, or the name of an operand inside a defined operator, `R` represents that function:

- For a primitive function, `R` is a 1-item vector of its symbol.
- For a system function, `R` is a 1-item vector of its name, enclosed.
- For a defined function or operator, `R` is its own representation, whose header has its original name rather than `Y`.
- For a derived function or a train, `R` is a vector of the representations of its parts, in which an array is itself and a primitive is its symbol.

<h3 class="example">Examples</h3>

Continuing with `Mean` from the example above:

```apl
      Plus←+
      ⎕VR 'Plus'
+
      V←⎕VR
      ⎕VR 'V'
┌───┐
│⎕VR│
└───┘
      Avg←Mean∘,
      ⎕VR 'Avg'
┌────────────────────────────────────┬─┬─┐
│     ∇ R←Mean X    ⍝ Arithmetic mean│∘│,│
│[1]    R←(+/X)÷≢X                   │ │ │
│     ∇                              │ │ │
└────────────────────────────────────┴─┴─┘
```

A part that is itself a derived function or a train is represented in the same way, so the nesting of `R` follows the structure of the function. `AHM`, which computes the arithmetic-harmonic mean, is an atop of `⊃` and a derived function whose left operand is a train of two trains:

```apl
      AHM←⊃((+⌿÷≢),≢÷1⊥÷)⍣≡
      AHM 1 2 4
2
      ⎕VR 'AHM'
┌─┬─────────────────────────────┐
│⊃│┌───────────────────────┬─┬─┐│
│ ││┌────────┬─┬──────────┐│⍣│≡││
│ │││┌──┬─┬─┐│,│┌─┬─┬────┐││ │ ││
│ ││││+⌿│÷│≢││ ││≢│÷│1 ⊥÷│││ │ ││
│ │││└──┴─┴─┘│ │└─┴─┴────┘││ │ ││
│ ││└────────┴─┴──────────┘│ │ ││
│ │└───────────────────────┴─┴─┘│
└─┴─────────────────────────────┘
```

Inside the operator `Show`, `F` is the name of its operand:

```apl
      ∇ R←(F Show) Y
        R←⎕VR 'F'
      ∇
      +Show 0
+
      Mean Show 0
     ∇ R←Mean X    ⍝ Arithmetic mean
[1]    R←(+/X)÷≢X
     ∇
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕VR VR
</div>
