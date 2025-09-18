<h1 class="heading"><span class="name">Serialising Namespaces</span></h1>

The Serialisation of an array is its conversion from its internal representation, which may contain pointers to other structures in the workspace, into a self-contained series of bytes. This allows the array to be written to a file, transmitted over a socket or used in a variety of other ways. The de-serialisation of an array is the conversion back to an internal format whose content and structure is identical to the original array.

If an array contains a reference to a namespace or object that is within the same array, it can be serialised and de-serialised normally.

If an array contains a reference to a namespace or object that is not internal to the array itself, this presents a problem, which is resolved as follows:

1. If the reference is a direct reference to Root (`#`) or to `⎕SE`, it is serialised as a reference to that symbol, but the contents of `#` or `⎕SE` are not included. When the array is de-serialised, this results in a reference to the Root (`#`) or `⎕SE` in the current workspace. The newly reconstituted array is not strictly identical to the original because the contents of `#` or `⎕SE` may be different.
2. If the reference is to an arbitrary external namespace or object, a copy of that object is included but its path is discarded. When the array is de-serialised, the copy is reconstituted as a sibling (that is, as a child of the same parent as the de-serialised array). In this case the contents of the external namespace or object are preserved, but not its path. The newly reconstituted array is not strictly identical to the original because the path to the external reference has changed.
3. If however, the external namespace or object itself contains an external reference, the operation fails with `DOMAIN ERROR`.

The following example uses `220⌶` but applies equally to an array serialised by, for example `⎕FAPPEND`.

<h2 class="example">Examples</h2>
```apl

       'A' ⎕NS ''
       'B' ⎕NS ''
       'C' ⎕NS ''
        A.b←B
        B.c←C
        s←1 (220⌶)A
       )ERASE A B C
       )OBS

      New←0(220⌶)s
      New
#.A
      New.b
#.B
      New.b.c
#.C

```
```apl
      )CLEAR
clear ws
      'A' ⎕NS ''
      'B' ⎕NS ''
      'X'⎕NS ''
      'X.C'⎕NS ''
      A.b←B
      B.c←X.C
      s←1(220⌶)A
DOMAIN ERROR: Namespace is not self contained
      s←1(220⌶)A
         ∧

```

Note that a successful `0(220⌶)` does not mean that a `1(220⌶)` on the result will succeed. If the original reference was to, say, the MenuBar of `⎕SE` you cannot reconstitute that in `#`.
