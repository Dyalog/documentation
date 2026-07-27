# <span>PagesBeginDirty</span> <span>Property</span>

**Description**

The PagesBeginDirty property indicates whether a new page of a document will be printed even if it has no content.

For example, with PagesBeingDirty set to `1` (the default), the following code prints an empty page following the page containing "hello":
```apl
'p' ⎕WC 'printer' ('PagesBeginDirty' 1)
'p.t' ⎕WC 'text' 'hello' (10 10)
p.NewPage  ⍝ prints the current page, marks the new page as "Dirty"
⎕EX 'p'    ⍝ prints the new page because it is marked as "Dirty"
```
However, with PagesBeingDirty set to `0`, the following code does not print an empty page following the page containing "hello":
```apl
'p' ⎕WC 'printer' ('PagesBeginDirty' 0)
'p.t' ⎕WC 'text' 'hello' (10 10)
p.NewPage  ⍝ prints the current page, does not mark the new page as "Dirty"
⎕EX 'p'    ⍝ does not print the new page because it is not marked as "Dirty"
```

**Application** 

Objects: [Printer](../objects/printer.md)
