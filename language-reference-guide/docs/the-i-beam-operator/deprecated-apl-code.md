<h1 class="heading"><span class="name">Deprecated APL Code</span> <span class="command">{R}←{X}14⌶Y</span></h1>

Indicates that APL code is deprecated so that its use will be recorded when logging of 'User' deprecated features is enabled.

For an overview of deprecated features see  [Deprecated features](../../../../programming-reference-guide/deprecated-features) within the Programming Reference Guide.

`Y` is the description of the feature which will appear in the log entry - either a character vector containing appropriate text, or ⍬ for a generic message.

`X` is an optional additional text which will appear as the ExtraInfo field within the log entry.

The shy result `R` is a Boolean value which indicates whether warnings for the 'User' deprecated feature are enabled.

<h2 class="example">Example</h2>

```apl
      my_obsolete_fn←{_←14⌶⍬ ⋄ ⍺+⍵}
      'deprecated.txt'(109⌶)0
      13⌶'User'
      1 my_obsolete_fn 2
3
      (⎕JSON⍠('Dialect' 'JSON5')('Compact' 0))⍣¨2⊃⎕NGET'deprecated.txt' 1
{
  ExtraInfo: "",
  Feature: "Use of deprecated application code",
  Message: "Use of deprecated feature",
  Stack: [
    "#.my_obsolete_fn{ Single-Line Dfn }",
  ],
  TS: "2025-02-11 14:55:05",
  Type: "Warning",
  WSID: "CLEAR WS",
}
```

See also [Deprecated Features](deprecated-features.md), [Log File for Deprecations](log-file-for-deprecations.md).