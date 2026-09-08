# Minor Updates and Bug Fixes

This page describes minor updates and bug fixes included in Dyalog v21.0.

## Stencil

Several issues related to corner-cases of the _stencil_ operator ([`⌺`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/stencil/)) have been fixed. The most significant of these are:

- The left argument to _stencil_'s left operand is now always a vector, never a scalar.
- `{⍵}⌺` and `{⊢⍵}⌺` on a nested vector no longer erroneously disclose elements.
- `{+/⍵}⌺` on a numeric vector now gracefully handles integer overflow.

## JSON Stings

JSON strings must only contain valid Unicode characters, that is, characters in the Unicode ranges U+0000-U+D7FF and U+E000-U+10FFFF. If a character array contains an invalid Unicode character, it is now replaced by the Unicode replacement character U+FFFD when generating a JSON string using `1∘⎕JSON` (and in other places where the interpreter generates JSON).