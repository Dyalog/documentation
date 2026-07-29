# Arguments and Operands

Within a dfn the arguments are referred to by fixed names, not declared in a header.

- `⍵` is the right argument, and is always available.
- `⍺` is the left argument. A dfn is ambivalent: when it is called monadically, `⍺` has no value until a statement beginning `⍺←` supplies a [default left argument](default-left-argument.md).

<h2 class="example">Examples</h2>
```apl
      {⍵} 5             ⍝ right argument
5
      2 {⍺,⍵} 5         ⍝ both arguments
2 5
```

A dop refers to its operands:

- `⍺⍺` is the left operand.
- `⍵⍵` is the right operand, present only in a dyadic operator.

An operand can be a function or an array.

<h2 class="example">Example</h2>
```apl
      -{⍺⍺ ⍵} 5         ⍝ ⍺⍺ is the operand function, here Negate
¯5
```

A dfn refers to itself as `∇`, and a dop as `∇∇`, which allows recursion without naming the operation (see [Recursion](recursion.md)).

<h2 class="example">Example</h2>
```apl
      {⍵≤1: 1 ⋄ ⍵×∇ ⍵-1} 5    ⍝ factorial by self-reference
120
```
