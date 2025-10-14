<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕R
</div>

<h1 class="heading"><span class="name">Replace</span> <span class="command">R←{X}(A ⎕R B) Y</span></h1>

`⎕R` (Replace) and `⎕S` (Search) are system operators which take search pattern(s) as their left arguments and transformation rule(s) as their right arguments; the derived function operates on text data to perform either a **search**, or a search and **replace** operation.

The search patterns may include *Regular Expressions* so that complex searches may be performed. `⎕R` and `⎕S` utilise the open-source regular-expression search engine PCRE, which is built into Dyalog APL and distributed according to the [PCRE licence](https://www.pcre.org/original/license.txt).

The transformation rules are applied to the text which matches the search patterns; they may be given as a simple character vector, numeric codes, or  a function.

The two system operators, `⎕R` for replace and `⎕S` for search, are syntactically identical. With `⎕R`, the input document is examined; text which matches the search pattern is amended and the remainder is left unchanged. With `⎕S`, each match in the input document results in an item in the result whose type is dependent on the transformation specified. The operators use the Variant operator to set options.

`A` specifies one or more search patterns, being given as a single character, a character vector, a vector of character vectors or a vector of both characters and character vectors. See search pattern following.

`B` is the transformation to be performed on matches within the input document; it may be either one or more transformation patterns (specified as a character, a character vector, a vector of character vectors, or a vector of both characters and character vectors), one or more transformation codes (specified as a numeric scalar or a numeric vector) or a function; see  transformation pattern, transformation codes and transformation function following.

`Y` specifies the input document; see input document below.

`X` optionally specifies an output stream; see output below.

`R` is the result value; see output below.

## Examples of replace operations
```apl
      ('.at' ⎕R '\u0') 'The cat sat on the mat'     
The CAT SAT on the MAT
```

In the search pattern the dot matches any character, so the pattern as a whole matches sequences of three characters ending 'at'. The transformation is given as a character string, and causes the entire matching text to be folded to upper case.

```apl
      ('\w+' ⎕R {⌽⍵.Match}) 'The cat sat on the mat'
ehT tac tas no eht tam
```

The search pattern matches each word. The transformation is given as a function, which receives a namespace containing various variables describing the match, and it returns the match in reverse, which in turn replaces the matched text.

## Examples of search operations
```apl
      STR←'The cat sat on the mat'
      ('.at' ⎕S '\u0') STR
CAT  SAT  MAT 
```

The example is identical to the first, above, except that after the transformation is applied to the matches the results are returned in a vector, not substituted into the source text.

```apl
      ('.at' ⎕S {⍵.((1↑Offsets),1↑Lengths)}) STR
4 3  8 3  19 3
```

When searching, the result vector need not contain only text and in this example the function returns the numeric position and length of the match given to it; the resultant vector contains these values for each of the three matches.
```apl
      ('.at' ⎕S 0 1) STR       
4 3  8 3  19 3
```

Here the transformation is given as a vector of numeric codes which are a short-hand for the position and length of each match; the overall result is therefore identical to the previous example.

These examples all operate on a simple character vector containing text, but the text may be given in several forms - character vectors, vectors of character vectors, and external data streams. These various forms constitute a 'document'. When the result also takes the form of a document it may be directed to a stream.

## Input Document

The input document may be an array or a data stream.

When it is an array it may be given in one of two forms:

1. A character scalar or vector
2. A vector of character vectors

Currently, the only supported data stream is a native file, specified as tie number, which is read from the current position to the end. If the file is read from the start, and there is a valid Byte Order Mark (BOM) at the start of it, the data encoding is determined by this BOM. Otherwise, data in the file is assumed to be encoded as specified by the InEnc option.

Hint: once a native file has been read to the end by `⎕R` or `⎕S` it is possible to reset the file position to the start so that it may be read again using:
```apl
      {} ⎕NREAD tienum 82 0 0
```

The input document is comprised of lines of text. Line breaks may be included in the data:

Implicitly

- Between each item in the outer vector (type 2, above)

Explicitly, as

- carriage return
- line feed
- carriage return and line feed together, in that order
- vertical tab (U+000B)
- newline (U+0085)
- form Feed (U+000C)
- line Separator (U+2028)
- paragraph Separator (U+2029)

The implicit line ending character may be set using the EOL option. Explicit line ending characters may also be replaced by this character - so that all line endings are normalised - using the NEOL option.

The input document may be processed in **line** mode, **document** mode or **mixed** mode. In document mode and mixed mode, the entire input document, line ending characters included, is passed to the search engine; in line mode the document is split on line endings and passed to the search engine in sections without the line ending characters. The choice of mode affects both memory usage and behaviour, as documented in the section 'Line, document and mixed modes'.

## Output

The format of the output is dependent on whether `⎕S` or `⎕R` are in use, whether an output stream is specified and, for `⎕R`, the form of the input and whether the ResultText option is specified.

An output data stream may optionally be specified. Currently, the only supported data stream is a native file, specified as tie number, and all output will be appended to it. Data in the stream is encoded as specified by the OutEnc option. If this encoding specifies a Byte Order Mark and the file is initially empty then the Byte Order Mark will be written at the start. Appending to existing data using a different encoding is permitted but unlikely to produce desirable results. If an input stream is also used, care must be taken to ensure the input and output streams are not the same.

## `⎕R`

With no output stream specified and unless overridden by the ResultText option, the derived function result will be a document which closely matches the format of the input document, as follows:

A **character scalar or vector** input will result in a **character vector** output. Any and all line endings in the output will be represented by line ending characters within the character vector.

A **vector of character vectors** as input will result in a **vector of character vectors** as document output. Any and all line endings in the output document will be implied at the end of each character vector.

A **stream** as input will result in a **vector of character vectors** document output. Any and all line endings in the output document will be implied at the end of each character vector.

Note that the shape of the output document may be significantly different to that of the input document.

If the ResultText option is specified, the output type may be forced to be a **character vector** or **vector of character vectors** as described above, regardless of the input document.

With an output stream specified the text is appended to the stream. If the appended text does not end with a line ending character then the line ending character specified by the EOL option is also appended. The resulting length of the file  is returned as a shy result.

## `⎕S`

With no output stream specified, the result will be a vector containing one item for each match in the input document, of types determined by the transformation performed on each match.

With an output stream specified each match is appended to the stream. If any match does not end with a line ending character then the line ending character specified by the EOL option is also appended.  The resulting length of the file  is returned as a shy result. Only text may be written to the stream, which means:

- When a transformation function is used, the function may only generate a character vector result.
- Transformation codes may not be used.

## Search pattern

For more information on the syntax of the search pattern, see the [PCRE documentation](../pcre-specifications.md).

There may be multiple search patterns. If more than one search pattern is specified and more than one pattern matches the same part of the input document then priority is given to the pattern specified first.

Note that when anchoring a search to the beginning of a line, it is essential to use `^` (`⎕UCS 94`), not `∧` (`⎕UCS 8743`).

## Transformation pattern

For each match in the input document, the transformation pattern causes the creation of text which, for `⎕R`, replaces the matching text and, for `⎕S`, generates one item in the result.

There may be either one transformation pattern, or the same number of transformation patterns as search patterns. If there are multiple search patterns and multiple transformation patterns then the transformation pattern used corresponds to the search pattern which matched the input text.

Transformation patterns may not be mixed with transformation codes or functions.

The following characters have special meaning:

|Character   |Meaning                                                                                                                      |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
|%           |acts as a placeholder for the entire line (line mode) or document (document mode or mixed mode) which contained the match    |
|&           |acts as a placeholder for the entire portion of text which matched                                                           |
|\n          |represents a line feed character                                                                                             |
|\r          |represents a carriage return                                                                                                 |
|\0          |equivalent to &                                                                                                              |
|\ *n*       |acts as a placeholder for the text which matched the first to ninth subpattern; *n* may be any single digit value from 1 to 9|
|\( *n* )    |acts as a placeholder for the text which matched the numbered subpattern; *n* may have an integer value from 0 to 63.        |
|\< *name* > |acts as a placeholder for the text which matched the named subpattern                                                        |
|\\          |represents the backslash character                                                                                           |
|\%          |represents the percent character                                                                                             |
|\&          |represents the ampersand character                                                                                           |
|\x{ *nnnn* }|represents a Unicode code point; *nnnn* is a hexadecimal sequence of characters yielding a value between 0x1 and 0x10FFFF.   |

The above may be qualified so that matching text is folded, or mapped to upper- or lower-case, by using the **f**, **u**, and **l** modifiers respectively; the effect is as if the text was processed by `⎕C`. See [Case Convert](c.md).

Character sequences beginning with the backslash place the modifier after the backslash; character sequences with no leading backslash add both a backslash and the modifier to the start of the sequence, for example:

|---|----------------------------------------------------------------------------------------|
|\u&|acts as a placeholder for the entire portion of text which matched, folded to upper case|
|\l0|equivalent to \l&                                                                       |

Character sequences beginning with the backslash other that those shown are invalid. All characters other than those shown are literal values and are included in the text without modification.

## Transformation codes

The transformation codes are a numeric scalar or vector. Transformation codes may only be used with `⎕S`. For each match in the input document, a numeric scalar or vector of the same shape as the transformation codes is created, with the codes replaced with values as follows:

|---|------------------------------------------------------------------------------------------------------------------------|
|0  |The offset from the start of the line (line mode) or document (document mode or mixed mode) of the start of the match.  |
|1  |The length of the match.                                                                                                |
|2  |In line mode, the block number in the source document of the start of the match. The value is origin zero. In document mode or mixed mode this value is always zero.|
|3  |The pattern number which matched the input document, origin zero.                                                       |

## Transformation Function

The transformation function is called for each match within the input document.  The function is monadic and is passed a namespace, containing the following variables:

|---|---|
|`Block`|The entire line (line mode) or document (document mode or mixed mode) in which the match was found.|
|`BlockNum`|With line mode, the block (line) number in the source document of the start of the match. The value is origin zero. With document mode or mixed mode the entire document is contained within one block and this value is always zero.|
|`Pattern`|The search pattern which matched.|
|`PatternNum`|The index-zero pattern number which matched.|
|`Match`|The text within Block which matched Pattern.|
|`Offsets`|A vector of one or more offsets relative to the start of Block. The first value is the offset of the entire match; any and all additional values are the offsets of the portions of the text which matched the subpatterns, in the order of the subpatterns within Pattern. `¯1` indicates no match, see below.|
|`Lengths`|A vector of one or more lengths, corresponding to each value in Offset. `¯1` indicates no match, see below.|
|`Names`|A vector of one or more character vectors corresponding to each of the values in Offsets, specifying the names given to the subpatterns within Pattern. The first entry (corresponding to the match) and all subpatterns with no name are included as length zero character vectors.|
|`ReplaceMode`|A Boolean indicating whether the function was called by `⎕R` (value 1) or `⎕S` (value 0).|
|`TextOnly`|A Boolean indicating whether the return value from the function must be a character vector (value 1) or any value (value 0).|

The return value from the function is used as follows:

With `⎕R` the function must return a character vector. The contents of this vector are used to replace the matching text.

With `⎕S` the function may return no value. If it does return a value:

- When output is being directed to a stream it must be a character vector.
- Otherwise, it may be any value. The overall result of the derived function is the catenation of the enclosure of each returned value into a single vector.

The passed namespace exists over the lifetime of `⎕R` or `⎕S`; the function may therefore preserve state by creating variables in the namespace.

The function may itself call `⎕R` or `⎕S`.

There may be only one transformation function, regardless of the number of search patterns.

The locations of the match within Block and subpatterns within Match are given as offsets rather than positions, that is, the values are the number of characters preceding the data, and are not affected by the Index Origin.

The value of `¯1` may appear in both the Offsets and Fields items (in corresponding positions). They indicate that the subpattern to which they refer did not appear in the match at all.

<h2 class="example">Example</h2>
```apl
      {}('(A)|(B)'⎕R{⎕←⍵.(Offsets Lengths)⋄'x'})'ABC'
 0 0  1 1 
 1 ¯1 1  1 ¯1 1 

```

The pattern has two subpatterns - (`A`) and (`B`). Therefore Offsets and Lengths would be expected to have three elements each - one for the entire match, one for the first subpattern and one for the second subpattern. But these subpatterns have a `|` between them which means they are alternates - only one can match.

When `ABC` is searched the first match is the `A` in the first subpattern. The second subpattern does not feature. Offsets is `0 0` and Lengths is `1 1`: the entire pattern matched from offset 0 length 1 and the first subpattern also matched from offset 0 length 1. The second subpattern did not feature in the match.

Note that `¯1` is only used as a "filler" when there are higher-numbered subpatterns that did match.

The second match is the B in the second subpattern. Offsets is `1 ¯1 1` and Lengths is `1 ¯1 1`: the entire pattern matched from offset 1 length 1 and the second subpattern also matched from offset 1 length 1. The first subpattern did not feature in the match and this is indicated by the `¯1`s. There has to be something between the offset/length for the entire pattern and the second subpattern.

## Variant Options

Options are specified using the Variant operator. The Principal option is IC.

Default values are highlighted thus.

### IC Option

When set, case is ignored in searches.

|---|-------------------------------|
|`1`|Matches are not case sensitive.|
|0 { .shaded } |Matches are case sensitive.|

<h2 class="example">Example</h2>
```apl
      ('[AEIOU]' ⎕R 'X' ⍠ 'IC' 1) 'ABCDE abcde'
XBCDX XbcdX
      ('[AEIOU]' ⎕R 'X' ⍠ 1)'ABCDE abcde'
XBCDX XbcdX
```

### Mode Option

Specifies whether the input document is interpreted in **line** mode, **document** mode or **mixed** mode.

|---|---|
|L { .shaded } |When line mode is set, the input document is split into separate lines (discarding the line ending characters themselves), and each line is processed separately. This means that the ML option applies per line, and the '^' and '$' anchors match the start and end respectively of each line. Because the document is split, searches can never match across multiple lines, nor can searches for line ending characters ever succeed. Setting line mode can result in significantly reduced memory requirements compared with the other modes.|
|`D`|When document mode is set, the entire input document is processed as a single block. The ML option applies to this entire block, and the '^' and '$' anchors match the start and end respectively of the block - not the lines within it. Searches can match across lines, and can match line ending characters.|
|`M`|When mixed mode is set, the '^' and '$' anchors match the start and end respectively of each line, as if line mode is set, but in all other respects behaviour is as if document mode is set - the entire input document is processed in a single block.|

<h2 class="example">Examples</h2>
```apl
      ('$' ⎕R '[Endline]' ⍠ 'Mode' 'L') 'ABC' 'DEF'
 ABC[Endline]  DEF[Endline] 
        
      ('$' ⎕R '[Endline]' ⍠ 'Mode' 'D') 'ABC' 'DEF'
 ABC  DEF[Endline]
         
      ('$' ⎕R '[Endline]' ⍠ 'Mode' 'M') 'ABC' 'DEF'
 ABC[Endline]  DEF[Endline]
```

### DotAll Option

Specifies whether the dot ('.') character in search patterns matches line ending characters

|---|-----------------------------------------------------------------------------------|
|0 { .shaded }   |The '.' character in search patterns matches most characters, but not line endings.|
|`1`|The '.' character in search patterns matches all characters.                       |

This option is invalid in line mode, because line endings are stripped from the input document.

<h2 class="example">Example</h2>
```apl
      ('.' ⎕R 'X' ⍠'Mode' 'D') 'ABC' 'DEF'
 XXX  XXX 
      ('.' ⎕R 'X' ⍠('Mode' 'D')('DotAll' 1)) 'ABC' 'DEF'
 XXXXXXXX
```

### EOL Option

Sets the line ending character which is implicitly present between character vectors, when the input document is a vector of character vectors.

|----|-------------------------------------|
|CR  |Carriage Return (U+000D)             |
|LF  |Line Feed (U+000A)                   |
|CRLF { .shaded } |Carriage Return followed by Line Feed|
|VT  |Vertical Tab (U+000B)                |
|NEL |New Line (U+0085)                    |
|FF  |Form Feed (U+000C)                   |
|LS  |Line Separator (U+2028)              |
|PS  |Paragraph Separator (U+2029)         |

In the Classic Edition, setting a value which is not in `⎕AVU` may result in a `TRANSLATION ERROR`.

<h2 class="example">Example</h2>
```apl
      ('\n' ⎕R'X' ⍠('Mode' 'D')('EOL' 'LF')) 'ABC' 'DEF'
 ABCXDEF
```

Here, the implied line ending between 'ABC' and 'DEF' is '\n', not the default '\r\n'.

### NEOL Option

Specifies whether explicit line ending sequences in the input document are normalised by replacing them with the character specified using the EOL option.

|---|--------------------------------|
|0 { .shaded } |Line endings are not normalised.|
|1  |Line endings are normalised.    |

<h2 class="example">Example</h2>
```apl
      a←'ABC',(1↑2↓⎕AV),'DEF',(1↑3↓⎕AV),'GHI'
      ('\n'⎕S 0 ⍠ 'Mode' 'D' ⍠ 'NEOL' 1 ⍠ 'EOL' 'LF') a
3 7
```

'\n' has matched both explicit line ending characters in the input, even though they are different.

### ML Option

Sets a limit to the number of processed pattern matches per line (line mode) or document (document mode and mixed mode).

|--------------------|----------------------------------------|
|Positive value n    |Sets the limit to the first n matches.  |
|0 { .shaded }       |Sets no limit.                          |
|Negative value `¯` n|Sets the limit to exactly the nth match.|

<h2 class="example">Examples</h2>
```apl
      ('.' ⎕R 'x' ⍠ 'ML' 2) 'ABC' 'DEF'
 xxC  xxF 
      ('.' ⎕R 'x' ⍠ 'ML' ¯2) 'ABC' 'DEF'
 AxC  DxF 
      ('.' ⎕R 'x' ⍠ 'ML' ¯4 ⍠ 'Mode' 'D') 'ABC' 'DEF'
 ABC  xEF

```

### Greedy Option

Controls whether patterns are "greedy" (and match the maximum input possible) or are not (and match the minimum). Within the pattern itself it is possible to specify greediness for individual elements of the pattern; this option sets the default.

|---|----------------------|
|1 { .shaded } |Greedy by default.    |
|0  |Not greedy by default.|

<h2 class="example">Examples</h2>
```apl
      ('[A-Z].*[0-9]' ⎕R 'X' ⍠ 'Greedy' 1)'ABC123 DEF456'
X
      ('[A-Z].*[0-9]' ⎕R 'X' ⍠ 'Greedy' 0)'ABC123 DEF456'
X23 X56
```

### OM Option

Specifies whether matches may overlap.

|---|-----------------------------------------------------------------------------------------------------------------------------------------|
|1  |Searching continues for all patterns and then from the character following the *start* of the match, thus permitting overlapping matches.|
|0 { .shaded } |Searching continues from the character following the *end* of the match.                                                                 |

This option may only be used with `⎕S`. With `⎕R` searching always continues from the character following the end of the match (the characters following the start of the match will have been changed).

<h2 class="example">Examples</h2>
```apl
      ('[0-9]+' ⎕S '\0' ⍠ 'OM' 0) 'A 1234 5678 B'
 1234  5678 
      ('[0-9]+' ⎕S '\0' ⍠ 'OM' 1) 'A 1234 5678 B'
 1234  234  34  4  5678  678  78  8

```

### InEnc Option

This option specifies the encoding of the input stream when it cannot be determined automatically. It is either:

- a character vector that specifies the file-encoding as shown in the table below.
- a 256-element numeric vector that maps each possible byte value (0-255) to a  Unicode code point (1st element = Unicode code point corresponding to byte value 0, and so on). ¯1 indicates that the corresponding byte value is not mapped to any character. Apart from ¯1, no value may appear in the table more than once.

When the stream is read from its start, and the start of the stream contains a recognised Byte Order Mark (BOM), the encoding is taken as that specified by the BOM and this option is ignored. Otherwise, the encoding is assumed to be as specified by this option.

|------------|----------------------------------------------------------------------------------------------------------------------------------|
|UTF-8 { .shaded } |The stream is processed as UTF-8 data. Note that ASCII is a subset of UTF-8, so this default is also suitable for ASCII data.     |
|UTF-16      |The stream is processed as UTF16 little-endian data on little-ended systems, or as UTF16 big-endian data on big-endian systems.   |
|UTF-16LE    |The stream is processed as UTF16 little-endian data.                                                                              |
|UTF-16BE    |The stream is processed as UTF16 big-endian data.                                                                                 |
|UTF-32      |The stream is processed as UTF32 little-endian data on little-ended systems, or as UTF32 big-endian data on big-endian systems.   |
|UTF-32LE    |The stream is processed as UTF32 little-endian data.                                                                              |
|UTF-32BE    |The stream is processed as UTF32 big-endian data.                                                                                 |
|ASCII       |The stream is processed as ASCII data. If the stream contains any characters outside of the ASCII range then an error is produced.|
|Windows-1252|The stream is processed as Windows-1252 (ANSI) data.                                                                              |
|ANSI        |Same as Windows-1252                                                                                                              |

For compatibility with the OutEnc option, the above UTF formats may be qualified with -BOM (for example, UTF-8-BOM) or -NOBOM. For input streams, the qualified and unqualified options are equivalent.

### OutEnc Option

When the output is written to a stream, this option specifies how the data is to be encoded.  It is either:

- a character vector that specifies the file-encoding as shown in the table below.
- a 256-element numeric vector that maps each possible byte value (0-255) to a  Unicode code point (1st element = Unicode code point corresponding to byte value 0, and so on). ¯1 indicates that the corresponding byte value is not mapped to any character. Apart from ¯1, no value may appear in the table more than once.

|------------|-------------------------------------------------------------------------------------------------------------------------------|
|Implied { .shaded }  |If input came from a stream then the encoding format is the same as the input stream, otherwise UTF-8                          |
|UTF-8       |The data is written in UTF-8 format.                                                                                           |
|UTF-16      |The data is written in UTF16 little-endian format on little-ended systems, or in UTF16 big-endian format on big-endian systems.|
|UTF-16LE    |The data is written in UTF-16 little-endian format.                                                                            |
|UTF-16BE    |The data is written in UTF-16 big-endian format.                                                                               |
|UTF-32      |The data is written in UTF32 little-endian format on little-ended systems, or in UTF32 big-endian format on big-endian systems.|
|UTF-32LE    |The data is written in UTF-32 little-endian format.                                                                            |
|UTF-32BE    |The data is written in UTF-32 big-endian format.                                                                               |
|ASCII       |The data is written in ASCII format.                                                                                           |
|Windows-1252|The data is written in Windows-1252 (ANSI) format.                                                                             |
|ANSI        |Same as Windows-1252                                                                                                           |

The above UTF formats may be qualified with -BOM (for example, UTF-8-BOM) to specify that a Byte Order Mark should be written at the start of the stream or, -NOBOM that it should not. For files, this is ignored if the file already contains any data.  If the -BOM or -NOBOM suffix is omitted, UTF-8 defaults to UTF-8-NOBOM, while the other UTF formats default to -BOM.

### Enc Option

This option sets both InEnc and OutEnc simultaneously, with the same given value. Any option value accepted by those options except Implied may be given.

### ResultText Option

For `⎕R`, this option determines the format of the result.

|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Implied { .shaded } |The output will either be a **character vector** or **a vector of character vectors** , dependent on the input document type.                   |
|Simple |The output will be a **character vector** . Any and all line endings in the output will be represented by line ending characters within the character vector.|
|Nested |The output will be a **vector of character vectors** . Any and all line endings in the output document will be implied at the end of each character vector.  |

This option may only be used with `⎕R`.

<h2 class="example">Examples</h2>
```apl
      ⎕UCS ¨ ('A' ⎕R 'x') 'AB' 'CD'                
  120 66  67 68                    
      ⎕UCS ('A' ⎕R 'x' ⍠ 'ResultText' 'Simple') 'AB' 'CD'
 120 66 13 10 67 68
```

### UCP Option

This affects the way PCRE that processes \B, \b, \D, \d, \S, \s,  \W,
\w,  and  some  of  the POSIX character classes.

|---|-----------------------------------------------------|
|1  |Unicode  properties are  used to classify characters.|
|0 { .shaded } |Only ASCII characters are recognized.                |

**Implementation Note**: this option is implemented by setting or not setting the PCRE_UCP option when calling pcre_compile(). More information can be found in the PCRE documentation.

<h2 class="example">Examples</h2>

By default, the character ø (which is not an ASCII character) is considered to be a "non-word" character, so:
```apl
      ('\w'⎕S'\0')'Bjørn'  ⍝ identify "word" characters
 B  j  r  n
      ('\W'⎕S'\0')'Bjørn'  ⍝ non-word" characters
 ø
```

When UCP is set to 1, Unicode characters are matched as "word" characters (\w) too.
```apl

      ('\w'⎕S'\0' ⍠'UCP' 1)'Bjørn'
 B  j  ø  r  n
```

### Regex Option

This option may be used to disable regular expression matching which is enabled by default. It is a singleton Boolean value that applies to both search and transformation patterns, or a 2-element vector of Boolean values that applies to them separately.

|---|----------------------------------------|
|1 { .shaded } |Regular expression matching is applied. |
|0  |regular expression matching is disabled.|


<h2 class="example">Examples</h2>
```apl
      STR
The cat sat on the mat

      ('.at' ⎕S '\u0') STR
 CAT  SAT  MAT 
      ('.at' ⎕S '\u0' ⍠('Regex' 0)) STR

      ('.at'⎕R'\u0')STR
The CAT SAT on the MAT
      ('.at'⎕R'\u0'⍠('Regex' (1 0)))STR
The \u0 \u0 on the \u0

```

## Line, document and mixed modes

The Mode setting determines how the input document is packaged as a block and passed to the search engine. In line mode each line is processed separately; in document mode and mixed mode the entire document is presented to the search engine. This affects both the semantics of the search expression, and memory usage.



## Semantic differences

- The ML option applies per block of data.
- In line mode, search patterns cannot be constructed to span multiple lines. Specifically, patterns that include line ending characters (such as '\r') will never match because the line endings are never presented to the search engine.
- By default the search pattern metacharacters '^' and '\$' match the start and end of the block of data. In line mode this is always the start and end of each line. In document mode this is the start and end of the document. In mixed mode the behaviour of '^' and '\$' are amended by setting the PCRE option 'MULTILINE' so that they match the start and end of each line within the document.


## Memory usage differences


Blocks of data passed to the search engine are processed and stored in the workspace. Processing the input document in line mode limits the total memory requirements; in particular this means that large streams can be processed without holding all the data in the workspace at the same time.

## Technical Considerations


`⎕R` and `⎕S` utilise the open-source regular-expression search engine PCRE, which is built into the Dyalog software and distributed according to the PCRE licence which is published separately.


Before data is passed to PCRE it is converted to UTF-8 format. This converted data is buffered in the workspace; processing large documents may have significant memory requirements. In line mode, the data is broken into individual lines and each is processed separately, potentially reducing memory demands.


It is possible to save a workspace with an active `⎕R` or `⎕S` on the stack and execution can continue when the workspace is reloaded with the same interpreter version. Later versions of the interpreter may not remain compatible and may signal a `DOMAIN ERROR` with explanatory message in the status window if it is unable to continue execution.


PCRE has a buffer length limit of 2<sup>31</sup> bytes (2GB). UTF-8 encodes each character using between 1 and 6 bytes (typically 1 or 3). In the very worst case, where every character is encoded in 6 bytes, the maximum block length which can be searched would be 357,913,940 characters.

## Further Examples



Several of the examples use the following vector as the input document:
```apl
      text
To be or not to be- that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
```


Replace all upper and lower-case vowels by `'X'`:
```apl
       ('[aeiou]' ⎕R 'X' ⍠ 'IC' 1) text
TX bX Xr nXt tX bX- thXt Xs thX qXXstXXn:   
WhXthXr 'tXs nXblXr Xn thX mXnd tX sXffXr   
ThX slXngs Xnd XrrXws Xf XXtrXgXXXs fXrtXnX,
Xr tX tXkX Xrms XgXXnst X sXX Xf trXXblXs   
```

Replace only the second vowel on each line by `'\VOWEL\'`:
```apl
       ('[aeiou]' ⎕R '\\VOWEL\\'⍠('IC' 1)('ML' ¯2)) text
To b\VOWEL\ or not to be- that is the question:   
Wheth\VOWEL\r 'tis nobler in the mind to suffer   
The sl\VOWEL\ngs and arrows of outrageous fortune,
Or t\VOWEL\ take arms against a sea of troubles
```

Case fold each word:
```apl
      ('(?<first>\w)(?<remainder>\w*)' ⎕R '\u<first>\l<remainder>') text
To Be Or Not To Be- That Is The Question:   
Whether 'Tis Nobler In The Mind To Suffer   
The Slings And Arrows Of Outrageous Fortune,
Or To Take Arms Against A Sea Of Troubles   
```

Extract only the lines with characters 'or' (in upper or lower case) on them:
```apl
      ↑('or' ⎕S '%' ⍠ ('IC' 1)('ML' 1)) text
To be or not to be– that is the question:   
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles 
```

Identify which lines contain the word 'or' (in upper or lower case) on them:
```apl
      ('\bor\b'⎕S 2⍠('IC' 1)('ML' 1))text
0 3

```

Note the difference between the characters *'or'* (which appear in 'fortune') and the word *'or'*.

Place every non-space sequence of characters in brackets:
```apl
      ('[^\s]+' ⎕R '(&)' ) 'To be or not to be, that is the question'
(To) (be) (or) (not) (to) (be,) (that) (is) (the) (question)
```

Replace all sequences of one or more spaces by newline:

Note that the effect of this is dependent on the input format

Character vector input results in a single character vector output with embedded newlines:

```apl
      ]display ('\s+' ⎕R '\r') 'To be or not to be, that is the question'
┌→───────┐
│To      │
│be      │
│or      │
│not     │
│to      │
│be,     │
│that    │
│is      │
│the     │
│question│
└────────┘
```

A vector of two character vectors as input results in a vector of 10 character vectors output:
```apl
      ]display ('\s+' ⎕R '\r') 'To be or not to be,' 'that is the question'
┌→─────────────────────────────────────────────────────────────┐
│ ┌→─┐ ┌→─┐ ┌→─┐ ┌→──┐ ┌→─┐ ┌→──┐ ┌→───┐ ┌→─┐ ┌→──┐ ┌→───────┐ │
│ │To│ │be│ │or│ │not│ │to│ │be,│ │that│ │is│ │the│ │question│ │
│ └──┘ └──┘ └──┘ └───┘ └──┘ └───┘ └────┘ └──┘ └───┘ └────────┘ │
└∊─────────────────────────────────────────────────────────────┘
```

Change numerals to their expanded names, using a function:
```apl

     ∇r←f a;n
[1]   n←'zero' 'one' 'two' 'three' 'four'
[2]   n,←'five' 'six' 'seven' 'eight' 'nine'
[3]   r←' ',⊃(⍎a.Match)↓n
     ∇
      verbose←('[0-9]' ⎕R f)
      verbose ⍕27×56×87
 one three one five four four
```

Swap 'red' and 'blue':
```apl
      ('red' 'blue' ⎕R 'blue' 'red') 'red hat blue coat'
blue hat red coat
```

Convert a comma separated values (CSV) file so that:

- dates in the first field are converted from European format to ISO, and
- currency values are converted from Deutsche Marks (DEM) to Euros (DEM 1.95583 to €1).

The currency conversion requires the use of a function. Note the nested use of `⎕R`.

Input file:

|--------------------------------------------------------------------------------------------------------------------------------------------|
|`01/03/1980,Widgets,DEM 10.20` `02/04/1980,Bolts,DEM 61.75` `17/06/1980,Nuts; special rate DEM 17.00,DEM 17.00` `18/07/1980,Hammer,DEM 1.25`|

Output file:

|----------------------------------------------------------------------------------------------------------------------------------|
|`1980-03-01,Widgets,€ 5.21` `1980-04-02,Bolts,€ 31.57` `1980-06-17,Nuts; special rate DEM 17.00,€ 8.69` `1980-07-18,Hammer,€ 0.63`|

```apl
     ∇ ret←f a;d;m;y;v
[1]    ⎕IO←0
[2]    :Select a.PatternNum
[3]    :Case 0
[4]        d m y←{a.Match[a.Offsets[⍵+1]+⍳a.Lengths[⍵+1]]}¨⍳3
[5]        ret←y,'-',m,'-',d,','
[6]    :Else
[7]        v←⍎a.Block[a.Offsets[1]+⍳a.Lengths[1]]
[8]        v÷←1.95583
[9]        ret←',€ ',('(\d+\.\d\d).*'⎕R'\1')⍕v
[10]   :EndSelect
     ∇
```
```apl
      in ← 'x.csv' ⎕NTIE 0
      out ← 'new.csv' ⎕NCREATE 0
      dateptn←'(\d{2})/(\d{2})/(\d{4}),'
      valptn←',DEM ([0-9.]+)'
      out (dateptn valptn ⎕R f) in
      ⎕NUNTIE¨in out
```
## Create a simple profanity filter:

For the list of objectionable words
```apl
       profanity←'bleeding' 'heck'
```


first construct a pattern which will match the words:
```apl
      ptn←(('^' '$' '\r\n') ⎕R '\\b(' ')\\b' '|'
                           ⎕OPT 'Mode' 'D') profanity
      ptn
\b(bleeding|heck)\b
```


then a function that uses this pattern:
```apl
      sanitise←ptn ⎕R '****' ⎕OPT 1
      sanitise '"Heck", I said'
"****", I said
```

Replace the characters 'or' with '\u0' without having to escape the backslash:


Escaping transformation strings can be a daunting task. To avoid doing so, one can simply enclose the string in braces. This is not a special feature, but just a consequence of how transformation functions are used.
```apl
      ('to' ⎕R {'\u0'})text
To be or not \u0 be– that is the question:
Whether 'tis nobler in the mind \u0 suffer
The slings and arrows of outrageous fortune,
Or \u0 take arms against a sea of troubles
```


