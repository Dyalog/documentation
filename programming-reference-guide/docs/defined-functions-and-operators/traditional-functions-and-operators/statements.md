# Statements

A statement is a line of characters understood by APL.  It may be composed of:

1. a LABEL (which must be followed by a colon `:`), or a CONTROL STATEMENT (which is preceded by a colon), or both, 
2. an EXPRESSION (see [Expressions](../../introduction/expressions.md)),
3. a SEPARATOR (consisting of the diamond character `⋄` which must separate adjacent expressions),
4. a COMMENT (which must start with the character `⍝`).

Each of the four parts is optional, but if present they must occur in the given order except that successive expressions must be separated by `⋄`. Any characters occurring to the right of the first comment symbol (`⍝`) that is not within quotes is a comment.

Comments are not executed by APL. Expressions in a line separated by `⋄` are taken in left-to-right order as they occur in the line. For output display purposes, each separated expression is treated as a separate statement.

<h2 class="example">Examples</h2>
```apl
      5×10
50
 
      MULT: 5×10
50
 
      MULT: 5×10 ⋄ 2×4
50
8
 
      MULT: 5×10 ⋄ 2×4  ⍝ MULTIPLICATION
50
8
```
