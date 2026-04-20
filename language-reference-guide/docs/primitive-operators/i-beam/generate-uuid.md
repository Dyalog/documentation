---
search:
  boost: 2
---
<h1 class="heading"><span class="name">Generate UUID</span> <span class="command">R←120⌶Y</span></h1>

This function generates a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) (**U**niversally **U**nique **ID**entifier) according to the [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562) specification. In this system, the string representation of each UUID comprises multiple groups of hexadecimal characters separated by single dashes/hyphens.

A UUID is a label that uniquely identifies objects in computer systems; it does not depend on a central registration authority or co-ordination between the parties generating them. UUIDs are also known as GUIDs (**G**lobally **U**nique **ID**entifiers).

`Y` specifies the UUID version required. Supported values of `Y` are:

|`Y`| Version | Generated Hexadecimal Values |
|---|----|---------------------------------------------------------|
| 0 | Nil UUID | All zero                                          |
| 4 | UUIDv4 | Random                                              |
| 7 | UUIDv7 | A combination of (Unix Epoch) time-based and random |

The result `R` is a vector containing the generated 36-character UUID.

<h2 class="example">Example</h2>
```apl
      120⌶4
32cd549f-eb33-4457-bf45-babf26dc2b53

      {⎕←120⌶⍵}¨⍬
00000000-0000-0000-0000-000000000000
```
