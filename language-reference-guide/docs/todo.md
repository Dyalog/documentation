
Found by running the guide's session examples in Dyalog 21.0 in a Linux container, default settings: `⎕IO←1`, `⎕ML←1`, `⎕FR←645`. Links are permalinks to [dyalog/documentation](https://github.com/dyalog/documentation) at `0afe7b461b`. Each one highlights the code block. Under each issue, "Docs show" quotes the source and "Dyalog 21.0 prints" is what the interpreter gives for the same input.

## Wrong in the docs

### 1. Format (Dyadic): wrong value in row 2

[`system-functions/format-dyadic.md:84–90](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/format-dyadic.md:84-L90)

The first column is `⍳4`, so row 2 starts with `2`, not `1`.

Docs show:

```
      '2I4,F7.1' ⎕FMT (⍳4)(2 2⍴ 0.1×⍳4)
   1   0    0.2
   1   0    0.4
   3
   4
```

Dyalog 21.0 prints:

```
      '2I4,F7.1' ⎕FMT (⍳4)(2 2⍴ 0.1×⍳4)
   1   0    0.2
   2   0    0.4
   3
   4
```

### 2. Format (Dyadic): `F5.2` output too wide

[`system-functions/format-dyadic.md:99–104](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/format-dyadic.md:99-L104)

`F5.2` is 5 characters wide. The first row is shown 6 wide, with two leading blanks; the `*****` rows are (correctly) 5.

Docs show:

```
      'F5.2' ⎕FMT 0.1×5 1000 ¯100
  0.50
*****
*****
```

Dyalog 21.0 prints:

```
      'F5.2' ⎕FMT 0.1×5 1000 ¯100
 0.50
*****
*****
```

### 3. Rank: results assume `⎕IO←0`, and the page doesn't say so

- [`primitive-operators/rank.md:92–98](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/rank.md:92-L98)
- [L101–111](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/rank.md:101-L111)
- [L114–124](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/rank.md:114-L124)

All three use `3 4⍴⍳12`, shown as `0 … 11`. With the default `⎕IO←1` it is `1 … 12`. Either say `⎕IO←0`
on the page or update the results.

Docs show:

```
      10 20 30 (+⍤0 1)3 4⍴⍳12
10 11 12 13
24 25 26 27
38 39 40 41

      10 20 30 ({⍺ ⍵}⍤0 1)3 4⍴⍳12
┌──┬─────────┐
│10│0 1 2 3  │
├──┼─────────┤
│20│4 5 6 7  │
├──┼─────────┤
│30│8 9 10 11│
└──┴─────────┘
```

Dyalog 21.0 prints (`⎕IO←1`):

```
      10 20 30 (+⍤0 1)3 4⍴⍳12
11 12 13 14
25 26 27 28
39 40 41 42

      10 20 30 ({⍺ ⍵}⍤0 1)3 4⍴⍳12
┌──┬──────────┐
│10│1 2 3 4   │
├──┼──────────┤
│20│5 6 7 8   │
├──┼──────────┤
│30│9 10 11 12│
└──┴──────────┘
```

The `({⍺ ⍵}⍤¯1)` example at L114 shows the same table and differs the same way.

### 4. Inverted Table Index-of: mixes `⎕IO` settings

- [`primitive-operators/i-beam/inverted-table-index-of.md:14–29](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/i-beam/inverted-table-index-of.md:14-L29)
- [L32–42](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/i-beam/inverted-table-index-of.md:32-L42)
- [L45–72](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/i-beam/inverted-table-index-of.md:45-L72)

`X` and `unvert X` show `⍳10` as `0 1 2 … 9`, which needs `⎕IO←0`. But `Y←(⊂⊂3 1 4 1 5 9)⌷¨X` is shown
as `GHI … tmamli`, which needs `⎕IO←1`. With `⎕IO←0`, `Y` is `JKL … aelees`. The final results
`3 1 4 1 5 9` come out the same under either setting. No single `⎕IO` gives the page as written.

Docs show:

```
      X←(10 3⍴⎕A) (⍳10) 'metalepsis'
      X
┌───┬───────────────────┬──────────┐
│ABC│0 1 2 3 4 5 6 7 8 9│metalepsis│
│DEF│                   │          │
...
      Y←(⊂⊂3 1 4 1 5 9)⌷¨X
      Y
 GHI  3 1 4 1 5 9  tmamli
 ABC
 JKL
 ABC
 MNO
 YZA
```

Dyalog 21.0 prints, with `⎕IO←1`:

```
      X
┌───┬────────────────────┬──────────┐
│ABC│1 2 3 4 5 6 7 8 9 10│metalepsis│
│DEF│                    │          │
...
```

And with `⎕IO←0`:

```
      Y
 JKL  3 1 4 1 5 9  aelees
 DEF
 MNO
 DEF
 PQR
 BCD
```

### 5. Print Width: the folded output is wrong

[`system-functions/pw.md:24–30](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/pw.md:24-L30)

`3⍴÷3` has three values. They fit on one 38-character line, so nothing folds. The docs show a fourth
value on a continuation line. That is the output of `4⍴÷3`, so the input should probably be `4⍴÷3`.

Docs show:

```
      ⎕PW←42

      ⎕←3⍴÷3
0.3333333333 0.3333333333 0.3333333333
      0.3333333333
```

Dyalog 21.0 prints:

```
      ⎕PW←42
      ⎕←3⍴÷3
0.3333333333 0.3333333333 0.3333333333
      ⎕←4⍴÷3
0.3333333333 0.3333333333 0.3333333333
      0.3333333333
```

### 6. Behind: curly quotes in the output

[`primitive-operators/behind.md:75–80](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/behind.md:75-L80)

Dyalog doesn't quote strings in output. The docs show typographic quotes.

Docs show:

```
      ⌽⍛≡¨⍛/ 'racecar' 'racer' 'hanna' 'asa' ⍝ apply filter
‘racecar’ ‘asa’
```

Dyalog 21.0 prints:

```
      ⌽⍛≡¨⍛/ 'racecar' 'racer' 'hanna' 'asa' ⍝ apply filter
 racecar  asa
```

### 7. Unicode Normalisation: mixed box styles

[`primitive-operators/i-beam/unicode-normalisation.md:44–68](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/i-beam/unicode-normalisation.md:44-L68)

The nested results are shown with `]Boxing on -s=max` (`┌→`, `└∊`). The simple results after them are shown
unboxed, which max style doesn't do. Either show every result in max style, or show the block unboxed.

Docs show:

```
      'KD'(5581⌶)'Brand™'
BrandTM
      'BrandTM'≡⍥('KD'∘(5581⌶))'Brand™'
1
```

Dyalog 21.0 prints, under `]Boxing on -s=max` (blank lines around the scalar as printed):

```
      'KD'(5581⌶)'Brand™'
┌→──────┐
│BrandTM│
└───────┘
      'BrandTM'≡⍥('KD'∘(5581⌶))'Brand™'

1

```

### 8. Name Representation: comment text in the output differs from the definition

[`system-functions/nr.md:15–31](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/nr.md:15-L31)

The function is defined with `⍝ Average`, and the `]Display` further down shows `⍝ Average`. But the
`+F←⎕NR'MEAN'` output shows `⍝Average`, without the space.

Docs show:

```
      +F←⎕NR'MEAN'
  R←MEAN X    ⍝Average   R←(+/X)÷⍴X
```

Dyalog 21.0 prints:

```
      +F←⎕NR'MEAN'
  R←MEAN X    ⍝ Average   R←(+/X)÷⍴X
```

## Out of date for Dyalog 21

### `⎕CR`: the output has lost its leading blank

- [`system-functions/cr.md:13–23](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/cr.md:13-L23)
- [`system-functions/cr.md:82–87](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/cr.md:82-L87)

Each row of `⎕CR` starts with a blank, and the docs show the rows without it. This is not a Dyalog 21
change. The page's own `⍴F` is `2 30`, but the header line as shown, `R←MEAN X    ⍝ Arithmetic mean`, is
only 29 characters. The missing column is the leading blank.

The difference is a single space, so here it is with the rows bracketed:

```
      '[',(⎕CR'MEAN'),']'
[ R←MEAN X    ⍝ Arithmetic mean]
[ R←(+/X)÷⍴X                   ]
      ⎕UCS (⎕CR'MEAN')[;1]
32 32
```

Docs show (no blank before `R`):

```
      ⎕CR'AVERAGE'
R←MEAN X    ⍝ Arithmetic mean
R←(+/X)÷⍴X
```

Dyalog 21.0 prints (one blank before `R`):

```
      ⎕CR'AVERAGE'
 R←MEAN X    ⍝ Arithmetic mean
 R←(+/X)÷⍴X
```

### `201⌶` now has 234 tokens, not 207

[`primitive-operators/i-beam/syntax-colour-tokens.md:24–36](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/i-beam/syntax-colour-tokens.md:24-L36)

Docs show:

```
      ⍴201⌶⍬
207 4
```

Dyalog 21.0 prints:

```
      ⍴201⌶⍬
234 4
```

The `3 4↑201⌶⍬` table that follows is unchanged.

### `⎕FIX` now accepts the script shown failing

[`system-functions/fix.md:99–105](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/fix.md:99-L105)

The example is there to show a script error, so it needs a script that still fails in 21.0.

Docs show:

```
      ⎕FIX':Namespace iaK' 'a←1 ⋄ adfn←{' '⍵' ' }' ':EndNamespace'
DOMAIN ERROR: There were errors processing the script
      ⎕FIX':Namespace iaK' 'a←1 ⋄ adfn←{' '⍵' ' }' ':EndNamespace'
      ∧
```

Dyalog 21.0 prints nothing: the namespace is fixed.

```
      ⎕FIX':Namespace iaK' 'a←1 ⋄ adfn←{' '⍵' ' }' ':EndNamespace'
```

### Journaling (`J`) is now on by default

- [`system-functions/fprops.md:61–67](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/fprops.md:61-L67)
- [`system-functions/fprops.md:70–74](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/fprops.md:70-L74)

A new component file reports `J` as 1, so the second example's returned previous value of `J` is 1 too.

Docs show:

```
      tn←'myfile64' ⎕FCREATE 0
      'SEUJ' ⎕FPROPS tn
64 0 1 0

      ('U' 0)('J' 1) ⎕FPROPS tn
1 0
```

Dyalog 21.0 prints:

```
      tn←'myfile64' ⎕FCREATE 0
      'SEUJ' ⎕FPROPS tn
64 0 1 1
      ('U' 0)('J' 1) ⎕FPROPS tn
1 1
```

### `1500⌶`: the hash table is never reported as built, and one output is missing

[`primitive-operators/i-beam/hash-array.md:26–40](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/i-beam/hash-array.md:26-L40)

The docs say that after `{⍵⍳2 3 5}R`, `1 (1500⌶)R` returns `2`, meaning "Y has a hash table". In 21.0 it
still returns `1`, meaning "marked for hashing, but the hash table has not yet been created".

- I also tried `R⍳2 3 5` directly, repeated lookups, and a 1000-element array. None of them made it
  report `2`.
- Both the Linux container and macOS gave `1`.
- I can't tell from outside whether 21.0 builds the hash later or differently, or whether the state
  report has changed. It needs a ruling from the interpreter team.

Separately, `{⍵⍳2 3 5}R` isn't assigned, so it prints `2 3 4`. The docs show nothing after it.

Docs show:

```
      R←1500⌶1 2 3    ⍝ R is marked for hashing

      1 (1500⌶)R
1
      S←R             ⍝ S is marked for hashing
      {⍵⍳2 3 5}R      ⍝ R is now hashed
      1 (1500⌶)R
2
```

Dyalog 21.0 prints:

```
      R←1500⌶1 2 3    ⍝ R is marked for hashing
      1 (1500⌶)R
1
      S←R             ⍝ S is marked for hashing
      {⍵⍳2 3 5}R      ⍝ R is now hashed
2 3 4
      1 (1500⌶)R
1
```

### `⎕R` with `'ResultText' 'Simple'` now appends a line ending

[`system-functions/r.md:455–460](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/r.md:455-L460)

The result now ends with `13 10`. Linux and macOS give the same.

Docs show:

```
      ⎕UCS ('A' ⎕R 'x' ⍠ 'ResultText' 'Simple') 'AB' 'CD'
 120 66 13 10 67 68
```

Dyalog 21.0 prints:

```
      ⎕UCS ('A' ⎕R 'x' ⍠ 'ResultText' 'Simple') 'AB' 'CD'
120 66 13 10 67 68 13 10
```

### Old error display

These examples show errors without the message detail, with `^` (U+005E) instead of the caret character `∧` (U+2227), or with a caret that
points at nothing. Dyalog 21.0 prints the detail after the colon, and `∧` under the failing primitive or
function. The caret positions below come from a script run, so a session may place them slightly
differently. The docs' carets in column 5 are left of the indented line in any case.

- [`system-functions/div.md:20–38](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/div.md:20-L38)

  Docs show:

  ```
        ÷0 1
  DOMAIN ERROR
        ÷0 1
        ^
  ```

  Dyalog 21.0 prints:

  ```
        ÷0 1
  DOMAIN ERROR: Divide by zero
        ÷0 1
        ∧
  ```

- [`system-functions/fr.md:67–72](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/fr.md:67-L72)

  Docs show:

  ```
        ⎕FR←645 ⋄ x+0
  DOMAIN ERROR
  ```

  Dyalog 21.0 prints:

  ```
        ⎕FR←645 ⋄ x+0
  DOMAIN ERROR: ⎕FR=645 limits arithmetic to the range +/-1.79E308 (approx)
        ⎕FR←645 ⋄ x+0
                   ∧
  ```

- [`system-functions/nappend.md:23–40](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/nappend.md:23-L40)

  Docs show:

  ```
        'ταβέρνα'⎕NAPPEND n
  DOMAIN ERROR
        'ταβέρνα'⎕NAPPEND n
       ∧
  ```

  Dyalog 21.0 prints:

  ```
        'ταβέρνα'⎕NAPPEND n
  DOMAIN ERROR: Left argument array could not be converted to the requested type
        'ταβέρνα'⎕NAPPEND n
                 ∧
  ```

- [`system-functions/set-external-variable.md:20–25](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/set-external-variable.md:20-L25)

  The message and the caret's position are right, but the caret is the wrong character. The docs use the
  ASCII circumflex `^` (U+005E); Dyalog marks the error with `∧` (U+2227, the APL "and" symbol). They look
  alike in many fonts. `div.md` above has the same wrong character.

  Docs show:

  ```
        V
  VALUE ERROR
        V
        ^
  ```

  Dyalog 21.0 prints:

  ```
        V
  VALUE ERROR
        V
        ∧
  ```

- `⎕SIGNAL`. The caret sits in column 5, left of the statement.
  - [`system-functions/signal.md:119–126](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/signal.md:119-L126)
  - [`system-functions/signal.md:140–147](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/signal.md:140-L147)

  Docs show:

  ```
        ⎕SIGNAL⊂('EN' 200)
  DOMAIN ERROR: Unexpected name in signalled ⎕DMX specification
        ⎕SIGNAL⊂('EN' 200)
       ∧
  ```

  Dyalog 21.0 prints:

  ```
        ⎕SIGNAL⊂('EN' 200)
  DOMAIN ERROR: Unexpected name in signalled ⎕DMX specification
        ⎕SIGNAL⊂('EN' 200)
        ∧
  ```

### Non-breaking spaces in code

These blocks contain non-breaking spaces (U+00A0), shown below as `⍽`. They appear in the six-space
indent of input lines, and in output where Dyalog prints an ordinary space. Copying such a line into a
session copies the non-breaking spaces too. The output otherwise matches Dyalog 21.0.

- [`primitive-functions/union.md:15–21](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-functions/union.md:15-L21)

  ```
  ⍽⍽⍽⍽⍽ 'WASH' ∪ 'SHOUT'
  WASHOUT
  ⍽
  ⍽⍽⍽⍽⍽ 'ONE' 'TWO' ∪ 'TWO' 'THREE'
   ONE⍽ TWO⍽ THREE
  ```

- [`primitive-functions/without.md:15–23](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-functions/without.md:15-L23)

  ```
  ⍽⍽⍽⍽⍽ 'MONDAY' 'TUESDAY' 'WEDNESDAY'~'TUESDAY' 'FRIDAY'
   MONDAY⍽ WEDNESDAY
  ```

- [`primitive-operators/beside.md:17–21](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/primitive-operators/beside.md:17-L21)

  ```
  ⍽⍽⍽⍽⍽ RANK ← ⍴∘⍴
  ⍽⍽⍽⍽⍽ RANK ¨ 'JOANNE' (2 3⍴⍳6)
   1⍽ 2
  ```

- `system-functions/r.md`:
  - [L42–46](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/r.md:42-L46)
  - [L50–53](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/r.md:50-L53)
  - [L56–59](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/r.md:56-L59)
  - [L269–278](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/r.md:269-L278)

  ```
  ⍽⍽⍽⍽⍽ STR←'The cat sat on the mat'
        ('.at' ⎕S '\u0') STR
  CAT⍽ SAT⍽ MAT
  ⍽⍽⍽⍽⍽ ('.at' ⎕S 0 1) STR
  4 3⍽ 8 3⍽ 19 3
   ⍽⍽⍽⍽ ('$' ⎕R '[Endline]' ⍠ 'Mode' 'M') 'ABC' 'DEF'
   ABC[Endline]⍽ DEF[Endline]
  ```

- [`system-functions/dct.md:22–26](https://github.com/dyalog/documentation/blob/0afe7b461b79de23005cf75557219d1a91a0c9f2/language-reference-guide/docs/system-functions/dct.md:22-L26)

  ```
  ⍽⍽⍽⍽⍽ ⎕DCT←1E¯10
  ⍽⍽⍽⍽⍽ 1.00000000001 1.0000001 = 1
  1 0
  ```

`r.md`, `union.md`, `without.md` and `beside.md` also have non-breaking spaces outside code blocks.
