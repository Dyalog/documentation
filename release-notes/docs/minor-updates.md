# Minor Updates and Bug Fixes

This page describes minor updates and bug fixes included in Dyalog v21.0.

## Stencil

Several issues related to corner-cases of the _stencil_ operator ([`⌺`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/stencil/)) have been fixed. The most significant of these are:

- The left argument to _stencil_'s left operand is now always a vector, never a scalar.
- `{⍵}⌺` and `{⊢⍵}⌺` on a nested vector no longer erroneously disclose elements.
- `{+/⍵}⌺` on a numeric vector now gracefully handles integer overflow.

## JSON Strings

JSON strings must contain valid Unicode characters, that is, characters in the ranges U+0000 to U+D7FF and U+E000 to U+10FFFF. Invalid Unicode characters in character arrays are now replaced by the Unicode Replacement Character U+FFFD when generating a JSON string using `1∘⎕JSON` (and in other places where the interpreter generates JSON).