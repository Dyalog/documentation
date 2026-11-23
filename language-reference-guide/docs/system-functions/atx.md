---
search:
  boost: 2
---

# <span>Extended Object Attributes</span> `R←X ⎕ATX Y`{{key}}

`⎕ATX` reports the attributes of the names in `Y` that the attribute codes in `X` select, such as their syntax, the time of their last edit, and their source.

<h2 class="example">Example</h2>

`plus` has an explicit result, is dyadic, and is not an operator:

```apl
      ∇ R←X plus Y
[1]    R←X+Y
      ∇
      10 11 12 ⎕ATX 'plus'
1 2 0
```

## Left Argument

`X` is an integer scalar or vector of the [attribute codes](#attributes) to report. Any other code signals `DOMAIN ERROR`.

## Right Argument

`Y` is one of:

- a character scalar or vector, which is a name.
- an enclosed character vector, which is a name whose attributes are reported enclosed.
- a vector of character vectors and scalars, which are names.

<h3 class="example">Example</h3>

An array that has no name can be given one by applying a dfn to it, in which it is `⍵`. Here, the attribute is the number of bytes that the array takes up, in a 64-bit interpreter:

```apl
      {23 ⎕ATX '⍵'}⍳1000
2032
```

Likewise, a function that has no name can be given one by making it the operand of a dop, in which it is `⍺⍺`. The code of the dop must use `⍺⍺` itself, not only in the name given to `⎕ATX`, or it is a dfn rather than a dop. Here, `⋄ ⍺⍺` does that, although it is never reached:

```apl
      {+/⍵}{30 31 32 ⎕ATX '⍺⍺' ⋄ ⍺⍺}⍬
1 0 1
```

## Result

`R` holds one value for each code in `X` and each name in `Y`:

|`Y`|`X` is a scalar|`X` is a vector|
|---|---------------|---------------|
|A name|The value|A vector of the values, one per code|
|An enclosed name|The value, enclosed|A vector of the values, one per code, enclosed|
|Names|A vector of the values, one per name|A vector with one item per code, each a vector of the values, one per name|

<h3 class="example">Examples</h3>

Continuing with `plus` from the example above:

```apl
      dfn←{⍵ ⍵}
      40 ⎕ATX 'plus'
3
      40 41 ⎕ATX 'plus'
3 1
      40 41 ⎕ATX ⊂'plus'
┌───┐
│3 1│
└───┘
      40 ⎕ATX 'plus' 'dfn'
3 3
      40 41 ⎕ATX 'plus' 'dfn'
┌───┬───┐
│3 3│1 2│
└───┴───┘
```

## Attributes

The attributes are in groups, each of which has a range of codes. Where an attribute does not apply to a name, for example, the author of a variable, `⎕ATX` reports the value in the last column of the group's table.

The examples continue with `plus` and `dfn` from the examples above.

### Identity

|Code|Attribute|
|----|---------|
|`0` |The name |

### Syntax

|Code|Attribute|Where it does not apply|
|----|---------|-----------------------|
|`10`|Whether a function or operator has a result: `1` for an explicit result, `¯1` for a [shy](../../programming-reference-guide/introduction/results.md#shy-results) result, or `0` for no result|`0`|
|`11`|The valence of a function, or of the functions that an operator derives: `0` niladic, `1` monadic, `2` dyadic, or `¯2` ambivalent|`0`|
|`12`|The valence of an operator: `0` not an operator, `1` monadic, or `2` dyadic|`0`|

<h4 class="example">Example</h4>

```apl
      ∇ {R}←Shy Y
[1]    R←Y
      ∇
      op←{⍺⍺ ⍵}
      10 11 12 ⎕ATX 'plus' 'Shy' 'dfn' 'op'
┌────────┬─────────┬───────┐
│1 ¯1 1 1│2 1 ¯2 ¯2│0 0 0 1│
└────────┴─────────┴───────┘
```

### Last Edit

|Code|Attribute|Where it does not apply|
|----|---------|-----------------------|
|`20`|The [account name](an.md) of the user who last edited a tradfn or tradop|`''`|
|`21`|The time of the last edit of a tradfn or tradop, as the number of days, including the fraction of a day, since 1899-12-31 at 00:00 UTC|`¯1`|
|`22`|The local time of the last edit of a tradfn or tradop, as a 7-item vector in the same form as [`⎕TS`](ts.md)|`⍬`|
|`23`|The number of bytes needed to store the value, without any parts that it shares with other arrays|`0`|

[`1 ⎕LOCK`](lock.md) clears the author and the time of the last edit.

<h4 class="example">Example</h4>

```apl
      20 21 22 ⎕ATX 'plus'
┌────┬───────────┬────────────────────┐
│pete│46345.28353│2026 11 20 6 48 17 0│
└────┴───────────┴────────────────────┘
      20 21 22 ⎕ATX 'dfn'
┌┬──┬┐
││¯1││
└┴──┴┘
```

### Restrictions

|Code|Attribute|Where it does not apply|
|----|---------|-----------------------|
|`30`|Whether the source of a function or operator can be displayed: `1` or `0`|`¯1`|
|`31`|Whether execution can be suspended inside a function or operator: `1` or `0`|`¯1`|
|`32`|Whether a function or operator responds to a weak interrupt: `1` or `0`|`¯1`|

`⎕LOCK` prevents displaying the source or suspending execution. Execution cannot be suspended inside a dfn or dop.

<h4 class="example">Example</h4>

```apl
      ∇ R←Hidden
[1]    R←0
      ∇
      1 ⎕LOCK 'Hidden'
      x←42
      30 31 32 ⎕ATX 'plus' 'Hidden' 'dfn' 'x'
┌────────┬────────┬────────┐
│1 0 1 ¯1│1 1 0 ¯1│1 1 1 ¯1│
└────────┴────────┴────────┘
```

### Class

|Code|Attribute|
|----|---------|
|`40`|The syntactic class: `¯1` an invalid name, `0` undefined, `1` a label, `2` a variable, `3` a function, `4` an operator, `8` an event, or `9` an object|
|`41`|The subclass: `0` none, `1` traditional or plain, `2` field, dynamic, or instance, `3` property, derived, or primitive, `4` class, `5` interface, `6` external, or `7` external interface|
|`42`|The full class, which is the class plus a tenth of the subclass, as [`⎕NC`](nc.md) reports it for a vector of names|

!!! Warning "Warning"
    Where these attributes are `¯1`, meaning an invalid name, they might have a different value in a future version of Dyalog, including values that are not currently possible and values that differ from those of `⎕NC`.

<h4 class="example">Example</h4>

```apl
      ns←⎕NS ''
      ↑40 41 42 ⎕ATX 'plus' 'dfn' 'x' 'op' 'ns' 'undefined' '3x'
3   3   2   4   9   0 ¯1
1   2   1   2   1   0  0
3.1 3.2 2.1 4.2 9.1 0 ¯1
```

### Source

|Code|Attribute|Where it does not apply|
|----|---------|-----------------------|
|`50`|The name of the file that the definition was [fixed](fix.md) from|`''`|
|`51`|The [file encoding](nget.md#file-encodings) of that file|`''`|
|`52`|A checksum of that file|`''`|
|`53`|The [line separator](nget.md#Line_Separators) in that file, for example, `10` for a line feed|`⍬`|
|`54`|The number of lines before the definition in its script|`0`|
|`55`|The number of lines in the definition|`0`|

Codes `54` and `55` also apply to a definition that was fixed from a script that is not a file.

<h4 class="example">Example</h4>

`c.apln` is a namespace script, and `range` and `Double` are defined in it:

```apl
      src←':Namespace c' '    range←{⍺↓⍳⍵}' '    ∇ R←Double Y' '      R←2×Y' '    ∇' ':EndNamespace'
      (⊂src)⎕NPUT'c.apln'
      2 ⎕FIX'file://c.apln'
      50 51 52 53 54 55 ⎕ATX 'c'
┌──────┬───────────┬────────┬──┬─┬─┐
│c.apln│UTF-8-NOBOM│f8406927│10│0│6│
└──────┴───────────┴────────┴──┴─┴─┘
      c.(54 55 ⎕ATX 'range' 'Double')
┌───┬───┐
│1 2│1 3│
└───┴───┘
```

### Definition

|Code|Attribute|Where it does not apply|
|----|---------|-----------------------|
|`60`|The source as it was typed|`0⍴⊂''`|
|`61`|The normalised source, as with the configuration parameters **AUTOFORMAT** set to `1` and **TABSTOPS** set to `4`|`0⍴⊂''`|
|`62`|The source as it was typed, or else the normalised source|`0⍴⊂''`|

A dfn or dop that is assigned in the Session has no source as it was typed, so code `60` reports an empty vector for it, and code `62` reports its normalised source.

<h4 class="example">Example</h4>

```apl
      2 ⎕FIX 'foo ← {' '⍵ ⍵ }'
      60 61 62 ⎕ATX 'foo'
┌───────────────┬──────────────────┬───────────────┐
│┌───────┬─────┐│┌──────┬─────────┐│┌───────┬─────┐│
││foo ← {│⍵ ⍵ }│││ foo←{│     ⍵ ⍵}│││foo ← {│⍵ ⍵ }││
│└───────┴─────┘│└──────┴─────────┘│└───────┴─────┘│
└───────────────┴──────────────────┴───────────────┘
      60 61 62 ⎕ATX 'dfn'
┌┬────────────┬────────────┐
││┌──────────┐│┌──────────┐│
│││ dfn←{⍵ ⍵}│││ dfn←{⍵ ⍵}││
││└──────────┘│└──────────┘│
└┴────────────┴────────────┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ATX ATX
</div>
