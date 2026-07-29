# mapchars

**Classic Edition only.**

In previous versions of Dyalog APL, certain pairs of characters in `⎕AV` were mapped to a single font glyph through the output translate table. For example, the ASCII pipe ¦ and the APL style `|` were both mapped to the APL style `|` . From Version 7.0 onwards, it has been a requirement that the mapping between `⎕AV` and the font is strictly one-to-one (this is a consequence of the new native file system). Originally, the mapping of the ASCII pipe and the APL style, the APL and ASCII quotes, and the ASCII ^ and the APL ^ were hard-coded. The mapping is defined by the **mapchars** parameter.

**mapchars** is a string containing pairs of hexadecimal values which refer to 0-origin indices in `⎕AV` . The first character in each pair is mapped to the second on output. The default value of **mapchars** is `DB0DEBA7EEC00BE0` which defines the following mappings.

|From|||To|||
|---|---|---|---|---|---|
|Hex|Decimal|Symbol|Hex|Decimal|Symbol|
|DB|219|`‘`|0D|13|`'`|
|EB|235|`^`|A7|167|`^`|
|EE|238|`⌷`|C0|192|`|`|
|0B|11|`.`|E0|224|`.`|

To clear all mappings, set `MAPCHARS=0000` .
