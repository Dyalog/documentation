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

## Assigning to a Name in the Enclosing Environment

Plain assignment always creates a local, so a dfn reaches a name outside itself in one of two ways.

*Modified assignment* updates an existing name in place instead of creating a new one. With [Right](../../../../language-reference-guide/primitive-functions/right) (`⊢`) as the modifying function, the value is replaced outright:

<h3 class="example">Example</h3>
```apl
      x←99
      {x⊢←1 ⋄ x} 0        ⍝ the global x is updated
1
      x
1
```

The name must already have a value; modified assignment to an undefined name signals a `VALUE ERROR`. Note also that a named function cannot be used as the modifying function in a dfn without `∘⊢`; see [Restrictions](restrictions.md).

Qualifying the name with a namespace path is the more general mechanism, because it also creates a name that does not yet exist. [`⎕THIS`](../../../../language-reference-guide/system-functions/this) names the dfn's own home namespace:

<h3 class="example">Example</h3>
```apl
      {⎕THIS.y←1 ⋄ 0} 0   ⍝ y need not exist beforehand
0
      y
1
```

Either way, where the name is local to an enclosing dfn, it is that local which is updated, following [Lexical Name Scope](static-name-scope.md). [Namespaces and Localisation](../../introduction/namespaces/namespaces-and-localisation.md) describes how a qualified name is resolved.
