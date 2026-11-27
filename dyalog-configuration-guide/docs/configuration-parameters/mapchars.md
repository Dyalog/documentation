# mapchars

!!! Info "Information"
    This configuration parameter is only relevant when using the Classic edition of Dyalog.

The mapping between `⎕AV` and the font must be strictly one-to-one. Historically a few pairs of `⎕AV` characters were mapped to a single font glyph (for example the ASCII pipe `¦` and the APL style `|`); **mapchars** defines any such mappings.

**mapchars** is a string of pairs of hexadecimal values, each an origin-`0` index into `⎕AV`. The first character of each pair is mapped to the second on output.

The default is `DB0DEBA7EEC00BE0`, which defines the following mappings:

| From (hex) | From (decimal) | From | To (hex) | To (decimal) | To |
|---|---|---|---|---|---|
| DB | 219 | `‘` | 0D | 13 | `'` |
| EB | 235 | `^` | A7 | 167 | `^` |
| EE | 238 | `⌷` | C0 | 192 | `\|` |
| 0B | 11 | `.` | E0 | 224 | `.` |

To clear all mappings, set `mapchars=0000`.
