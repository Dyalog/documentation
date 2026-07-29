# Model Syntax

A dfn is written as a sequence of one or more statements, separated by newlines or by the diamond (`⋄`) and enclosed in braces (`{}`). A dop takes the same form and additionally refers to its operands. The arguments and operands are referred to by a fixed set of names rather than being declared in a header:

| Name | Refers to |
|------|-----------|
| `⍵` | the right argument |
| `⍺` | the left argument |
| `⍺⍺` | the left operand (dops only) |
| `⍵⍵` | the right operand (dops only) |
| `∇` | the dfn itself, for recursion |
| `∇∇` | the dop itself, for recursion |

These names are described under [Arguments](arguments.md).

In its simplest form a dfn is a single expression:
```apl
      {(+/⍵)÷≢⍵} 1 2 3 4
2.5
```

A dfn is a value like any other function, so it can be named by ordinary assignment or used anonymously:
```apl
      mean←{(+/⍵)÷≢⍵}
      mean 1 2 3 4
2.5
```

A dfn is ambivalent, and its valence is not declared: it follows from whether the body refers to `⍺`, and from whether the dfn is applied with one argument or two. When a dfn that refers to `⍺` is called monadically, `⍺` has no value until a statement beginning `⍺←` supplies a [default left argument](default-left-argument.md). Likewise a dop is a monadic or dyadic operator according to whether it refers to `⍵⍵`.

The layout of a multi-line dfn, and the role of each line, are covered under [Statements](statements.md) and [Multi-line Dfns](multiline-dynamic-functions.md).
