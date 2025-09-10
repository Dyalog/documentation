<h1 class="heading"><span class="name">Namespaces</span></h1>

Names within namespaces may be referenced *explicitly* or *implicitly*.  An *explicit* reference requires that you identify the object by its full or relative pathname using a `'.'` syntax; for example:
```apl
      X.NUMB ← 88
```

sets the variable `NUMB` in namespace `X` to 88.
```apl
      88 UTIL.FOO 99
```

calls dyadic function `FOO` in namespace `UTIL` with left and right arguments of 88 and 99 respectively.  The interpreter can distinguish between this use of `'.'` and its use as the inner product operator, because the leftmost name: `UTIL` is a (class 9) namespace, rather than a (class 3) function.

The general namespace reference syntax is:
```apl
  SPACE . SPACE . (...) EXPR
```

Where `SPACE` is an *expression* which resolves to a namespace reference, and `EXPR` is any APL expression to be resolved in the resulting namespace.

There are two special space names:

`#`  is the top level or 'Root' namespace.

`##` is the parent or space containing the current namespace.

`⎕SE` is a system namespace which is preserved across workspace load and clear.

<h2 class="example">Examples</h2>
```apl
      WSDOC.PAGE.NO +← 1     ⍝ Increment WSDOC page count
 
      #.⎕NL 2                   ⍝ Variables in root space
 
      UTIL.⎕FX 'Z←DUP A' 'Z←A A'    ⍝ Fix remote function
 
      ##.⎕ED'FOO'         ⍝ Edit function in parent space
 
      ⎕SE.RECORD ← PERS.RECORD    ⍝ Copy from PERS to ⎕SE
 
      UTIL.(⎕EX ⎕NL 2)        ⍝ Expunge variables in UTIL
 
     
      (⊃⎕SE #).(⍎⊃↓⎕NL 9).(⎕NL 2)     ⍝ Vars in first ⎕SE
                                      ⍝ namespace.
 
      UTIL.⍎STRING         ⍝ Execute STRING in UTIL space
```

You may also reference a function or operator in a namespace *implicitly* using the mechanism provided by `⎕EXPORT` (See [Language Reference](../../../../language-reference-guide/system-functions/export)) and `⎕PATH`. If you reference a name that is undefined in the current space, the system searches for it in the list of exported names defined for the namespaces specified by `⎕PATH`. See [Language Reference](../../../../language-reference-guide/system-functions/path) for further details.

Notice that the expression to the right of a dot may be arbitrarily complex and will be executed within the namespace or ref to the left of the dot.
```apl
      X.(C←A×B)
      X.C
10 12 14
16 18 20
      NS1.C
10 12 14
16 18 20
```

## Summary

Apart from its use as a decimal separator (`3.14`), '`.`' is interpreted by looking at the type or *class* of the expression to its left:

|Template   |Interpretation           |Example          |
|-----------|-------------------------|-----------------|
|`∘.`       |Outer product            |`2 3 ∘.× 4 5`    |
|`function.`|Inner product            |`2 3 +.× 4 5`    |
|`ref.`     |Namespace reference      |`2 3 x.foo 4 5`  |
|`array.`   |Reference array expansion|`(x y).⎕NC⊂'foo'`|
