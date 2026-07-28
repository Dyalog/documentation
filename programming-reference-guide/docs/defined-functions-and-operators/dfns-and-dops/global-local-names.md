# Global and Local Names

A dfn does not declare its local names. Every name assigned within a dfn is automatically local to that dfn, so assigning to a name inside a dfn never changes a global of the same name.

<h2 class="example">Example</h2>
```apl
      x←99
      {x←1 ⋄ x} 0      ⍝ the inner x is local
1
      x                ⍝ the global x is unchanged
99
```

A name that is referenced but not assigned within the dfn is global: it is found in the enclosing environment. Because dfns nest lexically, a dfn defined inside another dfn can see the names local to the enclosing dfn. This is described under [Lexical Name Scope](static-name-scope.md).

There is no header in which to localise names, and none is needed: automatic localisation takes the place of the explicit locals list of a [traditional function](../traditional-functions-and-operators/global-local-names.md). The system function [`⎕SHADOW`](../../../../language-reference-guide/system-functions/shadow) skips dfns when it searches the stack for a tradfn in which to localise a name.
