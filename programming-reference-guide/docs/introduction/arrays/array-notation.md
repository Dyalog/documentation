<h1 class="heading"><span class="name">Array Notation</span></h1>


Array notation extends [vector notation](vector-notation.md) to define arrays of higher rank, and namespaces, and lets these definitions span multiple lines:

-   **Parentheses** embrace vector definitions and namespace name-value pairs
-   **Square brackets** embrace higher-rank arrays
-   **Diamonds** and **linebreaks** separate array elements and name-value pairs

Some examples show how these work.


## Ordered Arrays

Ordered arrays are indexed by position, as in `vec[3]` or `mat[2 4;5]`.


### Nested Vector { .example }

```apl
      ⍴z← (0 6 1 8 ⋄ 2*0 2 0 2 1
      2 7 1 8 2 8 ⋄ 3 1 4 1 5)
4
      z
┌───────┬─────────┬───────────┬─────────┐
│0 6 1 8│1 4 1 4 2│2 7 1 8 2 8│3 1 4 1 5│
└───────┴─────────┴───────────┴─────────┘
      ('Three'
       'Blind'
       'Mice')
┌─────┬─────┬────┐
│Three│Blind│Mice│
└─────┴─────┴────┘
```

### Matrix { .example }

```apl
      ⍴m←[0 6 1 8 ⋄ 1 4 1 4
       2 7 1 8 ⋄ 3 1 4 2]
4 4
      m
0 6 1 8
1 4 1 4
2 7 1 8
3 1 4 2

      ⍝ short elements are filled
      ⍴mice←['Three'
             'Blind'
             'Mice']
3 5
      mice,'|'
Three|
Blind|
Mice |

      ⍴RC←[0 'OK'
           1 'WS FULL'
           2 'SYNTAX ERROR'
           3 'INDEX ERROR'
           4 'RANK ERROR']
5 2
      ⍴expenses←0⌿[    ⍝ typed template matrix
      'Glasgow' 125.84
      ]
0 2
```

### Column Matrix { .example }

```apl
      (,⊂'Three') ≡ ('Three' ⋄)
1
      ⍴¨cm3←[('Three' ⋄)
             ('Blind' ⋄)
             ('Mice'  ⋄)]
5
5
4
      cm3
┌─────┐
│Three│
├─────┤
│Blind│
├─────┤
│Mice │
└─────┘
```

### Rank-3 Array { .example }

```apl
      ⍴block←[
       [3 1 4 ⋄ 1 5 ]
       [2 7 0 ⋄ 2]
      ]
2 2 3
      block
3 1 4
1 5 0

2 7 0
2 0 0

```


## Namespaces

Namespaces can be thought of as ‘semantic arrays’ (or dictionaries, or objects): unordered, and indexed by names rather than positions.

Array notation allows you to write a namespace literal as zero or more name-value pairs, embraced by parentheses.

```apl
      mt←()              ⍝ empty namespace
      ()()()             ⍝ vector of empty namespaces
      ( () ⋄ () ⋄ () )   ⍝ vector of empty namespaces
      n←(x:'hello')      ⍝ n.x is vector

      (x:['hello'        ⍝ n.x is matrix
        'world'])

      (y:(x:'hello'))    ⍝ nested namespaces

      (
        FirstName:'Wolfgang'
        LastName:'Mozart'
        Age:35
      )
```

### Scoping In Namespace Literals

Array and namespace literals can include value expressions.

```apl
      LUE←(answer:7×6)   ⍝ Life, the Universe, and Everything
```

Any assignments (made with `←`) in a value expression are made *in the scope around the namespace*, and persist there.

```apl
      long←'bobby'
      short←'jack'
      ns←(short:'jill' ⋄ inner:short∘.=short←3↑long)
      ns.inner
1 0 1
0 1 0
1 0 1
      short     ⍝ altered by inner assignment
bob
      ns.short  ⍝ unaffected by inner assignment
jill
```

## Specification

The new syntactic forms were previously errors in every mainstream APL implementation and therefore introduce no backward incompatibilities.

In the following:

-   A *name-value pair* is an APL name followed by a colon and a value expression.
-   A *separator* is a diamond or line break, and *separated* means separated by them.
-   An *empty* value expression or name-value pair is two separators with nothing but white space between them.

### Namespace

A namespace is defined by a parenthesised separated list of zero or more name-value pairs.

Empty name-value pairs define no namespace members.

### Vector

A vector is defined by a parenthesised separated list of two or more value expressions.

Empty value expressions define no vector elements.

### Matrices And Higher-rank Arrays

An array of rank 2 or higher is defined by a bracketed separated list of value expressions, which constitute the major cells of the array.

Short elements are padded to fill, and scalars are treated as length-1 vectors.

!!! info "Nested separators"

    Separators in a list of value expressions or name-value pairs make an enclosing parenthesis or bracket *broken*.

    Separators encapsulated in a dfn or further contained in array notation do not break a parenthesis or bracket.
    For example, in

        ({1=⍵:'y' ⋄ 'n'}?2)

    the diamond is part of the dfn and does not break the surrounding parenthesis.

### Unsupported

-   Scripted and external objects
-   Non-array namespace members
-   Reference loops
-   Class instances
-   Internal representations returned by `⎕OR`


### Formal Syntax

The array notation can be described in this form[^ebnf], where `expression` is any traditional APL expression:

    value ::= expression | list | block | space
    list  ::= '(' ( ( value sep )+ value? | ( sep value )+ sep? ) ')'
    block ::= '[' ( ( value sep )+ value? | ( sep value )+ sep? ) ']'
    space ::= '(' sep? ( name ':' value ( sep name ':' value )* )? sep? ')'
    sep   ::= [⋄#x000A#x000D#x0085]+


![Syntax diagram](/img/array-notation-syntax.png)
<!-- Eventually replace with Mermaid diagram. -->

!!! note "Sep values"

    The list of `sep` values is for illustration purposes and is to match the line breaks recognised by the APL implementation. However, these three values should be handled when reading Unicode text files.

[^ebnf]: Extended Backus–Naur.